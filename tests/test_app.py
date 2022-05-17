import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Connecting to webdriver")

driver = webdriver.Remote(
    command_executor=('http://selenium-env:4444/wd/hub'),
    options=webdriver.FirefoxOptions()
)

def test_increment():
    driver.get("http://devops_flask_app:5555/")

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) + 1

    button = driver.find_element(By.ID, "plus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    print("Test 1 passed")

def test_decrement():
    driver.get("http://devops_flask_app:5555/")

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) - 1

    button = driver.find_element(By.ID, "minus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    print("Test 2 passed")

try:
    print("Test 1")
    test_increment()

    print("Test 2")
    test_decrement()

finally:
    print("Tests finished")

    driver.quit()