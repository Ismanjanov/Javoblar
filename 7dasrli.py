# Darslik 7 | if-else shartlari va tarmoqlanish
# boshlandi _ 19.10.21  14'11
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for das in cars:
    if das != 'gm':
        print(das.title())
    else:
        print(das.upper())


admin = ['javlon']
sor = input('Ismiongizni kiriting\n>>>')
for ad in admin:
    if ad == sor.lower():
        print('Salom admin.Qanday xizmat')
    else:
        print(f'Hush kelibsiz {sor.title()}')


son = []
for n in range(2):
    son.append(int(input(f"{n+1}-Son  ")))

if son[0] == son[1]:
    print('sonlar teng')
else:
    print(f'Sonlarnig yigindisi {sum(son)}')

sora = int(input('son yozing !\n'))
if sora == 0:
    print('siz 0 ni yozibsiz')
elif sora >= 0:
    print('musbat son')
else:
    print('son manfiy')

ildiz = int(input('Biror bir son yozing men uni Ildizini xisoblab beraman !\n'))
if ildiz == 0:
    print('siz 0 ni yozibsiz')
elif ildiz >= 0:
    print(f'sonning ildizi {ildiz**(1/2)}')
else:
    print('son manfiy')

# yakunlandi 19.10.21 15"06