# Importing Packages
import matplotlib.pyplot as plt
import random
# Creating Probability Function, Girl = 1, Boy = 0
def count_girl():
    child_1 = random.randint(0, 1)
    child_2 = random.randint(0, 1)
    child_3 = random.randint(0, 1)

    # Determining if the child are the same gender
    if child_1 == child_2 == child_3:
        same_num = True
    else:
        same_num = False
    return same_num

# Inputs
num_simulations = 10000
max_num_count = 1000
count = 1

# Tracking
girl_probability = []
count_balance = []

# Creating Figure for Simulation Balances
fig = plt.figure()
plt.title("Monte Carlo [" + str(num_simulations) + "simulations]")
plt.xlabel("Simulations")
plt.ylabel("Count")
plt.xlim([0, max_num_count])

# For loop to run for the number of simulations desired
for i in range(num_simulations):
    balance = [1000]
    num_count = [0]
    num_girl = 0
    # Run until the player has rolled 1,000 times
    while num_count[-1] < max_num_count:
        same = count_girl()
        # Result if the dice are the same number
        if same:
            balance.append(balance[-1] + count)
            num_girl += 1
        # Result if the dice are different numbers
        else:
            balance.append(balance[-1] - count)

        num_count.append(num_count[-1] + 1)
# Store tracking variables and add line to figure
    girl_probability.append(num_girl/num_count[-1])
    count_balance.append(balance[-1])
    plt.plot(num_count, balance)

# Showing the plot after the simulations are finished
plt.show()

# Averaging win probability and end balance
overall_girl_probability = sum(girl_probability)/len(girl_probability)
overall_count_balance = sum(count_balance)/len(count_balance)
# Displaying the averages
print("All girl probability after " + str(num_simulations) + "count: " + str(overall_girl_probability))
print("Average ending balance after " + str(num_simulations) + "count: " + str(overall_count_balance))
