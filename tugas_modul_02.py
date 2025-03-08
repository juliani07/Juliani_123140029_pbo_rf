# Nama	: Juliani Leony Putri Melati Manalu
# NIM	: 123140029
# Kelas	: RF

import random

# Fungsi untuk menampilkan banner dalam game
def print_banner(text, symbol="="):
    
    # Membuat banner untuk tampilan lebih menarik dengan garis pemisah.
    
    print(symbol * 60)
    print(f"{text.center(60)}")
    print(symbol * 60)

# Kelas Robot yang berisi atribut dan metode untuk bertarung
class Robot:
    def __init__(self, name, hp, attack, defense, accuracy):
        
        # Inisialisasi robot dengan atribut:
        # name: Nama robot
        # hp: Health Points (HP)
        # attack: Kekuatan serangan
        # defense: Pertahanan
        # accuracy: Akurasi serangan (probabilitas mengenai musuh)
        # stunned: Status apakah robot sedang terkena stun
    
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy
        self.stunned = False

    def attack_enemy(self, enemy):
    
        # Metode untuk menyerang robot musuh.
        # Jika robot terkena stun, ia tidak bisa menyerang pada giliran ini.
        
        if self.stunned:
            print(f"⚡ {self.name} tidak bisa menyerang karena terkena STUN! ⚡")
            self.stunned = False  # Menghapus status stun setelah giliran ini
            return
        
        # Serangan hanya berhasil jika random number <= accuracy
        if random.random() <= self.accuracy:
            damage = max(self.attack - enemy.defense, 0)  # Menghitung damage setelah dikurangi defense musuh
            enemy.hp -= damage
            print(f"🔥 {self.name} menyerang {enemy.name} dan menyebabkan {damage} damage! 🔥")
        else:
            print(f"❌ {self.name} gagal menyerang! ❌")

    def stun_enemy(self, enemy):
        
        # Metode untuk memberikan efek stun pada musuh.
        # Ada peluang 30% untuk berhasil.
        
        if random.random() < 0.3:
            enemy.stunned = True
            print(f"⚡ {self.name} berhasil melakukan STUN pada {enemy.name}! ⚡")
        else:
            print(f"❌ {self.name} mencoba STUN tetapi gagal! ❌")

    def regen_health(self):
        
        # Metode untuk meregenerasi HP robot.
        # Menambah 10% dari HP saat ini.
        
        heal = int(self.hp * 0.1)
        self.hp += heal
        print(f"💚 {self.name} meregenerasi {heal} HP! 💚")

    def is_defeated(self):
        
        # Mengecek apakah robot telah kalah (HP <= 0).
        
        return self.hp <= 0

# Kelas Game untuk mengatur jalannya permainan
class Game:
    def __init__(self, robot1, robot2):
        
        # Inisialisasi game dengan dua robot yang bertarung.
        
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def display_status(self):
        
        # Menampilkan status kedua robot, termasuk HP, Attack, dan Defense.
        
        print(f"{self.robot1.name}: ❤️ {self.robot1.hp} | ⚔️ {self.robot1.attack} | 🛡️ {self.robot1.defense}")
        print(f"{self.robot2.name}: ❤️ {self.robot2.hp} | ⚔️ {self.robot2.attack} | 🛡️ {self.robot2.defense}")

    def play(self):
        
        # Metode utama untuk menjalankan permainan.
        # Robot bergiliran melakukan aksi sampai salah satu kalah.
        
        print_banner("🤖 Robot Battle Begins! 🤖")
        
        while not self.robot1.is_defeated() and not self.robot2.is_defeated():
            print_banner(f"Round {self.round}")
            self.display_status()
            
            # Pemilihan aksi oleh robot pertama
            print("1. ⚔️ Attack  2. ⚡ Stun  3. 💚 Regen  4. ❌ Giveup")
            action1 = int(input(f"{self.robot1.name}, pilih aksi: "))
            if action1 == 4:
                print_banner(f"🏆 {self.robot2.name} Menang! 🏆")
                return
            elif action1 == 1:
                self.robot1.attack_enemy(self.robot2)
            elif action1 == 2:
                self.robot1.stun_enemy(self.robot2)
            elif action1 == 3:
                self.robot1.regen_health()

            if self.robot2.is_defeated():
                print_banner(f"🏆 {self.robot1.name} Menang! 🏆")
                return
            
            # Pemilihan aksi oleh robot kedua
            print("1. ⚔️ Attack  2. ⚡ Stun  3. 💚 Regen  4. ❌ Giveup")
            action2 = int(input(f"{self.robot2.name}, pilih aksi: "))
            if action2 == 4:
                print_banner(f"🏆 {self.robot1.name} Menang! 🏆")
                return
            elif action2 == 1:
                self.robot2.attack_enemy(self.robot1)
            elif action2 == 2:
                self.robot2.stun_enemy(self.robot1)
            elif action2 == 3:
                self.robot2.regen_health()

            if self.robot1.is_defeated():
                print_banner(f"🏆 {self.robot2.name} Menang! 🏆")
                return
            
            self.round += 1

# Contoh Pemakaian Game
robot1 = Robot("Atreus", 500, 10, 2, 0.8)  # Robot pertama dengan 500 HP, 10 Attack, 2 Defense, 80% Akurasi
robot2 = Robot("Daedalus", 750, 8, 3, 0.7)  # Robot kedua dengan 750 HP, 8 Attack, 3 Defense, 70% Akurasi

game = Game(robot1, robot2)  # Membuat instance game dengan dua robot
game.play()  # Memulai permainan