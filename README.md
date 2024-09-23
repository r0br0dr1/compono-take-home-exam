Install python on Mac
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

Create a virtual environment (venv)
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

