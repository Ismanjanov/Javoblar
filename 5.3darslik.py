# 5darslik Lists (Ro'yxatlar)
# 08.10.21 8"15

ismlar = ['xakim','salim', 'olim']
print(f'salom {ismlar[0].title()}, bugun choyxona bormi ?\n')
print(f'{ismlar[1].title()}, bugun choyxonaga boramizmi ?\n')

sonlar = [1, 55, 9.3, -21, 23]
print(sonlar)
print(f'{sonlar[-1] + sonlar[3]}')
sonlar.insert(2, 99)
print(sonlar)
sonlar[0] = 2
print(sonlar)
kop = sonlar[2] + sonlar[3]
print(int(kop))
t_shaxslar = ['S.Xoking', 'A.Temur', 'I.Sino']
z_shaxslar = ['I.Musk', 'R.Sharma', 'M.Menson']
print(f'Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamoniy shaxslardan esa {z_shaxslar.pop(2)} bilan suxbat qilishni istar edim')
friends = ['salim', 'rustam', 'shoxrux', 'nozim', 'nabi']
print(friends)
friends.append('baxrom')
print(friends)
friends.remove('salim')
print(friends)
print(len(friends) + 1)
friends.insert(-1, 'raxmon')
friends.insert(0, 'maqsad')
friends.insert(3, 'bobur')
print(friends)

mexmonlar = []
mexmonlar.append(friends[0])
mexmonlar.append(friends[-1])
mexmonlar.append(friends.pop(4))
mexmonlar.append(friends.pop(3))
print(mexmonlar)
print(friends)

#yakunlandi 08.10.21 9"10