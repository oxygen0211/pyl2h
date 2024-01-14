import collections
import base64
import requests
from urllib.parse import urlencode, unquote

import rsa
from rsa import PrivateKey
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
    def hash_password(self, password):
        md5 = MD5.new()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest().upper()
    
    def login(self, username, password):
        
        data = {
            "appName": "Link2Home",
            "appType": "2",
            "appVersion": "1.1.1",
            "password": self.hash_password(password),
            "phoneSysVersion": "iOS 17.1.2",
            "phoneType": "iPad13,8",
            "username": username,
        }
        
        data["sign"] = self.get_sign(data)
        print("Request: {}".format(data))

        r = requests.post(login_url, params=data, headers=headers)
        body = r.json()
        print("Status: {}, Body: {}".format(r.status_code, body))

        if body['success'] and "data" in body:
            print("We are logged in!")
            self.session = body["data"]
        else:
            print("Login failed!")
            self.session = None

    def list_devices(self):
        if self.session is None:
            return []
        print("Getting registered devices...")
        data = {
            "token": self.session["token"]
        }

        data["sign"] = self.get_sign(data)
        r = requests.get(device_list_url, params=data)
        body = r.json()
        print("Status: {}, Body: {}".format(r.status_code, body))

    def get_sign(self, data):
        sorted_data = collections.OrderedDict(sorted(data.items()))
        query_string = unquote(urlencode(sorted_data)).encode("utf-8")

        query_string = ""
        for key in data:
            query_string = query_string + key + "=" + data[key] + "&"
        query_string = query_string[:-1].encode("utf-8")

        print(f'Query String: {query_string}')

        

        with open("pyl2h/private_key.pem") as key_file:
            key_data = key_file.read()
            key = RSA.import_key(key_data)
            #key = rsa.PrivateKey.load_pkcs1(key_data)
        
        hash = SHA1.new(query_string)
        signer = pkcs1_15.PKCS115_SigScheme(key)
        signature = signer.sign(hash)
        #signature = rsa.sign(query_string, key, 'SHA-1')
        encoded_sig = base64.b64encode(signature).decode('utf-8')
        return encoded_sig

    def get_sign_old(self, data):
        sorted_data = collections.OrderedDict(sorted(data.items()))
        query_string = unquote(urlencode(sorted_data))
        print(f'Query String: {query_string}')
        key = RSA.import_key(bytes.fromhex(private_key_hash))
        h = SHA1.new(query_string.encode("utf-8"))
        signature = pkcs1_15.new(key).sign(h)
        encoded_sig = base64.urlsafe_b64encode(signature).decode('ascii')
        return encoded_sig