print("Ini adalah mesin penerjemah bahasa buatan UTBK.")
List_Diket = list(input("Ketikkan urutan abjad menurut soal:"))
A = List_Diket[0]
B = List_Diket[1]
C = List_Diket[2]
D = List_Diket[3]
E = List_Diket[4]
F = List_Diket[5]
G = List_Diket[6]
H = List_Diket[7]
I = List_Diket[8]
J = List_Diket[9]
K = List_Diket[10]
L = List_Diket[11]
M = List_Diket[12]
N = List_Diket[13]
O = List_Diket[14]
P = List_Diket[15]
Q = List_Diket[16]
R = List_Diket[17]
S = List_Diket[18]
T = List_Diket[19]
U = List_Diket[20]
V = List_Diket[21]
W = List_Diket[22]
X = List_Diket[23]
Y = List_Diket[24]
Z = List_Diket[25]
Lagi = "Y"
while Lagi == "Y":
    List_Soal = list(input("Ketikkan yang ingin anda terjemahkan:"))
    Panjang = len(List_Soal)
    if Panjang == 1:
        Kata = globals()[List_Soal[0]]
        print(globals()[List_Soal[0]])
    elif Panjang == 2:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]])
    elif Panjang == 3:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]])
    elif Panjang == 4:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]])
    elif Panjang == 5:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]])
    elif Panjang == 6:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]])
    elif Panjang == 7:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]])
    elif Panjang == 8:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]] + globals()[List_Soal[7]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]] + globals()[List_Soal[7]])
    elif Panjang == 9:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]] + globals()[List_Soal[7]] + globals()[List_Soal[8]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]] + globals()[List_Soal[7]] + globals()[List_Soal[8]])
    else:
        Kata = globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]] + globals()[List_Soal[7]] + globals()[List_Soal[8]] + globals()[List_Soal[9]]
        print(globals()[List_Soal[0]] + globals()[List_Soal[1]] + globals()[List_Soal[2]] + globals()[List_Soal[3]] + globals()[List_Soal[4]] + globals()[List_Soal[5]] + globals()[List_Soal[6]] + globals()[List_Soal[7]] + globals()[List_Soal[8]] + globals()[List_Soal[9]])
    Lagi = input("Lanjut atau tidak (Y/N):")