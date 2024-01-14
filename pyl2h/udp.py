"""UDP functionality for internal communication with devices."""

import socket
import copy

class UDPServer:
    """UDP Listener/Server functionality"""
    def __init__(self) -> None:
        self.devices = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(("", 35932))

    def decode_status_broadcast(self, data, ip, dev):
        """Decode status update broadcasted by device"""
        mac = data[2:8]
        channel = data[len(data)-2]
        is_on = not data[len(data)-1] == 0

        dev["mac"] = mac
        dev["channels"][channel] = is_on
        dev["ip"] = ip

        return dev

    def process_message(self, data, address):
        """Process message received on UDP socket"""
        ip = address[0]
        old_state = self.devices[ip] if ip in self.devices else {"channels": {}}
        new_state = self.decode_status_broadcast(data, ip, copy.deepcopy(old_state))

        if old_state == new_state:
            return None

        self.devices[ip] = new_state
        return new_state

    def send_message(self, ip, message):
        """Send a message to a device or Broadcast"""
        self.sock.sendto(message, (ip, 35932))

    def set_status(self, ip, channel: int, state):
        """Change the status of a device by sending a UDP multicast to it"""
        state_byte = b'\xff' if state else b'\x00'
        channel_byte = bytes([channel])
        device = self.devices[ip]
        mac = device["mac"]
        message = b'\xa1\x04'+mac+b'\x00\x09\x01\xf2\x02\xd1\x71\x50\x01'+channel_byte+state_byte
        self.send_message(ip, message)

    def get_devices(self):
        """Get the currently known list of devices"""
        return self.devices

    def listen(self, subscriber=None):
        """Start listening for device Updates on the UDP procotol"""
        while True:
            data, addr = self.sock.recvfrom(1024)
            device_status = self.process_message(data, addr)
            if device_status is not None and subscriber is not None:
                subscriber(device_status)
