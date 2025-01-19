*** Settings ***
Library    actionLibrary.MathOperation

*** Test Cases ***
User should be able to add numbers
    ${result}    Add Numbers    2    3
    Log    ${result}
    Should Be Equal As Numbers    ${result}    5
