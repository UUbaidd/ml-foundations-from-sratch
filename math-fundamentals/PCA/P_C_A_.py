import numpy as np

X = np.array([[1,1],[2,2],[3,3]])
X_mean = np.mean(X,axis=0)
X_centered = X - X_mean # centered matrix
n = len(X)
Covariance = (X_centered.T @ X_centered) / (n -1) # covariance matrix

EigenValues,EigenVector = np.linalg.eigh(Covariance) #EigenValues and EigenVector
EigenValues_Inx = np.argsort(EigenValues)[::-1]  #sorted index

Sorted_EigenValues = EigenValues[EigenValues_Inx] #advance indexing
Sorted_EigenVectors = EigenVector[:, EigenValues_Inx] # Sorting vectors based on sorted eigen values

PC1 = Sorted_EigenVectors[:,:1]

projection = X_centered @ PC1 #feature reduced to 1 while preserving number of observations

#Inverse Projection 
X_reconstruction = projection @   PC1.T + X_mean


#Explained_Variance_Ratio
EVR_values = []
for i in Sorted_EigenValues:
    EVR = i/sum(Sorted_EigenValues)
    EVR_values.append(EVR)
print(f"EVR_Value {EVR_values} ")


# Now with sklearn
from sklearn.decomposition import PCA

pca_model = PCA(n_components=1)  #n_components for no of PC

pca_model.fit(X) # PCA automatically centered data

scikit_projection = pca_model.transform(X) #projection

EVA_scikit = pca_model.explained_variance_ratio_ # EVR

print(f"PCA1 : {PC1} and with scikit leaarn {pca_model.components_}")

print(np.allclose(projection,scikit_projection))

print(np.allclose(EVR_values[:1],EVA_scikit))# :1 for first row values

sklearn_reconstruction = pca_model.inverse_transform(scikit_projection) #reconstruction of matrix
print(sklearn_reconstruction)
