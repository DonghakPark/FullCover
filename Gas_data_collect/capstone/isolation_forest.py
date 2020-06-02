from sklearn.ensemble import IsolationForest
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

clf=IsolationForest(n_estimators=50, max_samples=50, contamination=float(0.004),
                        max_features=1.0, bootstrap=False, n_jobs=-1, random_state=None, verbose=0,behaviour="new")

GAS_DATA = pd.read_csv("./GAS_DATASET.csv")

# 50개의 노드 수, 최대 50개의 샘플
# 0.04%의 outlier 색출.
clf.fit(GAS_DATA)
pred = clf.predict(GAS_DATA)
GAS_DATA['Class']=pred
outliers=GAS_DATA.loc[GAS_DATA['Class']==-1]
outlier_index=list(outliers.index)
#print(outlier_index)
#Find the number of anomalies and normal points here points classified -1 are anomalous
print(GAS_DATA['Class'].value_counts())

###################################################

pca = PCA(n_components=3)
scaler = StandardScaler()
#normalize the metrics

X = scaler.fit_transform(GAS_DATA)
X_reduce = pca.fit_transform(X)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlabel("x_composite_3")
# Plot the compressed data points
ax.scatter(X_reduce[:, 0], X_reduce[:, 1], zs=X_reduce[:, 2], s=4, lw=1, label="inliers",c="green")
# Plot x's for the ground truth outliers
ax.scatter(X_reduce[outlier_index,0],X_reduce[outlier_index,1], X_reduce[outlier_index,2],
           lw=2, s=60, marker="x", c="red", label="outliers")
ax.legend()
plt.show()
###################################################
import numpy as np
from sklearn.decomposition import PCA
pca = PCA(2)
pca.fit(GAS_DATA)
res=pd.DataFrame(pca.transform(GAS_DATA))
Z = np.array(res)
plt.title("IsolationForest")
# plt.contourf( Z, cmap=plt.cm.Blues_r)
b1 = plt.scatter(res[0], res[1], c='green',
                 s=20,label="normal points")
b1 =plt.scatter(res.iloc[outlier_index,0],res.iloc[outlier_index,1], c='green',s=20,  edgecolor="red",label="predicted outliers")
plt.legend(loc="upper right")
plt.show()