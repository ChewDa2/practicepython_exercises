from datetime import date

current_year = date.today().year

name = input("Your name is: ")
age = int(input("What is your age: "))

output = 100 - age;
output_two = output + current_year
print("You will get 100 by {} years in {} year".format(output, output_two))

#full extras
number = int(input("\n enter another number: "))
print((("You will get 100 by {} years in {} year".format(output, output_two)) + '\n') * number)



        

