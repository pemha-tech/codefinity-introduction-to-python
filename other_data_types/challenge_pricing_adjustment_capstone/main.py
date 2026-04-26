grocery_inventory = {"Milk":("Dairy",3.50,8,),"Eggs":("Dairy",5.50,30,),"Bread":("Bakery",2.99,15,),"Apples":("Produce",1.50,50)}
detail_Eggs = grocery_inventory.get("Eggs")
price_Eggs = detail_Eggs[1]
print("the price of Eggs is:",price_Eggs)
if price_Eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs":("Dairy",4.50,30)})
else:
    print("The price of Eggs is reasonnable.")
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)
detail_Milk = grocery_inventory.get("Milk")
stock_Milk = detail_Milk[2]
if stock_Milk < 10:
    stock_Milk = stock_Milk +20
    print("milk needs to be restocked. increasing stock by 20 units.")
    grocery_inventory.update({"Milk":("Dairy",3.50,28)})
else:
    print("Milk has sufficient stock")
detail_Apples = grocery_inventory.get("Apples")
price_Apples = detail_Apples[1]
if price_Apples > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price",grocery_inventory)
else:
    print("Updated inventory:",grocery_inventory)
    
    