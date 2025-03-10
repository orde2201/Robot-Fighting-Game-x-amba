# Import library sys untuk menghentikan program secara paksa jika diperlukan
import sys

# Class Robot untuk membuat objek robot dengan atribut dan metode yang diperlukan
class Robot:
    def __init__(self, hp, shield, energy, name):
        # Inisialisasi atribut robot
        self.name = name  # Nama robot
        self.hp = hp  # Health Points (HP) robot
        self.shield = shield  # Shield robot
        self.energy = energy  # Energi robot
        self.attack = 10  # Damage serangan dasar
        self.skill = 20  # Damage serangan skill
        self.ultimate = 50  # Damage serangan ultimate

    # Metode untuk serangan dasar
    def basicAttack(self, target):
        print(f"{self.name} melakukan serangan dasar ke {target.name}!")
        damage = self.attack  # Damage serangan dasar

        # Menangani shield target terlebih dahulu
        if target.shield > 0:
            # Jika target memiliki shield, kurangi shield terlebih dahulu
            if target.shield >= damage:
                target.shield -= damage  # Shield berkurang sebesar damage
            else:
                remaining_damage = damage - target.shield  # Hitung sisa damage setelah shield habis
                target.shield = 0  # Shield habis
                target.hp -= remaining_damage  # Kurangi HP target dengan sisa damage
        else:
            # Jika tidak ada shield, langsung kurangi HP target
            target.hp -= damage
        print(f"{target.name} terkena serangan dasar!")

    # Metode untuk serangan skill
    def skillAttack(self, target):
        if self.energy >= 20:  # Cek apakah energi cukup untuk menggunakan skill
            print(f"{self.name} menggunakan skill Rider Kick ke {target.name}!")
            damage = self.skill  # Damage serangan skill

            # Menangani shield target terlebih dahulu
            if target.shield > 0:
                if target.shield >= damage:
                    target.shield -= damage  # Shield berkurang sebesar damage
                else:
                    remaining_damage = damage - target.shield  # Hitung sisa damage setelah shield habis
                    target.shield = 0  # Shield habis
                    target.hp -= remaining_damage  # Kurangi HP target dengan sisa damage
            else:
                target.hp -= damage  # Kurangi HP target langsung jika tidak ada shield
            print(f"{target.name} terkena Rider Kick!")
            self.energy -= 20  # Kurangi energi setelah menggunakan skill
            print(f"Energy {self.name} sekarang: {self.energy}")
        else:
            print(f"{self.name} tidak memiliki cukup energi untuk menggunakan skill!")

    # Metode untuk serangan ultimate
    def ultimateAttack(self, target):
        if self.energy >= 50:  # Cek apakah energi cukup untuk menggunakan ultimate
            print(f"{self.name} menggunakan Ultimate Laser Beammm!! ke {target.name}!")
            damage = self.ultimate  # Damage serangan ultimate

            # Menangani shield target terlebih dahulu
            if target.shield > 0:
                if target.shield >= damage:
                    target.shield -= damage  # Shield berkurang sebesar damage
                else:
                    remaining_damage = damage - target.shield  # Hitung sisa damage setelah shield habis
                    target.shield = 0  # Shield habis
                    target.hp -= remaining_damage  # Kurangi HP target dengan sisa damage
            else:
                target.hp -= damage  # Kurangi HP target langsung jika tidak ada shield
            print(f"{target.name} terkena Laser Beammm!!")
            self.energy -= 50  # Kurangi energi setelah menggunakan ultimate
        else:
            print(f"{self.name} tidak memiliki cukup energi untuk menggunakan ultimate!")

    # Metode untuk bertahan (guard)
    def guard(self):
        self.shield += 10  # Tambahkan 10 ke shield
        print(f"{self.name} meningkatkan shield! Shield sekarang: {self.shield}")

    # Metode untuk menampilkan status robot
    def displayStatus(self):
        return f"{self.name} [{self.hp}||{self.shield}||{self.energy}]"

