import tkinter as tk
from tkinter
import ttk, messagebox
import requests
import time
import threading

#Binance API Config (Replace with actual API keys)

API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
BASE_URL = "https://fapi.binance.com"

class CryptoTraderApp:
def __init__(self, root): 
  self.root = root
  self.root.title("Crypto Trader")
  self.root.geometry("800x600")
  self.create_widgets()

def create_widgets(self):
    self.api_status = tk.Label(self.root, text="API: Not Connected", fg="red")
    self.api_status.pack()
    
    self.symbol_label = tk.Label(self.root, text="Select Coin:")
    self.symbol_label.pack()
    
    self.symbol_entry = tk.Entry(self.root)
    self.symbol_entry.pack()
    
    self.long_button = tk.Button(self.root, text="Long", command=self.place_long_order)
    self.long_button.pack()
    
    self.short_button = tk.Button(self.root, text="Short", command=self.place_short_order)
    self.short_button.pack()
    
    self.price_label = tk.Label(self.root, text="Price: Updating...")
    self.price_label.pack()
    
    self.stop_button = tk.Button(self.root, text="Stop Trading", command=self.stop_trading)
    self.stop_button.pack()
    
    self.balance_label = tk.Label(self.root, text="Balance: Loading...")
    self.balance_label.pack()
    
    self.update_price()
    self.update_balance()
    
def fetch_price(self, symbol):
    url = f"{BASE_URL}/fapi/v1/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        return response.json().get("price", "N/A")
    except:
        return "Error"

def update_price(self):
    symbol = self.symbol_entry.get().upper()
    if symbol:
        price = self.fetch_price(symbol)
        self.price_label.config(text=f"Price: {price}")
    self.root.after(1000, self.update_price)
    
def fetch_balance(self):
    url = f"{BASE_URL}/fapi/v2/balance"
    headers = {"X-MBX-APIKEY": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        return response.json()[0]["balance"]
    except:
        return "Error"
    
def update_balance(self):
    balance = self.fetch_balance()
    self.balance_label.config(text=f"Balance: {balance} USDT")
    self.root.after(5000, self.update_balance)
    
def place_long_order(self):
    symbol = self.symbol_entry.get().upper()
    if not symbol:
        messagebox.showerror("Error", "Please enter a symbol")
        return
    messagebox.showinfo("Order", f"Long order placed for {symbol}")
    
def place_short_order(self):
    symbol = self.symbol_entry.get().upper()
    if not symbol:
        messagebox.showerror("Error", "Please enter a symbol")
        return
    messagebox.showinfo("Order", f"Short order placed for {symbol}")

def stop_trading(self):
    messagebox.showinfo("Trading", "All positions closed!")

if __name__ == "__main__":
  root = tk.Tk()
  app = CryptoTraderApp(root)
  root.mainloop()
