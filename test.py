import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("Matplotlib version", matplotlib.__version__)

fig = plt.figure()
fig.suptitle('figure sample plots')

fig, ax_lst = plt.subplots(1, 1, figsize=(8,5))

ax_lst.plot([1,2,3,4], 'ro-')
plt.show()
