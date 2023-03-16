import os
import time
from smtplib import SMTPException
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.utils import timezone
from selenium.webdriver.common.by import By
from selenium import webdriver
from fake_useragent import UserAgent
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


def scraper_alt():
    ua = UserAgent()
    chromedriver = '/usr/bin/chromedriver'
    opts = webdriver.ChromeOptions()
    opts.add_argument(f"user-agent={ua.random}")

    id_obj = "A value the model object AnalyzerALT that is automatically assigned when a command " \
             "is created in the management/command package. To get or set object field values"

    '''
    In the value of the variable "dependence" we take the value
    "dependence" fields of the "AnalyzerALT" model object.
    
    '''
    dependence = 0.1
    '''
    In the value of the "url" variable, we take the value 
    of the "url" field of the "AnalyzerALT" model object
    '''
    url = 'https://www.binance.com/ru/futures/ETHUSDT?utm_source=internal&utm_medium=homepage&utm_campaign=trading_dashboard'

    '''
    In the value of the "timing" variable, we take the value of the 
    "time_scraping" field of the "AnalyzerBTC" model object
    '''
    timing = 1 * 85600  # 85600 - so many seconds in a day

    with open('proxies.txt', encoding='utf-8') as f:
        proxies = f.readlines()
        iterator = proxies.__iter__()

        while timing > 0:
            try:
                start = int(time.time())
                proxy_ip = iterator.__next__()

            except StopIteration:
                iterator = proxies.__iter__()
                continue

            else:
                proxy_dict = {
                     'proxyType': 'MANUAL',
                     'httpProxy': proxy_ip,
                }

                webdriver.DesiredCapabilities.CHROME['proxy'] = proxy_dict
                browser = webdriver.Chrome(options=opts, executable_path=chromedriver)
                browser.get(url)

                elems = browser.find_elements(by=By.CLASS_NAME, value='draggableHandle')

                for elem in elems: #TODO edit file entry with name-pattern "result_analyzer_alt_id_object_analyzerALT"
                    if elem.text:
                        if dependence:
                            cleaned_price = float(elem.text) - (float(elem.text)*float(dependence))
                            print(f'dependenceON-price {elem.text}, dependenceOFF-price {cleaned_price}, {timezone.now()}')

                end = int(time.time())
                timing -= (end - start)


if __name__ == '__main__':
   scraper_alt()
