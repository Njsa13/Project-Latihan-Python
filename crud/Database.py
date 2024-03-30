from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "judul": 255 * " ",
    "penulis": 255 * " ",
    "tahun": "yyyy",
}

def init_console():
    try:
        with open(DB_NAME, "r", encoding="utf-8") as _:
            print("Database ditemukan")
    except FileNotFoundError:
        print("Database tidak ditemukan, silahkan buat database baru")
        Operasi.create_first_data()
