#8  Python Darslari | if-elif-else →
#23.10.21 22'32



a = int(input("Son kiriting: "))

if a % 2 ==0:
   print('Raxmat !')
else:
   print('Bu son juft emas')

yosh = int(input('Yoshingiz nechida ?\n'))
if yosh <=4 or yosh >= 60:
   print("sizga kirish bepul !")
elif yosh <= 18:
   print('sizga kirish 10k so\'m')
elif yosh >= 18:
   print('sizga kirish 20k so\'m')


q = float(input("Birinchi sonni kiriting !"))
w = float(input("Ikkinchi sonni kiriting !"))
if q < w:
    print(f"{q}<{w}")
elif q > w:
    print(f"{q}>{w}")
else:
    print('Sonlar teng')

maxsulotalar = ['banan','olma','anor','ankir', 'olxo\'ri', 'apilsin', 'mandarin', 'pomidor', 'nok', 'o\'rik']
xaridor = []
while range(5):
    xaridor.append(input("Nima olmoqchisiz ?\t"))
    if len(xaridor) ==5:
        break
if xaridor:
    for ola in xaridor:
        if ola in maxsulotalar:
            print(f"Do'konimizda {ola} bor")

        else:
            print(f'Do\'konimizda {ola} yo\'q edi')

# yakunlandi : 24.10.2021 0'34 (juft sonni topish uchun lo'p vaqt sariflandi .Lekin qaytib bunday takrorlanmaydi endi)