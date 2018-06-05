age = input("Enter your age - ")
age_int = int(age)

try:
    if age_int >=18 and age_int <21:
        print("wristbad")
    elif age_int >= 21:
        print("have a drink, normal entry")
    else:
        print("come back when you are older")
except ValueError:
    print("Numbers only please")