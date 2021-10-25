#                            21 Python Darslari  Funksiyaga ro'yxat uzatish
# boshlandi : 18.10.21 16'25

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)

def boy_insonlar(isim):
    boylar = {}
    while isim:
        ism = isim.pop()
        sora = input(f"Dunyo milyarderlari {ism.title()}ning boyligi qancha $ ?\t")
        boylar[ism] = sora
    return boylar

boylar1 = ['elon.M', 'j.bezos', 'b.geyts', 'u.baffet']
boylar = boy_insonlar(boylar1)
print(boylar)





