def create(data):
    with open('contacts.csv', 'a') as book:
        book.write(f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]}\n")
        return 'вы создали новый контакт'


def find(name):
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        book = {}
        for i in lines[0:-1]:
            member = i.split(' ')
            book[member[0]] = member[4]
        if name in book.keys():
            return book[name]
        else:
            return 'контакт не найден'


def exportTxt():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        txt = ''
        for i in lines[0:-1]:
            member = i.split(" ")
            txt += f'' \
            f'Surname: {member[0]} \nName: {member[1]} \nPatronymic: {member[2]} \nDate: {member[3]} \nPhone number: {member[4]} \nCategory: {member[5]}\n'\
            f'--------------------------------------------\n'
        with open('contactsBook.txt', 'w') as book:
            book.truncate()
            book.write(txt)
        return "Экспортирован в txt"





def exportXml():
    with open('contacts.csv', 'r') as data:
        lines = data.read().split('\n')
        xml = '<xml>\n'
        for i in lines[0:-1]:
            member = i.split(' ')
            xml += f'   <human>\n'
            xml += f'       <name>{member[1]}</name>\n'
            xml += f'       <surname>{member[0]}</surname>\n'
            xml += f'       <patronymic>{member[2]}</patronymic>\n'
            xml += f'       <date>{member[3]}</date>\n'
            xml += f'       <phone_number>{member[4]}</phone_number>\n'
            xml += f'       <category>{member[4]}</category>\n'
            xml += f'   </human>\n'
        xml += '</xml>'
        with open('contactsBook.xml', 'w') as book:
            book.truncate()
            book.write(xml)
        return "Экспортирован в xml"
