from . import Database
from . import Util
import time

def create_first_data():
    data = Database.TEMPLATE.copy()
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    tahun = input("Tahun: ")

    data["pk"] = Util.random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = tahun
    data_str = (
        f"{data['pk']},{data['date_add']},{data['judul']},"
        f"{data['penulis']},{data['tahun']}\n"
    )
    print(data_str)
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except IOError:
        print("Gagal membuat data:")

def read():
    try:
        with open(Database.DB_NAME, "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print("Gagal Membaca Database")
        return False