from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options ,service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

#Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
#login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username and password and click the button
username_field.send_keys('pythonusername')
password_field.send_keys('PythonStudent123$')
#login_button.click()
driver.execute_script("arguments[0].click();", login_button)

# Locate the Element dropdown
elements = (WebDriverWait(driver, 10)
           .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()

tex_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
tex_box.click()
# Locate the form fields and submit button
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form fields
fullname_field.send_keys('John Smith')
email_field.send_keys('johm@gmail.com')
current_address_field.send_keys('John Street 100, New York, USA')
permanent_address_field.send_keys('John Street 100, New York, USA')
driver.execute_script("arguments[0].click();", submit_button)

input("Press Enter to close the browser")
driver.quit()