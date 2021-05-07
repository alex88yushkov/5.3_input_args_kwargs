# Exercise 1
# Create a function that asks the user to enter 3 numbers
# and then prints on the screen their summary and average.

ls = []
print("enter 3 numbers")
for index in range(3):
    user_input = input("enter number " + str(index + 1) + ": ")
    ls.append(int(user_input))

def print_sum_avg(ls):
    sum = 0
    for i in ls:
        sum += i
    print("sum=", sum, "avg=", sum/len(ls))

print_sum_avg(ls)

########################################################################################################################
# Exercise 2
# Create another function for calculating summary and average
# and printing it to the screen, but it would accept *args
# instead of a list. Test how this function works by calling it with a list of numbers.

ls = []
print("enter 3 numbers")
for index in range(3):
    user_input = input("enter number " + str(index + 1) + ": ")
    ls.append(int(user_input))

def print_sum_avg_args(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("sum =", print_sum_avg_args(*ls), "avg =", print_sum_avg_args(*ls)/len(ls))

########################################################################################################################
# Exercise 4
# Create any program of your choice that will take the user's
# input and will perform any action with it (for example greeting
# program, program that calculates the factorial of the number, program
# that prints the word from the back and etc.)

print("Enter your weight (kg):")
weight = input()
print("Enter your height (cm):")
height = input()
h = int(height)/100
bmi = int(weight)/(h * h)
print("Your BMI is: ", bmi)
if bmi < 18.5:
    print("Underweight")
if bmi >= 18.5 and bmi < 25:
    print("Normal weight")
if bmi >= 25 and bmi < 30:
    print("Overweight")
if bmi > 30:
    print("Obesity")
