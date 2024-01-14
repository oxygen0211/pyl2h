"""CLI functionality for debugging and testing."""

import argparse
import asyncio
from time import sleep
from .udp import UDPServer

server = UDPServer()

def get_arguments() -> argparse.Namespace:
    """Get parsed passed in arguments."""

    parser = argparse.ArgumentParser(
        description="Matter Controller Server using WebSockets."
    )
    parser.add_argument(
        "--ip",
        type=str,
        default=None,
        help="IP of the device to be used for testing. Will Flip-Flop Channel 1 every Minute",
    )

    arguments = parser.parse_args()

    return arguments

def device_callback(device_status):
    """Callback for new status updates by devices."""
    print(f'New Device Update: {device_status}')

def monitor_updates():
    """Entrypoint for starting to listen for device updates"""
    server.listen(device_callback)

def main() -> int:
    """Main entrypoint for CLI based operation and example for usage"""
    args = get_arguments()
    ip = args.ip

    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, monitor_updates)

    while True:
        devices = server.get_devices()
        print("Devices:")
        for d in devices.items():
            print(devices[d])

        if ip is not None and ip in devices:
            dev = devices[ip]
            new_state = not dev["channels"][1]
            print(f'Switching device {ip} to {new_state}')
            server.set_status(ip, 1, new_state)

        sleep(60)
