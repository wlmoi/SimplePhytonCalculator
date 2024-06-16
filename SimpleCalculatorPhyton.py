import math
import os

global save

def logo():
    print('\033[93;1m  _  __     _ _          _       _             \033[0m')
    print('\033[93;1m | |/ /    | | |        | |     | |            \033[0m')
    print("\033[93;1m | ' / __ _| | | ___   _| | __ _| |_ ___  _ __ \033[0m")
    print("\033[93;1m |  < / _` | | |/ / | | | |/ _` | __/ _ \| '__|\033[0m")
    print('\033[93;1m | . \ (_| | |   <| |_| | | (_| | || (_) | |   \033[0m')
    print('\033[93;1m |_|\_\__,_|_|_|\_|\__,_|_|\__,_|\__\___/|_|   \033[0m')
    print("\033[96m  Kalkulator Sederhana / Simple Calculator\033[0m")
    print()
    print()
    print()                                               

# Prosedur opsi awal
def OpsiAwal():
    print('\033[37;2m***************** Main Menu *****************\033[0m')
    print()
    print("\033[35;1mPilihlah satu opsi dari menu utama:\033[0m")
    print('\033[94m-------------\033[0m')
    print("\033[35;1m0. Keluar dari program\033[0m")
    print("\033[35;1m1. Mode Operasi Dasar\033[0m")
    print("   |---pertambahan(+), pengurangan(-), pengalian(x), pembagian(÷)\033[0m")
    print("   |---perpangkatan(^), perakaran(√)\033[0m")
    print("   !---logaritma\033[0m")
    print("\033[35;1m2. Mode Trigonometri\033[0m")
    print("   |---sin, cos, tan, csc, cosin, cotan\033[0m")
    print("   !---invers (arcsin, arccos, arctan...)\033[0m")
    print("\033[35;1m3. Mode Statistik\033[0m")
    print("   |---mean, median, modus\033[0m")
    print("   !---standar deviasi")
    print("\033[35;1m4. Mode Regresi Linear\033[0m")
    print("   !---y = bx + a\033[0m")
    print('\033[94m-------------\033[0m')
    return

# Prosedur menu operasi dasar
def MenuOperasiDasar():
        print('\033[37;2m***************** Menu Operasi Dasar *****************\033[0m')
        print()
        print("\033[35;1mPilihlah satu opsi dari menu:\033[0m")
        print('\033[94m-------------\033[0m')
        print('0. Kembali ke menu utama')
        print('1. Pertambahan (+)')
        print('2. Pengurangan (-)')
        print('3. Pengalian (x)')
        print('4. Pembagian (÷)')
        print('5. Perpangkatan (^)')
        print('6. Akar (√)')
        print('7. Logaritma')
        print('\033[94m-------------\033[0m')

