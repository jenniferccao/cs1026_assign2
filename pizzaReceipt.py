def generateReceipt(pizzaOrder):

    if len(pizzaOrder) > 0: #if pizzaOrder not empty, run

        print ("Your order: ")
        tax = float()
        total = float()
        subtotal = float()
        for i in range (len(pizzaOrder)): #reiterates for each pizza

            #reset variables
            baseCost = float()
            extraCost = float()
            extraToppings = bool()
            size = str()

            size = (pizzaOrder[i][0]) #get size
            baseCost = getPrice(size, "base") #use cost function for base cost

            print ("Pizza {}: {:<2}{:>24}" .format(i+1, size, baseCost)) #print pizza number, size, and base cost
            #print (size, end=" ") #print pizza size
            #print ("{:>20}" .format(baseCost)) #print base cost

            k = 0 #declare counter
            for k in range (0, (len(pizzaOrder[i][1]))): #accesses toppings
                print("- {}" .format(pizzaOrder[i][1][k])) #print ingredients

            if len(pizzaOrder[i][1]) > 3:
                extraToppings = True

            if extraToppings == True:
                x = 0
                extraCost += getPrice(size, "extra") * (len(pizzaOrder[i][1])-3) #calculates extra cost
                for x in range (0, (len(pizzaOrder[i][1])-3)):
                    if size == "XL":
                        print("Extra Topping ({:<}{:<2}{:>16.2f}".format(size, ")", getPrice(size, "extra"))) #prints extra costs for size XL
                    else:
                        print("Extra Topping ({:<}{:<2}{:>17.2f}".format(size, ")", getPrice(size, "extra"))) #prints extra costs for other sizes

            subtotal = float(subtotal + (baseCost + extraCost))

        tax = (subtotal) *0.13 #calculates tax
        total = (subtotal + tax) #calculates total with tax
        print ("Tax: {:>30.2f}" .format(tax))
        print ("Total: {:>28.2f}" .format(total))

    else: #reciept for empty order
        print("You did not order anything")

def getPrice(size, type):
    if type == "base":
        if size == "S":
            return (7.99)
        if size == "M":
            return (9.99)
        if size == "L":
            return (11.99)
        if size == "XL":
            return (13.99)
    if type == "extra":
        if size == "S":
            return (0.50)
        if size == "M":
            return (0.75)
        if size == "L":
            return (1.00)
        if size == "XL":
            return (1.25)


