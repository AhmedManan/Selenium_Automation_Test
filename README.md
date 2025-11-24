# Selenium Automation Test

In this repository I have conduct Automation tests on multiple web application, specificly [DemoBlaze](https://demoblaze.com/index.html) & [SauceDemo](https://www.saucedemo.com/). To conduct the test I used Python, Pytest, Selenium & POM (page object model) framework.

## 🔎 View Live Report

* **Allure Report:** [View Allure Report](https://ahmedmanan.github.io/Selenium_Automation_Test/reports/allure-report/index.html)
* **HTML Report:** [View HTML Report](https://ahmedmanan.github.io/Selenium_Automation_Test/reports/report.html)


## Table Of Content
- [🔎 View Live Report](#-view-live-report)
- [Test Cases](#-test-cases)
    - [Test Execution Videos](#-test-execution-videos)
    - [Test Case Details](#-test-case-details)
- [Report Genaration](#-report-genaration)


## Test Cases

### Test Execution Videos

### Test Case Details

## Report Genaration

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
