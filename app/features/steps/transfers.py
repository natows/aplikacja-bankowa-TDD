from behave import *
import requests
from unittest_assertions import AssertEqual
assert_equal = AssertEqual()
URL = "http://localhost:5000/api/accounts"

@when('A transfer for account with pesel "{pesel}" with type "{type}" for amount "{amount}" is made')
def make_transfer(context,pesel,type,amount):
    json_body={"type": f"{type}",
               "amount": f"{amount}"}
    response = requests.post(URL + f"/{pesel}/transfer", json=json_body)
    context.response = response
    context.response_data = response.json()

@step('Account with pesel "{pesel}" has balance "{balance}"')
def check_balance(context,pesel,balance):
    response = requests.get(URL + f"/{pesel}")
    assert_equal(response.status_code, 200)
    account = response.json()
    assert_equal(account["balance"], int(balance))

@step('The response message is "{message}"')
def assert_response_message(context, message):
    assert_equal(context.response_data["message"],message)


