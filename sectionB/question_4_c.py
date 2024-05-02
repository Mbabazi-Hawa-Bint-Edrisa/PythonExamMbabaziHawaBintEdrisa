#calculating the value of d
import math

x_one = int(input('Enter the value of X1 \t'))
y_one = float(input('Enter the value of Y1 \t'))
x_two = int(input('Enter the value of X2 \t'))
y_two = float(input('Enter the value of Y2 \t'))


def calculating_d(X1,X2,Y1,Y2):
    d = math.sqrt((X1-X2)**2 + (Y1-Y2)**2)
    print("The value of d is: %.2f " %d)
    
calculating_d(x_one,y_one,x_two,y_two)    
    
    
    
    