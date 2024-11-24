# 16 Coffee Machine OOP

This project is part of Day 16 of the _100 Days of Code: Python Pro Bootcamp_ by Dr. Angela Yu. It demonstrates the application of object-oriented programming (OOP) principles in Python, improving upon the Day 15 procedural Coffee Machine project. By utilizing pre-written external modules, the project emulates real-world programming practices, including modularization and reusability.  


## Table of Contents

- [Features](#features)
- [Modules Used](#modules-used)
- [Logic Workflow](#logic-workflow)
- [Expected Terminal Output](#expected-terminal-output)
- [Usage](#usage)


## Features

- Display a menu of drinks: **espresso**, **latte**, **cappuccino**.  
- Handle user commands like `report` and `off`.  
- Check if there are enough resources to make the selected drink.  
- Process user payments through virtual coin input and ensure sufficient funds.  
- Dispense coffee and deduct resources appropriately.  


## Modules Used

### 1. `coffee_maker.py`
Manages the machine’s resources (water, milk, coffee).  
- Generates reports of available resources.  
- Checks resource sufficiency for selected drinks.  
- Deducts resources after a drink is made.  

### 2. `menu.py`
Handles menu items and user drink selection.  
- Stores drink data (ingredients and cost).  
- Finds drinks based on user input.  

### 3. `money_machine.py`
Simulates a coin-operated payment system.  
- Processes coins entered by the user.  
- Checks if the payment is sufficient and calculates change.  
- Keeps track of total profits.  



## Logic Workflow

1. **Prompt User Input:**  
   The user is asked:  
   ```plaintext
   What would you like? (espresso/latte/cappuccino):  
   ```  

2. **Handle Special Commands:**  
   - If the user enters `off`, the program terminates.  
   - If the user enters `report`, the program displays the available resources and total money earned.  

3. **Validate Drink Selection:**  
   - If the drink exists, the program checks if resources are sufficient.  
   - If not, it displays an error message.  

4. **Process Payment:**  
   - User inputs the number of quarters, dimes, nickels, and pennies.  
   - If the payment is insufficient, money is refunded.  

5. **Dispense Drink:**  
   - Resources are deducted, and the selected drink is prepared.  
   - A message confirms successful preparation.  


## Expected Terminal Output

### Start Menu:
```plaintext
What would you like? (espresso/latte/cappuccino): latte
```

### Insufficient Resources:
```plaintext
Sorry there is not enough milk.
```

### Processing Coins:
```plaintext
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.50 in change.
```

### Dispensing Drink:
```plaintext
Here is your latte ☕️. Enjoy!
```

### Report Command:
```plaintext
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $3.00
```


## Usage

1. Clone the repository.
2. Run the `main.py` file to start the coffee machine simulation.

Enjoy your virtual coffee machine experience! ☕️

---
<section align="center">
  <code>coderBri © 2024</code>
</section>