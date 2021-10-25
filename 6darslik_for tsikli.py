 #06 Python Darslari | for tsikli
 # 11.10.21 22'01
import random
mexmonlar = ['xakim', 'salim', 'sherzod', 'sardor', 'maqsad']
for m in mexmonlar:
    print(f'salom {m}')
print(f'kod {len(mexmonlar)}marta takrorlandi') #men boshqacha yul bilan chiqardim lekin bu yul nazarmda to'gri emas (sonni chiqarish)
sonlar = list(range(11, 100, 2))
kv_son = []
for son in sonlar:
    kv_son.append(son**3)
print(sonlar)
print(kv_son)



s_kino = []
print('5ta eng sevimli kinoyizngizni yozing !')
for d in range(5):
    s_kino.append(input(f'{d+1} kino nomini yozing: '))
print(s_kino)
suxbat = []
son_w = int(input('Bugun kimlar bilan suxbatlashdingiz yoki ko\'rishdingiz ? '))
for n in range(son_w):
    suxbat.append(input(f"{n+1}-ko\'rishgan odamni ismini yozing:  "))


print(suxbat)

#yakunlandi 11.10.21 22'44