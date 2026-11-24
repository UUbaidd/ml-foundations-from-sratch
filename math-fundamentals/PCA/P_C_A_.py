import numpy as np

X = np.array([[1,1],[2,2],[3,3]])
X_mean = np.mean(X,axis=0)
X_centered = X - X_mean
n = len(X)
Covariance = (X_centered.T @ X_centered) / (n -1)
EigenValues,EigenVector = np.linalg.eigh(Covariance)
EigenValues_Inx = np.argsort(EigenValues)[::-1]
print(EigenValues)
print(EigenValues_Inx)

Sorted_EigenValues = EigenValues[EigenValues_Inx] #advance indexing
Sorted_EigenVectors = EigenVector[:, EigenValues_Inx] # Sorting vectors based on sorted eigen values

PC1 = Sorted_EigenVectors[:,:1]
print(PC1.shape)
projection = X_centered @ PC1 #feature reduced to 1 while preserving number of observations

print(projection)

#Inverse Projection 
X_reconstruction = projection @   PC1.T + X_mean
print(X_reconstruction)

#Explained_Variance_Ratio
EVR_values = []
for i in Sorted_EigenValues:
    EVR = i/sum(Sorted_EigenValues)
    EVR_values.append(EVR)

