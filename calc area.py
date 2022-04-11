def calc_rect_area(base, height):
    global rect_area
    rect_area = base * height
    return 
def calc_tri_area(base, height):
    global tri_area
    tri_area = base * height * 0.5
    return tri_area

calculating = True  

print("Welcome to the area calculator")

while calculating:
    print("1: Calculate area of rectangle\n2: Calculate the area of right-angle triangle\n")
    while True:
        answer = int(input("What shapes area would you like to calculate? "))
        if answer == 1:
            base = float(input("What is the base length of you rectangle? "))
            height = float(input("What is the height of you rectangle? "))
            calc_rect_area(base, height)
            print("Area of rectangle is {:.2f}".format(rect_area))
            break
        elif answer == 2:
            base = float(input("What is the base length of you right-angle triangle? "))
            height = float(input("What is the height of you right-angle triangle? "))
            calc_tri_area(base, height)
            print("Area of right-angle triangle is {:.2f}".format(tri_area))
            break
        else:
            print("Enter a valid integer number! Needs to be either 1 or 2")
            continue
    continue_calculating = input("Would you like to continue calculating? yes/no ")
    if continue_calculating == "yes":
        continue
    elif continue_calculating == 'no':
        calculating = False

print("Thanks for using my calculating area program!")
