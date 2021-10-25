# 5darslik Lists (Ro'yxatlar)
# 09.10.21 21"45

davlatlar = ['polsha', 'kanada', 'qirg\'iziston','shetsiya', 'shvetsariya']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.sort()
print(davlatlar)


sonlar = list(range(120, 1200,2))
print(sonlar)
sonlar.sort()
raqamlar_yigindisi = sum(sonlar)  # royxatda eng kichik qiymatni topish uchun MIN funksyasidan foydalinadi
print(raqamlar_yigindisi)

max_s = max(sonlar)
min_s = min(sonlar)
print(max_s - min_s)

#royxatdagi elementlar shu yeriga tushuna olmadim !!


taomlar = ['palov', 'qovurdoq', 'sho\'rva', 'norin', 'shiringuruch']
non_uchun = []
non_uchun.append(taomlar[-1])
non_uchun.append('sariyog\'')
non_uchun.append('tuxum')
print(non_uchun)

non_uchun = tuple(non_uchun)
print(non_uchun)
# non_uchun[0] ='qaymoq va non'

# yakunlandi 09.10.21 22"23