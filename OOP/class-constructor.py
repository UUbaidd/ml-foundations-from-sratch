#######class and constructor#######
import numpy as np
class Matrix():
    
    # object's (deterministic) initialization
    def __init__(self,data):
        self.data = data #self refers to particular object on which a method is being executed
        self.rows = len(data)
        self.cols = len(data[0])
        
        if not isinstance(data, list):
            raise ValueError("Matrix data must be a list")
        if len(data) == 0:
            raise ValueError("Matrix cannot be empty")
        if self.cols == 0:
            raise ValueError ("Matrix must have atleast one col")
        for row in data:
            if not isinstance(row,list):
                raise ValueError("row should be list")
            if len(row) != self.cols:
                raise ValueError("All row must have same length")

            
    def __repr__(self):
        return f"Matrix {str(self.data)}"




    def __add__(self,other):
        result = []
        if self.rows != other.rows or other.cols != self.cols:
            raise ValueError("Dimention should be same")
        for i in range(self.rows):
            row_result = []
            for j in range(self.cols):
               row_result.append(self.data[i][j] + other.data[i][j])
            result.append(row_result)
        return Matrix(result)


    def __matmul__(self, other):

        if self.cols != other.rows:
            raise ValueError("Inner dimention should match") 
        result = []
        for i in range(self.rows):
            row_result  = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols): #other.rows is also valid
                    total +=self.data[i][k] * other.data[k][j]
                row_result.append(total)
            result.append(row_result)
        return Matrix(result)
            
A = Matrix([[1, 2], [3, 4]]) #self refers to particular object on which a method is being executed
B = Matrix([[14,5],[3,4]])
C = A@B
print(C)
# print(A.data) 
# print(A.rows)
# print(A)
