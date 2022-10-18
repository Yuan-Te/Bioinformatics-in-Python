#module
import math
print(math.pi)

double_pi = math.pi * 2
print(math.degrees(math.pi))
print(math.degrees(double_pi))


from math import pi, degrees #簡化
print(pi)
print(degrees(pi))


import mymodule
print(mymodule.choice_list)
n = 0
samples = 4
while n <= samples:
    print(mymodule.make_choice())
    n += 1


from urllib.request import urlretrieve #用urlretrieve下載檔案，在開起檔案，只讀取前十行！！
url = "http://winterolympicsmedals.com/medals.csv"
path = "/Users/LaiYuanTe/Downloads/medals.csv"
urlretrieve(url, path)

# lines_to_read = 10
# with open(path, 'r') as file:
#     n = 0
#     lines = file.readlines()
#     while n < lines_to_read:
#         print(lines[n])
#         n += 1
import pandas as pd
df = pd.read_csv(path)
print(df.head(10))

import numpy
array = numpy.array([1,2,3,4,5,6])
print(numpy.mean(array))
print(numpy.std(array))


