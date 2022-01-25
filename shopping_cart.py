i1= 0
i2=0
i3=0
 

cart = {
        "Vegetables" : ([i1]), 
        "Fruits" : ([i2]),
        "Meats" : ([i3])
    }    


print("Welcome to Eric's Emporium!")


running = True
while running:
    user_input = input("What are you shopping for today?" + " " "Vegetables/Fruits/Meats")

    if user_input.lower() == "vegetables":
        print(f"One vegetable has been added to your cart!")
        i1 = i1 +1
        cart["Vegetables"] = [i1]
    elif user_input.lower() == "fruits":
        print(f"One fruit has been added to your cart!")
        i2 = i2 +1
        cart["Fruits"] = [i2]
    elif user_input.lower() == "meats":
        print(f"One meat has been added to your cart!")
        i3 = i3 +1
        cart["Meats"] = [i3]
        
    input_is_valid =False
    while not input_is_valid:
        more_options = input(f"What would you like to do now? Keep shopping/View Cart/Go Home and Eat")
        if (more_options.lower() == "keep shopping"):
            input_is_valid =True
        elif (more_options.lower() == "view cart"):
            print(cart)
        elif (more_options.lower() == "go home and eat"):
            print(f"Come back again soon!")
            print(cart)
            input_is_valid= True
            running = False
            


