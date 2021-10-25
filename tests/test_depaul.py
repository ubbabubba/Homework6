from pytest import mark
from selenium.webdriver.common.by import  By
from selenium import webdriver

@mark.UI
def test_can_navigate_to_using_different_browsers(driver,test_urls_depaul):
    driver.get(test_urls_depaul)
    depaul_name = driver.find_element(By.CSS_SELECTOR,"div.col-7.mt-xs-1.mt-sm-4>a.logo-long").text
    assert 'DePaul University' == depaul_name

@mark.session
def test_request(request_mod,test_urls_depaul):
    response = request_mod.get(test_urls_depaul)
    assert response.status_code == 200





















#@mark.parametrize('urls', ['https://www.subaru.com/', 'https://www.honda.com/', 'https://www.toyota.com/' ])
#def test_can_navigate_to_using_different_browsers(driver,urls):