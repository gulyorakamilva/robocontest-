# QIYMAT QAYTARUVCHI FUNKSIYA
# def add_1(a, b):
#     print(a + b)

# add_1(4 , 5)

# def add_2(a, b):
#     return a + b

# print(add_2(3, 4))
# value = add_2(5 ,8)
# print(value)

# def toliq_ism_yasa(ism,familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism #qiymat qaytarish uchun return opertatori ishlatiladi
# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# print(toliq_ism_yasa(ism, familiya))


# print("a" * 2) #harfni 2 marta takrorlaydi
# print("abc" * 3) #harfni 3 marta takrorlaydi
# # print("abc" + 5) #TypeError: can only concatenate str (not "int") to str

# def is_even(number):
#     if number % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"

# print(is_even(4)) #Juft
# result = is_even(7)
# print(result) #Toq

from itertools import count



# volwes = ["a", "o", "i", "u", "e"]
# def count_volwes(text):
#     count = 0
#     for char in text:
#         if char == volwes[0] or char == volwes[1] or char == volwes[2] or char == volwes[3] or char == volwes[4]:
#             count += 1
#     return count
# print(count_volwes("javaskrib"))
# print(count_volwes("python"))

# # string bo'yicha for loop ishlatish
# # text = "Hello world"
# # for char in text:+
# #     print(char)


N = input().strip()

even_sum, odd_sum = 0, 0

for index in range(len(N)):
    digit = int(N[index])
    odd_sum += digit if (index + 1) % 2 == 1 else even_sum += digit
        

diff = even_sum - odd_sum
print("Yes") if diff == 0 or diff % 11 == 0 else print("No")