Feature: Upload CV Functionality

  Scenario: Upload a CV and verify if data is captured
    Given the upload cv is available on the webpage
    When I upload a CV
    Then CV is uploaded successfully and data is captured
