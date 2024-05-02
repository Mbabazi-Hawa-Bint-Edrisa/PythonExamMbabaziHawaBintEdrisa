def employee_bonuses():
    run = 1

    while run == 1:

        salary =  int(input("Enter salary amount: "))
        years_of_service =  int(input("Enter years of service: "))
        
        if years_of_service > 4:

            net_bonus_amount = int((8/100 * salary))
            
        elif years_of_service ==3:
            
            net_bonus_amount = int((5/100 * salary))
            
        else:

            net_bonus_amount = 0

        final_pay = salary + net_bonus_amount     

        print(f"Your net bonus amount is: {net_bonus_amount:,} and your final pay is {final_pay:,}")    

        run = int(input("Enter 1 to continue and any number to quit: "))

        if run !=1:
            break


employee_bonuses()
    
            
           

    
    