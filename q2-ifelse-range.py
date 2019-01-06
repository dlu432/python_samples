input_num = int(input("Enter number: "))


if (input_num % 2):
    print("Weird")
else:
    if (input_num >= 2) and (input_num <=5):
        print("Not Weird")
    elif (input_num >=6) and (input_num <=20):
        print("Weird")
    elif (input_num > 20):
        print("Not Weird")
