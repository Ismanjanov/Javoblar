   # 8 darslik
# LIST DAVOMI 03.09.2021
#                 .SORT JADVALNI ALIFBO DEK TARTIBLAYDI

buyumlar = ['sichqoncha', 'manitor', 'klavatura', 'printer', 'keys', 'mplata', 'kuleer', 'usb kabel', 'fleshka']
print(buyumlar)

buyumlar.sort()   #mana natija alifbo ketma-ketligida taxalandi
print(buyumlar)

buyumlar.sort(reverse=True) # AGAR teskarisiga taxlamoqchi bolsak (alifbo) unda (reverse=True) ARGUMENTIDAN FOYDALANAMIZ
print(buyumlar)

print(sorted(buyumlar)) # SORTED orqali jadvalni uzgartirmagan xolatda tartiblash mumkun

print(sorted(buyumlar, reverse=True)) #bu yo'l orqali jadvalni uzgartirmagan xolatda teslkarisiga tartiblash mumkun

#                    Sonlarda
raqamlar = [-1, 258, 3, 77, 23, -4, -10, -985, 88, 45]
print(sorted(raqamlar))
print(sorted(raqamlar, reverse=True))
raqamlar.sort()
print(raqamlar)
raqamlar.sort(reverse=True)
print(raqamlar)
#                         RO'YXATNI AYLATISH UCHUN " .REVERSE() " METODIDAN FOYDALANAMIZ
raqamlar.reverse()
print(raqamlar)

#          RO'YXATDAGI ELEMENTLAR SONI/UZUNLIGINI ULCHASH UCHUN .LEN funksyasidan FOYDALANILADI
print(len(raqamlar))
print(len(buyumlar))

 #             Range argument bu malum oraliqdagi sonlarni oladi va ...

son = list(range(0,10))
print(son)
son = list(range(0,11))
print(son)

                               # range argumennti qadamlarin tariblash(qadamlar orqali ishalsh)

toq_sonlar = list(range(1,25,2))  # BU YERDA FAQAT TOQ SONLARNI OLADI. BUNING UCHUN QADAMNI 2 YOZISH KERAK
print(toq_sonlar)

juuft_sonlar = list(range(0,20,2))
print(juuft_sonlar)

juftson_9797gacha = list(range(0,9797,2)) # b
print(len(juftson_9797gacha))             #bu yol orqali malum sonlar orasida nechata juft yoki toq borligini ossonlik bilan topish mumkun

  # royxatda eng katta qiymatni topish uchun MAX funksyasidan foydalinadi
max_son = max(juftson_9797gacha)
print(max_son)

raqamlar.sort()
print(raqamlar)
raqamlar_engkattsasi = max(raqamlar)  # royxatda eng katta qiymatni topish uchun MAX funksyasidan foydalinadi
print(raqamlar_engkattsasi)

# royxatda eng kichik qiymatni topish uchun MIN funksyasidan foydalinadi
raqamlar.sort()
print(raqamlar)
raqamlar_engkichigi = min(raqamlar)  # royxatda eng kichik qiymatni topish uchun MIN funksyasidan foydalinadi
print(raqamlar_engkichigi)

                                        # royxatdagi sonlar yigindisi qiymatni topish uchun SUM funksyasidan foydalindi
raqamlar.sort()
print(raqamlar)
raqamlar_yigindisi = sum(raqamlar)  # royxatda eng kichik qiymatni topish uchun MIN funksyasidan foydalinadi
print(raqamlar_yigindisi)

                #Misol
narxlar = [1500, 5920, 4000, 7500, 9500, 1000]
arzoni = min(narxlar)
qimmati = max(narxlar)
jami = sum(narxlar)
print(f'Buyumlarning eng arzoni {arzoni}, eng qimmati esa {qimmati}.Jammi summa: {jami} ')
 #  RO'YXATNI BOLISH UCHUN [BOSHIDAGI Qiymat : Kerakli qiymat]
buyumlar = ['sichqoncha', 'manitor', 'klavatura', 'printer', 'keys', 'mplata', 'kuleer', 'usb kabel', 'fleshka']
print(buyumlar)
print(buyumlar[0:4]) #ETIBOR BERISH KERAK 0 dan 3 gacha bolgan elementlarni oldi
print(buyumlar[4:])  #ETIBOR BERISH KERAK 4 dan oxirgacha olsi.Agar qiymat berilmasa shnday bo'ladi


moshinalar = ['lasetti', 'kamaz', 'lambargini', 'Tesla', 'ferari']
print(moshinalar)
mening_moshinalarim = moshinalar   #BU USUL XATO IKKALASI BITTA NARSA BOLIB QOLADI PASROQDA SHUNI TUSHUNTIRILGAN
mening_moshinalarim.remove('kamaz') #OCHISH UCHUN
mening_moshinalarim.remove('lasetti')
mening_moshinalarim.remove('lambargini')
mening_moshinalarim.append("BMW")
print(mening_moshinalarim)
print(moshinalar)  #Etibor berin biz faqat MEN_M bilan ishlagan edik lekin Moshi lar ham uzgardi buni quyuda...xal qil..

moshinalar = ['lasetti', 'kamaz', 'lambargini', 'Tesla', 'ferari']
mening_moshinalarim = moshinalar[:] #MANA SHU YOL ORQALI COOPY QILISHIMZ MUMKUN
mening_moshinalarim.remove('kamaz')
print(moshinalar)              #MANA UZGARMADI
print(mening_moshinalarim)     #MANA UZGARDI

                #O'ZGARMAS RO'YXAT TUZISH UCHUN TUPLE () QAVUSDAN FOYDILANIDI
#MISOL
fan = ('matematika', 'fizika', 'ingiliz tili', 'adabiyot', 'informatika')
print(fan)
print(fan[0:3])
print(fan[1:3])
#fan[0] = 'chizmachilik' #mana bunga qiymat berib bolmay
#fan.append('chizmachilik') #mana bunga qiymat qo'shib bolmay
#moshinalar.append("honda")
#print(moshinalar) #bunda ishladi lekin uzgarmasda ishlamadi
#fan.remove('matematika')  # #mana bunda elementni ochirib xam bolmaydi
print(type(fan)) #buni oddiy LISTga utkazish uchun uzagrti = list(uzagrti) shu usulda
fan = list(fan)
print(type(fan)) #mana uzgardi endi boshqa amallarni qollash mumkun boladi
fan.append('chizmachilik')
print(fan) #chizmachilik qoshildi
fan.remove('chizmachilik') #chizmachilik o'chirildi
print(fan)
fan[0] = 'chizmachilik' #listni ichidagi qiymatni boshqasiga uzgartirdik
print(fan)
print('03.09.2021 16.21 da tugatim')
#03.09.2021 16.21 da tugatim