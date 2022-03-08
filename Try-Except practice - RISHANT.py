# 08/03/2022 Period 5
# 1st task
while True:
    try:
        number = int(input("Enter a number "))
        break
    except ValueError:
        print('Please enter a whole number')

# 2nd task
while True:
    try:
        height = float(input("Enter a your height in meters: "))
        break
    except ValueError:
        print('Please enter a valid height in meters e.g 1.65')

