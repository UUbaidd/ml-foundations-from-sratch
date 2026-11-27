import numpy as np
import matplotlib.pyplot as plt
# X = np.array([1,2,3,4,5])
# experience, project completed
X = np.array([[1,2,3,4],[2,3,5,6]]) #features as row
X = np.transpose(X) # To make features as col
y = np.array([30,40,55,60]) #salary

print(f"Shape of X {X.shape}")
print(f"Shape of Y {y.shape}")
#Assume shape of X is:  X = (100,3) and shape of w will be :   w = (3,1) then resulted dimention would be (100,1)
#reshaping X
# X = X.reshape(X.shape[0],1)
y = y.reshape(-1,1)
print(f"After reshpae, shape of X {X.shape}")

#parameter initilaisation 
w = np.zeros((X.shape[1],1))
b = 0
# lr= 0.1
lr= 0.01
epochs= 1000
#prediction function
def prediction(features,w,b,):

    predict_value = np.dot(features,w) + b
    return predict_value

#loss function
#for seperately calcuating loss of any value


#calculate gradient
def calculate_gradient(X,y,prediction):
    error = y - prediction
    gradient_w = -(2*( X.T @ error ))/ len(prediction) # staric for element wise multiplication and scalar multiplication
    gradient_b = (-2 *(np.sum(error))) /len(prediction) # np.dot or '@' for matrix multiplication
    return gradient_w, gradient_b   

def update_weights(w,b,lr,gradient_w, gradient_b):
    w_update = w - lr*(gradient_w)
    b_update = b-lr*(gradient_b)
    return w_update, b_update


def mse_loss(result,y):
    
    error = y - result
    
    squre = error * error
        
    M_S_E = np.mean(squre)
    return  M_S_E
    

def train(X, y, w, b, lr, epochs):
    loss_history = []
    for epoch in range(epochs):

        predict_value = prediction(X, w, b)
        loss = mse_loss(predict_value,y)
        w_grad, b_grad = calculate_gradient(X,y,predict_value)
        w, b = update_weights(w,b,lr,w_grad, b_grad)

        if epoch % 100 == 0:
            print(f"loss : {loss} at epoch {epoch}")
            
        loss_history.append(loss)
        
    return w,b, loss_history

#y_hat -> prediction
w,b, loss_history = train(X,y,w,b,lr,epochs)

predict_value = prediction(X,w,b)
print(f"Prediction {predict_value}")
final_loss = mse_loss(predict_value,y)
print(f"final loss {final_loss}")
print(f"values of w: {w} ,  values of b : {b} , learning rate {lr}")
# print(f"loss history {loss_history}")
print(f"Epoch value is {epochs}, so len of history should be same, {len(loss_history)}")
plt.plot(loss_history)
plt.show()

