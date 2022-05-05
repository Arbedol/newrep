import pandas as pd
import matplotlib.pyplot as plt
from random import randint
d={"day":[i for i in range(1,32)],
"km":[randint(50,150) for i in range(1,32)]}
day={'day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], 'km': [129, 110, 58, 67, 114, 110, 81, 126, 110, 83, 62, 93, 144, 126, 79, 150, 107, 144, 82, 109, 52, 142, 63, 131, 95, 147, 89, 136, 92, 69, 114]}
df=pd.DataFrame(day)
df.plot(kind='')
plt.show()

