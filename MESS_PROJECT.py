print("THIS IS VIT BHOPAL'S SAFAL MESS ,AUTOMATIC BEVERAGE SERVER MACHINE")
print("MESS STAFF IS REQUESTED TO PLEASE FILL THE MACHINE")

# taking input from the mess staff for the initial fill in the machine
milk_stored_L = float(input("enter the quantity of milk (in Litre)to store in machine"))
milk_stored = (milk_stored_L * 1000)
print("\n"*20)
coffee_stored_L = float(input("enter the quantity of coffee (in Lite)to store in machine"))
coffee_stored = (coffee_stored_L * 1000)
print("\n"*20)
tea_stored_L = float(input("enter the quantity of tea (in Litre)to store in machine"))
tea_stored = (tea_stored_L * 1000)
print("\n"*20)

# storing that entered value in the dictionary with the key value
stored_beverages = {
    'milk': milk_stored,
    'coffee': coffee_stored,
    'tea': tea_stored
}


# print(dict[stored_beverages])
# print(stored_beverages["milk"])

# this function helps to check for every order that is the enough amount of beverage left to serve
# if left it will return false else it will false
def check_stored_resources(order):
    if order == 1:
        # 120 ml of beverage will be served as per mess menu
        if stored_beverages['milk'] < 120:
            print("sorry insufficient milk needs a refill")
            return False
        return True
    if order == 2:
        if stored_beverages['coffee'] < 120:
            print("sorry insufficient coffee needs a refill")
            return False
        return True
    if order == 3:
        if stored_beverages['tea'] < 120:
            print("sorry insufficient tea needs a refill")
            return False
        return True


# this function will subtract the amount of beverage served from the original fill value
# it will keep the track of the remaining beverage left and will update the list
def make_beverage(order):
    if order == 1:
        stored_beverages['milk'] = (stored_beverages['milk'] - 120)
    elif order == 2:
        stored_beverages['coffee'] = (stored_beverages['coffee'] - 120)
    elif order == 3:
        stored_beverages['tea'] = (stored_beverages['tea'] - 120)
    else:
        print("wrong order please enter milk or coffee or tea")


# this function will print the dictionary individually with the updated amount of beverage lefy
def report():
    print("milk:",stored_beverages["milk"], "ml")
    print("coffee:",stored_beverages["coffee"], "ml")
    print("tea:",stored_beverages["tea"], "ml")


# this function will refill the machine and will add the amount of beverage if any left
def refill():
    milk_stored_L = float(input("enter the quantity of milk (in L)to store in machine"))
    milk_stored = (milk_stored_L * 1000)
    print("\n" * 20)
    stored_beverages['milk'] += milk_stored
    coffee_stored_L = float(input("enter the quantity of coffee (in L)to store in machine"))
    coffee_stored = (coffee_stored_L * 1000)
    print("\n" * 20)
    stored_beverages['coffee'] += coffee_stored
    tea_stored_L = float(input("enter the quantity of tea (in L)to store in machine"))
    tea_stored = (tea_stored_L * 1000)
    print("\n" * 20)
    stored_beverages['tea'] += tea_stored

def server():
    who_is = int(input("press 1 if you are a student \npress 2 if you are mess staff"))
    print("\n"*20)
    if who_is == 1:
        is_on = True
        while is_on:
            # this verification is replacing the face verification that mess face verification that we do
            # so it is referring to that only but because of the limited knowledge cant do that right now
            # so used a simple verification.
            verification = int(input("press 1 if you are alloted to safal messs \n"
                                     "press 2 if you are alloted mayuri mess\n"))
            print("\n" * 20)


            if verification == 1:
                order = int(input("press 1 if you like to have milk\n"
                                  "press 2 if you like to have coffee\n"
                                  "press 3 if you like to have tea\n"))


                # this will check resources every time for the loop so beverage will only be served
                # when there would be sufficient amount of beverage in the machine
                if check_stored_resources(order) == True:
                    # this make beverage function will help to deduct the amount from the original value
                    # and will return the actual amount after deduction for every cup
                    make_beverage(order)
                    if order == 1:
                        order = "milk"
                    elif order == 2:
                        order = "coffee"
                    elif order == 3:
                        order = "tea"
                    print("\n" * 20)

                    print(f"here is your 120 ml of  {order} ENJOY !")

                    is_on = False
                    server()
                # else:
            elif verification == 2:
                print("\n" * 20)
                print("sorry this is safal mess machine you have been alloted mayuri mess"
                          "the next machine to me is mayuri machine please take from there")

                server()


            else:
                print('wrong input')
                server()

    elif who_is==2:
        is_on = True
        while is_on:
            store = int(input("press 1 to refill the machine\n"
                              "press 2 to turn off the machine\n"
                              "press 3 to see the quantity left in the machine\n"))
            print("\n" * 20)
            if store == 1:
                refill()
                server()
            elif store == 2:
                is_on = False
            elif store == 3:
                report()
                server()
    else:
        print("wrong input")
        server()


server()







