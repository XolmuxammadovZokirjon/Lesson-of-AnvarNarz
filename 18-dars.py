# 18-dars: WHILE VA RO'YXATLAR

# print("Yaqin do'stlaringizni ro'yxatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != "ha":
#         break
# 
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# cars = ["lacetti","nexia","toyota","nexia","audi","malibu","nexia"]
# while 'nexia' in cars:
#     cars.remove("nexia")
# print(cars)
talabalar  = ["hasan","husan","olim","botir"]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)