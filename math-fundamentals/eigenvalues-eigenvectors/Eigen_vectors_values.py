
import numpy as np

A_Matrix = np.array([[2,1,3],[0,4,2],[0,0,6]])

eigenvalues, eigenvectors = np.linalg.eig(A_Matrix)
#Numpy return eigenvectors in Euclidean length
print("_________using np.linagl.eigh() function_________")
print(f"EigenValues: {eigenvalues} and EigenVectors: {eigenvectors}")

for i in range(len(eigenvalues)):

    eigenvalues_ = eigenvalues[i]
    eigenvectors_ = eigenvectors[:, i]
    lamda_V = eigenvalues_ * eigenvectors_
    A_V = A_Matrix @ eigenvectors_
    print(f"Lamda _ V : {lamda_V} and A _ V : {A_V}")
    print(f"floating point precision  : {np.allclose(lamda_V,A_V) }")

 

#using np.linalg.eigh()

A_Matrix_2 = [[4,1],[1,4]]

M2_eigenvalues, M2_eigenvectors = np.linalg.eigh(A_Matrix_2)
print("_________using np.linagl.eigh() function_________")
print(f"eigenvalues of Matrix 2 : {M2_eigenvalues}  eigenvectors of Mattrix 2 : {M2_eigenvectors}")

for i in range(len(M2_eigenvalues)):

    M2_eigenvalues_ = M2_eigenvalues[i]
    M2_eigenvectors_ = M2_eigenvectors[:, i]
    M2_lamda_V = M2_eigenvalues_ * M2_eigenvectors_
    M2_A_V = A_Matrix_2 @ M2_eigenvectors_
    print(f"Lamda _ V : {M2_lamda_V} and A _ V : {M2_A_V}")
    print(f"floating point precision  : {np.allclose(M2_lamda_V,M2_A_V) }")
