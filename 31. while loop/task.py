# 1.

while True:
    try:
        num_one = float(input("Please enter number one: "))
        num_two = float(input("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue
    try:
        print(num_one / num_two)
    except ZeroDivisionError as e:
        print(f"error: {e}")
        continue
    answer = input("Do you whant continue? (yes/no): ")
    if answer == 'no':
        print("You finished")
        break


while True:
    try:
        num_one = float(input("Please enter number one: "))
        num_two = float(input("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue
    print(num_one / num_two)
    answer = input("Do you whant to continue? (yes/no): ")
    if answer == 'no':
        break
