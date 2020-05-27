import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("./GAS_DATASET.csv")
#데이터 로드

clf=IsolationForest(n_estimators=50, max_samples=50, contamination=float(0.004),
                        max_features=1.0, bootstrap=False, n_jobs=-1, random_state=None, verbose=0,behaviour="new")
clf.fit(data)
pred = clf.predict(data)
data['anomaly'] = pred
outliers = data.loc[data['anomaly'] == -1]
outlier_index = list(outliers.index)
print(data['anomaly'].value_counts())

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

pca = PCA(n_components=3)
scaler = StandardScaler()

#정규화 실시

X = scaler.fit_transform(data)
X_reduce = pca.fit_transform(X)
fig = plt.figure()
# Plot the compressed data points
fig.scatter(X_reduce[:, 0], X_reduce[:, 1], s=4, lw=1, label="inliers",c="green")
fig.scatter(X_reduce[outlier_index,0],X_reduce[outlier_index,1],lw=2, s=60, marker="x", c="red", label="outliers")
fig.legend()
plt.show()