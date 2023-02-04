
import view as v
import module as m


def createContact():
    return m.create(v.createNewContact())

def findContact():
    return m.find(v.findPhone())



def exportContact(swith):
    function = [m.exportTxt, m.exportXml]
    return function[int(swith)-3]()



def menu(answer):
    
    if answer == '1':
        showRes(createContact())
    elif answer == '2':
        showRes(findContact())
    elif answer == '3' or '4':
        showRes(exportContact(answer))
    else:
        showRes('Ошибка ввода!')
    menu(v.showMenu())



def showRes(res):
    v.viewRes(res)