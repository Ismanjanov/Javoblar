# 28.09.2021 6:36
#              16chi darslik NESTING (bunda biror narsani ichida boshqa narsani joylash, saqlassh tushuniladi)
#lug'at
shaxar0 = {'davlat':'USA',
           'shaxar':'new-york',
           'axoli':'ruslar ko\'p',
           'maydoni':'o\'rtacha',
           'ish': 3000}
shaxar1 = {'davlat':'Polsha',
           'shaxar':'Varshava',
           'axoli':'ko\'p',
           'maydoni':'kichik',
           'ish': 1000}
shaxar2 = {'davlat':'rossiya',
           'shaxar':'moskva',
           'axoli':'ko\'p',
           'maydoni':'katta',
           'ish': 500}

shaxar = [shaxar2, shaxar1, shaxar0]
for sha in shaxar:
    print(f"{sha['davlat'].title()},"
          f"{sha['shaxar'].title()},"
          f"{sha['axoli'].title()},"
          f"{sha['maydoni'].title()}."
          f"{sha['ish']}$")          #bu usul  orqali qis vaqt va kod bilan yozish mumkun

print(f"{shaxar[0]['ish']}")
print(f"amerikada o\'rtacha ishalab oyiga {shaxar[2]['ish']}$ topish mumkun")
# yuqorida usul orali lugatni aloxida aloxida tuzb chiqish kerak edi bu osson va yez usuli quyudagicha:


pc = []
for p in range(5):
    new_pc = {
        'platasi':'asus',
        'diski':'ssd 120Gb',
        'ozusi':None,
        'narxi':60}
    pc.append(new_pc)
    #mana qisqa ko bilan biz lugat yaratib oldik endi buni uzgartirish yoki qoshimcah qoshishni koramz

for giga in pc[1:4]:
    giga['platasi']='gigabayte'
    giga['narxi']= 70

for rayn in pc[3:]:
    rayn['platasi']='rayzen'
    rayn['narxi']= 100

for uz in pc:
    if uz['platasi']=='rayzen':
        uz['ozusi']='12 GB'
    else:
        uz['ozusi'] = '8 GB'


for eed in pc:
    print(eed)


 #   Lug'atni ichida ro'yxatlarni joylaymiz

dasturchilar = {'Sardor':['python','Jango'],
                'Ulug\'bek':['C++','sql'],
                'manyorbek':['python','mql','jango'],
                'jalolidin':['python','php','jango'],
                'oybek':['web dizayner','photoshop ustasi']}
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyudagi dasturlash tillarni biladi :")
    for til in tillar:
        print(til.upper())
#bir tafsiya agar print qilinayotgan malumotnibir qatorda chiqarmoqchi bo'lasangzi  END='' argumentini q'shib ketish kerak

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyudagi dasturlash tillarni biladi :")
    for til in tillar:
        print(f'{til.upper()}')