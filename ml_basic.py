#Basic Machine learning Porgram: Predict marks based on study hours

From sklearn.liner_model import linearRegression
import numpy as np

#Data: [hours studied], [marks]
x = np.array([[2], [4], [6], [8]]) #hous of study
y = np.array([50, 60, 70, 80,])     #marks

#create and train model
model = LinearRegression()
model.fit(x, y)

#predict for 5 hours of study
hours - 5
prediction - mode.predict([[hours]])

print("if you study [hours] hours, predicted marks - [prediction[0]:.2f}")
