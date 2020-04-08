from helper import *

# Importing the data.
# Create a A(t) column. We need to insert 0 at the beginning of N(t) as
# len(cumsum(x)) = len(x) - 1. Need to make it the same length.
data = pd.read_excel('data/adoptionseries2_with_noise.xlsx')
data['A(t)'] = pd.Series(np.insert(data['N(t)'].values, 0, 0).cumsum())

# Performing a non linear optimization. The function to be optimized over is
# discrete_bass_func, which returns N(t) values given the A(t) values.
# We provide the same to curve_fit, for optimization.
popt, pconv = curve_fit(discrete_bass_func, data['A(t)'].values, data['N(t)'].values, p0 = [0.02, 0.5])

#Getting optimized values. M = 100 is given.
p_pred, q_pred = popt
M = 100

# More information about function in helper.py. In essence,
# extrapolates N(t) values from existing data until a
# certain point.
N, A = extrapolate_bass(p_pred, q_pred, M, till_period=30, N = data['N(t)'].values, A = data['A(t)'].values)

# N(30) corresponds to N[29], as indexing in python starts from 0.
print("p: {}\nq: {}\nN(30): {}".format(p_pred, q_pred, N[29]))
