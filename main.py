#Number guessing (Computer)
import random as rd
user_number = int(input())
lower_bound = 1 #set by user to computer to check within these limits, your wish any number u can fix as upper_bound
upper_bound = 1000 #set by user to computer to check within these limits,your wish any number u can fix as upper_bound
comp_number = rd.randint(lower_bound,upper_bound)
count = 0
while comp_number != user_number:
    if comp_number < user_number:
        comp_number = rd.randint(comp_number,user_number)
        print(f"{comp_number} too low!")
        count = count+1
       
    else:
        if comp_number > user_number:
            comp_number = rd.randint(user_number,comp_number)
            print(f"{comp_number} too high!")
            count = count+1
if user_number == comp_number:
    print(f"The Number is {comp_number}")
    print(f"The Computer Guessed it Correctly at {count}th Iteration")
