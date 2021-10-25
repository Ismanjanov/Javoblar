# Darslik 5 Matn bilan ishlash (Strings)
# 05.10.2021 18"24

kocha ="Bog\'bon"
maxalla ='Sog\'bon'
tuman = 'Bodomzor'
viloyat = 'Samarqand'


print(kocha)
print(maxalla)
print(tuman)
print(viloyat)
# bogbon kochasi, Sogbon maxallasi, bodomzor tumani, Samarqand viloyati
print(f'{kocha} ko\'chasi, {maxalla} maxallasi, {tuman} tumani, {viloyat} viloyati')


foy_maxallasi = input("sizning maxallangizni nomini yozing  \n<<<")
print(foy_maxallasi)
foy_kocha = input("sizning kochangizni nomini yozing  \n<<<")
print(foy_kocha)
foy_tuman = input("sizning tumaningizni nomini yozing  \n<<<")
print(foy_tuman)
foy_viloyat = input("sizning viloyatingizni nomini yozing  \n<<<")
print(f"{foy_viloyat}\t")

manzil = (f"Siz {foy_viloyat.upper()}ning {foy_tuman.title()} tumaning, {foy_maxallasi.capitalize()} maxallaning {foy_kocha.lower()} ko\'chasida yashar ekansizda !  ")
print(manzil)

# Yakunlandi 05.10.21 18'48