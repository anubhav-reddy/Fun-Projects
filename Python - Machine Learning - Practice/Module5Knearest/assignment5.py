import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn import preprocessing
matplotlib.style.use('ggplot') # Look Pretty


def plotDecisionBoundary(model, X, y):
  fig = plt.figure()
  ax = fig.add_subplot(111)

  padding = 0.6
  resolution = 0.0025
  colors = ['royalblue','forestgreen','ghostwhite']

  # Calculate the boundaries
  x_min, x_max = X[:, 0].min(), X[:, 0].max()
  y_min, y_max = X[:, 1].min(), X[:, 1].max()
  x_range = x_max - x_min
  y_range = y_max - y_min
  x_min -= x_range * padding
  y_min -= y_range * padding
  x_max += x_range * padding
  y_max += y_range * padding

  # Create a 2D Grid Matrix. The values stored in the matrix
  # are the predictions of the class at said location
  xx, yy = np.meshgrid(np.arange(x_min, x_max, resolution),
                       np.arange(y_min, y_max, resolution))

  # What class does the classifier say?
  Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
  Z = Z.reshape(xx.shape)

  # Plot the contour map
  plt.contourf(xx, yy, Z, cmap=plt.cm.terrain)
  plt.axis('tight')

  # Plot our original points as well...
  for label in range(len(np.unique(y))):
    indices = np.where(y == label)
    plt.scatter(X[indices, 0], X[indices, 1], c=colors[label], label=str(label), alpha=0.8)

  p = model.get_params()
  plt.title('K = ' + str(p['n_neighbors']))


# 
# TODO: Load up the dataset into a variable called X. Check the .head and
# compare it to the file you loaded in a text editor. Make sure you're
# loading your data properly--don't fail on the 1st step!
#
x = pd.read_csv('D:\Online COurses\Python\Data\Module5Knearest\Datasets/wheat.data',header = 0, index_col = 0)
print(x.head(5))

#
# TODO: Copy the 'wheat_type' series slice out of X, and into a series
# called 'y'. Then drop the original 'wheat_type' column from the X
#
y = x.wheat_type.copy()
x = x.drop(labels = ['wheat_type'],axis=1)

# TODO: Do a quick, "nominal" conversion of 'y' by encoding it to a SINGLE
# variable (e.g. 0, 1, 2). This is covered in the Feature Representation
# reading as "Method 1)". In actuality the classification isn't nominal,
# but this is the fastest way to encode you 3 possible wheat types into a
# label that you can plot distinctly. More notes about this on the bottom
# of the assignment.
#
y = y.astype("category").cat.codes

#
# TODO: Basic nan munging. Fill each row's nans with the mean of the feature
#
x= x.fillna(x.mean())


# 
# TODO: Use SKLearn's regular "normalize" preprocessor to normalize X's feature data
#
T = preprocessing.normalize(x)

#x = pd.DataFrame(T, columns = x.columns)

#
# TODO: Split out your training and testing data.
# INFO: Use 0.33 test size, and use random_state=1. This is important
# so that your answers are verifiable. In the real world, you wouldn't
# specify a random_state.
#
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(T,y,test_size = 0.33, random_state = 1)

#
# TODO: Project both your X_train and X_test features into PCA space.
# This has to be done because the only way to visualize the decision
# boundary in 2D, would be if your KNN algo ran in 2D as well
#
from sklearn.decomposition import PCA
pca  = PCA(n_components = 2)

T_train = pca.fit_transform(x_train)

T_test = pca.fit_transform(x_test)


#
# TODO: Run KNeighborsClassifier. Start out with K=7 neighbors. NOTE:
# Be sure train your classifier against the PCA transformed feature
# data above! You do not, however, need to transform your labels.
#
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(T_train,y_train)
#knn.fit(T_test,y_test)
print(knn.score(T_test,y_test))

# HINT: Ensure your KNeighbors classifier object from earlier is called 'knn'.
# This method plots your TEST points against the boundary learned from your
# training data:
plotDecisionBoundary(knn, x_test, y_test)


#
# TODO: Display the accuracy score.

# NOTE: You don't have to run .predict before calling .score, since
# .score will take care of running your predictions for the params
# you provided.
#
knn.predict(T_test)


print(knn.score(T_test,y_test))


#
# BONUS: Instead of the ordinal conversion, try and get this assignment
# working with a proper Pandas get_dummies for feature encoding. HINT:
# You might have to update some of the plotDecisionBoundary code.


plt.show()

