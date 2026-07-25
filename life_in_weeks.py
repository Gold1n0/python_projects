def life_in_weeks(age): 
    remaining_weeks = (52 * 90) - (52*age)
    print(f"You have {remaining_weeks} weeks left.")
    
age_input = int(input("How old are you? "))
life_in_weeks(age_input)