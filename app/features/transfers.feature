Feature: Transfers

Scenario: Making account for transfers
Given Number of accounts in registry equals: "0"
When I create an account using name: "Natalia", surname: "Nataliowa", pesel: "89092909800"
Then Number of accounts in registry equals: "1"
And Account with pesel "89092909800" exists in registry

Scenario: A succesful incoming transfer 
Given Account with pesel "89092909800" exists in registry
When A transfer for account with pesel "89092909800" with type "incoming" for amount "1000" is made
Then Account with pesel "89092909800" has balance "1000"
And The response message is "The order has been accepted"

Scenario: A succesful outgoing transfer
Given Account with pesel "89092909800" exists in registry
When A transfer for account with pesel "89092909800" with type "outgoing" for amount "400" is made
Then Account with pesel "89092909800" has balance "600"
And The response message is "The order has been accepted"

Scenario: A failed outgoing transfer
Given Account with pesel "89092909800" exists in registry
When A transfer for account with pesel "89092909800" with type "outgoing" for amount "1000" is made
Then Account with pesel "89092909800" has balance "600"
And The response message is "The order has NOT been accepted"

Scenario: A succesful express transfer 
Given Account with pesel "89092909800" exists in registry
When A transfer for account with pesel "89092909800" with type "express" for amount "200" is made
Then Account with pesel "89092909800" has balance "399"
And The response message is "The order has been accepted"

Scenario: A failed express transfer
Given Account with pesel "89092909800" exists in registry
When A transfer for account with pesel "89092909800" with type "express" for amount "1000" is made
Then Account with pesel "89092909800" has balance "399"
And The response message is "The order has NOT been accepted"

Scenario: Wrong type of transfer given
Given Account with pesel "89092909800" exists in registry
When A transfer for account with pesel "89092909800" with type "nieistniejacy" for amount "1000" is made
Then Account with pesel "89092909800" has balance "399"
And The response message is "Incorrect type of transfer"

Scenario: Deleting the account to clear the environment
Given Account with pesel "89092909800" exists in registry
When I delete account with pesel: "89092909800"
Then Account with pesel "89092909800" does not exist in registry
And Number of accounts in registry equals: "0"




