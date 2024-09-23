from selenium import webdriver
import allure
import subprocess
from pathlib import Path

def before_all(context):
    try:
        subprocess.check_call(["pip", "install", "--upgrade", "pip"])
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Pip packages updated and installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during pip installation: {e}")
        raise

    #WebDriver setup
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)

    project_folder = Path(__file__).parents[1].absolute()
    context.upload_folder = project_folder / "uploads"

    allure.dynamic.folder = "allure-results"

def after_all(context):
    context.driver.quit()
