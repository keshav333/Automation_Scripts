 
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
msg_box = driver.find_element_by_xpath(inp_xpath)

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
