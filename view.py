def createNewContact():
    surName = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    date = input("Введите дату рождения: ")
    phoneNumber = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [surName, name, patronymic, date, phoneNumber, note]



def findPhone():
    print("Поиск телефона по фамилии")
    return input('Введите фамилию: ')



def showMenu():
    return input('1. Создать контакт\n' \
                   '2. Найти контакт\n' \
                   '3. Экспор в txt\n' \
                   '4. Экспор в xml\n' \
                   'Нажмите Enter чтобы выйти\n')




def viewRes(res):
    print(f"{res}\n")