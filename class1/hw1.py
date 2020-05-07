from sklearn import *

from sklearn.datasets import load_digits

digits = load_digits()

print(digits.DESCR)

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[9])
plt.show()