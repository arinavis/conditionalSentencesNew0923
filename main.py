# if 7:
#     print('OK')
# else:
#     print('pokytis')

# SĄLYGOS 2024-09-24

    # 2 uzd. Liepkite vartotojui suvesti savo amžių.
    # Patikrinkite ar amžius yra didesnis arba lygus 18-ai, jei taip -išveskite "jūs galite balsuoti".

# amzius = int( input('Įveskite savo amžių:'))
# if amzius >= 18:
#     print('Jūs galite balsuoti')

    #  3 uzd. Leiskite vartotojui suvesti norimą kiekį pažymių
    #  (pavyzdžiui, jūs nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus).
    #  Raskite šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip -išveskite "vidurkis teigiamas".

# pazymis1 = int( input('Įveskite pažymį:'))
# pazymis2 = int( input('Įveskite pažymį:'))
# pazymis3 = int( input('Įveskite pažymį:'))
# vidurkis = (pazymis1 + pazymis2 + pazymis3)/3
# if vidurkis >= 5:
#     print('Vidurkis teigiamas')
# else:
#     print('vidurkis neigiamas')

    # 4 uzd.
skaicius = 5
if skaicius % 5 == 0:
    print(f"Skaičiaus {skaicius} daugybos lentelė nuo 1 iki 5:")
    for i in range(1, 6):
        print(f"{skaicius} x {i} = {skaicius * i}")

if skaicius % 2 == 0:
    print(skaicius, (skaicius ** skaicius) / 2)

# sk1 = int(input("Įveskite pirmąjį skaičių: "))
# if sk1 % 7 != 0:
#     sk2 = int(input("Įveskite antrąjį skaičių: "))
#     suma = sk1 + sk2
#     skirtumas = sk1 - sk2
#     sandauga = sk1 * sk2
#     dalmuo = sk1 / sk2 \
#         if sk2 != 0 else "Dalyba iš nulio negalima"
#     print(f"Skaičių {sk1} ir {sk2} suma: {suma}")
#     print(f"Skaičių {sk1} ir {sk2} skirtumas: {skirtumas}")
#     print(f"Skaičių {sk1} ir {sk2} sandauga: {sandauga}")
#     print(f"Skaičių {sk1} ir {sk2} dalmuo: {dalmuo}")
# else: print("Dalinasi iš 7")

    # 5 uzd
# num1 = int( input('1 skaičius: '))
# num2 = int( input('2 skaičius: '))
# num3 = int( input('3 skaičius: '))

# if num1 > num2:
#     print("true pirma sąlyga")
# elif num2 > num3:
#     print("true antra sąlyga")
# elif num3 > num1:
#     print("true trečia sąlyga")

    # 6 uzd.
# if num1 == num2:
#     print("true pirma sąlyga")
# elif num2 == num3:
#     print("true antra sąlyga")
# elif num1 == 0:
#     print("true trečia sąlyga")
# elif num2 < 0:
#     print("true ketvirta sąlyga")
# elif num3 > 0:
#     print("true penkta sąlyga")

    # 7 uzd.
# pazymis = int( input('Įveskite pažymį: '))
# if pazymis == 10:
#     print('Puiku')
# elif pazymis >= 9:
#     print('labai gerai')
# elif pazymis >= 7:
#     print('gerai')
# elif pazymis >= 5:
#     print('patenkinamai')
# elif pazymis < 5:
#     print('egzaminas neišlaikytas')

    # 7 uzd.
# skc = int( input('Jūsų skaičius: '))
# if skc % 2 == 0:
#     print('Lyginis')
# else: print('Nelyginis')

    # 9 uzd.
failas = 'main.py'
if failas.endswith('.py'):
    print('python failas')
    print('pradedamas darba')
else: print('kitoks formatas')

sk1 = 65
if sk1 % 2 == 0:
    print('skaičius lyginis')
elif sk1 % 5 == 0:
    print('dalinasi iš 5')
elif sk1 == 3:
    print('lygus 3')
else: print('skaičius neatitinka sąlygų')

# 12 uzd.
# SK1 = int( input('Skaičius: '))
# SK2 = int( input('Skaičius: '))
# SK3 = int( input('Skaičius: '))
#
# if SK1 > SK2 and SK1 > SK3:
#     print(f'Pirmas sk didžiausias')
# elif SK2 > SK1 and SK2 > SK3:
#     print(f'Antras sk didžiausias')
# elif SK3 > SK1 and SK3 > SK2:
#     print(f'Trečias sk didžiausias')

# 14 uzd.
print()
rez1 = 2
rez2 = 5
rez3 = 2
vidurkis = (rez1 + rez2 + rez3) / 3
if vidurkis > 8 and vidurkis <= 10:
    print('[8-10]')
elif vidurkis > 5 and vidurkis <= 8:
    print('[5-8]')
else: print('mažiau 5')

# 15 uzd.
print()
pirmas = 25
antras = 86

if pirmas > antras or pirmas == 0:
    print('Labas')
elif antras > pirmas or antras == 5:
    print('Hello')
elif pirmas > antras and pirmas == 20:
    print('Hola')
elif antras > pirmas and antras < 100:
    print('Hej')

