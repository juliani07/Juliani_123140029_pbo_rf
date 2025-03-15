from abc import ABC, abstractmethod

# Kelas abstrak Plant sebagai blueprint untuk tanaman
class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name  # Nama tanaman
        self.water_needs = water_needs  # Kebutuhan air standar (liter)
        self.fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk standar (kg)

    @abstractmethod
    def grow(self):
        pass  # Metode abstrak yang harus diimplementasikan oleh subclass

    # Metode untuk menyesuaikan kebutuhan air berdasarkan curah hujan
    def calculate_needs(self, rainfall, soil_moisture):
        if rainfall > 5:  # Jika hujan lebih dari 5mm, kurangi kebutuhan air
            self.water_needs -= rainfall // 2
        self.water_needs = max(self.water_needs, 0)  # Pastikan kebutuhan air tidak negatif

    # Menampilkan informasi kebutuhan air dan pupuk setelah penyesuaian
    def show_needs(self, rainfall, soil_moisture):
        print(f"{self.name} is growing in the field")
        print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
        print(f"Adjusted Water Needs: {self.water_needs} liters" + (" (reduced due to rain)" if rainfall > 5 else ""))
        print(f"Adjusted Fertilizer Needs: {self.fertilizer_needs} kg\n")

# Kelas turunan untuk tanaman padi
class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 4)  # Rice butuh 20 liter air & 4 kg pupuk

    def grow(self):
        print("Rice is growing in the paddy field")

# Kelas turunan untuk tanaman jagung
class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 20, 7)  # Corn butuh 20 liter air & 7 kg pupuk

    def grow(self):
        print("Corn is growing in the farm")

if __name__ == "__main__":
    # Buat objek tanaman
    rice = RicePlant()
    corn = CornPlant()

    # User input untuk simulasi kondisi cuaca
    print("Enter weather conditions for Rice:")
    rainfall_rice = int(input("Enter rainfall (mm): "))  # Masukkan curah hujan untuk padi
    soil_moisture_rice = int(input("Enter soil moisture (%): "))  # Masukkan kelembapan tanah
    
    print("\nEnter weather conditions for Corn:")
    rainfall_corn = int(input("Enter rainfall (mm): "))  # Masukkan curah hujan untuk jagung
    soil_moisture_corn = int(input("Enter soil moisture (%): "))  # Masukkan kelembapan tanah

    # Proses pertumbuhan & penyesuaian kebutuhan
    rice.grow()
    rice.calculate_needs(rainfall_rice, soil_moisture_rice)
    rice.show_needs(rainfall_rice, soil_moisture_rice)

    corn.grow()
    corn.calculate_needs(rainfall_corn, soil_moisture_corn)
    corn.show_needs(rainfall_corn, soil_moisture_corn)
