from pizzaReceipt import generateReceipt

TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
userToppings = []
pizzaOrder = []

answer = str(input("Do you want to order pizza? "))

if answer.lower() == "no" or answer.lower() == "q":
    generateReceipt(pizzaOrder)
else:
    doneOrder = False
    while doneOrder == False:
        #reset variables and lists for new order
        pizza = ()
        userToppings = []
        validAnswer = bool()
        size = str()

        while validAnswer != True:
            answer = str(input("\nChoose a size: S, M, L, or XL: ").upper())
            if answer == "S" or answer == "M" or answer == "L" or answer == "XL":
                size = (answer.upper())
                validAnswer = True

        doneToppings = False

        while doneToppings == False:
            print ("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n('")
            answer = str(input())
            if answer.upper() == "X": #if user is done order
                doneToppings = True
            elif answer.upper() == "LIST": #if user asks for list
                print(TOPPINGS)
            elif answer.upper() in TOPPINGS: #if user adds toppings
                print("Added {} to your pizza" .format(answer.upper()))
                userToppings.append(answer.upper()) #adds topping list to pizza
            else:
                print ("Invalid topping") #if topping invalid

        pizza = size, userToppings #create pizza
        pizzaOrder.append(pizza) #adds pizza to order list

        answer = str(input("\nDo you want to continue ordering? "))
        if answer.lower() == "no" or answer.lower() == "q":
            generateReceipt(pizzaOrder)
            doneOrder = True #exits order loop
        #repeats if ordering again




