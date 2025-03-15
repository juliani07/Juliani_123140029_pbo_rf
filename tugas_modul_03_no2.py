from abc import ABC, abstractmethod

# Kelas induk Employee (abstrak)
class Employee(ABC):
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.task_completed = task_completed
    
    @abstractmethod
    def work(self):
        pass  # Metode ini harus diimplementasikan di setiap subclass

    # Evaluasi performa berdasarkan jam kerja dan tugas selesai
    def evaluate_performance(self):
        efficiency = self.task_completed / max(self.hours_worked, 1)  # Hindari pembagian nol
        
        # Klasifikasi rating performa
        if efficiency > 1.5:
            return "High Performance"
        elif efficiency > 1.0:
            return "Medium Performance"
        else:
            return "Low Performance"

# Karyawan dengan peran Software Engineer
class SoftwareEngineer(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Software Engineer", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} is coding and fixing bugs!")

# Karyawan dengan peran Data Scientist
class DataScientist(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Data Scientist", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} is analyzing data and building ML models!")

# Karyawan dengan peran Product Manager
class ProductManager(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Product Manager", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} is planning features and coordinating teams!")

# Simulasi penggunaan program dengan input dari user
if __name__ == "__main__":
    employees = []
    num_employees = int(input("Enter the number of employees: "))  # Minta jumlah karyawan
    
    for _ in range(num_employees):
        name = input("Enter employee name: ")  # Nama karyawan
        role = input("Enter role (Software Engineer, Data Scientist, Product Manager): ")  # Pilih role
        hours_worked = int(input("Enter hours worked: "))  # Masukkan jam kerja
        task_completed = int(input("Enter tasks completed: "))  # Masukkan jumlah tugas selesai
        
        # Buat objek berdasarkan peran yang dipilih
        if role.lower() == "software engineer":
            employees.append(SoftwareEngineer(name, hours_worked, task_completed))
        elif role.lower() == "data scientist":
            employees.append(DataScientist(name, hours_worked, task_completed))
        elif role.lower() == "product manager":
            employees.append(ProductManager(name, hours_worked, task_completed))
        else:
            print("Invalid role! Skipping this entry.")
    
    # Tampilkan aktivitas kerja dan evaluasi performa mereka
    print("\nEmployee Performance Report:")
    for emp in employees:
        emp.work()
        print(f"Performance Rating for {emp.name} ({emp.role}): {emp.evaluate_performance()}\n")
