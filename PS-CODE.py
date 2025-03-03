"""
CPRG-216-B
Group 7: Assignment: Programming Strategies
Description:
"""
from json.encoder import INFINITY

movie_ticket_price ={
    "1":{"Avengers:Endgame":12.00},
    "2":{"The Kitchen":10.00},
    "3":{"Killers of the Flower Moon":8.00},
    "4":{ "Dune:Part Two":9.50}
}

ticket_types={
    "1":{"Standard":0},
    "2": {"VIP":5},
    "3": {"":0.0}
}

addons={
    "1": {"3D Glasses" :3.00},
    "2": {"Popcorn Combo":7.00}
}



print('*' * 50)
print("{:>40}".format("Welcome to Movie Booking System"))
print('*' * 50)
print()
print('*' * 50)
print("{:>35}".format("Step 1: Select a Movie"))
print('*' * 50)

print("1. Avengers: Endgame ($12.00)\n2. The Kitchen ($10.00)\n3. Killers of the Flower Moon ($8.00)\n4. Dune:Part Two ($9.50)")
movie = input("Your selection (1-4): ")
if movie in movie_ticket_price:
    selected_movie = list(movie_ticket_price[movie].keys())[0]

    price = movie_ticket_price[movie][selected_movie]

    print(f"You selected '{selected_movie}' priced at ${price}")
else:
    print('Invalid Selection. Please choose a valid movie number.')
    exit()


print('*' * 50)
print("{:>38}".format("Step 2: Select a show time"))
print('*' * 50)


print("1. 1:00 PM\n2. 4:30 PM\n3. 8:00 PM")
show = input("Your selection (1-3): ")

match show:
    case "1":
        print("You selected show time '1:00 PM'")
    case "2":
        print("You selected show time '4:30 PM'")
    case "3":
        print("You selected show time '8:00 PM'")
    case _:
        print('Invalid Selection. Please choose a valid show time number.')
        exit()



print('*' * 50)
print("{:>40}".format("Step 3: Choose Ticket type"))
print('*' * 50)
print("1. Standard (No additional charge)\n2. VIP (+$5.00)")
ticket = input("Your selection (1-2): ")
if ticket in ticket_types:
    ticket_type = list(ticket_types[ticket].keys())[0]
    additional_price = ticket_types[ticket][ticket_type]
    total_price = price + additional_price
    print(f"You selected '{ticket_type}' ticket priced at ${total_price}")
else:
    print('Invalid selection. Please choose a valid ticket type number.')
    exit()



print("1. 3D Glasses (+$3.00)\n2. Popcorn (+$7.00)\n0.Proceed without more add-ons")
limit=0
addons_tracker =0
addon_mini_price=0
while True:
    addon = input("Your selection (0-2): ")

    if addon in addons:
        selected_addon = list(addons[addon].keys())[0]
        additional_addon_price = addons[addon][selected_addon]
        total_addon_price = addons_tracker + additional_addon_price
        addon_mini_price = total_addon_price
        additional_price = addons[addon][selected_addon]
        total_price = total_price + additional_price

        if limit >=1 and addon == "1":
            print("You cannot select 3D Glasses more than once")
        else:
            limit +=1
            print(f"'{selected_addon}' added for ${additional_price}")
    if addon== "0":
        print("Add-ons total:$",addon_mini_price)
        print("Total cost for this ticket:$",total_price)




















    # match selection:
    #     case "1":
    #         if limit >= 1:
    #             print("You cannot select 3D Glasses more than once.")
    #         else:
    #             limit += 1
    #             total_addons_cost += addons['3D Glasses']
    #             print(f"3D Glasses added for (${addons['3D Glasses']})")
    #
    #     case "2":
    #         total_addons_cost += addons['Popcorn Combo']
    #         print(f"Popcorn Combo added for (${addons['Popcorn Combo']})")
    #
    #     case "0":
    #         print("Add-ons total:$0.00")
    #         # if ticket in ticket_data:
    #         #     print("Total cost for the ticket is ",ticket_data[ticket])
    #
    #         if ticket == "1":
    #             print("Total cost for this ticket is ", ticket_types['1'])
    #         else:
    #             print("Total cost for this ticket is ", ticket_types['2'])
    #         print("Would you like to continue? (y/n)")



        # case _:
        #     print("Invalid selection. Please choose a valid option.")
        # continue_choice = input("Would you like to continue? (y/n): ")
        # if continue_choice.lower() != 'y':
        # break














# ======================================================================================================
# COST CALCULATION



