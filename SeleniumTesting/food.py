from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
import os
load_dotenv()

def test_1(driver, url):
    '''
    Verify that a web page title matches an expected value.
    '''
    driver.get(url)
    title = driver.title
    print("Test case 1: Verify that a web page title matches an expected value.")
    if title == "Wastella":
        print(Fore.GREEN + "Test passed")
    else:
        print(Fore.RED + "Test failed")
    print(Style.RESET_ALL)

def test_2(driver, url):
    '''
    Verify that no login is possible with empty email.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys("")
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 2: Verify that no login is possible with empty email.")
    try:
        WebDriverWait(driver, 8).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_3(driver, url):
    '''
    Verify that no login is possible with empty password.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys("")

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 3: Verify that no login is possible with empty password.")
    try:
        WebDriverWait(driver, 8).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_4(driver, url):
    '''
    Verify that no login is possible with wrong email.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys("wrongemail@gmail.com")
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 4: Verify that no login is possible with wrong email.")
    try:
        WebDriverWait(driver, 8).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_5(driver, url):
    '''
    Verify that no login is possible with wrong email format.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys("tester1.com")
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 5: Verify that no login is possible with wrong email format.")
    try:
        WebDriverWait(driver, 8).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_6(driver, url):
    '''
    Verify that login is possible with correct credentials.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 6: Verify that login is possible with correct credentials.")
    try:
        WebDriverWait(driver, 8).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.GREEN + "Test passed")  
      
    except Exception as e:
        print(Fore.RED + "Test failed")

    print(Style.RESET_ALL)

def test_7(driver, url):
    '''
    Verify if show password works correctly
    '''
    driver.get(url)
    
    eye_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/div/button/span[1]")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")

    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))
    eye_button.click()
    input_type = password_field.get_attribute("type")
    print(input_type)

    print("Test case 7: Verify if show password works correctly.")
    if input_type == "text":
        print(Fore.GREEN + "Test passed")
    else:
        print(Fore.RED + "Test failed")
    print(Style.RESET_ALL)

def test_8(driver, url):
    '''
    Verify that sign up is not posssible with empty first name.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("apoorv@gmail.com")
    password_field.send_keys("apoorv123")
    passwordRepeat_field.send_keys("apoorv123")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 8: Verify that sign up is not posssible with empty first name.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_9(driver, url):
    '''
    Verify that sign up is not posssible with empty last name.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("")
    email_field.send_keys("apoorv@gmail.com")
    password_field.send_keys("apoorv123")
    passwordRepeat_field.send_keys("apoorv123")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 9: Verify that sign up is not posssible with empty last name.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_10(driver, url):
    '''
    Verify that sign up is not posssible with empty email.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("")
    password_field.send_keys("apoorv123")
    passwordRepeat_field.send_keys("apoorv123")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 10: Verify that sign up is not posssible with empty email.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_11(driver, url):
    '''
    Verify that sign up is not posssible with empty password.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("apoorv@gmail.com")
    password_field.send_keys("")
    passwordRepeat_field.send_keys("apoorv123")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 11: Verify that sign up is not posssible with empty password.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_12(driver, url):
    '''
    Verify that sign up is not posssible with empty repeat password.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("apoorv@gmail.com")
    password_field.send_keys("apoorv123")
    passwordRepeat_field.send_keys("")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 12: Verify that sign up is not posssible with empty repeat password.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_13(driver, url):
    '''
    Verify that sign up is not posssible with non matching passwords.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("apoorv11@gmail.com")
    password_field.send_keys("apoorv123")
    passwordRepeat_field.send_keys("apoorv12")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 13: Verify that sign up is not posssible with non matching passwords.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_14(driver, url):
    '''
    Verify that sign up is posssible with correct credentials.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("apoorv12@gmail.com")
    password_field.send_keys("apoorv123")
    passwordRepeat_field.send_keys("apoorv123")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 14: Verify that sign up is posssible with correct credentials.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.GREEN + "Test passed")  
      
    except Exception as e:
        print(Fore.RED + "Test failed")

    print(Style.RESET_ALL)

