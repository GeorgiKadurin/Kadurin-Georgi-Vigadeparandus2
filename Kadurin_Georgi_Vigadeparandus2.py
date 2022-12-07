from math import * #строчка кода была написона неправильно 

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #+ float
S=a**2
print("Ruudu pindala", round(S,1)) #round(S,1)
P=4*a
print("Ruudu ümbermõõt", round(P,1)) #поменял '' на " round(P,1)
di=a*sqrt(2) #убрал math и добавил t
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #удалил лишюю скобку
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #+ float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #+ float
S=b*c
print("Ristküliku pindala", round(S,1)) #поставил " round(S,1)
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P,1)) #round(P,1)
di=sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di,1)) #Убрал " round(di,1)
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #изменил '' на " 
d=2*r #поставил *
print("Ringi läbimõõt", round(d,1)) # 
S=pi*r**2 #-() +*
print("Ringi pindala", round(S,2))
C=2*pi*r #+2*
print("Ringjoone pikkus", round(C,2))
