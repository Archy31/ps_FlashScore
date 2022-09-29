url = 'https://www.flashscore.com.ua/?rd=flashscore.ru.com'

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'user-agent': '''Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'''
}

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from time import sleep

def get_driver():
    options = webdriver.FirefoxOptions()
    options.set_preference('dom.webdriver.enabled', False)
    options.set_preference('dom.webnofications.enabled', False)
    options.set_preference('media.volume_scale', '0.0')
    options.headless = True
    options.set_preference('general.useragent.override', f'{headers["user-agent"]}')

    driver = webdriver.Firefox(executable_path='webDrivers/geckodriver-v0.31.0-linux64/geckodriver', options=options)

    return driver


def get_premier_liga():
    xpath = '/html/body/div[4]/div[1]/div/div/aside/div/div[2]/div[2]/div[1]/div[1]'
    driver = get_driver()
    try:
        print("\nИдет процесс парсинга сайта, пожалуйста подождите!\n")
        driver.get(url)
        driver.find_element(by.By.XPATH, value=xpath).click()
        sleep(3)

        matches = driver.find_element(by.By.CLASS_NAME, value='soccer').find_elements(by.By.CLASS_NAME, value='event__match')
        for match in matches:
            time_event = match.find_element(by.By.CLASS_NAME, value='event__time').text
            print(time_event)

            commands = match.find_elements(by.By.CLASS_NAME, value='event__participant')
            for comm in commands:
                print(comm.text)
            
            print("\n")
        
            
    except Exception as e:
        return e

    finally:
        driver.close()
        driver.quit()


def main():
    get_premier_liga()


if __name__ == '__main__':
    main()