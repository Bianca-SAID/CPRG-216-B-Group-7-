# CPRG-216-B-Group-7-
This is a repository meant to for group work for CPRG-216.

[file:///C:/Users/Bianca%20Rogers/Downloads/Assignment%20Programing%20Strategies%20(1).pdf](url)

For our Group 7 Assignment, we will need to create a program (described above) in two parts. 

Part 1:
Create a single ticket booking system that allows users to:
-Select a movie
-Select ticket types
-Select add-ons
-Select show times
Then calculate the total cost and display a summary of the ticket booking. 

Part 2:
Update Part 1 to include multiple ticket bookings in one session:
-After each ticket booking, the program asks if the user wants to book another movie
ticket
Compute and display a billing summary after all bookings:
-Total Cost before tax
-GST 5%
-Final Amount due 

Formulas:
✓ Ticket Cost = Movie Ticket Price + Charge for Ticket Type + Total Charge of Add-ons
✓ Total Cost of N-Tickets = ∑ 𝑡𝑖𝑐𝑘𝑒𝑡 𝑐𝑜𝑠𝑡 𝑁−𝑡𝑖𝑐𝑘𝑒𝑡
𝑓𝑖𝑟𝑠𝑡 𝑡𝑖𝑐𝑘𝑒𝑡
✓ Final Total Amount = Total Cost of N-Tickets – discount + GST amount

Additional Requirements:
• The program should exactly implement the provided test runs (check test_runs.pdf)
o Format your program’s output to match that of the provided test runs.
• The program must validate the user input (e.g., movie, showtime, ticket type, and addons) for valid selection. The program should
o Ensure all inputs are within the allowed ranges.
o If a value entered by the user falls outside of the allowed values, display an
appropriate message, and have them try again.
o The program should not go to the next step until a valid value has been input.
• It is NOT necessary to verify that input values match the expected data type. In other
words, you can assume that the user will enter digits for an integer item such as options
for movies, showtime, ticket type, and add-ons.

Test Plan
• Check test_runs.pdf for sample test runs
