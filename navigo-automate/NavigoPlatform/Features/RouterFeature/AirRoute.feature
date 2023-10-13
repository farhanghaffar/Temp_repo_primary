Feature: New Air routes

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened

    Scenario: Create New AirRoute
        Then Provide valid username and password
        And Click on the Login button
        And Login is successful and dashboard is opened
        And Click on Create New Route button
        And Enter all the details of Origin Airport
        And Enter all the details of Destination Airport

