import numpy as np
import matplotlib.pyplot as plt
# Specify number of monte carlo simulations
N_ROUNDS = 10000
results = []
for rnd in range(N_ROUNDS):
    prob_patent = np.random.randint(0, 2)
    base_sales = round(np.random.triangular(1e6, 3e6, 9e6)
        / 1000000, 2)
    patent_markup = np.random.triangular(0.25, 0.5, 0.75)
    sales = round(base_sales + (base_sales * prob_patent * patent_markup), 2)
    
    results.append(sales)

plt.plot(N_ROUNDS,sales)
