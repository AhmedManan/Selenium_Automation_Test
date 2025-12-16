# Selenium Automation Test

In this repository I have conduct Automation tests on multiple web application, specificly [DemoBlaze](https://demoblaze.com/index.html) & [SauceDemo](https://www.saucedemo.com/). To conduct the tests I used Python, Pytest, Selenium. To ensure Behavior-Driven Development (BDD) testing I used Behave. In both cases I implemented POM (page object model) structure.

## 🔎 View Live Report

* **Allure Report:** [View Allure Report](https://ahmedmanan.github.io/Selenium_Automation_Test/reports/allure-report/index.html)
* **HTML Report:** [View HTML Report](https://ahmedmanan.github.io/Selenium_Automation_Test/reports/report.html)


## Table Of Content
- [ View Live Report](#view-live-report)
- [Test Cases](#Test-Cases)
    - [Pytest Test List](#Pytest-Test-List)
    - [Behave BDD Test List](#Behave-BDD-Test-List)
- [Report Generation](#Report-Generation)


## Test Cases

### Pytest Test List

| Serial | Test Script Name / Details                                  | Status                   |
|--------|-------------------------------------------------------------|--------------------------|
| 01     | Test Demoblaze login with valid credentials                 | ✔️ |
| 02     | Test Demoblaze login with invalid credentials               | ✔️ |
| 03     | Test saucedemo login with valid credentials                 | ✔️ |
| 04     | Test saucedemo login with invalid credentials               | ✔️ |
| 05     | Test Saucedemo cart product adding & removing functionality | ✔️ |

### Behave BDD Test List
| Serial | Test Script Name / Details                                 | Status                   |
|--------|------------------------------------------------------------|--------------------------|
| 01     | Test Demoblaze login with valid credentials                | ✔️ |
| 02     | Test Demoblaze login with invalid parameterize credentials | ✔️ |

## Report Generation

#### Allure Report Generation

Generating Allure and HTML test reports in Pytest requires installing the necessary plugins and using specific command-line options.

First, Install the Allure Pytest adapter:
````bash
pip install allure-pytest
````
Now, Run your tests using the --alluredir option, which specifies the directory to save the raw Allure data files (usually JSON and TXT files).
````bash
pytest --alluredir=allure-results
````
Now, Use the Allure CLI tool to convert the collected data into an interactive HTML report and open it in your browser.
````bash
allure serve allure-results
````
To generate the static HTML report in the allure-report folder, which you can then view by opening the index.html file use 
````bash
allure generate allure-results -o allure-report
````
#### HTML Report Generation

A simple HTML report can be generated using the pytest-html plugin.
````bash
allure generate allure-results -o allure-report
````

Use the --html option, providing the name and path for the final HTML report file.
````bash
pytest --html=report.html --self-contained-html
````
A file named report.html (or whatever you specified) will be generated in your project directory. Open this file in any web browser to view the report.
