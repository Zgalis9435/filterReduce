from functools import reduce
listUser=list()
exit=False
def operationList(x):
    opList = list(filter(lambda x:x%2==0, x))
    return opList
def intNumber():
    userNumber= int(input('Introduce un número:'))
    return userNumber

while(exit==False):
    userOption=int(input('Introduce una opción'
                     '\n1.Introducir un número en la lista'
                     '\n2.Devolver los números pares'
                     '\n3.Devolver la suma de todos los números'
                     '\n4.Salir'))
    match userOption:
        case 1:
            listUser.append(intNumber())
        case 2:
            print (operationList(listUser))
        case 3:
            print(reduce(lambda x,y:x+y,operationList(listUser)))
        case 4:
            exit=True
