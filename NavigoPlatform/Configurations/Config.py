import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def HeadlessChromeBrowser(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')  # Required for headless mode
    # options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'  # Set the path to Chrome 118
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(TestConfig.URL)


def ChromeBrowser(context):
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)  # Required for headless mode
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(TestConfig.URL)


def ChromeWithParamBrowser(context, headless_mode):
    options = webdriver.ChromeOptions()
    if headless_mode:
        options.add_argument('--headless=new')
    else:
        options.add_argument('start-maximized')
        options.add_experimental_option("detach", True)  # Required for headless mode
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.get(TestConfig.URL)


class TestConfig:
    BROWSER = 'chrome'
    MOZ_BROWSER = 'Mozilla'

    URL = "https://qa3-platform.navigo.global/apps/router"
    USERNAME = "automation@navigo-inc.com"
    PASSWORD = "1234" 

    IMPLICIT_WAIT = 10

    # Dynamically generate the log file name
    LogPath = "/Logs"
    TimeStamp = datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S")
    TimeOnly = str(datetime.datetime.now().now())
    LogFileName = "./Logs" + f"test_{TimeStamp}.log"
    logger = logging.getLogger(TimeOnly)
    logging.basicConfig(filename=LogFileName, level=logging.INFO)
