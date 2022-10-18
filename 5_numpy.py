import numpy as np
array_1 = np.array([1,2,3,4])
print(np.shape(array_1))
array_2 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.shape(array_2))

zero_array_1 = np.zeros(6)
one_array_1 = np.ones((6, 3))
print(zero_array_1)
print(one_array_1)

array = np.empty(2, dtype=int) #隨機選數字
print(array)

array = np.arange(0,11,2) #排列
print(array)

array = np.linspace(0, 20, 5)
print(array)

array = np.ones((4, 4), dtype=np.int64) #取整數
print(array)

array = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array[array > 5])
print(array[(array > 5) & (array % 2 == 0)])

indices = np.nonzero(array) #取index
print(indices)
print(array[indices])


# Basic operation
array = np.array([[1, 2], [3, 4], [5, 6]])
# We can apply the sum over any axis (note we could also use np.sum(array, axis=0))
print('Sum over entire array:', array.sum())
print('Sum over axis 0 (columns):', array.sum(axis=0))
print('Sum over axis 1 (rows):', array.sum(axis=1))
# The mean is often a useful operation (e.g. geometric mean)
print('\nMean over entire array:', array.mean())
print('Mean over axis 0 (columns):', array.mean(axis=0))
print('Mean over axis 1 (rows):', array.mean(axis=1))
# How about the min / max
print('\nMax over entire array:', array.max())
print('Max over axis 0 (columns):', array.max(axis=0))
print('Min over axis 1 (rows):', array.min(axis=1))

other = np.ones(array.shape)  # Create an array of ones with the same shape as `array`
# We can easily sum two arrays elementwise
print('Elementwise Sum:\n\n', array + other)  # equivalent to np.add(array, other)
# We can calculate the difference of two arrays elementwise
print('\nElementwise Difference:\n\n', array - other)  # equivalent to np.subtract(array, other)
# Elementwise multiplication
print('\nElementwise Multiplication:\n\n', array * other)  # equivalent to np.multiply(array, other)


temp_in_kelvin = np.array([0, 100, 200, 300, 400])
# Convert kelvin to celsius
temp_in_celsius = temp_in_kelvin - 273.15
print('After Conversion:', temp_in_celsius) #array中全部減去-273.15

#array加上array（不同shape還是可以相加）
coordinates = np.array([
    [1.2, 2.4, 3.6],
    [4.1, 5.5, 6.8],
    [7.1, 8.2, 9.1],
    [10.2, 11.4, 12.9]
])
vector = np.array([1., 0., -1.])
translated = coordinates + vector
print('Translated Coordinates:\n\n', translated)


data = np.array([[1, 2], [3, 4], [5, 6]])
print(np.shape(data))
print(data.reshape(2, 3))


arr = np.arange(6)
print('Original:\n', arr)
print('\nReshape(2, 3):\n',arr.reshape((2, 3)))
print('Transpose:\n', data.T)
print('\nTranspose:\n', data.transpose())


#均方根差值
def rmsd(v, w):
    d = v - w
    rmsd = np.sqrt(np.mean(np.square(d)))
    return rmsd
# Coordinates V (X, Y, Z)
v = np.array([
    [-0.98353, 1.81095, -0.03140],
    [0.12683,  1.80418, -0.03242],
    [-1.48991, 3.22740,  0.18102],
    [-1.35042, 1.15351,  0.78475],
    [-1.35043, 1.42183, -1.00450],
    [-1.12302, 3.61652,  1.15412],
    [-2.60028, 3.23418,  0.18203],
    [-1.12302, 3.88485, -0.63514],
])
# Coordinates W (X, Y, Z)
w = np.array([
    [-1.18012, 1.83558, -0.02389],
    [-0.07891, 1.97662, -0.00383],
    [-1.87442, 3.17118,  0.18101],
    [-1.47136, 1.13188,  0.78415],
    [-1.47377, 1.40501, -1.00437],
    [-1.58078, 3.60175,  1.16149],
    [-2.97563, 3.03014,  0.16095],
    [-1.58318, 3.87488, -0.62704],
])
print('RMSD:', rmsd(v,w))