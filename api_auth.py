import json
import os
from cryptography.fernet import Fernet

CONFIG_FILE = "config.json"
KEY_FILE = "secret.key"

def generate_key():
  key = Fernet.generate_key()
  with open(KEY_FILE, "wb") as key_file:
    key_file.write(key)

def load_key():
  if not os.path.exists(KEY_FILE):
    generate_key()
  with open(KEY_FILE, "rb") as key_file:
    return key_file.read()

def encrypt_data(data):
  key = load_key()
  cipher_suite = Fernet(key)
  return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(data):
  key = load_key()
  cipher_suite = Fernet(key)
  return cipher_suite.decrypt(data.encode()).decode()

def save_api_credentials(api_key, api_secret):
  encrypted_data = {
    "api_key": encrypt_data(api_key),
    "api_secret": encrypt_data(api_secret)
  }
  with open(CONFIG_FILE, "w") as file:
    json.dump(encrypted_data, file)

def get_api_credentials():
  if not os.path.exists(CONFIG_FILE):
    raise Exception("API credentials not found. Please save them first.")
  with open(CONFIG_FILE, "r") as file:
    encrypted_data = json.load(file)
  return decrypt_data(encrypted_data["api_key"]), decrypt_data(encrypted_data["api_secret"])

if __name__ == "__main__":
  api_key = input("Enter your Binance API Key: ")
  api_secret = input("Enter your Binance API Secret: ")
  save_api_credentials(api_key, api_secret)
  print("API credentials saved securely.")

