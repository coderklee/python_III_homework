import math

def square_feet(length, width):
    area = length * width
    return area

def calc_circle(radius):
    circum = math.pi * radius ** 2
    return circum

def area_calc_logic(user_calc):
    if user_calc == "square":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print(square_feet(length,width))
    elif user_calc == "circle":
        radius = float(input("Give the radius: "))
        print("The circumference of your circle is: ")
        print(calc_circle(radius))

print("This program will calculate square feet of a house and the circumference of a circle. \n")
area_calc_logic(input("What area would you like to calculate? Enter 'square' or 'circle' to decide. "))