import numpy as np
from tabulate import tabulate

def main():
    # load data nya agak sulit karena dalam data terdapat data string, maka melalui documentasi melalui https://numpy.org/doc/1.26/reference/generated/numpy.loadtxt.html#numpy-loadtxt dapat diketahui bahwa menggunakan skiprows dan usecols untuk menentukan row yg pertama ingin dihilangkan dan juga akan menggunakan colom dari pertama (dari 0) sampai akhirnya
    nim = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv', delimiter=',', skiprows=1, usecols=(0), dtype=str)
    latsol = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv', delimiter=',', skiprows=1, usecols=(1, 2, 3, 4, 5, 6, 7))
    kuis = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Kuis.csv', delimiter=',', skiprows=1, usecols=(1, 2, 3, 4, 5, 6, 7))
    lab = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Lab.csv', delimiter=',', skiprows=1, usecols=(1, 2))
    proyek = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Proyek.csv', delimiter=',', skiprows=1, usecols=(1, 2))
    jurnal = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Jurnal.csv', delimiter=',', skiprows=1, usecols=(1, 2))
    ujian = np.loadtxt('https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Ujian.csv', delimiter=',', skiprows=1, usecols=(1, 2))

    total = [latsol, kuis, lab, proyek, jurnal, ujian]
    bobot = [0, 0, 0, 0, 35/100, 15/100]

    total_bobot = []
    total_bobot.append(latsol * 0)
    total_bobot.append(kuis * 0)
    total_bobot.append(lab * 0)
    total_bobot.append(proyek * 0)
    jurnal_1 = jurnal[:,0] * 70/100
    jurnal_2 = jurnal[:,1] * 0
    jurnal_1 = jurnal_1.reshape(np.size(jurnal_1), 1)
    jurnal_2 = jurnal_2.reshape(np.size(jurnal_2), 1)
    jurnal_bobot = np.block([jurnal_1, jurnal_2])

    total_bobot.append(jurnal_bobot)
    total_bobot.append(ujian * 15/100)

    total_bobot_gabungan = []
    for i in total_bobot:
        total_bobot_gabungan.append(np.sum(i, axis=1))

    total_bobot_gabungan = return_npblock(total_bobot_gabungan)

    nilai_akhir = np.sum(total_bobot_gabungan, axis=0)

    index = []
    for i in nilai_akhir:
        index.append(get_index(i))

    table_akhir = zip(nim, nilai_akhir, index)

    print(tabulate(table_akhir, headers=["NIM", "Nilai Akhir", "Indeks Penilaian"], tablefmt='rounded_grid'))

    print("\nAnalisis Data Sebelum")
    hitung_index(index)
    print("\nRata rata per data")
    for i in total:
        print(np.mean(i))

    print("\ntotal dengan bobot")
    for i in total_bobot_gabungan:
        print(np.mean(i))

    print("\nRata-rata:", np.mean(nilai_akhir))

def get_index(nilai):
    if nilai > 90:
        return "A"
    elif nilai > 85:
        return "A-"
    elif nilai > 80:
        return "B+"
    elif nilai > 75:
        return "B"
    elif nilai > 65:
        return "B-"
    elif nilai > 60:
        return "C+"
    elif nilai > 50:
        return "C"
    elif nilai > 45:
        return "C-"
    elif nilai > 40:
        return "D"
    else:
        return "F"
def hitung_index(s):
    A = 0
    F = 0
    for i in s:
        if "A" == i:
            A += 1
        elif "F" == i:
            F += 1
    print("A:", A)
    print("F:", F)

def return_npblock(array):
    matrix = np.block([
        [array[0]],
        [array[1]],
        [array[2]],
        [array[3]],
        [array[4]],
        [array[5]],
    ])

    return matrix


if __name__ == "__main__":
    main()
