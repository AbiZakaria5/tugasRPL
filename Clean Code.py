from dataclasses import dataclass

KURUS = "Kurus"
NORMAL = "Normal"
KELEBIHAN = "Kelebihan berat badan"
OBESITAS = "Obesitas"

@dataclass
class DataPengguna:
    nama: str
    berat: float
    tinggi: float

class BMICalculator:
    def hitung_bmi(self, berat: float, tinggi: float) -> float:
        tinggi_meter = tinggi / 100
        return berat / (tinggi_meter ** 2)

    def tentukan_kategori(self, bmi: float) -> str:
        if bmi < 18.5:
            return KURUS
        if bmi < 25:
            return NORMAL
        if bmi < 30:
            return KELEBIHAN
        return OBESITAS

class KonsolUI:
    def ambil_input_pengguna(self) -> DataPengguna:
        nama = input("Masukkan nama: ")
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (cm): "))
        return DataPengguna(nama, berat, tinggi)

    def tampilkan_hasil(self, pengguna: DataPengguna, bmi: float, kategori: str):
        print("\n=== HASIL BMI ===")
        print(f"Nama     : {pengguna.nama}")
        print(f"BMI      : {bmi:.2f}")
        print(f"Kategori : {kategori}")


def main():
    ui = KonsolUI()
    kalkulator = BMICalculator()

    pengguna = ui.ambil_input_pengguna()
    bmi = kalkulator.hitung_bmi(pengguna.berat, pengguna.tinggi)
    kategori = kalkulator.tentukan_kategori(bmi)

    ui.tampilkan_hasil(pengguna, bmi, kategori)


if __name__ == "__main__":
    main()
