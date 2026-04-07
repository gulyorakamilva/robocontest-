text= "Hey guys"
print(len(text)) #8
# string ichidagi harflar va bo'shliq ham hisobga olinadi
# string ichidagi belgilar 0 dan boshlab indexlanadi
print(text[0]) #H
print(text[1]) #e
print(text[2]) #y
print(text[3]) #space
print(text[4]) #g
print(text[5]) #u
print(text[6]) #y
print(text[7]) #s
length = len(text)
# oxirgi belgini olish uchun length - 1 indexidan foydalanamiz
print(text[length - 1]) #s
# for loop yordamida string ichidagi harflarni chiqarish
# 1- usul
for char in text:
    print(char)
# 2- usul
for index in range(len(text)):
    print(index,text[index])

# in operatori yordamida string ichida ma'lum bir harf yoki so'z bor-yo'qligini tekshirish
print("welcome" in text) #true
print(("hey" in text )) # false
print("$" in text) # false

# robocontest
N = input()
if "13" in N:
    print("omadsiz chipta")
else:
    print("omadli chipta")

