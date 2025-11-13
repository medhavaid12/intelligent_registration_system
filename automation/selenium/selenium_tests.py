from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import os

# prepare output directory
out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'screenshots')
os.makedirs(out_dir, exist_ok=True)
log_path = os.path.join(out_dir, 'selenium_results.log')

# use webdriver-manager to install / manage chromedriver
driver = None
try:
  driver_path = ChromeDriverManager().install()
  service = Service(driver_path)
  driver = webdriver.Chrome(service=service)
except Exception as e:
  # fallback: try to use chromedriver on PATH or system-installed ChromeDriver
  print('webdriver-manager failed to install driver, falling back to system chromedriver. Error:', e)
  driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8000/web/index.html')

def save(name):
  path = os.path.join(out_dir, name)
  driver.save_screenshot(path)
  return path

with open(log_path, 'w', encoding='utf-8') as log:
  try:
    # Negative scenario
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'email').send_keys('john@example.com')
    driver.find_element(By.ID, 'phone').send_keys('+911234567890')
    driver.find_element(By.CSS_SELECTOR, 'input[value="Male"]').click()
    driver.find_element(By.ID, 'password').send_keys('Pass@123')
    driver.find_element(By.ID, 'submitBtn').click()
    time.sleep(1)
    msg = driver.find_element(By.ID, 'resultMsg').text
    s1 = save('negative.png')
    log.write('Negative: ' + msg + '\n')
    log.write('Negative screenshot: ' + s1 + '\n')

    # Positive scenario
    driver.refresh()
    driver.find_element(By.ID, 'firstName').send_keys('John')
    driver.find_element(By.ID, 'lastName').send_keys('Doe')
    driver.find_element(By.ID, 'email').send_keys('john@example.com')
    driver.find_element(By.ID, 'phone').send_keys('+911234567890')
    driver.find_element(By.CSS_SELECTOR, 'input[value="Male"]').click()
    driver.find_element(By.ID, 'password').send_keys('Pass@123')
    driver.find_element(By.ID, 'submitBtn').click()
    time.sleep(1)
    msg2 = driver.find_element(By.ID, 'resultMsg').text
    s2 = save('positive.png')
    log.write('Positive: ' + msg2 + '\n')
    log.write('Positive screenshot: ' + s2 + '\n')

  except Exception as e:
    log.write('ERROR: ' + str(e) + '\n')
    save('error.png')
  finally:
    driver.quit()

print('Artifacts written to:', out_dir)
