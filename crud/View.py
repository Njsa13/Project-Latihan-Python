from . import Operasi


def read_console():
    data_file = Operasi.read()

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
