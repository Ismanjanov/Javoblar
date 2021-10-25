# 22 darslik Moslashuvchi funksya ( *args , **kwargs
# Boshlandi : 24.10.21 10'56

def summa(*sonlar):
    """Kiritilgan sonlarni xisoblab beruvchi funksya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1,2,5,99,88)) #uzun

def summ(*sonla):
    """Kiritilgan sonlarni xisoblab beruvchi funksya"""
    return sum(sonla)
print(summ(1,2,5,99,88)) # qisqasi :)


def aftoinfo(kompanya,model,**malumotlar):
    """afto malumotlarni lugat shaklida qaytaruvchi funksya"""
    malumotlar['kompanya'] = kompanya
    malumotlar['model'] = model
    return malumotlar
afto = aftoinfo("gm","malibu", rangi='qara', narxi=2133)

def rapida(model,yili,**qoshimcha):
    qoshimcha['model'] = model
    qoshimcha['yili'] = yili
    return qoshimcha

zapchaslar = rapida('asus',2017,ram='8GB',videok='2GB')
print(zapchaslar)

#yakunlandi 24.10.21 11'27