"""
CPRG-216-B
Group 7: Assignment: Programming Strategies
Description:
"""

print('*' * 50)
print("Welcome to Movie Booking System")
print('*' * 50)

# Implementing the movie section
# Using the match case syntax
print('*' * 50)
print("Step 1: Select a Movie")
print('*' * 50)

print("1. Avengers: Endgame($12.00)\n2.The Kitchen($10.00)\n3.Killers of the Flower Moon($8.00)\n4.Dune:Part Two($9.50)")

movie = input("Your selection (1-4):")
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






#comment test test test