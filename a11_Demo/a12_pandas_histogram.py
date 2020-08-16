import pandas as pd
import matplotlib.pyplot as plt

tips = pd.read_csv('tips.csv')

# tips.info()
# tips.describe()
# tips.head(10)
# tips.tail(10)
# tips.shape

s = tips['tip']
s.plot.hist(density=True)
s.plot.kde()
plt.show()
