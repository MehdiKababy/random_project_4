# # ماشین حساب
# while True:
#     Run = input("Run Calculator (yes or no) ? ")
#     if Run == "yes" or Run == "Yes":
#         num_1 = int(input("Enter Number : "))
#         Operator = input("Enter Operator (+,-,*,/,**,%) : ")
#         num_2 = int(input("Enter Number 2 : "))
#         if Operator == "+":
#             print(f'{num_1} {Operator} {num_2} = {num_1 + num_2}')
#             continue
#         elif Operator == "-":
#             print(f'{num_1} {Operator} {num_2} = {num_1 - num_2}')
#             continue
#         elif Operator == "*":
#             print(f'{num_1} {Operator} {num_2} = {num_1 * num_2}')
#             continue
#         elif Operator == "/":
#             print(f'{num_1} {Operator} {num_2} = {num_1 / num_2}')
#             continue
#         elif Operator == "**":
#             print(f'{num_1} {Operator} {num_2} = {num_1 ** num_2}')
#             continue
#         elif Operator == "%":
#             print(f'{num_1} {Operator} {num_2} = {num_1 % num_2}')
#             continue
#         else:
#             print("There should be no empty space at the entrances")
#             print("Try Again")
#     elif Run == "no" or Run == "No":
#         print("Calculator Task Finished")
#         break
#     else:
#         print("Enter Yes or No")
#         print("Try Again")


# print("Welcome to Calculator")
# while True:
#     number_Operator = input("Enter mathematical calculations : ")
#     if number_Operator == "exit" or number_Operator == "exit()" or number_Operator == "Exit" or number_Operator == "Exit()":
#         print("Calculator Task Finished")
#         break
#     num_Split = number_Operator.split()
#     if len(num_Split) == 3:
#         num_1, operstor, num_2 = num_Split
#         num_1 = int(num_1)
#         num_2 = int(num_2)
#         if operstor == "+":
#             print(f'{num_1} {operstor} {num_2} = {num_1 + num_2}')
#             continue
#         elif operstor == "-":
#             print(f'{num_1} {operstor} {num_2} = {num_1 - num_2}')
#             continue
#         elif operstor == "*":
#             print(f'{num_1} {operstor} {num_2} = {num_1 * num_2}')
#             continue
#         elif operstor == "/":
#             print(f'{num_1} {operstor} {num_2} = {num_1 / num_2}')
#             continue
#         elif operstor == "**":
#             print(f'{num_1} {operstor} {num_2} = {num_1 ** num_2}')
#             continue
#         elif operstor == "%":
#             print(f'{num_1} {operstor} {num_2} = {num_1 % num_2}')
#             continue
#         else:
#             print("error")
#     else:
#         print("Your input must be 3 characters (two numbers and one operator) with a space between them")
#         print("Try again")


print("Welcome to Calculator")
while True:
    number_Operator = input("Enter mathematical calculations (To Exit, Write exit) : ")
    if (
        number_Operator == "exit"
        or number_Operator == "exit()"
        or number_Operator == "Exit"
        or number_Operator == "Exit()"
    ):
        print("Calculator Task Finished")
        break
    check_Numbers = number_Operator.split()
    after_Check = []
    for i in check_Numbers:
        if (
            i.isnumeric()
            or i == "+"
            or i == "-"
            or i == "*"
            or i == "/"
            or i == "//"
            or i == "%"
	        or i == "**"
        ):  # اگر ورودی عدد یا یکی از عملگر های ریاضی باشد
            after_Check.append(i)
    if after_Check == check_Numbers and len(check_Numbers) >= 3:
        result = eval(number_Operator)
        print(result)
    else:
        print("Input must be a number and an operator")
        print("Try again")