# Prosedur operasi dasar
def OperasiDasar():
    while True:
        os.system('cls')
        logo()
        MenuOperasiDasar()
        opdas = input('> ')

        if opdas == '0':
            break
        elif opdas in ('1','2','3','4'):
            try :
                os.system('cls')
                logo()
                if opdas == '1': title = 'Penambahan'
                elif opdas == '2': title = 'Pengurangan'
                elif opdas == '3': title = 'Perkalian' 
                elif opdas == '4': title = 'Pembagian'                 
                print(f'\033[37;2m***************** Operasi {title} *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan angka pertama:\033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Masukkan/ ketikkan 'Ans' untuk menggunakan hasil")
                print("dari perhitungan sebelumnya\033[0m")
                print('\033[94m-------------\033[0m')
                num1 = input('> ')
                if num1 == 'Ans':
                    num1 = save
                num1 = float(num1)

                os.system('cls')
                logo()
                if opdas == '1': title = 'Penambahan'
                elif opdas == '2': title = 'Pengurangan'
                elif opdas == '3': title = 'Perkalian' 
                elif opdas == '4': title = 'Pembagian'                 
                print(f'\033[37;2m***************** Operasi {title} *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan angka kedua:\033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Masukkan/ ketikkan 'Ans' untuk menggunakan hasil")
                print("dari perhitungan sebelumnya\033[0m")
                print('\033[94m-------------\033[0m')
                num2 = input('> ')
                if num2 == 'Ans':
                    num2 = save
                num2 = float(num2)

                os.system('cls')

                if opdas == '1':
                    Result = add(num1,num2); op = '+'
                if opdas == '2':
                    Result = subtract(num1,num2); op = '-'
                if opdas == '3':
                    Result = multiply(num1,num2); op = 'x'
                if opdas == '4':
                    Result = divide(num1,num2); op = '÷'
                save = Result
                print ()
                print (f'{num1} {op} {num2} = {Result}')
                print ()
            except ValueError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
            except UnboundLocalError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")

        elif opdas == '5':
            try :
                os.system('cls')
                logo()
                print(f'\033[37;2m***************** Operasi Perpangkatan *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan angka: \033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Masukkan/ ketikkan 'Ans' untuk menggunakan hasil")
                print("dari perhitungan sebelumnya\033[0m")
                print('\033[94m-------------\033[0m')
                num1 = input('> ')
                if num1 == 'Ans':
                    num1 = save
                num1 = float(num1)

                os.system('cls')
                logo()
                print(f'\033[37;2m***************** Operasi Perpangkatan *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan derajat pangkat: \033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Masukkan/ ketikkan 'Ans' untuk menggunakan hasil")
                print("dari perhitungan sebelumnya\033[0m")
                print('\033[94m-------------\033[0m')
                num2 = input('> ')
                if num2 == 'Ans':
                    num2 = save
                num2 = float(num2)
                Result = pangkat(num1,num2)
                print ()
                print (f'{num1} ^ {num2} = {Result}')
                print ()
            except ValueError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
            except UnboundLocalError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
            save = Result
            print()
        elif opdas == '6':
            try :
                os.system('cls')
                logo()
                print(f'\033[37;2m***************** Operasi Perakaran *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan angka: \033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Masukkan/ ketikkan 'Ans' untuk menggunakan hasil")
                print("dari perhitungan sebelumnya\033[0m")
                print('\033[94m-------------\033[0m')
                num1 = input('> ')
                if num1 == 'Ans':
                    num1 = save
                num1 = float(num1)

                os.system('cls')
                logo()
                print(f'\033[37;2m***************** Operasi Perakaran *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan derajat akar: \033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Masukkan/ ketikkan 'Ans' untuk menggunakan hasil")
                print("dari perhitungan sebelumnya\033[0m")
                print('\033[94m-------------\033[0m')
                num2 = input('> ')
                if num2 == 'Ans':
                    num2 = save
                num2 = 1/float(num2)
                Result = pangkat(num1,num2)
                print ()
                print (f'akar {1/num2} dari {num1} = {Result}')
                print ()
            except ValueError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
            except UnboundLocalError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
            save = Result
            print()

        elif opdas == '7':
            Result = logaritma()


        if opdas not in ('1','2','3','4','5','6','7'):
            print()
            print("\033[31m\033[1mERROR : \033[0m\033[31mMenu invalid telah dipilih\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))

# Definisi toleransi trigonometri
tolerance = 10e-15

# Prosedur opsi trigonometri
def Trigonometri():
    while True:
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
        print()
        print(f"\033[35;1mPilihlah satu opsi dari menu: \033[0m")
        print('\033[94m-------------\033[0m')
        print('0. Kembali ke menu utama')
        print('1. Sin')
        print('2. Cos')
        print('3. Tan')
        print('4. Csc')
        print('5. Sec')
        print('6. Cot')
        print('7. Invers')
        print('\033[94m-------------\033[0m')
        global input_trigono
        input_trigono = input('> ')
        print ()
        if input_trigono == '0':
            break
        elif input_trigono in ('1','4'):
            hasilsincsc = sincsc()
            save = hasilsincsc
            print()
            if input_trigono == '1':
                print(f'sin = {hasilsincsc}')
            elif input_trigono == '4':
                print(f'csc = {hasilsincsc}')
            print()
        elif input_trigono in ('2','5'):
            hasilcossec = cossec()
            print()
            if input_trigono == '2':
                print(f'cos = {hasilcossec}')
            elif input_trigono == '5':
                print(f'sec = {hasilcossec}')
            print()
            save = hasilcossec
        elif input_trigono in ('3','6'):
            hasiltancot = tancot()
            print()
            if input_trigono == '3':
                print(f'tan = {hasiltancot}')
            elif input_trigono == '6':
                print(f'cot = {hasiltancot}')
            print()
            save = hasiltancot
        elif input_trigono == '7':
            invers()
            if input_invers in (1,2,3,4,5,6):
                bulatradian = "{:.3f}".format(inversradian)
                bulatderajat = "{:.2f}".format(inversderajat)
                print()
                print(f'Result: {bulatradian} radian')
                print(f'Result: {bulatderajat} derajat')
                print()
            elif input_invers == 0:
                break
            elif input_invers == 7:
                continue
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))

# Prosedur opsi statistik
def Statistik():
    n = 0
    while True:

        i =1
        Data = [] 
        Input = 0

        while Input != "X" and  Input != "x" : 
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Statistik *****************\033[0m')
            print()
            print(f"\033[35;1mInput data ke-{i}, bila sudah selesai tekan/input 'x': \033[0m")
            print('\033[94m-------------\033[0m')
            print(Data)
            print('\033[94m-------------\033[0m')

            Input = input(f"> ")
            if Input != "X" and  Input != "x" :
                try :
                    y = float(Input)
                    Data.append(y)
                except ValueError :
                    print()
                    print("\033[31m\033[1mERROR \033[0m")
                    print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
                except UnboundLocalError:
                    print()
                    print("\033[31m\033[1mERROR \033[0m")
                    print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
            

        n = len(Data)
        if n < 2:
            print ("Data kurang")
        else :
            break
   
    for i in range(n):
        idxmin=i
        for j in range (i+1, n):
            if Data[j]<Data[idxmin]:
                idxmin=j
        Data[i],Data[idxmin]=Data[idxmin],Data[i]

    while True:
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Statistik *****************\033[0m')
        print()
        print(f"\033[35;1mPilihlah salah satu opsi: \033[0m")
        print('\033[94m-------------\033[0m')
        print ("0. Kembali")
        print ("1. Mean")
        print ("2. Median")
        print ("3. Modus")
        print ("4. Standar deviasi")
        print ("5. Total")
        print ("6. Ganti data") 
        print('\033[94m-------------\033[0m')
        print(Data)
        print('\033[94m-------------\033[0m')
    
        proses = input("> ")

        print()
        if proses == '1':
            n = len(Data)
            total=0
            for i in range (n):
                total+=Data[i]
            print('Mean = ', total/n)
            # IMPELEMENTASIKAN MEDIAN MODUS DAN SIMPANGAN BAKU DI SINI
        elif proses == '5':
            Total = 0
            for i in range (n):
                Total += data[i]
            print('Total = ', Total)
        elif proses == '3':
            
            n = len(Data)                       #preparasi
            last = 0; i = 0
            data = [0 for i  in range (n)]
            for x in range (n):
                if last != Data[x]: 
                    data[i] = Data[x]
                    last = data[i]
                    i += 1
            #ngilangin 0 nya
            true_frek = 0
            for i in range (n):
                if data[i] != 0:
                    true_frek += 1
            metadata = [0 for i in range (true_frek)]
            for i in range (true_frek):
                metadata [i] = data[i]
            #dapetin jumlahnya 
            i = 0
            frekuensi = [0 for i in range (true_frek)]
            counter = 0
            for x in range (true_frek):
                while metadata[x] == Data[i]:
                    counter += 1
                    i += 1
                    if i == len(Data):
                        break
                frekuensi[x] = counter
                counter = 0
            #Mencari frek terbanyak dan jumlah modus
            max = 0
            for i in range (true_frek):
                if max < frekuensi[i]:
                    max = frekuensi[i]
            jumlah_modus = 0
            for i in range (true_frek):
                if frekuensi[i] == max:
                    jumlah_modus += 1
            #Mencari semua modus
            output = [0 for x in range (jumlah_modus)]
            x = 0
            for i in range (true_frek):
                if x > jumlah_modus:
                    break
                if frekuensi[i] == max:
                    output[x] = metadata[i]
                    x += 1
            #Output
            if metadata == output:
                print ("Data tidak memiliki modus")
            else : 
                print ('Modus : ', end="")
                for i in range (jumlah_modus-1):
                    print (output[i], end=', ')
                print (output[jumlah_modus-1]) 


        elif proses == '2':
            n = len(Data)
            if n % 2 == 1:
                n -= 1
                print ('Median =', Data[n//2])
            elif n % 2 == 0:
                n //= 2
                print ('Median =', (Data[n]+Data[n-1])/2)


        elif proses == '4':
            n = len(Data)
            # cari rata-rata
            total = 0
            for i in range (n):
                total += Data[i]
            mean = total/n
            # cari sigma
            sigma = 0
            for i in range (n):
                sigma += (Data[i]-mean)**2
            # hasil
            print ('Standar deviasi =', (sigma/n)**0.5)


        elif proses == '6':
            n = 0
            while True:
                i =1
                Data = [] 
                Input = 0
                while Input != "X" and  Input != "x" : 
                    os.system('cls')
                    logo()
                    print(f'\033[37;2m***************** Statistik *****************\033[0m')
                    print()
                    print(f"\033[35;1mInput data ke-{i}, bila sudah selesai tekan/input 'x': \033[0m")
                    print('\033[94m-------------\033[0m')
                    print(Data)
                    print('\033[94m-------------\033[0m')
                    Input = input(f"> ")
                    if Input != "X" and  Input != "x" :
                        try :
                            y = float(Input)
                            Data.append(y)
                        except ValueError :
                            print()
                            print("\033[31m\033[1mERROR \033[0m")
                            print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
                        except UnboundLocalError:
                            print()
                            print("\033[31m\033[1mERROR \033[0m")
                            print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))               
                n = len(Data)
                if n < 2:
                    print ("Data kurang")
                else :
                    break
            for i in range(n):
                idxmin=i
                for j in range (i+1, n):
                    if Data[j]<Data[idxmin]:
                        idxmin=j
                Data[i],Data[idxmin]=Data[idxmin],Data[i]


        elif proses == '0':
            break
        print ()
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        os.system('cls')
    return

# Fungsi untuk pertambahan 2 angka
def add(x, y): 
    return x + y

# Fungsi untuk pengurangan 2 angka
def subtract(x, y):
    return x - y

# Fungsi untuk perkalian 2 angka
def multiply(x, y):
    return x * y

# Fungsi untuk pembagian 2 angka
def divide(x, y):
    if y == 0:
        return "\033[31m\033[1mERROR can not divide by 0\033[0m"
    return x / y

# Fungsi untuk perpangkatan
def pangkat(x, y):
    if y == 0:
        return 1
    return x ** y

# Prosedur untuk logaritma
def logaritma():
    os.system('cls')
    logo()
    print(f'\033[37;2m***************** Operasi Logaritma *****************\033[0m')
    print()
    print(f"\033[35;1mPilihlah satu opsi dari menu:\033[0m")
    print('\033[94m-------------\033[0m')
    print('1. Logaritma')
    print('2. Logaritma Natural')
    print('\033[94m-------------\033[0m')
    log = input('> ')

    if log != '1' and log != '2':
        print()
        print("\033[31m\033[1mERROR\033[0m")
        return    
    while True:
        if log == '1':
            try :  
                os.system('cls')
                logo()
                print(f'\033[37;2m***************** Operasi Logaritma *****************\033[0m')
                print()
                print(f"\033[35;1mMasukkan nilai basis:\033[0m")
                print('\033[94m-------------\033[0m')
                print("\033[93;1m*HINT*\033[35;2m Numerus adalah bilangan pokok. Ingat! basis")
                print("harus > 0 dan != 1. \033[0m\033[93;1mPada a log x, a adalah basis.\033[0m")
                print('\033[94m-------------\033[0m')
                y = input('> ')
                if y == 'Ans':
                    y = save
                y = float(y)
                break
            except UnboundLocalError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
                print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))            
            except ValueError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")
                print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))    
        elif log == '2':
                y = 2.718281828459
                break
    while True:
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Operasi Logaritma *****************\033[0m')
        print()
        print(f"\033[35;1mMasukkan nilai numerus:\033[0m")
        print('\033[94m-------------\033[0m')
        print("\033[93;1m*HINT*\033[35;2m Numerus adalah bilangan yang dicari nilai loga-")
        print("ritmanya. Ingat! Numerus harus lebih besar dari 0. \033[0m\033[0m")
        print("\033[93;1mPada a log x, x adalah numerus.\033[0m")
        print('\033[94m-------------\033[0m')
        try :
            x = input('> ')
            if x == 'Ans':
                x = save
            if x == 'e':
                x = 2.718281828459
            x = float(x)
            if x > 0:
                print ()
                if log == '1':
                    print (f'{y} log {x} = {math.log(x,y)}')
                elif log == '2':
                    print (f'e log {x} = {math.log(x,y)}')
                print ()
                save = math.log(x,y)
                break
            else :
                print ()
                print("\033[31m\033[1mERROR\033[0m")        
                print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))    
        except UnboundLocalError:
                print ()
                print("\033[31m\033[1mERROR\033[0m")        
                print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))    
        except ValueError :
                print ()
                print("\033[31m\033[1mERROR\033[0m")        
                print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))    


