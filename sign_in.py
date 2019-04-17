import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wireless import Wireless


# Checking WiFi adapter
def setup_wifi(wireless):
	print('Checking WiFi adapter.')
	if not wireless.power():
		print('WiFi adapter is off.')
		quit()

	print('Checking WiFi Network.')
	if wireless.current() != 'TESTING':
		print("Not connected to the network 'TESTING'.")
		print("Currently connected to the network '" + wireless.current() + "'.")
		quit()


# Checking if already signed-in
def isAlreadySignedIn():
	print('Checking if already signed-in.')
	signedIn = False
	try:
		req = requests.get('http://clients3.google.com/generate_204')
		if req.status_code != 204:
			raise Exception
		else:
			signedIn = True
	except:
		pass

	if signedIn:
		print('Already signed-in.')
		quit()


# Sign In Precedure
def signIn():
	print('Signing-in.')
	options = Options()
	options.add_argument("--headless") # Remove this to see browser open filling credentials, etc
	browser = webdriver.Chrome(options=options)

	SITE = "http://172.16.1.230/" # You can use any http website here
	browser.get(SITE)

	username = browser.find_element_by_name('user.username')
	username.click()
	username.send_keys("manavjeet.cs17") # YOUR USERNAME

	password = browser.find_element_by_name('user.password')
	password.click()
	password.send_keys("abcd123") # YOUR PASSWORD

	browser.find_element_by_xpath("//input[@type='submit']").click()
	time.sleep(0.15)
	browser.find_element_by_xpath("//input[@type='submit']").click()
	time.sleep(0.15)
	browser.quit()


wireless = Wireless()

setup_wifi(wireless)
isAlreadySignedIn()
signIn()

print("Sign-In Complete")
