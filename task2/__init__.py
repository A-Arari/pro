import traceback, time

from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

# (Webdriver: driver, Boolean: free)
init = False
init_completed = False
driver_list = []

def _get_driver():
    global chrome_options
    print('crawl:', 'getting new driver')

    return webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)

    
def init_driver_list():
    global driver_list, init_completed

    print('crawl:', 'init drivers')
    for i in range(settings.MAX_CRAWL_COUNT):
        driver_list.append([_get_driver(), True])
    init_completed = True


def get_driver():
    global driver_list, init, init_completed
    try:

        print('crawl:', 'G-D')
        if not init:
            init = True
            init_driver_list()

        while not init_completed:
            time.sleep(1)

        driver = index = None
        while driver is None:
            print('nulling', driver_list)
            if driver_list is None:
                init_driver_list()
                
            for i in range(len(driver_list)):
                if driver_list[i][1] == True:
                    if driver_list[i][0] is None:
                        driver_list[i][0] = _get_driver()

                    driver_list[i][1] = False
                    driver = driver_list[i][0]

                    index = i
                    break

        print('crawl:', 'Driver', index, 'is available')

        return driver, index
    except Exception as e:
        traceback.print_exc()
        raise e


def free_driver(index):
    print('crawl:', 'Freeing driver', index)
    driver_list[index][1] = True
    if driver_list[index][0] is None:
        driver_list[index][0] = _get_driver()


p = -1

def set_p(pv):
    global p
    print('setting p', p, pv)
    p = pv
    print('DONE setting p', p, pv)


def get_p():
    global p

    p += 1
    return p


def decrease_p():
    global p

    p -= 1
    if p < 0:
        p = -1
