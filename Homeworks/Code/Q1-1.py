from helper import *

# Read in the data
data = pd.read_excel('data/adoptionseries2_with_noise.xlsx')

# Create a A(t) column. We need to insert 0 at the beginning of N(t) as
# len(cumsum(x)) = len(x) - 1. Need to make it the same length.
# Also creating the sqared variable
data['A(t)'] = pd.Series(np.insert(data['N(t)'].values, 0, 0).cumsum())
data['A(t)_2'] = data['A(t)'] ** 2

# Last 2 columns are the input data. (A(t) & A(t) ** 2)
# 2nd column is the output data. (N(t))
X = data.iloc[:, 2:]
y = data.iloc[:, 1]

# Simple linear regression
model = LinearRegression()
model = model.fit(X, y)

# equation in form of ca(t)^2 + ba(t) + a
b, c = model.coef_
a = model.intercept_

# Solving for p, q & M. Look at Assessing Primary Demand9.
p_pred = (np.sqrt(b**2 - 4*a*c) - b) / 2
q_pred = (np.sqrt(b**2 - 4*a*c) + b)/ 2
M_pred = -q_pred / c

# More information about function in helper.py. In essence,
# extrapolates N(t) values from existing data until a
# certain point.
N, A = extrapolate_bass(p_pred, q_pred, M_pred, till_period=30, N = data['N(t)'].values, A = data['A(t)'].values)

#N(30) corresponds to N[29], as indexing in python starts from 0.
print("p: {}\nq: {}\nM: {}\nN(30): {}".format(p_pred, q_pred, M_pred, N[29]))
