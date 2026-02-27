from datetime import date

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
NEPTU_HARI = {
    "Senin": 4,
    "Selasa": 3,
    "Rabu": 7,
    "Kamis": 8,
    "Jumat": 6,
    "Sabtu": 9,
    "Minggu": 5
}

PASARAN = ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]
NEPTU_PASARAN = {
    "Legi": 5,
    "Pahing": 9,
    "Pon": 7,
    "Wage": 4,
    "Kliwon": 8
}

TANGGAL_REFERENSI = date(1900, 1, 1)
HARI_REF_INDEX = 0       
PASARAN_REF_INDEX = 1    

def hitung_hari(tanggal_lahir: date) -> str:
    selisih = (tanggal_lahir - TANGGAL_REFERENSI).days
    index_hari = (HARI_REF_INDEX + selisih) % 7
    return HARI[index_hari]

def hitung_pasaran(tanggal_lahir: date) -> str:
    selisih = (tanggal_lahir - TANGGAL_REFERENSI).days
    index_pasaran = (PASARAN_REF_INDEX + selisih) % 5
    return PASARAN[index_pasaran]

def hitung_neptu(nama_hari: str, nama_pasaran: str) -> int:
    return NEPTU_HARI[nama_hari] + NEPTU_PASARAN[nama_pasaran]

def tampilkan_hasil(nama: str, tgl: date, hari: str, pasaran: str, neptu: int):
    print()
    print("=" * 50)
    print("          HASIL PERHITUNGAN WETON JAWA")
    print("=" * 50)
    print(f"  Nama          : {nama}")
    print(f"  Tanggal Lahir : {tgl.strftime('%d-%m-%Y')}")
    print("-" * 50)
    print(f"  Hari Lahir    : {hari}")
    print(f"  Pasaran Lahir : {pasaran}")
    print(f"  Weton Lengkap : {hari} {pasaran}")
    print("-" * 50)
    print(f"  Neptu Hari    : {NEPTU_HARI[hari]}  ({hari})")
    print(f"  Neptu Pasaran : {NEPTU_PASARAN[pasaran]}  ({pasaran})")
    print(f"  Total Neptu   : {neptu}")
    print("-" * 50)

def main():
    print("===== KALKULATOR WETON JAWA =====")
    print(" - Hitung Neptu")
    print(" - Hitung Pasaran")
    print()

    nama = str(input("Masukkan nama lengkap Anda : "))
    tanggal = int(input("Masukkan tanggal lahir Anda: "))
    bulan = int(input("Masukkan bulan lahir Anda  : "))
    tahun = int(input("Masukkan tahun lahir Anda  : "))

    try:
        tanggal_lahir = date(tahun, bulan, tanggal)
    except ValueError:
        print("Tanggal yang dimasukkan tidak valid!")
        return

    hari = hitung_hari(tanggal_lahir)
    pasaran = hitung_pasaran(tanggal_lahir)
    neptu = hitung_neptu(hari, pasaran)

    tampilkan_hasil(nama, tanggal_lahir, hari, pasaran, neptu)

if __name__ == "__main__":
    main()

