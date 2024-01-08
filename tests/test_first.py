import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def test_initiateBrowser():

    firefox_service = Service()
    driver = webdriver.Firefox(service=firefox_service)

    driver.get("https://rahulshettyacademy.com/angularpractice/")


