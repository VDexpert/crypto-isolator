import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from fake_useragent import UserAgent
from random import randint


def deceiver():
    ua = UserAgent()
    chromedriver = '/usr/bin/chromedriver'
    opts = webdriver.ChromeOptions()
    opts.add_argument(f"user-agent={ua.random}")

    id_obj = "A value the model object AnalyzerALT that is automatically assigned when a command " \
             "is created in the management/command package. To get or set object field values"

    '''
    In the value of the "url" variable, we gets the value 
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

        count = 0
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

                links = browser.find_elements(by=By.TAG_NAME, value='a')

                count_break = randint(10 if len(links) > 10 else 5, 20 if len(links) > 20 else len(links))

                with open('logs_imitate_real_behaviour.txt', 'a', encoding='utf-8') as logs:
                    for link in links:
                        time.sleep(randint(2, 10))

                        try:
                            end = int(time.time())
                            timing -= (end - start)
                            browser.get(links[randint(0, count_break)].get_attribute('href'))
                            count += 1
                            logs.write(f'\n{count}_switch_from_{url}')

                        except:
                            continue

if __name__ == '__main__':
    deceiver()
