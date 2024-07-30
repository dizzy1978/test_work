import pytest
from selenium import webdriver

@pytest.fixture(scope = 'session')
def browser(request):
    print("\nSTART CHROME BROWSER")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nQUIT BROWSER..")
    browser.quit()

