from helper import *

# Importing the data.
# Create a A(t) column. We need to insert 0 at the beginning of N(t) as
# len(cumsum(x)) = len(x) - 1. Need to make it the same length.
data = pd.read_excel('data/adoptionseries2_with_noise.xlsx')
data['A(t)'] = pd.Series(np.insert(data['N(t)'].values, 0, 0).cumsum())

# Performing a non linear optimization. The function to be optimized over is
# discrete_bass_func, which returns N(t) values given the A(t) values.
# We provide the same to curve_fit, for optimization.
# See helper.py for more infomation about the function
popt, pconv = curve_fit(continuos_bass_func, data['t'].values, data['N(t)'].values,
                bounds = (0., [1., 1.]),
                p0 = [0.02, 0.5])
p_pred, q_pred = popt

# Estimating the value of N(30).
N_30 = continuos_bass_func(29, p_pred, q_pred)

print("p: {}\nq: {}\nN(30): {}".format(p_pred, q_pred, N_30))
