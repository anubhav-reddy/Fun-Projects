import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('D:\Online COurses\Python\Data\Module3\Module3\Datasets\\wheat.data', header = 0)
print(df.head(5))



#
# TODO: Drop the 'id' feature
# 
df = df.drop(labels = ['id','wheat_type'], axis= 1)


#
# TODO: Compute the correlation matrix of your dataframe
# 
a = df.corr()


#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.imshow(a, cmap = plt.cm.Blues, interpolation = 'nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)
plt.show()


