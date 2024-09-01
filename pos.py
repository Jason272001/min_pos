SandiRubyJane, [7/15/2022 11:59 PM]
cart = {}

def welcome():
    print("Welcome to MooMart!")
    print("Thank you for choosing MooMart! We offer a great variety of goods of only the finest quality!")
    yesorno = input(" Is this your first time shopping here? (yes/no): ")
    while yesorno != "yes" and yesorno != "no":
        yesorno = input("If this is your first time shopping here, please key in \"yes\". If not, please key in \"no\". ")
    if yesorno == "yes":
        signup = input("Would you like to sign up for a free MooMart membership?")
        print("As a member, you will be the first few to know about our latest promotions, get exclusive offers and enjoy ADDITIONAL DISCOUNT!")
        if signup == "yes":
            email = input("Enter your email: ")
        if signup == "no":
            print()
    if yesorno == "no":
        print()
    print("Happy shopping!")
    main()


def display_menu():
    print()
    print("MAIN MENU")
    print(8*"-")
    print("1: Add items to cart")
    print("2: View and Edit items in shopping cart")
    print("3: Check-Out and Make Payment")
    print("4: Exit")
    print()


def main():
    choice = 0
    while choice != 4:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_items()
        elif choice == 2:
            view_edit()
        elif choice == 3:
            payment()
        elif choice == 4:
            print("Exiting page...\nHave a good day Sir/Ma'am! ")


