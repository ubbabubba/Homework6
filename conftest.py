#conftest.py
#fixtures for use in test_depaul.py

#libraries needed
from pytest import fixture
from selenium import webdriver
import requests


# request fixture
@fixture
def request_mod(request):
   yield requests.Session()


#fixture for different browsers
# will run two different browsers
@fixture(params=[[webdriver.Chrome, webdriver.ChromeOptions], [webdriver.Firefox, webdriver.FirefoxOptions]])
def driver(request):
   driver = request.param[0]
   options = request.param[1]
   driver_option =  options()
   driver_option.add_argument('--disable-extensions')
   driver_option.add_argument('--headless')
   driver_option.add_argument('log-level=3')
   driver_object = driver(options=driver_option)
   yield driver_object
   driver_object.quit()


test_depaul_urls = ['https://las.depaul.edu/academics/criminology/undergraduate/criminology-ba/Pages/default.aspx', \
                    'https://las.depaul.edu/academics/modern-languages/undergraduate/chinese-studies/Pages/default.aspx', \
                     'https://las.depaul.edu/academics/art-media-and-design/undergraduate/art-media-design/Pages/default.aspx', \
                     'https://csh.depaul.edu/academics/mathematical-sciences/undergraduate/data-science-ba/Pages/default.aspx']

@fixture(params=test_depaul_urls)
def test_urls_depaul(request):
    data = request.param
    return data