# Prosedur untuk sin dan csc
def sincsc():
    os.system('cls')
    logo()
    print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
    print()
    print(f"\033[35;1mPilih satuan: \033[0m")
    print('\033[94m-------------\033[0m')
    print('1. Radian')
    print('2. Derajat')
    print('\033[94m-------------\033[0m')
    mode = input('> ')
    if mode == '1':
        mode2 = 'radian'
    elif mode == '2':
        mode2 = 'derajat'
    else :
        mode = '2'
        mode2 = 'derajat'

    try :    

        if input_trigono == '1':
            
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mMasukkan nilai {mode2}: \033[0m")
            print('\033[94m-------------\033[0m')
            nilai = float(input((f'> ')))
            if mode == '1':
                res = math.sin(nilai)
                if tolerance > res > 0 :
                    return 0 
                else:
                    return res
            if mode == '2':
                res = math.sin(math.radians(nilai))
                if tolerance > res > 0 :
                    return 0
                else:
                    return res        
        
        elif input_trigono == '4':
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mMasukkan nilai {mode2}: \033[0m")
            print('\033[94m-------------\033[0m')
            nilai = float(input((f'> ')))
            if nilai == 0:
                return 'infinity'
            elif mode == '1':
                res = (1/math.sin(nilai))
                if res > 10000000 :
                    return 'Infinity'
                else:
                    return res
            elif mode == '2':
                res = (1/math.sin(math.radians(nilai)))
                if res > 10000000 :
                    return 'Infinity'
                else:
                    return res
    except UnboundLocalError:
        print ()
        print("\033[31m\033[1mERROR\033[0m")
    except ValueError:
        print ()
        print("\033[31m\033[1mERROR\033[0m")

# Prosedur untuk cos dan sec
def cossec():
    os.system('cls')
    logo()
    print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
    print()
    print(f"\033[35;1mPilih satuan: \033[0m")
    print('\033[94m-------------\033[0m')
    print('1. Radian')
    print('2. Derajat')
    print('\033[94m-------------\033[0m')
    mode = input('> ')
    if mode == '1':
        mode2 = 'radian'
    elif mode == '2':
        mode2 = 'derajat'
    else :
        mode = '2'
        mode2 = 'derajat'

    try :    

        if input_trigono == '2':
            
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mMasukkan nilai {mode2}: \033[0m")
            print('\033[94m-------------\033[0m')
            nilai = float(input((f'> ')))
            if mode == '1':
                res = math.cos(nilai)
                if tolerance > res > 0 :
                    return 0 
                else:
                    return res
            if mode == '2':
                res = math.cos(math.radians(nilai))
                if tolerance > res > 0 :
                    return 0
                else:
                    return res        
        
        elif input_trigono == '5':
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mMasukkan nilai {mode2}: \033[0m")
            print('\033[94m-------------\033[0m')
            nilai = float(input((f'> ')))
            if nilai == 0:
                return 'infinity'
            elif mode == '1':
                res = (1/math.cos(nilai))
                if res > 10000000 :
                    return 'Infinity'
                else:
                    return res
            elif mode == '2':
                res = (1/math.cos(math.radians(nilai)))
                if res > 10000000 :
                    return 'Infinity'
                else:
                    return res
    except UnboundLocalError:
        print ()
        print("\033[31m\033[1mERROR\033[0m")
    except ValueError:
        print ()
        print("\033[31m\033[1mERROR\033[0m")
        
# Prosedur untuk tan dan cot
def tancot():
    os.system('cls')
    logo()
    print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
    print()
    print(f"\033[35;1mPilih satuan: \033[0m")
    print('\033[94m-------------\033[0m')
    print('1. Radian')
    print('2. Derajat')
    print('\033[94m-------------\033[0m')
    mode = input('> ')
    if mode == '1':
        mode2 = 'radian'
    elif mode == '2':
        mode2 = 'derajat'
    else :
        mode = '2'
        mode2 = 'derajat'

    try :    

        if input_trigono == '3':
            
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mMasukkan nilai {mode2}: \033[0m")
            print('\033[94m-------------\033[0m')
            nilai = float(input((f'> ')))
            if mode == '1':
                res = math.tan(nilai)
                if tolerance > res > 0 :
                    return 0 
                else:
                    return res
            if mode == '2':
                res = math.tan(math.radians(nilai))
                if tolerance > res > 0 :
                    return 0
                else:
                    return res        
        
        elif input_trigono == '6':
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mMasukkan nilai {mode2}: \033[0m")
            print('\033[94m-------------\033[0m')
            nilai = float(input((f'> ')))
            if nilai == 0:
                return 'infinity'
            elif mode == '1':
                res = (1/math.tan(nilai))                                                                   
                if res > 10000000 :
                    return 'Infinity'
                else:
                    return res
            elif mode == '2':
                res = (1/math.tan(math.radians(nilai)))
                if res > 10000000 :
                    return 'Infinity'
                else:
                    return res
    except UnboundLocalError:
        print ()
        print("\033[31m\033[1mERROR\033[0m")
    except ValueError:
        print ()
        print("\033[31m\033[1mERROR\033[0m")
        
# Prosedur trigonometri invers
def invers():
    while True:
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
        print()
        print(f"\033[35;1mPilih satuan: \033[0m")
        print('\033[94m-------------\033[0m')
        print ('0. Kembali')
        print ('1. Arc sin')
        print ('2. Arc cos')
        print ('3. Arc tan')
        print ('4. Arc csc')
        print ('5. Arc sec')
        print ('6. Arc cot')
        print ('7. Kembali ke menu trigonometri')
        print('\033[94m-------------\033[0m')
        global input_invers
        input_invers = input('> ')
        try :
            input_invers = int(input_invers)
        except ValueError:
            print("\033[31m\033[1mERROR : \033[0m\033[31mMenu invalid telah dipilih\033[0m")
            print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
            input_invers = 7
        if input_invers in (0,7):
            break
        else:
            global modeinvers
            os.system('cls')
            logo()
            print(f'\033[37;2m***************** Operasi Trigonometri *****************\033[0m')
            print()
            print(f"\033[35;1mInput nilai: \033[0m")
            print('\033[94m-------------\033[0m')

            try :
                nilai = int(input('> '))
            except ValueError:
                print("\033[31m\033[1mERROR : \033[0m")
                print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
            global inversradian
            global inversderajat
            if input_invers == 1:
                inversradian = math.asin(nilai)
                inversderajat = math.degrees(math.asin(nilai))
                return
            elif input_invers == 4:
                inversradian = math.asin(1/nilai)
                inversderajat = math.degrees(math.asin(1/nilai))
                return
            elif input_invers == 2:
                inversradian = math.acos(nilai)
                inversderajat = math.degrees(math.acos(nilai))
                return
            elif input_invers == 5:
                inversradian = math.acos(1/nilai)
                inversderajat = math.degrees(math.acos(1/nilai))
                return
            elif input_invers == 3:
                inversradian = math.atan(nilai)
                inversderajat = math.degrees(math.atan(nilai))
                return
            elif input_invers == 6:
                inversradian = math.atan(1/nilai)
                inversderajat = math.degrees(math.atan(1/nilai))
                return

# Prosedur opsi regresi linear
def RegresiLinear():


    #Input panjang array
    os.system('cls')
    logo()
    print(f'\033[37;2m***************** Regresi Linear *****************\033[0m')
    print()
    print(f"\033[35;1mMasukkan banyaknya data: \033[0m")
    print('\033[94m-------------\033[0m')
    try :
        n = int(input('> '))
        if n < 2:
            print ()
            print("\033[31m\033[1mERROR : \033[0m\033[31mData kurang\033[0m")
            print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
            return RegresiLinear()
        x = [0 for i in range (n)]
        y = [0 for i in range (n)]
    except UnboundLocalError:
        print ()
        print ("\033[31m\033[1mERROR\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        return RegresiLinear()
    except ValueError:
        print ()
        print ("\033[31m\033[1mERROR\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        return RegresiLinear()

    # Input array
    for i in range (n):
     try :
        #input x
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Regresi Linear *****************\033[0m')
        print()
        print(f"\033[35;1mMasukkan nilai x ke-{i+1}: \033[0m")
        print('\033[94m-------------\033[0m')
        print('X', x)
        print('Y', y)
        print('\033[94m-------------\033[0m')
        x[i] = float(input('> '))
        #input Y
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Regresi Linear *****************\033[0m')
        print()
        print(f"\033[35;1mMasukkan nilai y ke-{i+1}: \033[0m")
        print('\033[94m-------------\033[0m')
        print('X', x)
        print('Y', y)
        print('\033[94m-------------\033[0m')
        y[i] = float(input('> '))
        print ()
     except ValueError :
        print ()
        print ("\033[31m\033[1mERROR\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        return RegresiLinear()
     except UnboundLocalError:
        print ()
        print ("\033[31m\033[1mERROR\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        return RegresiLinear()

    #kontrol proses
    try:
        totalx = 0
        totaly = 0
        for i in range(n):
            totalx += x[i]
            totaly += y[i]
        rata_x = totalx/n
        rata_y = totaly/n

        # Menghitung parameter regresi (m dan c)
        numer = 0
        denom = 0
        denomy = 0
        for i in range(n):
            numer += (x[i] - rata_x)* (y[i] - rata_y)
            denom += (x[i] - rata_x)**2
            denomy += (y[i] - rata_y)**2
        b = numer / denom
        a = rata_y - (b * rata_x)
    #--------------
        def korelasi_pearson(x, y):
            correlation = numer / ((denom**(1/2)) * (denomy**(1/2)))
            return correlation

        correlation = korelasi_pearson(x, y)
    except ZeroDivisionError:
        print ()
        print("\033[31m\033[1mERROR : \033[0m\033[31mTerjadi pembagian dengan 0\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        return RegresiLinear()
    #-----------

    while True:
        os.system('cls')
        logo()
        print(f'\033[37;2m***************** Regresi Linear *****************\033[0m')
        print()
        print(f"\033[35;1mPilihlah satu opsi dari menu: \033[0m")
        print('\033[94m-------------\033[0m')
        print('0. Kembali ke menu utama')
        print('1. Tentukan nilai b')
        print('2. Tentukan nilai a')
        print('3. Tentukan nilai r')
        print('\033[94m-------------\033[0m')
        print ('X', x)
        print ('Y', y)
        print('\033[94m-------------\033[0m')
        print("\033[93;1m*HINT*\033[35;2m y = bx + a\033[0m")
        print('\033[94m-------------\033[0m')
        f = input('> ')
        print ()

        if(f == '1'):
            print('b =', b)
            save = b
        elif(f == '2'):
            print('a =', a)
            save = a
        elif(f == '3'):
            print('r =', correlation)
            save = correlation
        elif(f == '0'):
            break
        print()
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))
        os.system('cls')

# Looping utama dari kalkulator
while True:
    os.system('cls')
    logo()
    OpsiAwal()

    user_input = input("> ")

    if user_input == '0':
        os.system('cls')
        break
    elif user_input == '1':
        OperasiDasar() 
    elif user_input == '2':
        Trigonometri()
    elif user_input == '3':
        Statistik()
    elif user_input == '4':
        RegresiLinear()
    else:
        print ()
        print("\033[31m\033[1mERROR : \033[0m\033[31mMenu invalid telah dipilih\033[0m")
        print(input('\033[92mTekan \033[1m[ENTER]\033[0m\033[92m untuk melanjutkan...\033[0m'))