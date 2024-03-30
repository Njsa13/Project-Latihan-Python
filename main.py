"""Latihan Project Python"""

import os
import crud

if __name__ == "__main__":
    SISTEM_OPERASI = os.name

    match SISTEM_OPERASI:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DI DATABASE PERPUSTAKAAN")
    print("=========================")

    # Check database
    crud.init_console()

    while True:
        match SISTEM_OPERASI:
            case "posix":
                os.system("clear")
            case "nt":
                os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DI DATABASE PERPUSTAKAAN")
        print("=========================")

        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        match user_option:
            case "1":
                crud.read_console()
            case "2":
                print("Create Data")
            case "3":
                print("Update Data")
            case "4":
                print("Delete Data")

        is_done = input("Apakah Selesai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir")