def add_items():
    categories = {'A': 'Dairy', 'B': 'Packaged Goods', 'C': 'Canned Goods', 'D': 'Condiments/Sauces', 'E': 'Drinks & Beverages'}
    print()
    for key, value in categories.items():
        print("{}: {}".format(key, value, sep="\n"))
    category = input("Enter the alphabet that corresponds to the category of the item you are looking for: ")
    category = category.upper()
    while category not in categories:
        print("Invalid selection.\nPlease try again.")
        print()
        category = input("Enter the alphabet that corresponds to the category of the item you are looking for: ")
    if category == "A":
        dairy = {"Milk": 2.461, "Butter": 4.815, "Eggs": 3.638, "Cheese Slices": 3.3705,
                 "Evaporated Milk Creamer": 1.498, "Milo": 13.375, "Biscuits": 5.671, "Yogurt": 1.0165}
        while True:
            print(100 * "-")
            print(" * DAIRY * ")
            for key, value in dairy.items():
                print("{}: {:.2f}".format(key, value,sep = "\n"))
            option = input("What would you like to add into your cart?\n")
            option = option.title()
            if option in dairy:
                quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                stock = 300
                while quantity > stock:
                    print("The quantity you have entered exceeds the stock available currently.")
                    quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                cart.update({option:quantity})
                print("{} {} has been added to cart.".format(quantity, option))
                option2 = input("Would you like to...\n(A) Add more dairy products into your cart,\n OR"
                                "\n(B) Go back to Main Menu\n OR \n(C) Browse other categories?")
                if option2 == "A" or option2 == "a":
                    continue
                if option2 == "B" or option2 == "b":
                    main()
                if option2 == "c" or option2 == "C":
                    add_items()
            elif option not in dairy:
                print(
                    "The item you have chosen is not available in MooMart. We are sorry for the inconvenience caused.")
                option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                while option != "yes" and option != "no":
                    print(

SandiRubyJane, [7/15/2022 11:59 PM]
"Please enter \"yes\" if you would like to add more items into cart or \"no\" to proceed to Main Menu.")
                    print()
                    option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                if option == "no":
                    print("Heading back to main menu...")
                    main()
                elif option == "yes":
                    continue
    if category == "B":
        packaged = {"Bread": 2.889, "Cereal": 7.49, "Crackers": 3.317, "Chips": 2.782, "Raisin": 2.247, "Nuts": 2.14,
                    "Green Bean": 1.1235, "Barley": 1.1235}
        while True:
            print(100 * "-")
            print(" * PACKAGED GOODS * ")
            for key, value in packaged.items():
                print("{}: {:.2f}".format(key, value,sep = "\n"))
            option = input("What would you like to add into your cart? \n ")
            option = option.title()
            if option in packaged:
                quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                stock = 300
                while quantity > stock:
                    print("The quantity you have entered exceeds the stock available currently.")
                    quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                cart.update({option: quantity})
                print("{} {} has been added to cart.".format(quantity, option))
                option2 = input("Would you like to...\n(A) Add more dairy products into your cart,\n OR"
                                "\n(B) Go back to Main Menu\n OR \n(C) Browse other categories?")
                if option2 == "A" or option2 == "a":
                    continue
                if option2 == "B" or option2 == "b":
                    main()
                if option2 == "c" or option2 == "C":
                    add_items()
            elif option not in packaged:
                print("The item you have chosen is not available in MooMart. We are sorry for the inconvenience caused.")
                option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                while option != "yes" and option != "no":
                    print("Please enter \"yes\" if you would like to add more items into cart or \"no\" to proceed to Main Menu.")
                    print()
                    option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                if option == "no":
                    print("Heading back to main menu...")
                    main()
                elif option == "yes":
                    continue
    if category == "C":
        canned = {"Tomato": 1.5515, "Button Mushroom": 1.2305, "Baking Bean": 1.4445, "Tuna Fish": 1.5515,
                  "Kernel Corn": 1.3375, "Sardine Fish": 1.177, "Chicken Luncheon Meat": 2.0865,
                  "Pickled Lettuce": 1.0165}
        while True:
            print(100 * "-")
            print(" * CANNED GOODS * ")
            for key, value in canned.items():
                print("{}: {:.2f}".format(key, value,sep = "\n"))
            option = input("What would you like to add into your cart? \n ")
            option = option.title()
            if option in canned:
                quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                stock = 300
                while quantity > stock:
                    print("The quantity you have entered exceeds the stock available currently.")
                    quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                cart.update({option: quantity})
                print("{} {} has been added to cart.".format(quantity, option))
                option2 = input("Would you like to...\n(A) Add more dairy products into your cart,\n OR"

SandiRubyJane, [7/15/2022 11:59 PM]
"\n(B) Go back to Main Menu\n OR \n(C) Browse other categories?")
                if option2 == "A" or option2 == "a":
                    continue
                if option2 == "B" or option2 == "b":
                    main()
                if option2 == "c" or option2 == "C":
                    add_items()
            elif option not in canned:
                print("The item you have chosen is not available in MooMart. We are sorry for the inconvenience caused.")
                option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                while option != "yes" and option != "no":
                    print("Please enter \"yes\" if you would like to add more items into cart or \"no\" to proceed to Main Menu.")
                    print()
                    option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                if option == "no":
                    print("Heading back to main menu...")
                    main()
                elif option == "yes":
                    continue
    if category == "D":
        cs = {"Fine Salt": 0.856, "Sea Salt Flakes": 1.391, "Chicken Stock": 3.3705, "Chilli Sauce":2.8355,
              "Oyster Sauce": 4.815, "Sweet Soy Sauce": 4.0125, "Tomato Ketchup": 3.424, "Sesame Oil": 5.2965}
        while True:
            print(100 * "-")
            print(" * CONDIMENTS and SAUCES * ")
            for key, value in cs.items():
                print("{}: {:.2f}".format(key, value,sep = "\n"))
            option = input("What would you like to add into your cart?\n ")
            option = option.title()
            if option in cs:
                quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                stock = 300
                if quantity > stock:
                    print("The quantity you have entered exceeds the stock available currently.")
                    quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                cart.update({option: quantity})
                print("{} {} has been added to cart.".format(quantity, option))
                option2 = input("Would you like to...\n(A) Add more dairy products into your cart,\n OR"
                                "\n(B) Go back to Main Menu\n OR \n(C) Browse other categories?")
                if option2 == "A" or option2 == "a":
                    continue
                if option2 == "B" or option2 == "b":
                    main()
                if option2 == "c" or option2 == "C":
                    add_items()
            elif option not in cs:
                print("The item you have chosen is not available in MooMart. We are sorry for the inconvenience caused.")
                option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                while option != "yes" and option != "no":
                    print("Please enter \"yes\" if you would like to add more items into cart or \"no\" to proceed to Main Menu.")
                    print()
                    option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                if option == "no":
                    print("Heading back to main menu...")
                    main()
                elif option == "yes":
                    continue
    if category == "E":
        db = {"Green Tea Canned 300 Ml": 16.05, "Blackcurrant Ribena 300 Ml": 33.17, "100 Plus 24 Cans": 16.05,
              "Orange Cordial 2 Litre": 4.173, "Mineral Water 24 X 600 Ml": 7.49, "Pineapple Juice": 0.856,
              "Nescafe Coffee": 10.593, "Coke 24 Cans": 13.268}
        while True:
            print(100 * "-")
            print(" * DRINKS & BEVERAGES * ")
            for key, value in db.items():
                print("{}: {:.2f}".format(key, value,sep = "\n"))
            option = input("What would you like to add into your cart?\n")
            option = option.title()

SandiRubyJane, [7/15/2022 11:59 PM]
if option in db:
                quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                stock = 300
                if quantity > stock:
                    print("The quantity you have entered exceeds the stock available currently.")
                    quantity = int(input("Please input the quantity of {} you would like to purchase: ".format(option)))
                cart.update({option: quantity})
                print("{} {} has been added to cart.".format(quantity, option))
                option2 = input("Would you like to...\n(A) Add more dairy products into your cart,\n OR"
                                "\n(B) Go back to Main Menu\n OR \n(C) Browse other categories?")
                if option2 == "A" or option2 == "a":
                    continue
                if option2 == "B" or option2 == "b":
                    main()
                if option2 == "c" or option2 == "C":
                    add_items()
            elif option not in db:
                print("The item you have chosen is not available in MooMart. We are sorry for the inconvenience caused.")
                option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                while option != "yes" and option != "no":
                    print("Please enter \"yes\" if you would like to add more items into cart or \"no\" to proceed to Main Menu.")
                    print()
                    option = input("Is there anything else you would like to add into your cart? (yes/no): ")
                if option == "no":
                    print("Heading back to main menu...")
                    main()
                elif option == "yes":
                    continue