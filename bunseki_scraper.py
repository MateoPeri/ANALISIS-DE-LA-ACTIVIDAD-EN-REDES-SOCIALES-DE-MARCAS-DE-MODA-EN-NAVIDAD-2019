import bs4, requests, os, time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

marcas = ['nike','adidas','zara','hm','dior','gucci','levis','ralphlauren',
          'calvinklein','forever21','lacoste','puma','tommyhilfiger','louisvuitton',
          'vans','boss','chanelofficial']

url = 'https://bunseki.me/report/{}/instagram/2019-12-22/2020-01-22'
downloadDir = r'D:\Users\mateo\OneDrive - meligrana.com\Documentos\Deberes\inv\Scripts\data'
# NO HACE FALTA LOGIN PARA DESCARGAR CSV!!!
'''
user = 'pedroperranca@gmail.com'
pwd = '1234abcd'

browser = webdriver.Firefox()
browser.get('https://bunseki.me/login')

userElem = browser.find_element_by_css_selector('div.form-group:nth-child(1) > input:nth-child(1)')
userElem.send_keys(user)
pwdElem = browser.find_element_by_css_selector('div.form-group:nth-child(2) > input:nth-child(1)')
pwdElem.send_keys(pwd)
pwdElem.send_keys(Keys.ENTER)
'''

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.preferences.instantApply", True)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", downloadDir)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml")
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.folderList", 2)

browser = webdriver.Firefox(firefox_profile=fp)
time.sleep(5)
for m in marcas: # solo 1 pq tarda mucho
    browser.get(url.format(m))
    browser.find_element_by_css_selector('.align-self-start').click()
    time.sleep(5)
