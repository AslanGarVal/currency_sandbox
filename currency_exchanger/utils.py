import requests
from bs4 import BeautifulSoup

class GoogleFinanceResponseException(Exception):
    '''
    Raised when request returns 404
    '''
    pass

class ResponseParsingException(Exception):
    '''
    Raised when div container with class-id is not found
    '''
    pass


def build_google_finance_query(currency_from: str, currency_to: str) -> str:
    return f'https://www.google.com/finance/quote/{currency_from}-{currency_to}'

def request_google_finance_quote(query_url: str) -> str | GoogleFinanceResponseException: 
    '''
    Make a GET request to Google using the provided query url. 
    Return an HTML string as a response

    Params: 
        query_url (str): query url to generate GET request
    Returns: 
        (str): HTML string of the content
    '''

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(query_url, headers=headers)

    if response.status_code != 200: 
        raise GoogleFinanceResponseException("Something went wrong while requesting conversion, check your URL!")
    elif '<title>Error 404 (Not Found)!!1</title>' in response.text:
        raise GoogleFinanceResponseException("Query returned succesfully, but no result was found. Check your URL!")
    else:
        return response.text

def parse_HTML_string_for_value(html_string: str, class_id: str = 'YMlKec fxKbKc') -> float:
    '''
    Receives an HTML string and searches for a div with class equalling provided class_id.
    Returns the value contained in said div as float. 

    Warning: Since we are scraping Google's data, this may break without notice and refactoring will be required

    Params: 
        html_string (str): HTML string to be parsed
        class_id (str): 
    '''
    soup = BeautifulSoup(html_string, features = 'lxml')

    div_search_result = soup.find('div', {'class': class_id})

    if div_search_result:
        return float(div_search_result.text)
    else: 
        raise ResponseParsingException(f"Provided class id: {class_id} was not found.")
