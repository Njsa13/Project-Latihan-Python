from . import operasi


def read_console():
    data_file = operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    print("\n" + "=" * 100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("=" * 100)
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]

        print(f"{index + 1:4} | {judul:.40} | {penulis:.40} | {tahun:5}", end="")
    print("=" * 100 + "\n")


def create_console():
    print("\n\n" + "=" * 100)
    print("Silahkan tambahkan data buku\n")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka dengan format yyyy")
        except ValueError:
            print("Tahun harus angka dengan format yyyy")

    operasi.create(tahun, judul, penulis)
    print("Berikut adalah data anda yang baru ditambahkan")
    read_console()


def update_console():
    read_console()
    while True:
        no_buku = int(input("Masukan nomor buku yang ingin di update: "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        print("\n" + "=" * 100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        user_option = input("Pilih data [1,2,3]:")
        print("\n" + "=" * 100)
        match user_option:
            case "1":
                judul = input("Judul\t: ")
            case "2":
                penulis = input("Penulis\t: ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka dengan format yyyy")
                    except ValueError:
                        print("Tahun harus angka dengan format yyyy")
            case _:
                print("Index tidak cocok")

        is_done = input("Apakah sudah selesai (Y/N) ? ")
        if is_done == "y" or is_done == "Y":
            break

    operasi.update(no_buku, pk, data_add, tahun, judul, penulis)

def delete_console():
    read_console()
    while True:
        no_buku = int(input("Masukan nomor buku yang ingin di delete: "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(",")
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]
            print("Data yang ingin anda hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Apakah sudah selesai (Y/N) ? ")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil dihapus")