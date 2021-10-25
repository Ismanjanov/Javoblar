#     Darslik 15 qism      27.09.2021
#      lug'at bilan ishlash
telefonlar = {'xiomi':'redmi 10',
              'samsung':'S10',
              'apple':'iphone x',
              'huawey':'mono9'}
#print(telefonlar['xiomi'])
#print(telefonlar.values()) # valuse metodi orqali faqat qiymatlarni ko'rish mumkun
#        ITEMS  .items lug'atdagi barcha element qiymatlarni aloxida juftlik qilib ekranga chiqarishda ishlatamiz
print(telefonlar.items()) #natija
# dict_items([('xiomi', 'redmi 10'), ('samsung', 'S10'), ('apple', 'iphone x'), ('huawey', 'mono9')])
#buni tartiblash uchun for siklidan foydalanamiz
for kalit, qiymat in telefonlar.items():
    print(f'Rusumi: {kalit}')
    print(f'Modeli: {qiymat}\n') #mana boldi tartibli

kompyuterlar = {'akbar':'pc stol',
                'sardor':'nountbook  2GB',
                'ulug\'bek':'noutbook 8Gb',
                'manyorbek':'pc h110 8Gb',
                'maqasad':'noutbook 4GB',
                'bobur':'xozircha yo\'q'}
for k, q in kompyuterlar.items():
    print(f'{k}da  {q} kompyuter bor\n')

#    .keys() bu metoq orqali faqat lugatdagi kalitlarni olish mumkun


komp_qurlma = {'Ona plata':60,
               'protsesor':70,
               'tezkor xotira':20,
               'qattiq disk':30,
               'kuller':15,
               'video karta':200,
               'keys':20}
#print('Eng kerakli pc qurulmalari:')
#for qurulmalar in komp_qurlma.keys():
#   print(qurulmalar.title())

oktybr_uchun = ['kuller', 'qattiq disk']
for olish in komp_qurlma:
    if olish in oktybr_uchun:
        print(f"{olish.title()} {komp_qurlma[olish]}$")
for buyum in komp_qurlma:
    if buyum in komp_qurlma:
        print(f'Iltimos {buyum} ham  olinb keling !')

print(komp_qurlma.keys())
print(komp_qurlma.values())

print("Xozirda kerakli qurulmalar:")
for narsalar in komp_qurlma:
    if narsalar in sorted(komp_qurlma):   #sorted bu metod elementlarni alifbo tartibida togrilab beradi
        print(narsalar.title())

#   sets malumot turi bu bir nechta elementlarni faqat bitta qilib beradi

telef = {'akbar':'sam s7',
         'sardor':'redmi 9c 4GB',
         'ulug\'bek':'sam J8',
         'manyorbek':'Redmi 8A',
         'maqasad':'redmi Go',
         'bobur':'sam J8'}
print('Tanishlarim quyudagi telefonni ishlatadi')
for tel in telef.values():
    print(tel) #bu yerda bir xil qiymatlar yana takrorlanmoqda

print('Tanishlarim quyudagi telefonni ishlatadi')
for tel1 in set(telef.values()):
    print(f'{tel1}\n') #mana endi takrorlanmadi bnda set() yordamida

#tugallandi 10:37 27.09.2021
