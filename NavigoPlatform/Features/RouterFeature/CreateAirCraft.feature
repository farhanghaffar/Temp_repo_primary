Feature: Create New Aircrafts

    Background:
        Given Launch the browser
        When Open the router app https://qa2-platform.navigo.global/apps/router/
        Then The login portal has been opened
        And Provide valid username and password
        And Click on the Login button
        Then Login is successful and dashboard is opened

    @CreateAircraft
    Scenario: Create New AirCraft
        And Click on Tabs Aircraft and Available Aircraft
        And Click on Create New Aircraft Btn
        And Enter all Aircraft Details
        And Upload Seat Schematics file
        And Goto Seat Availability Tab and upload Seat which is less than total number of available Seats
        Then Save Aircraft
        Then Verify its been Create or not
