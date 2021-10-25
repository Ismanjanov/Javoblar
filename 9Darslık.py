# 9 darslik  FOR LOOP SIkillar
# 21"42 04.09.2021

                        #FOR
# for orqali bitta kodni qayta qayta yozmaslik uchun ishlatsak bo'ladi !
#misol

Oquvchilar_royxati = ['Salim', 'Nazokat', 'Baxrom', 'Sherzod', 'Alijon', 'Sardor']
print(f'Salom {Oquvchilar_royxati[1].title()} sizni Talaba bo\'lganingiz bilan tabriklayman!')
print(f'Salom {Oquvchilar_royxati[0].title()} sizni Talaba bo\'lganingiz bilan tabriklayman!') #buni ro'yxatdagilarga bittada yozish ucchun for dan foydalanamiz

for box in Oquvchilar_royxati: #fordan keyngi so'z istalgan so'z bolishi mumkun lekin codni tanasida shu soz qatnashishi kerak
    print(f'Salom {box} sizni Talaba bo\'lganingiz bilan tabriklayman!\n') #ya'ni bunday


son = list(range(1,8))
print(f'Ro\'yxat sonlar:{son}\n')
for on in son:
    print(f'{on} ning kvadrati {on**2} ga teng')
    print(f'{on}ing yarmi {on*0.5} ga teng\n')


sonlar = list(range(11))
sonlarning_kvadrati =[]         #bu yerda bosh jadval yaratb oldik va uni
for sanoq in sonlar:
    sonlarning_kvadrati.append(sanoq**2)        #jadvalni APPEND metodi orqali to'ldirib oldikk

print(sonlar)
print(sonlarning_kvadrati)


#misol foydalanuvchi orali jadvalni toldirish


orzular = []
print("Beshta orzuyingizni yozing ?")
for m in range(5):
    orzular.append(input(f"Sizning {m+1} Orzuyingiz bu ?\t "))
print(f'Siz albatta bu Orzularga : {orzular} erishasiz !')


#tugatilgan vaqt

          # 23'"00 04.09.2021





