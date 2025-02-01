from behave import *
import requests
from unittest_assertions import AssertEqual
assert_equal = AssertEqual()
URL = "http://localhost:5000/api/accounts"

@when('I create an account using name: "{name}", surname: "{surname}", pesel: "{pesel}"')
def create_account(context, name, surname, pesel):
    json_body = { "name": f"{name}",
    "surname": f"{surname}", 
    "pesel": pesel
    }
    create_resp = requests.post(URL, json = json_body)
    assert_equal(create_resp.status_code, 201)

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    response = requests.get(URL + "/count")
    assert_equal(response.status_code, 200)
    real_count = response.json()
    assert_equal(real_count["Count"], int(count))

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(URL + f"/{pesel}")
    assert_equal(response.status_code, 200)


@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/{pesel}")
    assert_equal(response.status_code, 404)


@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/{pesel}")
    assert_equal(response.status_code, 200)

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["name", "surname"]:
        raise ValueError(f"Invalid field: {field}. Must be 'name' or 'surname'.")
    json_body = { f"{field}": f"{value}" }
    response = requests.patch(URL + f"/{pesel}", json = json_body)
    assert_equal(response.status_code, 200)

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/{pesel}")
    assert_equal(response.status_code, 200)
    account = response.json()
    assert_equal(account[f"{field}"], value)