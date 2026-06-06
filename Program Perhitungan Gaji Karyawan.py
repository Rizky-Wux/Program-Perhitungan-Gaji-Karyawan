    # Program Perhitungan Gaji Karyawan
    # Menggunakan Array (List), Operator, dan Percabangan

    # Array gaji pokok berdasarkan golongan
    gaji = [5000000, 6500000, 9500000]

    # Array persentase lembur
    persen_lembur_array = [30, 32, 34, 36, 38]

    print("====================================")
    print(" PROGRAM PERHITUNGAN GAJI KARYAWAN ")
    print("====================================")

    # Input golongan
    golongan = input("Masukkan Golongan (A/B/C): ").upper()

    # Menentukan gaji pokok
    if golongan == "A":
        gaji_pokok = gaji[0]
    elif golongan == "B":
        gaji_pokok = gaji[1]
    elif golongan == "C":
        gaji_pokok = gaji[2]
    else:
        print("Golongan tidak valid!")
        exit()

    # Input jam lembur
    jam_lembur = int(input("Masukkan Jumlah Jam Lembur: "))

    # Menentukan persentase lembur
    if jam_lembur == 1:
        persen_lembur = persen_lembur_array[0]
    elif jam_lembur == 2:
        persen_lembur = persen_lembur_array[1]
    elif jam_lembur == 3:
        persen_lembur = persen_lembur_array[2]
    elif jam_lembur == 4:
        persen_lembur = persen_lembur_array[3]
    elif jam_lembur >= 5:
        persen_lembur = persen_lembur_array[4]
    else:
        persen_lembur = 0

    # Menghitung gaji lembur
    gaji_lembur = gaji_pokok * persen_lembur / 100

    # Menghitung total gaji
    total_gaji = gaji_pokok + gaji_lembur

    # Menampilkan hasil
    print("\n===== HASIL PERHITUNGAN =====")
    print("Golongan            :", golongan)
    print("Gaji Pokok          : Rp {:,.0f}".format(gaji_pokok))
    print("Persentase Lembur   :", str(persen_lembur) + "%")
    print("Gaji Lembur         : Rp {:,.0f}".format(gaji_lembur))
    print("Total Gaji          : Rp {:,.0f}".format(total_gaji))