# Class Round untuk mengelola ronde pertarungan
class Round:
    def __init__(self, roundNow):
        self.roundNow = roundNow  # Nomor ronde saat ini

    # Metode untuk menampilkan ronde saat ini
    def displayRound(self):
        return f"Round-{self.roundNow} " + 70 * "="

# Membuat dua robot untuk pertarungan
robot1 = Robot(100, 100, 100, "Ambatron TDR-3000")
robot2 = Robot(100, 100, 100, "Ambatron Thinkpad")

# Inisialisasi ronde pertama
roundNow = Round(1)
print(roundNow.displayRound())  # Tampilkan ronde pertama
print(f"{robot1.displayStatus()}")  # Tampilkan status robot1
print(f"{robot2.displayStatus()}")  # Tampilkan status robot2

# Loop utama untuk pertarungan (Player vs Player)
while True:
    # Tambahkan energi setiap ronde untuk kedua robot
    robot1.energy += 10
    robot2.energy += 10

    # Loop untuk memilih aksi robot1
    while True:
        print(f"\n--- Pilih aksi untuk robot1 (Ambatron TDR-3000) ---")
        print("1. Basic Attack(Atk : 10)\n2. Guard\n3. Skill (Rider Kick)(Atk : 20)\n4. Ultimate (Laser Beammm!!)(Atk : 50)\n5. Menyerah")
        choice1 = input("Pilih aksi robot1 (1-5): ")

        if choice1 == "1":
            robot1.basicAttack(robot2)  # Lakukan serangan dasar
            break
        elif choice1 == "2":
            robot1.guard()  # Lakukan guard
            break
        elif choice1 == "3":
            robot1.skillAttack(robot2)  # Lakukan serangan skill
            break
        elif choice1 == "4":
            robot1.ultimateAttack(robot2)  # Lakukan serangan ultimate
            break
        elif choice1 == "5":
            print(f"{robot1.name} menyerah! {robot2.name} menang!")  # Robot1 menyerah
            sys.exit()  # Keluar dari program
        else:
            print("Pilihan tidak valid, coba lagi.")  # Pesan kesalahan jika input tidak valid

    # Cek apakah robot2 sudah kalah (HP <= 0)
    if robot2.hp <= 0:
        print(f"{robot2.name} telah hancur! {robot1.name} menang!")
        break  # Keluar dari loop pertarungan

    # Tampilkan status setelah aksi robot1
    print("\nStatus setelah aksi robot1:")
    print(f"{robot1.displayStatus()}")
    print(f"{robot2.displayStatus()}")

    # Loop untuk memilih aksi robot2
    while True:
        print("\n--- Pilih aksi untuk robot2 (Ambatron Thinkpad) ---")
        print("1. Basic Attack\n2. Guard\n3. Skill (Rider Kick)\n4. Ultimate (Laser Beammm!!)\n5. Menyerah")
        choice2 = input("Pilih aksi robot2 (1-5): ")

        if choice2 == "1":
            robot2.basicAttack(robot1)  # Lakukan serangan dasar
            break
        elif choice2 == "2":
            robot2.guard()  # Lakukan guard
            break
        elif choice2 == "3":
            robot2.skillAttack(robot1)  # Lakukan serangan skill
            break
        elif choice2 == "4":
            robot2.ultimateAttack(robot1)  # Lakukan serangan ultimate
            break
        elif choice2 == "5":
            print(f"{robot2.name} menyerah! {robot1.name} menang!")  # Robot2 menyerah
            sys.exit()  # Keluar dari program
        else:
            print("Pilihan tidak valid, coba lagi.")  # Pesan kesalahan jika input tidak valid

    # Cek apakah robot1 sudah kalah (HP <= 0)
    if robot1.hp <= 0:
        print(f"{robot1.name} telah hancur! {robot2.name} menang!")
        break  # Keluar dari loop pertarungan

    # Tampilkan status setelah aksi robot2
    print("\nStatus setelah aksi robot2:")
    print(f"{robot1.displayStatus()}")
    print(f"{robot2.displayStatus()}")

    # Lanjutkan ke ronde berikutnya
    roundNow.roundNow += 1  # Tambahkan nomor ronde
    print(roundNow.displayRound())  # Tampilkan ronde baru
