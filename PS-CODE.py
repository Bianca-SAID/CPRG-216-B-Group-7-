"""
CPRG-216-B
Group 7: Assignment: Programming Strategies
Description:
"""

from typing import final
discount_percentage:final =0.95
GST_percentage:final =0.05
movie_ticket_price = {
    "1": {"Avengers: Endgame": 12.00},
    "2": {"The Kitchen": 10.00},
    "3": {"Killers of the Flower Moon": 8.00},
    "4": {"Dune: Part Two": 9.50}
}

ticket_types = {
    "1": {"Standard": 0},
    "2": {"VIP": 5.0}
}

showTimes = {
    "1": "1:00 PM",
    "2": "4:30 PM",
    "3": "8:00 PM"
}

addons = {
    "1": {"3D Glasses": 3},
    "2": {"Popcorn Combo": 7}
}

continue_booking ="y"
while continue_booking=="y":
    print('*' * 50)
    print("{:>40}".format("Welcome to Movie Booking System"))
    print('*' * 50)
    print()
    print('*' * 50)
    print("{:>35}".format("Step 1: Select a Movie"))
    print('*' * 50)

    print("1. Avengers: Endgame ($12.00)\n2. The Kitchen ($10.00)\n3. Killers of the Flower Moon ($8.00)\n4. Dune: Part Two ($9.50)")
    movie = input("Your selection (1-4): ")
    if movie in movie_ticket_price:
        selected_movie = list(movie_ticket_price[movie].keys())[0]
        movie_price = float(movie_ticket_price[movie][selected_movie])
        print("Movie Price", movie_price)
        print(f"You selected '{selected_movie}' priced at ${movie_price}")
    else:
        print('Invalid Selection. Please choose a valid movie number.')
        break

    print('*' * 50)
    print("{:>38}".format("Step 2: Select a show time"))
    print('*' * 50)

    print("1. 1:00 PM\n2. 4:30 PM\n3. 8:00 PM")
    show = input("Your selection (1-3): ")
    if show in showTimes:
        print(f"You selected show time '{showTimes[show]}'")
    else:
        print("Invalid Selection. Please choose a valid show time number.")
        break

    print('*' * 50)
    print("{:>40}".format("Step 3: Choose Ticket type"))
    print('*' * 50)
    print("1. Standard (No additional charge)\n2. VIP (+$5.00)")
    ticket = input("Your selection (1-2): ")

    if ticket in ticket_types:
        ticket_type = list(ticket_types[ticket].keys())[0]
        additional_price = ticket_types[ticket][ticket_type]
        total_price = movie_price + additional_price
        print("total price at ticket type", total_price)
        print(f"You selected '{ticket_type}' ticket priced at ${total_price}")
    else:
        print('Invalid selection. Please choose a valid ticket type number.')
        break

    print("1. 3D Glasses (+$3.00)\n2. Popcorn (+$7.00)\n0. Proceed without more add-ons")
    selected_addons = set()
    addon_sum = 0
    adding_addons = True
    sub_total = 0

    while adding_addons:
        addon = input("Your selection (0-2): ")
        if addon in addons:
            if addon == "1" and addon in selected_addons:
                print("You cannot select 3D Glasses more than once")
            else:
                selected_addons.add(addon)
                selected_addon = list(addons[addon].keys())[0]
                selected_addon_price = addons[addon][selected_addon]
                addon_sum += selected_addon_price
                total_price += selected_addon_price
                print(f"'{selected_addon}' added for ${selected_addon_price}")
        elif addon == "0":
            print("Add-ons total: $", addon_sum)
            print("Total cost for this ticket: $", total_price)
            adding_addons = False
        else:
            print("Invalid selection. Please choose a valid add-on number.")

    request = input("Would you like to book another ticket? (Y/N): ")
    if request.lower() == 'n':
        if sub_total > 50:
            discount1 = discount_percentage * sub_total
            GST_Amount = GST_percentage * sub_total
            Total_amount = sub_total - (sub_total - discount1) + GST_Amount
            print("*****Billing Report****")
            print("Number of booked tickets")
            print(f"Subtotal before discounts", {sub_total})
            print("GST(5%)", GST_Amount)
            print("Total Amount", Total_amount)
        continue = False


















































