import requests

def build_google_finance_query(currency_from: str, currency_to: str) -> str:
    return f'https://www.google.com/finance/quote/{currency_from}-{currency_to}'

def request_google_finance_quote(query_url: str) -> str: 
    '''
    Make a GET request to Google using the provided query url. 
    Return an HTML string as a response

    Params: 
        query_url (str): query url to generate GET request
    Returns: 
        (str): HTML string of the content
    '''

    pass

def parse_HTML_string_for_value(html_string: str, class_id: str) -> float:
    '''
    Receives an HTML string and searches for a div with class equalling provided class_id.
    Returns the value contained in said div as float. 

    Warning: Since we are scraping Google's data, this may break without notice and refactoring will be required
    '''