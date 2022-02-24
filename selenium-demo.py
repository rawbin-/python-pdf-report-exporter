import base64

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("http://www.baidu.com")
driver.add_cookie({
    "name": 'xxxtoken',
    "value": "sdvsdvsdv",
    "expires": -1,
    "path": "/",
    "domain": ".baidu.com"
})

result = driver.print_page()
with open('selenium-out.pdf', 'wb') as file:
    file.write(base64.b64decode(result))

driver.quit()
