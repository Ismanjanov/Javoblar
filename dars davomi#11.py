# davomi ...
# 13.09.21 13'40
#RESTARAN UCHUN DASTUR
import time

narx = 15000
non = True
osh = False
if non and osh:
    narx = narx + 10000
elif non or osh:
    narx = narx + 5000

print(f'Jaami summa  {narx} so\'m')

#pc yigdirish jarayoni

m_plata = 30
ram = True
usb = False
kuler = True
karnay = False
ssd_128 = True
monitor = True
cpu = True

if ram:
    m_plata = m_plata + 12
if usb:
    m_plata = m_plata + 5
if kuler:
    m_plata = m_plata + 10
if cpu:
    m_plata = m_plata +7
if karnay:
    m_plata = m_plata + 4
if ssd_128:
    m_plata = m_plata + 15
if monitor:
    m_plata = m_plata + 26

print(f'OLingan qisimlarni ummumiy summasi {m_plata}$')
import time
queulmalar = ['usb_kabel', 'wifi_adapter', 'printer', 'flashka']
olmoq = input('nima sotib olmpoqchi siz?\n<<<')
if olmoq.lower() in queulmalar:
    print('Sizning buyurtmangiz qabul qilindi !')
else:
    print(f"xozircha bizda {olmoq} qurulma mavjud emas!")
    time.sleep(5)
    print(f'Agar xoxlasngiz Bizda arzon narlarda {queulmalar} va boshqa maxsulotlar bor')



queulmalar = ['usb kabel', 'Wifi-adapter', 'Printer', 'usb-Flashka']
savachada = ['usb kabel', 'Wifi-adapter', 'nakleyka', 'keys']
if savachada:
    for olmo in savachada:
        if olmo in queulmalar:
            print(f'bizda {olmo} bor')
        else:
            print(f'bizda {olmo} yo\'q edi')
