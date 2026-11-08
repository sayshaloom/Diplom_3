import pytest
import requests

from selenium import webdriver
from data.urls import Urls
from data.helpers import generate_user_payload


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user():
    payload = generate_user_payload()
    response = requests.post(Urls.API_REGISTER, json=payload)
    access_token = response.json().get("accessToken")

    yield payload

    if access_token:
        requests.delete(Urls.API_USER, headers={"Authorization": access_token})    