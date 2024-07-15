Coffee Machine Program

User Interaction

1. Drink Selection
   - Prompt: `"What would you like? (espresso/latte/cappuccino):"`
   - Action: Based on the user's input, the machine will prepare the selected drink.
   - Note: This prompt will reappear after each action to serve the next customer.

2. Turning Off the Machine
   - Command: Enter `"off"` at the prompt.
   - Function: Maintainers can use this command to turn off the machine, ending the program.

3. Generating a Report
   - Command: Enter `"report"` at the prompt.
   - Function: Displays the current resource levels, such as:
     ```
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
     ```

Resource Management

4. Checking Resources
   - Function: Ensure there are enough resources to make the selected drink.
   - Example: If a latte requires 200ml of water but only 100ml is available, the machine will respond with: `"Sorry, there is not enough water."`

Financial Transactions

5. Processing Coins
   - Action: Prompt the user to insert coins if there are enough resources.
   - Coin Values: 
     - Quarters = $0.25
     - Dimes = $0.10
     - Nickels = $0.05
     - Pennies = $0.01
   - Calculation: Sum the monetary value of the inserted coins. Example:
     ```
     1 quarter + 2 dimes + 1 nickel + 2 pennies = $0.52
     ```

6. Validating Transactions
   - Action: Check if the user has inserted enough money for the selected drink.
   - Insufficient Funds: If not enough, the machine will respond with: `"Sorry, that's not enough money. Money refunded."`
   - Sufficient Funds: The cost of the drink is added to the machine's total profit.
   - Change: If too much money is inserted, the machine provides change, rounded to two decimal places. Example: `"Here is $2.45 in change."`

Making Coffee

7. Brewing the Drink
   - Action: If the transaction is successful and there are sufficient resources, the machine deducts the ingredients from its inventory.
   - Example Report Before and After:
     ```
     Before purchasing latte:
     Water: 300ml
     Milk: 200ml
     Coffee: 100g
     Money: $0

     After purchasing latte:
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
     ```
   - Completion: Notify the user with: `"Here is your latte. Enjoy!"` (or the selected drink).
