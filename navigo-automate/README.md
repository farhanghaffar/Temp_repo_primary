## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.

Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**configuration** directory contains the configuration files

**drivers** One can use the headless driver for that

**requirements.txt** TBD

**reports** TBD



### **Commands to run the tests**

**To run the test with allure report**  TDB
`behave -f allure_behave.formatter:AllureFormatter -o reports/ NavigoPlatform/features/login.feature`

[comment]: <> (updated by Farhan)
**To run the test without allure report** `behave NavigoPlatform/features/login.feature`

**To generate the html allure report from the json files inside reports folder**
`allure serve reports/`   TDB
