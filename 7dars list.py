# Assalomu aleykum
# 7 darslik LIST bilan ishlash 02.09.2021

mevalar = ['banan', 'olxo\'ri', 'gilos', 'anjir']
narxlar = [1500, 3000, 4500, 3000]
raqamlar = ['bir', 'o\'n uch', 'yigirma uch', 23, 18, 13]

print(mevalar[0])
print(f'{narxlar[-1]}  {narxlar[2]}')
print(narxlar[-2] + narxlar[1])

#mevalar[0] = 'apelsin'
#print(mevalar[0])

                                           #.append listga biror naras qo'shishda ishlattiladi
#mevalar.append('anor')
#print(mevalar[-1])
#mevalar.append('uzum')
print(mevalar)
                                       #.insert listdagi malum elementni urniga indeks orqali boshqa element qo'shish
mevalar.insert(2, 'nok')
print(mevalar)
mevalar.insert(0, 'limon')
print(mevalar)

cars = ['mersedes', 'lambargini', 'traker', 'tesla']
#print(cars)
#cars.append("taxo")
#ars.append("gentra")
#cars.append("cobalt")
#cars.insert(1, 'ferari')
#cars.insert(3, 'mersedes')
print(cars)
#print(cars[1], cars[2] )
#print(cars[3].title())
#narxlar.append(1200, 8000, 7777, 4500, 2323, 1000)
#print(narxlar)
                                #del orqali listdagi ma... ni indeksi orqali uchirish
del cars[0]
print(cars)
cars.insert(2, 'matiz')
print(cars)
                                 #.remove agar elementni indeksini bilmasa ishlatiladi
#misol
cars.remove('matiz')
print(cars)
cars.append('malibu')
print(cars)
cars.append('matiz')
print(cars)
del cars[-1]
print(cars)
              #remove elementni uchirish uchun
cars.append('matiz')
cars.append('matiz')
cars.append('matiz')
cars.append('matiz')
cars.append('matiz')
cars.append('matiz')
print(cars)
cars.remove('matiz')
print(cars)
cars.remove('matiz')
cars.remove('matiz')
cars.remove('matiz')
cars.remove('matiz')
print(cars)

                    #.pop metoti listdan elementni boshqa elementga olish uchun iwlatiladi
pc_uchun = ['Ssd120 GB', 'Manito19 yoki 22ligi', 'sichqoncha rbg', 'kalvaturaRbg', 'kalonka', 'mikrafon']
print(pc_uchun)
kerak = "xozir muximi"
olish =  pc_uchun.pop(1)
print(olish)
print(f'Menga {kerak} : {olish} maxsulot')
print(f'Keyinroq kerakli pulni topsam {pc_uchun}ni olaman')


 # yakuniy

oquv = ['Najim', 'Xakim', 'Jobir', 'Islom', 'Shoxrux']
print(oquv)
oquv.append('ismoil')   #.append
print(oquv)
oquv.insert(0, 'jonibek'.title())  #.insert
print(oquv)
del oquv[0]              #del indeks orqali uchirish
print(oquv)
oquv.remove('ismoil')    #.remove element orqali uchirish
print(oquv)
kochirish = oquv.pop(0)  #.pop ideks orqali boshqa uzgaruvchiga elementni utkazish
print(oquv)
print(kochirish)