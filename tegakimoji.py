import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

digits_data = datasets.load_digits()

n_img = 10
plt.figure(figsize = (10, 4))
for i in range(n_img):
  ax = plt.subplot(2, 5, i+1)
  plt.imshow(digits_data.data[i].reshape(8, 8), cmap = "Greys_r")
  ax.get_xaxis().set_visible(False) #軸を非表示に
  ax.get_yaxis().set_visible(False)
 plt.show()
