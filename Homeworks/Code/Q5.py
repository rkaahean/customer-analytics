from helper import *

"""
Check the report made for submission. All details there.
"""

size = 100

data = pd.read_excel('data/adoptionseries2_with_noise.xlsx')
data['A(t)'] = pd.Series(np.insert(data['N(t)'].values, 0, 0).cumsum())

p = np.random.random_sample(size)
q = np.random.random_sample(size)

min_sq = 10
min_pq = (0, 0)
for p, q in list(zip(p, q)):
    popt, _ = curve_fit(discrete_bass_func, data['A(t)'], data['N(t)'], p0 = [p, q])

    p, q = popt
    N, A = get_bass_model(p, q, 100, period = data.shape[0])

    if sum((N - data['N(t)'])**2) < min_sq:
        min_sq = sum((N - data['N(t)'])**2)
        min_pq = p, q

p, q = min_pq
print("Optimal starting points; p = {} & q = {}".format(p, q))