def test_15(driver, url):
    '''
    Verify that sign up is not posssible without strong password.
    '''
    driver.get(url)
    
    goToSignUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[2]/div/button/span[1]")
    goToSignUp_button.click()

    # wait until a 3rd field is visible in the form (login page only has 2)
    wait = WebDriverWait(driver, 5)
    form_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")))

    firstName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    lastName_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[3]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[4]/div/div/input")
    passwordRepeat_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[5]/div/div/input")

    firstName_field.send_keys("Apoorv")
    lastName_field.send_keys("Pandit")
    email_field.send_keys("apoorv14@gmail.com")
    password_field.send_keys("apoorv")
    passwordRepeat_field.send_keys("apoorv")

    signUp_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]")
    signUp_button.click()
    expected_url = "http://localhost:3000/"
    print("Test case 15: Verify that sign up is not posssible without strong password.")
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
        # WebDriverWait(driver, 20).until(driver.current_url == expected_url)
        print(Fore.RED + "Test failed")  
      
    except Exception as e:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_16(driver, url):
    '''
    Verify that logout button redirects to login page.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"

    print("Test case 16: Verify that logout button redirects to login page.")
    try:
      WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
      logout_button = driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/button/span[1]")
      logout_button.click()
 
      expected_login_url = "http://localhost:3000/auth"

      try:
        WebDriverWait(driver, 5).until(EC.url_to_be(expected_login_url))
        print(Fore.GREEN + "Test passed")
      
      except Exception as e:
        print(Fore.RED + "Test failed")

    except Exception as e:
      print(Fore.RED + "Login failed")

    print(Style.RESET_ALL)

def test_17(driver, url):
    '''
    Verify that if not logged in, sign in button shows up.
    '''
    driver.get(url)
    
    signIn_button = driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/a/span[1]")
    span_text = signIn_button.text

    print("Test case 17: Verify that if not logged in, sign in button shows up.")
    if span_text == "SIGN IN":
        print(Fore.GREEN + "Test passed")
    else:
        print(Fore.RED + "Test failed")

    print(Style.RESET_ALL)

def test_18(driver, url):
    '''
    Verify that if logged in, logout button shows up.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"

    try:
      WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
      logout_button = driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/button/span[1]")
      span_text = logout_button.text

      print("Test case 18: Verify that if logged in, logout button shows up.")
      if span_text == "LOGOUT":
          print(Fore.GREEN + "Test passed")
      else:
          print(Fore.RED + "Test failed")

      print(Style.RESET_ALL)


    except Exception as e:
      print(Fore.RED + "Login failed")

    print(Style.RESET_ALL)

def test_19(driver, url):
    '''
    Verify that if logged out, accept buttons are disabled.
    '''
    driver.get(url)
    
    wait = WebDriverWait(driver, 5)
    accept_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div/div[5]/button")))

    print("Test case 19: Verify that if logged out, accept buttons are disabled.")
    if accept_button.is_enabled():
        print(Fore.RED + "Test failed")
    else:
        print(Fore.GREEN + "Test passed")

    print(Style.RESET_ALL)

def test_20(driver, url):
    '''
    Verify that if contact no. not entered, post is not possible.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"

    try:
      WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
      contact_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/div[1]/div/input")
      description_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/div[2]/div/textarea")
      submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/button[1]/span[1]")

      contact_field.send_keys("")
      description_field.send_keys("Location: Varje, Pune - 41105 Quantity: 7Kg Type: non-preservable")

      submit_button.click()
      sleep(5)

      page_source = driver.page_source
      desired_text = "Location: Varje, Pune - 41105 Quantity: 7Kg Type: non-preservable"

      print("Test case 20: Verify that if contact no. not entered, post is not possible.")
      if desired_text in page_source:
          print(Fore.RED + "Test failed")
      else:
          print(Fore.GREEN + "Test passed")

      print(Style.RESET_ALL)


    except Exception as e:
      print(Fore.RED + "Login failed")

    print(Style.RESET_ALL)

def test_21(driver, url):
    '''
    Verify that if description not entered, post is not possible.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"

    try:
      WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
      contact_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/div[1]/div/input")
      description_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/div[2]/div/textarea")
      submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/button[1]/span[1]")

      contact_field.send_keys("1234567891")
      description_field.send_keys("")

      submit_button.click()
      sleep(5)

      page_source = driver.page_source
      desired_text = "1234567891"

      print("Test case 21: Verify that if description not entered, post is not possible.")
      if desired_text in page_source:
          print(Fore.RED + "Test failed")
      else:
          print(Fore.GREEN + "Test passed")

      print(Style.RESET_ALL)


    except Exception as e:
      print(Fore.RED + "Login failed")

    print(Style.RESET_ALL)

