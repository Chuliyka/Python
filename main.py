# Task1
# a = 1 #int
# print(a)
# print(type(a))
# b = 1.25 #float 
# print(b)
# print(type(b))
# logic_t = True #bool
# print(logic_t)
# print(type(logic_t))
# logic_f = False #bool
# print(logic_f)
# print(type(logic_f))
# text = "Hello"
# print(text)
# print(type(text))

# # Task2
# first_number = int(input("Введіть перше число: "))
# second_number = int(input("Введіть друге число: "))

# print("Додавання: ",first_number + second_number)
# print("Віднімання: ",first_number - second_number)
# print("Множення: ",first_number*second_number)
# print("Ділення: ",int(first_number/second_number))


# task3

def calc():
    first_number = int(input("Введіть перше число: "))
    second_number = int(input("Введіть друге число: "))
    print("+- додавання,- -віднімання,* -множення,/ -ділення,** -піднести до степеня")
    action = input("Введіть дію: ")
    result = int()

    if action == "+":
        result = first_number + second_number
        print("Результат: ",result)
    elif action == "-":
        result = first_number - second_number
        print("Результат: ",result)
    elif action == "*":
        result = first_number * second_number
        print("Результат: ",result)
    elif action == "/":
        result = first_number / second_number
        print("Результат: ",result )
    elif action == "**":
        result = first_number ** second_number
        print("Результат: ",result )


    action_second = input("Чи бажаєте ви порівняти числа? ")
    action_second = action_second.capitalize()

    if action_second == "Так":
        if first_number > second_number:
            print("Перше число більше ніж друге")
        elif first_number < second_number:
            print("Перше число менше ніж друге")
        elif first_number == second_number:
            print("Числа рівні")
    else:
        print("Щасти!")      

    action_third = input("Чи бажаєте ви перевести результат в інші типи даних?")
    action_third = action_third.capitalize()

    if action_third == "Так":
        print("Int: ",int(result))
        print("Float: ",float(result))
        print("String: ",str(result))
        if result == 1 or result == 0:
            print("Bool: ",bool(result))
        else:
            print("Дане число не можна перевести в Bool значення!")
    else:
        print("До побачення!")

        



calc()

