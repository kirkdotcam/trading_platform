from dotenv import load_dotenv
import os
import alpaca_trade_api as tradeapi

load_dotenv()

api_key = os.getenv("APCA_API_KEY_ID")
secret_api_key = os.getenv("APCA_API_SECRET_KEY")

alpaca = tradeapi.REST(api_key, secret_api_key, base_url='https://paper-api.alpaca.markets')

alpaca_account = alpaca.get_account()