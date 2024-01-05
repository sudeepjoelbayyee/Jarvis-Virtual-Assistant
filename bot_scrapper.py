from time import sleep 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.simplefilter("ignore")
url = f'https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Chat%20with%20bot%22%2C%22botConversationDescription%22%3A%22This%20chatbot%20was%20built%20surprisingly%20fast%20with%20Botpress%22%2C%22botId%22%3A%2254b79537-fce2-43b6-9111-c2b645d56c5b%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%2254b79537-fce2-43b6-9111-c2b645d56c5b%22%2C%22webhookId%22%3A%2251a2b2db-6349-4d75-9dfa-0980292734f8%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22frontendVersion%22%3A%22v1%22%2C%22showPoweredBy%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%22DX1M9F8av8BtBnX22LgwQY3llSYiLtrI%22%7D%7D'
chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
# chrome_options.add_argument("--headless=new")  # Enable headless mode (runs Chrome without GUI)
chrome_options.add_argument('--log-level=3')  # Set Chrome log level
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)


def click_on_chat_button():
    try:
        button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/button'))
        )
        button.click()
        print('Chat button clicked')
        sleep(2)
    except Exception as e:
        print(f"Error clicking on chat button: {e}")
    while True:
        try:
            loader = driver.find_element(
                By.CLASS_NAME, 'bpw-widget-btn bpw-floating-button bpw-anim-undefined')
            is_visible = loader.is_displayed()
            print('Initializing Jarvis...')

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Jarvis is Initializing.')
            break
        sleep(1)


def sendQuery(text):
    # Find and interact with the textarea element
    textarea = driver.find_element(By.ID, 'input-message')
    textarea.send_keys(text)
    sleep(1)

    send_btn = driver.find_element(By.ID, 'btn-send').click()
    sleep(1)


def isBubbleLoaderVisible():
    print('Jarvis Is Typing...')
    while True:
        try:
            bubble_loader = driver.find_element(
                By.CLASS_NAME, 'bpw-typing-group')
            is_visible = bubble_loader.is_displayed()

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print('Jarvis Is Sending Mesage...')
            break
        sleep(1)


chatnumber = 2


def retriveData():
    print('Retriving Chat...')
    global chatnumber
    sleep(1)
    p = driver.find_element(
        By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div/p')
    print("\nJarvis: " + p.text)
    chatnumber = chatnumber + 2
    return(p.text)


click_on_chat_button()
# def ai_brain():
#     query = input('\nYou: ')
#     sendQuery(query)
#     isBubbleLoaderVisible()
#     retriveData()


# /html/body/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[4]/div/div[2]/div/div/div/div/div/p
#/html/body/div/div/div/div[2]/div[1]/div/div/div[6]/div/div[2]/div/div/div/div/div/p