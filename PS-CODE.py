"""
CPRG-216-B
Group 7: Assignment: Programming Strategies
Description:
"""

#Format Ticket 
print('*' * 50)
print("{:>40}".format("Welcome to Movie Booking System"))
print('*' * 50)
print()
print('*' * 50)
print("{:>35}".format("Step 1: Select a Movie"))
print('*' * 50)

print("1. Avengers: Endgame ($12.00)\n2. The Kitchen ($10.00)\n3. Killers of the Flower Moon ($8.00)\n4. Dune:Part Two ($9.50)")

#Implement movie Selection
movie = input("Your selection (1-4): ")
match movie:
    case "1":
        print("You selected 'Avengers:Endgame' priced at $12.00")
    case "2":
        print("You selected ' The Kitchen' priced at $10.00")
    case "3":
        print("You selected 'Killers of the Flower Moon ' priced at $8.00")
    case "4":
        print("You selected ' Dune: Part Two' priced at $9.50")
    case _:
        print('Invalid Selection. Please choose a valid movie number.')

print()
print('*' * 50)
print("{:>38}".format("Step 2: Select a show time"))
print('*' * 50)

#Implement show time selection
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

#Ticket type selection table 3:
print('*' * 50)
print("{:>40}".format("Step 3: Choose Ticket type"))
print('*' * 50)
print("1. Standard (No additional charge)\n2. VIP (+$5.00)")
 
ticket = input("Your selection (1-2): ")
match ticket:
    case "1":
        print("You choose ticket 'You selected 'Standard' ticket priced at $12.00'")    
    case  "2":
        print("You selected 'VIP' ticket priced at $15.00")
    case _:
        print('Invalid selection. Please choose a valid ticket type number.')

print(f"Total amount {51.45:>29.2f}")
print('*' * 50)
print("Thank you for choosing Movie Booking System!")




