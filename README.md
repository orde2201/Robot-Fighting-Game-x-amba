# Robot-Fighting-Game-x-amba

# Dokumentasi Game Pertarungan Robot

## Deskripsi
Game ini merupakan permainan berbasis teks di mana dua robot bertarung satu sama lain secara bergantian. Pemain dapat memilih aksi untuk menyerang, bertahan, atau menggunakan kemampuan khusus. Permainan berlangsung hingga salah satu robot kehabisan HP atau menyerah.

## Struktur Kelas

### 1. `Robot`
Kelas ini merepresentasikan sebuah robot dalam permainan.

#### **Konstruktor (`__init__` method)**
```python
Robot(hp, shield, energy, name)
```
- `hp` : Jumlah Health Points (HP) robot.
- `shield` : Jumlah perisai yang dapat menyerap serangan.
- `energy` : Energi yang digunakan untuk melakukan skill dan ultimate.
- `name` : Nama robot.

#### **Metode dalam `Robot`**
- `basicAttack(target)`: Melakukan serangan dasar ke robot target.
- `skillAttack(target)`: Menggunakan skill spesial "Rider Kick" jika memiliki cukup energi.
- `ultimateAttack(target)`: Menggunakan serangan pamungkas "Laser Beammm!!" jika memiliki cukup energi.
- `guard()`: Menambah nilai shield sebesar 10.
- `displayStatus()`: Menampilkan status robot dalam format `[HP || Shield || Energy]`.

### 2. `Round`
Kelas ini merepresentasikan ronde dalam permainan.

#### **Konstruktor (`__init__` method)**
```python
Round(roundNow)
```
- `roundNow` : Menyimpan nomor ronde saat ini.

#### **Metode dalam `Round`**
- `displayRound()`: Menampilkan informasi tentang ronde saat ini.

## Mekanisme Permainan
1. Dua robot dibuat dengan HP, shield, dan energy awal 100.
2. Permainan berlangsung dalam ronde, di mana setiap ronde pemain secara bergantian memilih aksi.
3. Pemain dapat memilih antara:
   - Basic Attack (10 damage)
   - Guard (menambah 10 shield)
   - Skill Attack (Rider Kick - 20 damage, membutuhkan 20 energy)
   - Ultimate Attack (Laser Beammm!! - 50 damage, membutuhkan 50 energy)
   - Menyerah (mengakhiri permainan)
4. Setiap ronde, energi bertambah 10.
5. Jika HP salah satu robot habis, lawan menang.
6. Jika seorang pemain memilih menyerah, lawan otomatis menang.

## Contoh Jalannya Permainan di Terminal
```
Round-1 ==================================================================
Ambatron TDR-3000 [100||100||100]
Ambatron Thinkpad [100||100||100]

--- Pilih aksi untuk robot1 (Pemain 1) ---
1. Basic Attack(Atk : 10)
2. Guard
3. Skill (Rider Kick)(Atk : 20)
4. Ultimate (Laser Beammm!!)(Atk : 50)
5. Menyerah
Pilih aksi robot1 (1-5): 1
Ambatron TDR-3000 melakukan serangan dasar ke Ambatron Thinkpad!
Ambatron Thinkpad terkena serangan dasar!

Status setelah aksi robot1:
Ambatron TDR-3000 [100||100||110]
Ambatron Thinkpad [100||90||110]
```

## Kesimpulan
Game ini merupakan permainan sederhana yang menggunakan konsep pemrograman berorientasi objek (OOP) dengan kelas `Robot` dan `Round`. Permainan melibatkan strategi dalam penggunaan serangan, pertahanan, dan pengelolaan energi. Jalankan melalui terminal menggunakan Python untuk memulai pertarungan!

