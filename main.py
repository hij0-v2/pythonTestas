# 1 Dalis:
#
# 1. Sukurti bent 4 skirtingus data tipus.
#
# 2. Sukurti 3 skirtingas data struktūras
# su minimum 3 įrašais ir atvaizduoti kiekvieną įraša į atskira eilute.
#
# 3. Kokiu stilium kuriami python kintamieji?
# pvz: MANO_KINTAMASIS = 1, Mano_Kintamasis = 2 ir t.t.
#
# 4. Kaip sukurti kintamajį reprezentuojantį float data tipą?
#
# 5. Parašyti funkcija kuri visada gražins įrašus iš
# sarašo padavus bet kokį sarašą kaip parametrą.

# -- 1
sk = 1
sk1 = 0.1
string = 'hello'
boolean = True
# -- 2
my_list = [1, 2, 3, 'yes']
for i in my_list:
    print(i)
my_dict = {1: 'Mario', 2: 'Freddy', 3: 'Romas'}
for i in my_dict:
    print(i)
my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)
# -- 3

# -- 4
my_float = 7.0
my_float = float(7)


# -- 5
def list_ret(list):
    return print(list)


# 2 Dalis:
#
# 6. Kokias reikšmes turės x ir y kintamieji?
# kintamasis = "IlgasSakinys"
# x = kintamasis[2:5]
# y = kintamasis[7:9]
#
# 7. Kuo skiriasi mutable nuo not mutable data strukturos ir data tipai?
#
# 8. Jeigu norėtumėm patobulinti mūsų funkcija
# kuri išspauzdina sarašo įrašus žinant,
# kad type(kintamasis) gražina kintamojo data tipą
# parašyti funkcija kuri patikrina ar
# parametras funkcijoje yra list ar dictionary ir išspauzdinti jų reikšmes.

# -- 6
# x = "IlgasSakinys"[2:5]
# y = "IlgasSakinys"[7:9]
# print(x)
# print(y)
# x = gas
# y = ki

# -- 7
# muttable can be changed
# unmuttable can't ne changed

# -- 8

def data_type(r):
    if type(r) is list:
        print(list[r])
    else:
        print(r)


