# Funktion - ma`lum vazifani bajaruvchi kod bloki.
# Funksiya yaratish uchun def kalit so`zidan foydalanamiz.
# pythondagi tayyor funksiyalar - print(), input(), len() va boshqalar.
print("Hello world!")
# Funksiyani e`lon qilish(declaration)
def salom_ber():
    print("Salom, dunyo!")

# Funksiyani chaqirish(call)
salom_ber() #Natija: Salom, dunyo!
salom_ber() #Natija: Salom, dunyo!


# Funksiyada parametrlar, argumentlar
def salom_ber(ism):
    print(f"Assalomu aleykum, {ism}!")

salom_ber("Gulyora") #Natija: Assalomu aleykum, Gulyora!
salom_ber("Maftuna") #Natija: Assalomu aleykum, Maftuna!
salom_ber("Mahliyo") #Natija: Assalomu aleykum, Mahliyo!


def yigindi(a, b):
    print(a + b)

yigindi(7, 8) #Natija: 15
yigindi(10, 20) #Natija: 30

def calculate_age( birth_year= 1995, name='Olim'):
    age = 2026 - birth_year
    print(f"{name}, sizning yoshingiz: {age}")

calculate_age(2005, 'Ismoil')
calculate_age(2010, 'Gulnora')
calculate_age()

def yosh_hisobla(tugilgan_yil, joriy_yil=2020):#joriy yil uchun st. qiymat2020
    print(f"siz {joriy_yil - tugilgan_yil} yoshdasiz")
yosh_hisobla(1995, 2020)

# Amaliyot
# # 1 
# def tugilgan_yilni_topish(ism,yosh)
#      yil = 2026 - yosh
#      print(f"{ism},{yil} yilda tug`ilgansiz")
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# tugilgan_yilni_topish(ism, yosh)

# # 2
# def kvadrat_kub_hisobla(son):
#     kvadrat = son ** 2
#     kub = son ** 3
#     print(f"{son} ning kvadrati: {kvadrat}, kubi: {kub}")
# son = int(input("Son kiriting: "))
# kvadrat_kub_hisobla(son)

# # 3
# son = int(input("Son kiriting: "))
# def tekshir_son(son):
#     if son % 2 == 0:
#         print("bu son juft")
#     else:
#         print("bu son toq")

# 4.
# def solishtirish(a, b):
#     if a > b:
#         print(f"{a} katta {b} dan")
#     elif a < b:
#         print(f"{a} kichik {b} dan")
#     else:
#         print(f"{a} va {b} teng")
# solishtirish(5, 10) 
# solishtirish(10, 5)
# solishtirish(7, 7)

# 5.
# def daraja_hisobla(son, daraja):
#     natija = son ** daraja
#     print(f"{son} ning {daraja} darajasi: {natija}")
# son = int(input("Son kiriting: "))
# daraja = int(input("Daraja kiriting: "))
# daraja_hisobla(son, daraja)

# 6
# def daraja_hisobla(son, daraja=2):
#     natija = son ** daraja
#     print(f"{son} ning {daraja} darajasi: {natija}")
# x = int(input("Son kiriting: "))
# y = int(input("daraja kiriting:"))
# daraja_hisobla(x, y)

# 7
# def bolinish(son):
#     for i in range(2, 11):
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo`linadi")  
#         else:
#             print(f"{son} {i} ga qoldiq bilan bo`linadi")
# son = int(input("Son kiriting: "))
# bolinish(son)
