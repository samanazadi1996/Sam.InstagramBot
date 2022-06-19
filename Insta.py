from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(5)


def Open():
    browser.get('https://www.instagram.com/')
    print("Open")


def Hide():
    browser.set_window_position(-10000, 0)
    print("Hide")


def Login(username, password, slp=2):
    sleep(slp)
    browser.find_element_by_css_selector(
        "input[name='username']").send_keys(username)
    browser.find_element_by_css_selector(
        "input[name='password']").send_keys(password)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    print("Login")


def ClickOnNotNow(slp=2):
    sleep(slp)
    browser.find_element_by_xpath('//button[text()="Not Now"]').click()
    print("Not Now")


def LikePosts(slp=3):
    browser.refresh()
    sleep(10)
    likes_button = browser.find_elements_by_xpath(
        "//*[name()='svg' and @aria-label='Like']")

    lenLikes = 0
    for element in likes_button:
        try:
            element.click()
            lenLikes += 1
            sleep(slp)
        except:
            print("Error")

    print(f"Like Posts {lenLikes} from {len(likes_button)}")
    LikePosts(slp)


def Close():
    browser.close()
    print("Close")
