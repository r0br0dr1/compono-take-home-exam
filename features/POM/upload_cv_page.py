import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UploadCVPage:
    def __init__(self, driver):
        self.driver = driver

    def click_upload_cv_if_available(self):
        try:
            # Wait for the element to be clickable
            upload_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='upload-cv-button']"))
            )
            # If the button is clickable, click it
            upload_button.click()
        except:
            # If the element is not clickable or not found, handle the exception
            print("Upload your CV button is not available or not clickable.")

    def click_upload_cv(self):
        self.driver.find_element(By.XPATH, "//button[@data-testid='upload-cv-button']").click()

    def upload_file(self, folder_path):
        """Uploads any file found in the specified folder."""
        # Iterate through the folder and find any file
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                self.driver.find_element(By.NAME, "cv-upload").send_keys(file_path)
                print(f"Uploaded file: {file_path}")
                return
        raise FileNotFoundError(f"No files found in folder: {folder_path}")

    def wait_for_upload(self, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, "//div[text()='Uploaded successfully']"))
            )
            return True
        except:
            return False

    def wait_for_upload_success(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Your CV has been uploaded, and your profile has been prefilled!']"))
        )

    def refresh_page(self):
        self.driver.refresh()

    def open_skills_experience(self):
        self.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile/experience-and-skills")

    def open_qualifications(self):
        self.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile/qualifications")

    def open_profile_page(self):
        self.driver.get("https://candidate-qa-test.dev.platform.compono.dev/profile")

    def close_overlay(self):
        self.driver.find_element(By.CSS_SELECTOR, "svg.CloseIconButton-sc-19wgu2s-0").click()