def test_22(driver, url):
    '''
    Verify that if contact and description is entered, post is successfull.
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"

    try:
      WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
      contact_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/div[1]/div/input")
      description_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/div[2]/div/textarea")
      submit_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div/form/button[1]/span[1]")

      contact_field.send_keys("1234567892")
      description_field.send_keys("Location: kothrud, pune - 41103 Quantity: 12Kg Type: Non - Preservable")

      submit_button.click()
      sleep(5)

      page_source = driver.page_source
      desired_text = "Location: kothrud, pune - 41103 Quantity: 12Kg Type: Non - Preservable"

      print("Test case 22: Verify that if contact and description is entered, post is successfull.")
      if desired_text in page_source:
          print(Fore.GREEN + "Test passed")
      else:
          print(Fore.RED + "Test failed")

      print(Style.RESET_ALL)


    except Exception as e:
      print(Fore.RED + "Login failed")

    print(Style.RESET_ALL)

def test_23(driver, url):
    '''
    Verify that others accept button is clickable 
    '''
    driver.get(url)
    
    email_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[1]/div/div/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/div[1]/div[2]/div/div/input")
    email_field.send_keys(os.getenv("FOODAPP_EMAIL"))
    password_field.send_keys(os.getenv("FOODAPP_PASSWORD"))

    login_button = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button[1]/span[1]")
    login_button.click()
    expected_url = "http://localhost:3000/"

    try:
      WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))

      wait = WebDriverWait(driver, 5)
      accept_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div/div[5]/button")))

      print("Test case 23: Verify that others accept button is clickable ")
      if accept_button.is_enabled():
          accept_button.click()
          sleep(2)
          print(Fore.GREEN + "Test passed")
      else:
          print(Fore.RED + "Test failed")

      print(Style.RESET_ALL)

    except Exception as e:
      print(Fore.RED + "Login failed")

    print(Style.RESET_ALL)

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')  # Set log level to suppress warnings
    chrome_options.add_argument(f'--disable-logging')  # Disable logging to avoid log messages

    driver = webdriver.Chrome(options=chrome_options)

    test_1(driver, "http://localhost:3000/")
    test_2(driver, "http://localhost:3000/auth")
    test_3(driver, "http://localhost:3000/auth")
    test_4(driver, "http://localhost:3000/auth")
    test_5(driver, "http://localhost:3000/auth")
    test_5(driver, "http://localhost:3000/auth")
    test_6(driver, "http://localhost:3000/auth")
    test_7(driver, "http://localhost:3000/auth")
    test_8(driver, "http://localhost:3000/auth")
    test_9(driver, "http://localhost:3000/auth")
    test_10(driver, "http://localhost:3000/auth")
    test_11(driver, "http://localhost:3000/auth")
    test_12(driver, "http://localhost:3000/auth")
    test_13(driver, "http://localhost:3000/auth") # change email after use
    test_14(driver, "http://localhost:3000/auth") # change email after use
    test_15(driver, "http://localhost:3000/auth") # change email after use
    test_16(driver, "http://localhost:3000/auth") 
    test_17(driver, "http://localhost:3000/") 
    test_18(driver, "http://localhost:3000/auth") 
    test_19(driver, "http://localhost:3000/") 
    test_20(driver, "http://localhost:3000/auth") 
    test_21(driver, "http://localhost:3000/auth") 
    test_22(driver, "http://localhost:3000/auth") 
    test_23(driver, "http://localhost:3000/auth") 

    driver.quit()

    # use powershell for coloured output
    #  .\env\Scripts\activate