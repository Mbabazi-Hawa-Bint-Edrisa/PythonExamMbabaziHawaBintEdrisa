#temperature conversion
def celicius_to_fahrenheit():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius ")
    
    option = int(input("Choose (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius : "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")
        
    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit : "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid option!") 


celicius_to_fahrenheit()  
    