from selenium import webdriver
import telegram

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.instagram.com/p/CZ3S-2KjwLu/')
driver.save_screenshot("screenshot.png")
driver.quit()

TELEGRAM_BOT_TOKEN = '5178704848:AAFBm3sleUn3aVBRNd4t5Zw6K-xIeRjdQ4s'
TELEGRAM_CHAT_ID = '-790475399'
PHOTO_PATH = 'screenshot.png'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="From Telegram Bot")

bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))