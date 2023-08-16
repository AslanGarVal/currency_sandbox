import pytest

from currency_exchanger.utils import *

class TestQueryBuilder:
    def test_google_query(self):
        from_cur = 'MXN'
        to_cur = 'PEN'

        reference_result = 'https://www.google.com/finance/quote/MXN-PEN'

        assert build_google_finance_query(from_cur, to_cur) == reference_result

class TestRequestGoogleFinanceQuote:
    def test_google_finance_quote(self):
        failing_test_url = 'https://www.google.com/finance/quotsee/PEN-MXNa'
        with pytest.raises(GoogleFinanceResponseException):
            request_google_finance_quote(failing_test_url)

    def test_returns_string(self):
        correct_test_url = 'https://www.google.com/finance/quote/MXN-PEN'
        assert type(request_google_finance_quote(correct_test_url)) == str

    def test_correct_url(self):
        correct_test_url = 'https://www.google.com/finance/quote/MXN-PEN'
        print(request_google_finance_quote(correct_test_url)[:20])
        assert ('html' in request_google_finance_quote(correct_test_url)) == True

class TestHTMLValueParser:
    def test_not_found_div(self):
        with open('resources/succesfull_request_sample.txt', 'r') as f:
            text_to_sample = f.read()
            with pytest.raises(ResponseParsingException):
                parse_HTML_string_for_value(text_to_sample, 'papa')

    def test_found_div(self):
        with open('resources/succesfull_request_sample.txt', 'r') as f:
            text_to_sample = f.read()
            assert parse_HTML_string_for_value(text_to_sample, 'YMlKec fxKbKc') == 4.5924

        