import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser(request):
    print("\nSTART CHROME BROWSER")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nQUIT BROWSER..")
    browser.quit()

