import requests
from bs4 import BeautifulSoup
from utils import build_google_finance_query

class CurrencyConversion:
    def __init__(self, currency_from: str, currency_to: str) -> None:
        self.currency_from = currency_from
        self.currency_to = currency_to
    
    def convert(self) -> float:
        google_finance_query = build_google_finance_query(self.currency_from, self.currency_to)
        

