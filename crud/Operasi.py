from . import database
from . import util
import time
import os


def create_first_data():
    data = database.TEMPLATE.copy()
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka dengan format yyyy")
        except ValueError:
            print("Tahun harus angka dengan format yyyy")

    data["pk"] = util.random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)
    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"

    try:
        with open(database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except IOError:
        print("Gagal menambahkan data")


def read(**kwargs):
    try:
        with open(database.DB_NAME, "r", encoding="utf-8") as file:
            content = file.readlines()
            if "index" in kwargs:
                index_buku = int(kwargs["index"]) - 1
                if index_buku < 0 or index_buku > len(content) - 1:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except FileNotFoundError:
        print("Gagal Membaca Database")
        return False


def create(tahun, judul, penulis):
    data = database.TEMPLATE.copy()
    data["pk"] = util.random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)
    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"

    try:
        with open(database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except IOError:
        print("Gagal membuat data")


def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = database.TEMPLATE.copy()
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + database.TEMPLATE["penulis"][len(penulis) :]
    data["judul"] = judul + database.TEMPLATE["judul"][len(judul) :]
    data["tahun"] = str(tahun)
    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"

    try:
        with open(database.DB_NAME, "r+", encoding="utf-8") as file:
            lines = file.readlines()
            lines[no_buku - 1] = data_str
            file.seek(0)
            file.writelines(lines)
    except FileNotFoundError:
        print("Error dalam mengupdate buku")


def delete(no_buku):
    try:
        with open(database.DB_NAME, "r", encoding="utf-8") as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except FileNotFoundError:
        print("Error dalam menghapus buku")
        
    os.remove(database.DB_NAME)
    os.rename("data_temp.txt", database.DB_NAME)
