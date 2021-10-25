# 1o darsl if else tarmoqlanuvchi qaytarish
# 08.09.21 15'21

indikator = ['fibanachi', 'ema', 'bulujer bens', 'macda', 'moving everej']
indikator.sort()
print(indikator)

for indi in indikator:
    if indi == 'ema':
        print(indi.upper())
    else:
        print(indi.title())


simvil = ['<<<#############################################################################>>>']
for sim in simvil:
    if sim == '<<<#############################################################################>>>':
        print(sim.upper())


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# 1 vazifa  cars degan ro'yxat tuzing, ro'yxat elementlarini
#ng birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
#coreckt


#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.


login = ["admin"]
foydalanuvchi_ismi = []
foydalanuvchi_ismi.append(input('Asalomu aleykum loginingizni kiriting !\n<<<'))
print(foydalanuvchi_ismi)
for log in foydalanuvchi_ismi:
    if log.lower() == 'admin':
        print(input("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?\n<<<"))
    else:
        print(f"Xush kelibsiz, {log.title()} !")
        foydalanuvchi_orzualri = []
        foydalanuvchi_orzualri.append(input(f'{log.title()}, sizning orzularingiz nima ?\n<<<'))
        print(f'{log.title()}, siz bu  orzularga alabatta yetasiz !')

 #Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son = []
for kirt in range(2):
    son.append(input(f'{kirt+1}Istalgan sonni  yozing ?'))
print("Sonlar teng") if son[0] == son[1] else print('')

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")
