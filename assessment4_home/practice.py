# Question 1: The Spaza Shop Inventory
# You have a dictionary representing the stock at a shop:
# stock = {"Bread": 15, "Milk": 8, "Eggs": 30, "Apples": 5}

# Write a function called get_low_stock that takes the dictionary and a threshold (integer) as arguments. The function should return a list of item names that have stock strictly less than the threshold.

# Assessment Area: Functions, Data Structures (Dict/List), Loops.

# def get_Low_stock(a:dict, threshold:int) -> list:

#     return []
    

# Question 3: The Log File Parser
# You have a raw string from a terminal log:
# log_entry = "2026-02-18 | ERROR | Database connection failed"

# Use String Manipulation (like .split()) to extract only the error message ("Database connection failed").

# Use an f-string to print the result in this exact format: Status Report: [Database connection failed].

# Assessment Area: Data Manipulation, String Formatting.

log_entry = "2026-02-18 | ERROR | Database connection failed"

message = log_entry.split(" | ")[2]
print(f"Status Report: [{message}]")


# temps = 


