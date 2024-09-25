Install python on Mac:
1. go to https://www.python.org/downloads/
2. download python
3. install python3
4. verify installation: python3 --version
5. verify pip3 is installed: pip3 --version
- if not installed: python3 -m ensurepip --upgrade

  
Open the terminal on the project directory

Install Allure on Mac
1. install Homebrew (if not already installed): /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. follow the installation steps
3. verify Homebrew installation: brew --version
4. install allure: brew install allure
5. verify allure installation: allure --version

Create a virtual environment (venv) on Mac
1. navigate to the project folder on terminal
2. create the virtual env: python3 -m venv venv
3. activate the virtual env: source venv/bin/activate

To install the required tools:
1. on the venv terminal: pip install -r requirements.txt

****
To manually install the requirement:
install Behave:
1. on the venv terminal: pip install behave
2. to verify behave: behave --version

install allure-behave
1. on the venv terminal: pip install allure-behave

install Selenium:
1. on the venv terminal: pip install selenium
*****

Run the test:
behave -f allure_behave.formatter:AllureFormatter -o allure-results

View results:
allure serve allure-results

--------

Install python on Windows:
1. go to https://www.python.org/downloads/
2. download python
3. install python
     - Select the checkbox “Add Python to PATH” at the bottom of the installation screen.
4. verify installation: python --version
5. verify pip is installed: pip --version
6. add python to Environment Variables
     - press Windows + R, type sysdm.cpl, and hit Enter
     - in the System Properties window, go to the Advanced tab.
     - select Environment Variables > System variables
     - find and select the variable named Path, then click Edit.
     - in the Edit Environment Variables window, click New and paste the path to your Python installation directory (e.g., C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python39\)
     - click New again and paste the path to the Scripts folder (e.g., C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python39\Scripts\)
     - click Ok to save
  
Install Allure on Windows:
1. install Java: Download the Java JDK from Oracle’s website or from AdoptOpenJDK.
2. download Allure: https://github.com/allure-framework/allure2/releases
     - allure-commandline.zip
3. Extract Allure
4. add Allure to Environment Variables
     - press Windows + R, type sysdm.cpl, and hit Enter
     - in the System Properties window, go to the Advanced tab.
     - select Environment Variables > System variables
     - find and select the variable named Path, then click Edit.
     - in the Edit Environment Variables window, click New and paste the path to the Allure bin directory
     - click Ok to save

Create a virtual environment (venv) on Windows:
1. open the terminal on the project directory
2. create a virtual env: python -m venv venv
3. activate the virtual env: venv\Scripts\activate

To install the required tools:
1. on the venv terminal: pip install -r requirements.txt

Run the test:
behave -f allure_behave.formatter:AllureFormatter -o allure-results

View results:
allure serve allure-results
