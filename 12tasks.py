def task1():
    print("Hello,Python!")
    return()

## print("Hello World")
##    name = input("What is your name?")
##    print("Hello, " + name)

def task2():
    print("Привет,Python!")
    print("Hello,Python!")
    print("Bonjour,Python!")
    print("Hej,Python!")
    print("Hola,Python!")
    return()

def task3():
    print("Привет" + " " + "Python!")
    return()

def task4():
    print("(\___/)")
    print("(='.'=)")
    print("(\")_(\")")
    return()

def task5():
    print("Привет,Python!\nHello,Python!\nBonjour,Python!\nHej,Python!\nHola,Python!")
    return()

def task6():
    name=input("Как вас зовут? ")
    print("Здравствуйте, "+name)
    return()

def task7():
    name=input("Как вас зовут? ")
    print("Здравствуйте, "+name)
    hobby=input("Что вам нравится? ")
    print("Отлично! "+ hobby + " - хорошее увлечение")

    return()

def task8():
    login = input("Login: ")
    passw = input("Password: ")
    newpass = input("New password: ")
    print("User " + login + " has changed the password to " + newpass)
    return()

def task9():

    s1 = input("Введите 1ю песню: ")
    s2 = input("Введите 2ю песню: ")
    s3 = input("Введите 3ю песню: ")
    s4 = input("Введите 4ю песню: ")
    s5 = input("Введите 5ю песню: ")
    print("Вот ваш плейлист: ")
    print(s5)
    print(s4)
    print(s3)
    print(s2)
    print(s1)
    print("Но учитель рекомендует такие песни послушать:"
        "\nHaddaway - What Is Love"
        "\nE-Type - Angels Crying"
        "\nBad Boys Blue - You're A Woman"
        "\nNo Doubt - Dont Speak"
        "\nAce Of Base - All That She Wants")
    return()

def task10():
    flightNumber = input("Введите номер рейса: ")
    airlineNameRus = input("Введите название авиакомпании (на русском языке): ")
    airlineNameEn = input("Введите название авиакомпании (на английском языке): ")
    arriveRus = input("Введите город прилета (на русском языке): ")
    arriveEn = input("Введите город прилета (на английском языке): ")
    print("Заканчивается посадка на рейс " + flightNumber + " авиакомпании " + airlineNameRus + " до " + arriveRus)
    print("This is the final boarding call for " + airlineNameEn + " flight " + flightNumber + " to " + arriveEn)
    return()

def task11():
    name1 = input()
    name2 = input()
    print("Привет, " + name1 + "!\nПривет, " + name2 + "!")
    return()


def task12():
    s = input()
    totalIncome = int(s)
    goldenWatchPrice = ((totalIncome - 48 * 96) * 16) / 96
    print(goldenWatchPrice)
    return()


## main program
selection=""
while selection!="0":
    selection=input("\n====================================\nEnter task number from 1 to 12. Or enter 0 to stop: ")
    print("You selected task N"+selection)
    print("---------------------------------")
    if selection == "1": task1()
    if selection == "2": task2()
    if selection == "3": task3()
    if selection == "4": task4()
    if selection == "5": task5()
    if selection == "6": task6()
    if selection == "7": task7()
    if selection == "8": task8()
    if selection == "9": task9()
    if selection == "10": task10()
    if selection == "11": task11()
    if selection == "12": task12()





