from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.alert import Alert


class SkillsExperienceHandler:
    def __init__(self, driver):
        self.driver = driver

    def open_skills_experience(self):
        try:
            self.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile/experience-and-skills")
        except Exception as e:
            print(f"Failed to navigate to 'Experience and Skills' page: {e}")

    def open_qualifications(self):
        try:
            self.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile/qualifications")
        except Exception as e:
            print(f"Failed to navigate to 'qualifications' page: {e}")

    def check_for_delete_elements(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Delete')]"))
            )
            return True
        except TimeoutException:
            print("No element with 'delete' found.")
            return False

    def check_for_delete_elements_link(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.sc-eLExRp.chNjwi"))
            )
            return True
        except TimeoutException:
            print("No element with 'delete' found.")
            return False

    def delete_elements(self):
        try:
            while True:
                if not self.check_for_delete_elements():
                    break

                delete_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-dfVpRl.iLFcJp"))
                )

                parent_element = delete_button.find_element(By.XPATH, "../../..")

                delete_button.click()

                WebDriverWait(self.driver, 5).until(EC.alert_is_present())  # Wait for the alert to appear
                alert = Alert(self.driver)
                alert.accept()
                print("Accepted the confirmation dialog.")

                self.driver.refresh()
                WebDriverWait(self.driver, 5).until(
                    EC.staleness_of(parent_element)
                )

        except (NoSuchElementException, TimeoutException):
            print("No more elements to delete or an error occurred.")

    def delete_elements_link(self):
        try:
            while True:
                if not self.check_for_delete_elements_link():
                    break

                delete_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-eLExRp.chNjwi"))
                )

                parent_element = delete_button.find_element(By.XPATH, "../../..")

                delete_button.click()
                print("Clicked 'Delete' button.")

                WebDriverWait(self.driver, 5).until(EC.alert_is_present())  # Wait for the alert to appear
                alert = Alert(self.driver)
                alert.accept()
                print("Accepted the confirmation dialog.")

                self.driver.refresh()
                WebDriverWait(self.driver, 5).until(
                    EC.staleness_of(parent_element)
                )

        except (NoSuchElementException, TimeoutException):
            print("No more elements to delete or an error occurred.")

    def open_profile_page(self):
        self.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile")

    def handle_deletions(self):
        while self.check_for_delete_elements_link():
            self.delete_elements_link()
        self.open_skills_experience()  # Navigate to the Experience and Skills page
        while self.check_for_delete_elements():
            self.delete_elements()
        self.open_qualifications()
        while self.check_for_delete_elements():
            self.delete_elements()
        self.open_profile_page()

    def check_experience_skills_is_filled(self):
        self.open_skills_experience()
        self.check_for_delete_elements_link()



