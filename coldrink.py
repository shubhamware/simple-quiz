def greet(name):
    print(f"Hello {name.upper()} ")
    print("welcome to the shop!")

greet("Ramesh Ware")

def My_menu(**user):
    print(user)

My_menu(drink='mango',price=30)
My_menu(drink='watermelon',price=35)
My_menu(drink='grape',price=25)
My_menu(drink='orange',price=30)
My_menu(drink='apple',price=40)
My_menu(drink='Pomegranate',price=60)
My_menu(drink='Beet',price=40)
My_menu(drink='Cranberry',price=45)
My_menu(drink='Pineapple',price=50)

def My_order(drink,price,quantity):
    print(f"Sir/mam you order the {quantity} {drink} drinks and price of the drink is {price}")
    total= quantity*price
    print(f" Sir/madam Your bill is:{total} Rs")
    return total


    
a=My_order('watermelon',35,4)
b=My_order('apple',40,2)
total_bill=a+b
print(f"your total bill is:{total_bill} Rs")










    

    
    

    


        
    

    


    
    






    
