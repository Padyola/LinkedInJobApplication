from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "/Users/SEUPCAQUI/Desktop/chromeDriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.set_window_size(1920, 1080)
driver.get("Link da pagina do linkedin que voce quer")

sign_in_button = driver.find_element_by_link_text("Entrar")
sign_in_button.click()
email_field = driver.find_element_by_id("username")
email_field.send_keys("email123") #Seu email aqui

password_field = driver.find_element_by_id("password")
password_field.send_keys("Senha123") #Sua senha aqui
password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("Called")
    listing.click()
    time.sleep(1)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(1)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        phone.send_keys("")
        next_button = driver.find_element_by_css_selector("footer button")

        if  next_button.get_attribute("data-control-name") == "continue_unify":
            next_button.click()

        else:
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_element_by_xpath(
                "//button[contains(@class, 'artdeco-button')]//*[contains(.,'Descartar')]/..")
            discard_button.click()
            print("Complex aplication, skipped...")
            continue

        time.sleep(1)
        review_button = driver.find_element_by_class_name("artdeco-button--primary")

        if review_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_xpath(
                "//button[contains(@class, 'artdeco-button')]//*[contains(.,'Descartar')]/..")
            discard_button.click()
            print("Complex aplication, skipped...")
            continue

        else:
            review_button.click()
            time.sleep(1)
            submit_button = driver.find_element_by_class_name("artdeco-button--primary")
            if submit_button.get_attribute("data-control-name") == "submit_unify":
                submit_button.click()
                time.sleep(1)
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
            else:
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
                time.sleep(1)
                discard_button = driver.find_element_by_xpath(
                    "//button[contains(@class, 'artdeco-button')]//*[contains(.,'Discard')]/..")
                discard_button.click()
                print("Complex aplication, skipped...")
                continue

    except NoSuchElementException:
        print("No application button, skipped.")
        continue
