#student grade calculations
def student_grades():

    print("\n Student Grades ")

    
    marks = int(input('Enter marks:\t'))
    
    
    if marks>=90 and  marks<=100:
        print("Grade is A")

    elif marks>=80 and marks<=89:
        print("Grade is B")

    elif marks>=70 and marks<=79:   
        print("Grade is C") 

    elif marks>=60 and marks<=69:   
        print("Grade is D")   

    elif marks>=50 and marks<=59:   
        print("Grade is E")  

    else:
        print("Fail")  
        
        
student_grades()   




 



       
