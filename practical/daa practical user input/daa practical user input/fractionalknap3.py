
def fractional_knapsack(capacity, items):

    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit = 0

    for weight, profit in items:

        if capacity == 0:
            break

        if weight <= capacity:
            capacity -= weight
            total_profit += profit
        else:
            total_profit += profit * (capacity / weight)
            capacity = 0

    return total_profit


n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    profit = int(input(f"Enter profit of item {i+1}: "))
    items.append((weight, profit))

capacity = int(input("Enter knapsack capacity: "))

result = fractional_knapsack(capacity, items)

print("Maximum Profit:", result)
##time complexity of fractional knapsack problem is O(nlogn) and space complexity is O(1)

# Line-by-Line Explanation
# Step 1: Create a function
# def fractional_knapsack(capacity, items):



# - def is used to define a function.
# - fractional_knapsack is the function name.
# - capacity is the maximum weight the bag can hold.
# - items contains the weight and profit of each item.
# Example: capacity = 50, items = [(10,60), (20,100), (30,120)].
# Step 2: Sort items (most important line)
# items.sort(key=lambda x: x[1] / x[0], reverse=True)



# This line sorts items based on the profit-to-weight ratio.
# - items.sort() sorts the list.
# - lambda is a small anonymous function.
# - x[0] represents weight.
# - x[1] represents profit.
# - x[1] / x[0] calculates profit divided by weight.
# - reverse=True sorts from highest to lowest.
# Example:
# Item	Weight	Profit	Ratio
# A	10	60	6
# B	20	100	5
# C	30	120	4

# The algorithm selects A first because its ratio is highest.
# Step 3: Initialize total profit
# total_profit = 0



# Initially, the bag is empty, so profit is zero.
# Step 4: Iterate through items
# for weight, profit in items:



# This loop takes one item at a time.

# For example, in the first iteration:
# weight = 10profit = 60



# In the second iteration:
# weight = 20profit = 100



# Step 5: Check whether the bag is full
# if capacity == 0:    break



# - If capacity becomes zero, the bag is full.
# - break stops the loop.
# Step 6: Take the complete item
# if weight <= capacity:    capacity -= weight    total_profit += profit



# This condition checks whether the complete item can fit inside the bag.

# Suppose:
# Capacity = 50
# Weight = 10
# Profit = 60


# Then:
# capacity -= weight



# Means:
# capacity = 50 - 10 = 40


# And:
# total_profit += profit



# Means:
# total_profit = 0 + 60 = 60


# Now the remaining capacity is 40.
# Step 7: Take a fraction of an item
# else:    total_profit += profit * (capacity / weight)    capacity = 0



# This executes when the complete item cannot fit inside the bag.

# Example:

# Remaining capacity = 20

# Item weight = 30

# Item profit = 120

# Calculate the fraction:
# \[
# Fraction=\frac{20}{30}=0.6667
# \]

# Calculate profit:
# \[
# Profit=120\times\frac{20}{30}=80
# \]

# So we add 80 to the total profit.
# Previous profit = 160
# Fractional profit = 80

# Total profit = 240


# Then capacity = 0 because the bag is full.
# Step 8: Return the maximum profit
# return total_profit



# Returns the calculated maximum profit to the calling function.

# 3. User Input Explanation
# Take the number of items
# n = int(input("Enter number of items: "))



# - input() takes input from the user.
# - int() converts the input into an integer.
# - n stores the number of items.
# Create an empty list
# items = []



# Creates an empty list to store the items.
# Take weight and profit
# for i in range(n):    weight = int(input("Enter weight: "))    profit = int(input("Enter profit: "))    items.append((weight, profit))



# - range(n) repeats the loop n times.
# - weight stores the weight of each item.
# - profit stores the profit.
# - append() adds each item to the list as a tuple.
# After entering three items:
# items = [(10, 60), (20, 100), (30, 120)]



# Take capacity and call function
# capacity = int(input("Enter capacity: "))result = fractional_knapsack(capacity, items)print("Maximum Profit:", result)



# The user enters the bag capacity, the function calculates maximum profit, and print() displays the answer.

# 4. Dry Run – Understand How the Program Works
# Interactive Dry Run
# Step 1 of 3

# Knapsack capacity: 50 kg
# 10 kg

# 40 kg


# Remaining capacity
# 40 kg


# Total profit
# 60



# Item A
# Take all 10 kg. Profit increases by 60.
#  PreviousNext Step 

# 5. Time Complexity
# Operation	Time complexity
# Sorting items	O(n log n)
# Traversing items	O(n)
# Calculating profit	O(1) per item
# Overall	O(n log n)

# Why O(n log n)?

# Because sorting takes O(n log n), which is greater than O(n), so sorting dominates the overall time complexity.
# 6. Important Viva Questions
# Q1. Why do we use lambda?

# Ans: To calculate the profit-to-weight ratio for sorting.

# Q2. What does reverse=True mean?

# Ans: It sorts the items in descending order.

# Q3. What does append() do?

# Ans: It adds an item to the list.

# Q4. What does break do?

# Ans: It stops the loop when the bag becomes full.

# Q5. Why do we use capacity / weight?

# Ans: To calculate the fraction of an item that can fit in the remaining capacity.

# Q6. What is the time complexity?

# Ans: O(n log n).

# Q7. Why is Fractional Knapsack called a Greedy Algorithm?

# Ans: Because it selects the item with the highest profit-to-weight ratio at each step.

# For your practical viva, focus especially on these two lines: