# tarmoqlanuvchi
#  07.09.2021 22'08

#       IF bu AGAR ma'nosida keladi
davlatalar = ['salvadoe', 'usa', 'vetnam', 'pokiston']
for davlat in davlatalar:
    print(davlat.title()) #bu yerda barcha davlatlar bosh xarifi katta xarf bilan chiqdi lekin usa bunday yozilma edi buni quyudagicha yechimi bor







davlatalar = ['salvadoe', 'usa', 'vetnam', 'pokiston']
for davlat in davlatalar:
    if davlat == 'usa': #bu ni video darslikdan toliq tushunib olishingiz mumkun == belgisi shu narsaga tengmi ? ddegan shart xisolanadi
        print(davlat.upper())
    else: #agar unday bolmasa boshqa kodni bajarishga utkizib beradi bu ELSE:
        print(davlat.title())


print(davlat)
davlat == 'usa'
davlat == 'pokiston'

q = 3 #buni konsul yordamida ishlanadi
q != 21  #bu ifoda orqali teng emsami sharti


telefon = input('Qanday Telfon modelilari bor ?\n<<<<')
if telefon.lower() != 'mi':
    print(f'Uzur menga {telefon.title()} kerak emas!')
else:
    print(f'katta raxmat Mi telefonini qidiryapgan edim.')


javob = float(input('15*5 nechiga teng ? \n<<<<'))
if javob!=75:
    print('Javobingiz xato !')
else:
    print("tabrik tog'ri javoni  topdingiz !")


yosh = int(input("Yoshingiz nechida ?"))
if yosh>=18:
    print('xush kelibsiz')
else:
    print("KIRISH MUMKUN EMAS")


#07.09.21 23'08
