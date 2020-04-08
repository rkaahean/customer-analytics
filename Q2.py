from helper import *

"""
Analyzing and visualizing various p & q values.
"""

# Creating a subplot of 6 rows and 2 columns.
fig, axs = plt.subplots(6, 2, figsize = (12, 15), sharex=True)

# Creating a parameter grid
params = {
    'p': [0.05, 0.04, 0.06, 0.1, 0.09, 0.101],
    'q': [0.05, 0.06, 0.04, 0.1, 0.101, 0.09]
}

# Plotting the plots.
i = 0
period = 30 # Plotting 30 periods. Change as required.

for parameter in list(zip(*params.values())):
    p, q = parameter

    t = list(range(1, period+1))

    # Getting bass model for given p & q. Check helper.property
    # for more information regarding the function.
    N, A = get_bass_model(p, q, M = 100, period=period)

    # Plotting on ith row and 1st column, the new adoption rates.
    # Changing the y-axis limits to make all plots of same scale.
    axs[i][0].plot(t, N, 'o', markersize = 4)
    axs[i][0].set_ylim(0, 11)

    # Removing top and right spines. Setting title.
    axs[i][0].spines['top'].set_visible(False)
    axs[i][0].spines['right'].set_visible(False)
    axs[i][0].set_title('Adoption Count for p = {} and q = {}'.format(p, q))
    axs[i][0].set_ylabel("New Customers")

    # Plotting on ith row and 2nd column, the Cumulative adoption rates
    # Ensuring same scale along y-axis.
    axs[i][1].plot(t, np.cumsum(N), 'o', markersize = 4)
    axs[i][1].set_ylim(0, 110)

    # Removing top and right spines. Setting title.
    axs[i][1].spines['top'].set_visible(False)
    axs[i][1].spines['right'].set_visible(False)
    axs[i][1].set_title('Cumulative Adoption Count for p = {} and q = {}'.format(p, q))
    axs[i][1].set_ylabel("Total Customer Count")

    i = i + 1

# Labelling xaxis. Tight layout for cleaner look.
fig.text(0.5, 0.001, 'Time (t)', ha='center', fontsize = 'large')
fig.tight_layout()

# Comment if plot needs to be hidden on execution. Do not use fig.show().
#plt.show()

# Saving image. Increase dpi for better quality.
fig.savefig('images/Q2', dpi = 500)
