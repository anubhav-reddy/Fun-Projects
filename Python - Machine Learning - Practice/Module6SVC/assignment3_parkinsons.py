import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn import preprocessing

X = pd.read_csv('D:\Online COurses\Python\Data\Module6SVC\Datasets/parkinsons.data', header = 0, index_col = 0)
y = X.status.copy()
X = X.drop(labels = 'status', axis =1)

#T = preprocessing.Normalizer().fit_transform(X)
T = preprocessing.StandardScaler().fit_transform(X)
#T = preprocessing.MinMaxScaler().fit_transform(X)
#T = preprocessing.MinMaxScaler().fit_transform(X)
pca = False



if pca == True:
    from sklearn.decomposition import PCA
    pca = PCA(n_components=14)
    T = pca.fit_transform(T)
else:
    from sklearn import manifold
    iso = manifold.Isomap(n_neighbors=5, n_components=6)
    T = iso.fit_transform(T)


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(T,y,test_size=0.30,random_state = 7)




def SVCModel(a,b):
    svc = SVC(C=a,gamma = b )
    svc.fit(X_train,y_train)
    score = svc.score(X_test,y_test)
    print('Score is: ',score)
    return score


z = [] 
for i in np.arange(0.05,2.01,0.05):
    c = i
    i = i + 0.05
    for j in np.arange(0.001,0.10001,0.001):
        Gamma = j
        j = j + 0.001
        z.append(SVCModel(c,Gamma))
    
        

print(max(z))

    