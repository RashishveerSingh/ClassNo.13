# write program to make calculater ushing funcion

def plas(a,b):
    return a+b

def mainus(a,b):
    return a-b

def maltipelikasion(a,b):
    return a*b

def diivaiid(a,b):
    return a/b
print("a/b/c/d")
print("a is plas")
print("b is mainus")
print("c is maltipelikasion")
print("d is diivaiid")

choice = input("enter selection:")
Naamber_wan = int(input("enter your naamber:"))
Naamber_too = int(input("enter your naamber:"))

if choice == 'a':
    print(Naamber_wan, "+" ,Naamber_too, "=", plas(Naamber_wan,Naamber_too))
elif choice == 'b':
    print(Naamber_wan, "-" ,Naamber_too, "=", mainus(Naamber_wan,Naamber_too))
elif choice == 'c':
    print(Naamber_wan, "*" ,Naamber_too, "=", maltipelikasion(Naamber_wan,Naamber_too))
elif choice == 'd':
    print(Naamber_wan, "/" ,Naamber_too, "=", diivaiid(Naamber_wan,Naamber_too))
else:
    print("THE INPUT THAT YOU ENTERED IS NOT VALID ,PLEASE ENTER A VALID INPUT >:(")