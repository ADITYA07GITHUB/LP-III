
def knapsack(W, wt, val, n):
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


n = int(input("Enter number of items: "))

wt = []
val = []

for i in range(n):
    wt.append(int(input("Enter weight: ")))
    val.append(int(input("Enter profit: ")))

W = int(input("Enter knapsack capacity: "))

print("Maximum Profit:", knapsack(W, wt, val, n))

##time complexity of knapsack problem is O(nW) and space complexity is O(nW)

# Line-by-line Explanation
# Step 1: Define the function
# def knapsack(W, wt, val, n):



# This function calculates the maximum profit.
# Variable	Meaning
# W	Maximum capacity of bag
# wt	List of item weights
# val	List of item profits
# n	Total number of items

# Step 2: Create the DP table
# dp = [[0 for j in range(W + 1)] for i in range(n + 1)]



# This creates a 2D table filled with zeros.

# For example, if n = 3 and W = 5, the table initially looks like:
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0


# - Rows represent the number of items considered.
# - Columns represent the capacity of the bag.
# - dp[i][w] stores the maximum profit using the first i items with capacity w.
# Why n + 1 and W + 1?

# Because we also need a row for zero items and a column for zero capacity.
# Step 3: Apply two loops
# for i in range(1, n + 1):    for w in range(1, W + 1):



# The first loop checks each item.

# The second loop checks every bag capacity from 1 to W.

# Example:

# If n = 3 and W = 5:
# - i goes from 1 to 3.
# - w goes from 1 to 5.
# Step 4: Check whether the item fits
# if wt[i - 1] <= w:



# This checks whether the current item can fit inside the bag.

# Example:

# Current item weight = 3

# Current capacity = 5

# Since 3 <= 5, the item can fit.

# Why i - 1?

# Because Python lists start from index 0, while our DP rows start from 1 for the first item.
# Step 5: Find the maximum profit
# dp[i][w] = max(    val[i - 1] + dp[i - 1][w - wt[i - 1]],    dp[i - 1][w])



# This is the most important line for your viva.

# We have two choices:

# Choice 1: Include the item
# val[i - 1] + dp[i - 1][w - wt[i - 1]]



# We add the profit of the current item to the best profit obtainable from previous items using the remaining capacity.

# Choice 2: Exclude the item
# dp[i - 1][w]



# We skip the current item and use the maximum profit calculated from previous items.

# The max() function selects the greater profit.
# Step 6: If the item does not fit
# else:    dp[i][w] = dp[i - 1][w]



# If the item is heavier than the current capacity, we cannot select it.

# So we copy the maximum profit from the previous row.
# Step 7: Return the answer
# return dp[n][W]



# Returns the maximum profit using all n items with the full bag capacity W.

# 3. Explain the User Input Code
# Number of items
# n = int(input("Enter number of items: "))



# Takes the number of items from the user.

# int() converts the input into an integer.
# Create empty lists
# wt = []val = []



# - wt stores weights.
# - val stores profits.
# Take weight and profit
# for i in range(n):    wt.append(int(input("Enter weight: ")))    val.append(int(input("Enter profit: ")))



# The loop runs n times.

# append() adds each entered value to its list.

# For example, after entering four items:
# wt = [1, 3, 4, 5]val = [10, 40, 50, 70]



# Take bag capacity
# W = int(input("Enter knapsack capacity: "))



# Takes the maximum weight the bag can carry.
# Print result
# print("Maximum Profit:", knapsack(W, wt, val, n))



# Calls the knapsack function and prints the maximum profit.

# 4. Dry Run with Example
# Suppose:
# Item	Weight	Profit
# 1	1	10
# 2	3	40
# 3	4	50
# 4	5	70

# Capacity = 8

# The completed DP table is:
# DP Table – Maximum Profit
# Item / W	0	1	2	3	4	5	6	7	8
# 0	0	0	0	0	0	0	0	0	0
# 1	0	10	10	10	10	10	10	10	10
# 2	0	10	10	40	50	50	50	50	50
# 3	0	10	10	40	50	60	60	90	100
# 4	0	10	10	40	50	70	80	90	110

# Rows 0–4 represent how many items are considered; columns 0–8 represent bag capacity.
# The final answer is:

# dp[4][8] = 110

# We select item 2 and item 4.
# - Total weight = 3 + 5 = 8
# - Total profit = 40 + 70 = 110
# 5. Time and Space Complexity
# Time Complexity: O(n × W)

# Because the code uses two nested loops:
# for i in range(1, n + 1):    for w in range(1, W + 1):



# The outer loop runs n times and the inner loop runs W times.

# Therefore, total operations are proportional to n × W.

# Space Complexity: O(n × W)

# Because we create a 2D DP table containing (n + 1) × (W + 1) elements.
# 6. How to Explain This Code to the Examiner
# Sir/Madam, this program solves the 0/1 Knapsack problem using Dynamic Programming. First, we take the number of items, their weights, profits, and the bag capacity from the user. Then we create a DP table. For every item, we check whether it fits in the bag. If it fits, we calculate the maximum profit by including or excluding the item. If it does not fit, we copy the previous maximum profit. Finally, we return the maximum profit. The time and space complexity are both O(n × W).

# Remember for viva: The examiner may ask why we use i - 1, why we use max(), what dp[i][w] represents, and why the time complexity is O(n × W). These four points are especially important.