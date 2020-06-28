# Complete the function below calculate your age after different numbers of years.

def calc_age(x):
    # Let's assume my age is 17
    
    print(f"Right now I'm {17} years old.\n")
    print(f"Right now I'm {x} years old.\n")
    # My age next year
    print(f"Next year I'll be {x + 1} years old.\n")

    # My age in 10 years
    print(f"In 10 years, I'll be {x + 10}!\n")


    # My age in 50 years!
    print("In 50 years, I'll be {x + 50}! Wow!\n")




def append_to_list(x):  # Be sure to choose the parameter for your function
    x.append(123)
    return x  # Return your new list





if __name__ == '__main__':
    # Use the print statements below to check your code. Do not change the starter_list or your program will not pass the automated test.
    age_now = 15
    print(age_calc(age_now))
