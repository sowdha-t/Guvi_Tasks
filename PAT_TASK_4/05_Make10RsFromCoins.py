"""
Problem Statement: How can I use Python to find all the ways to make Rs.10 using Rs. 1
Rs.2 , Rs.5 and Rs.10 coins?

"""

# setting the amount
amount_to_get = 10
ways_found = 0

# For each possible combinations for Rs.10 range ( 1 coin) Rs. 5 (max 2 coins) Rs. 2 (max 5 coins) Rs.1 (max 10 coins)

for count_10 in range(0, 2):
    for count_5 in range(0, 3):
        for count_2 in range(0, 6):
            for count_1 in range(0, 11):
                total = (count_10 * 10) + (count_5 * 5) + (count_2 * 2) + (count_1 * 1)
                if total == amount_to_get:            # Check if it adds up to Rs.10
                    ways_found += 1
                    print(f"Way {ways_found}: Rs10 - {count_10}, Rs5 - {count_5},Rs2 x {count_2}, Rs1 - {count_1}")

#Print the final count for the combination of different input coins
print(f"\nTotal number of ways: {ways_found}")


