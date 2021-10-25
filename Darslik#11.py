# IF ELIF ELSE
# 10.09.2021 8'12

# Avalgi darsdan misol
son = int(input('Son kiriting !\n<<<'))
if son<0:
    print('son manfiy ')
else:
    print('son musbat')


# elif funksiyasi orqali biz bir nechta shartni bajarishimiz mumkun Misol :

yosh = int(input('Yoshingiz nechida ?\n<<<'))
if yosh<5:
    narx = "Bepul"
elif yosh<12:   # elif orqali bir nechta birmatadan tekshirish mumkun bajarsa bo'ladi !
    narx = '1000 So\'m'
elif yosh<18:
    narx = '2000 So\'m'
else:
    narx = '2500 So\'m'
print(f'Siz uchunn yo\'l xaqqi {narx}')       #lekin bu funk bitta kamchiligi faqat bir marta ishlatiladi xalos ko'p marta ishlatiladiga .....


# Bir nechta shartni bajarish uchun or and aperatprrini ishlatamiz
#misol

kun = input("Bugun qanday kun ? \n<<<")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun Dam olish kuni')
else:
    print("Bugun ish kuni !")


#misol (AND)

kun = input("Bugun qanday kun ?\n<<<")
harorat = float(input('Havo harorati qanday ? \n<<<'))
xaro = []
if kun.lower()=='yakshanba' and  harorat>=30:
    print("chomilishga kettik")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz !")
else:
    if harorat<30:
        xaro = 'salqin'
    elif harorat>30:
        xaro = 'issiq'
    print(f'Bugungi {xaro} xavoda kuningiz Omadli bo\'lsin' )

# endi ikkala apeartorni bir cod da ( and or ni ) ishlatamiz

day = input('Bugun qanday kun ?\n<<<')
havo_xarorati = float(input('Havo harorati qanday ? \n<<<'))
xaro =[]
if (day.lower()=='yakshanba' or day.lower()=='shanba') and havo_xarorati>=30:
    print("Cho'milgani kettik")
elif (day.lower()=='yakshanba' or day.lower()=='shanba') and havo_xarorati<30:
    print("Uyda dam olamiz")
else:
    if havo_xarorati<30:
        xaro = 'salqin'
    elif havo_xarorati>30:
        xaro = 'issiq'
    print(f'Bugungi {xaro} xavoda kuningiz Omadli bo\'lsin')


#BOOLEAN ma'lumot turi
# Miisol : kino teater uchun code

narx = 5000
popkorm = False
cola = True

if popkorm and cola:
    narx = naxr + 5000
elif popkorm or cola:
    narx = narx + 2500
print(f'Jami summa {narx} sum')