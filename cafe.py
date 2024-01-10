'''
Practical Task instructions:
Imagine you are running a cafe
  - Create a list called menu, which should contain at least four items sold in 
    the cafe.

  - Create a dictionary called stock, which should contain the stock 
    value for each item on your menu.

  - Create another dictionary called price, which should contain the prices for
    each item on your menu.

  - Calculate the total_stock worth in the cafe. 

  - Print out the result of your calculation
'''

'''
1. Create a list called "menu" containing four items sold in the cafe.
2. Create a dictionary called "stock" containing the value of each item.
3. Create another dictionary called "price" containing the prices of each item.
4. Create a variable called "total_stock" to store the worth of the cafe
   (0 - starts the count).

5. Create a for loop that iterates through each item in the menu.
6. Within the for loop, create an "item_value" variable that will store
   the value of each item through the calculation "stock[i] * price[i]".
   This calculation works by the for loop also iterating through stock and 
   price variables, acknowledging only the number of items and price as these 
   are the value (key : value).

7. Calculate the price of all of the items together, stored in "total_stock".
8. Print total_stock and round it to 2 decimal places.

'''

menu = ["Hot chocolate", "Crossaint", "Red velvet cupcake", "Caramel latte"]

stock = {"Hot chocolate" : 40, "Crossaint" : 10, "Red velvet cupcake" : 15,
"Caramel latte": 60}

price = {"Hot chocolate" : 2.50, "Crossaint" : 1.00, "Red velvet cupcake" : 1.50,
"Caramel latte" : 3.00}

total_stock = 0

for i in menu:
    item_value = stock[i] * price[i]
    total_stock += item_value

print(f" The total stock worth in the cafe is: £{total_stock:.2f}")
