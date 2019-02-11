import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import arviz as az

az.style.use('arviz-darkgrid')


n_params = [1, 2, 4]  # Number of trials
p_params = [0.25, 0.5, 0.75] #Probability of success

x = np.arange(0, max(n_params)+1)
f, ax = plt.subplots(len(n_params), len(p_params), sharex=True,
                     sharey=True,
                     figsize=(8, 7), constrained_layout=True)


for i in range (len(n_params)):
    for j in range(len(p_params)):
        n = n_params[i]
        p = p_params[j]

        y = stats.binom(n=n, p=p).pmf(x)

        ax[i, j].vlines(x, 0, y, colors='C0', lw=5)
        ax[i, j].set_ylim(0, 1)
        ax[i, j].plot(0, 0, label=f"N = {n}\nTheta = {p}", alpha=0)
        ax[i,j].legend()

        ax[2,1].set_xlabel('y')
        ax[1,0].set_ylabel('p(y | Theta, N)')
        ax[0,0].set_xticks(x)


params = [0.5, 1, 2, 3]
x = np.linspace(0, 1, 100)
f, ax = plt.subplots(len(params), len(params), sharex=True,
                     sharey=True,
                     figsize=(8, 7), constrained_layout=True)


for i in range(4):
    for j in range(4):
        a = params[i]
        b = params[j]
        
        y = stats.beta(a, b).pdf(x)
        
        ax[i,j].plot(x, y)
        ax[i,j].plot(0, 0, label=f"alpha = {a}\nbeta = {b}", alpha=0)
        ax[i,j].legend()

ax[1,0].set_yticks([])
ax[1,0].set_xticks([0, 0.5, 1])
f.text(0.5, 0.5, 'Theta', ha='center')
f.text(0.07, 0.5, 'p(Theta)', va='center', rotation=0)