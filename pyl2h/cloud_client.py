import collections
import base64
import requests
from urllib.parse import urlencode

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1, MD5
from Crypto.PublicKey import RSA
from Crypto.IO import PKCS8

from .const import private_key_hash, login_url, device_list_url, user_agent, accept_language

headers = {
            "Accept": "*/*",
            "User-Agent": user_agent,
            "Accept-Language": accept_language,
            "Content-Type": "application/x-www-form-urlencoded"
        }

class Cloud_Client:
    
    def login(self, username, password):
        md5 = MD5.new()
        md5.update(password.encode("utf-8"))
        pass_hash = md5.hexdigest()
        
        data = {
            "appName": "Link2Home",
            "appType": "2",
            "appVersion": "1.1.1",
            "password": pass_hash.upper(),
            "phoneSysVersion": "iOS 16.1.1",
            "phoneType": "iPhone13,3",
            "username": username,
        }
        
        data["sign"] = self.get_sign(data)
        print("Request: {}".format(data))

        r = requests.post(login_url, params=data, headers=headers)
        body = r.json()
        print("Status: {}, Body: {}".format(r.status_code, body))

        if "data" in body:
            print("We are logged in!")
            self.session = body.data

    def list_devices(self):
        print("Getting registered devices...")
        data = {
            "token": self.session.token
        }

        data["sign"] = self.get_sign(data)
        r = requests.get(device_list_url, params=data)
        body = r.json()
        print("Status: {}, Body: {}".format(r.status_code, body))
    def get_sign(self, data):
        sorted_data = collections.OrderedDict(sorted(data.items()))
        query_string = urlencode(sorted_data)

        #key = PKCS8.unwrap(bytes.fromhex(private_key_hash))
        key = RSA.import_key(bytes.fromhex(private_key_hash))
        h = SHA1.new(query_string.encode("utf-8"))
        print("hash: {}".format(h))
        signature = pkcs1_15.new(key).sign(h)
        return base64.b64encode(signature).decode('ascii')