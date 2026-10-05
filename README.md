# Muhammad Sholahuddin Sanjaya

# NIM 2609116048

# Kelas B

## Mini Project 2 Dengan Tema Sistem Jadwal Pertandingan Sepak Bola

### Deskripsi Singkat

Tujuan saya Memilih Tema ini adalah Untuk Mencari Tahu Bagaimana Sistem Penjadwalan Bola dapat Bekerja Dengan Baik Dan Benar, 

Dan juga Di kode Yang Saya Buat Sudah Terbagi Menjadi Dua User Yaitu Admin Dan Fans. 

Agar keamanan Program atau Akses Ke program Tidak Diakses Oleh Sembarangan Orang. 

Dan juga Untuk Opsi Opsi Pada setiap User (Admin & Fans) Itu Berbeda Beda

### Gambar Flowchart

<img width="2092" height="1642" alt="Flowchart Sistem Jadwal Sepak Bola" src="https://github.com/user-attachments/assets/dfbbe4e0-a49c-4e31-ab80-81e98af8bb4f" />

Diatas Merupakan Gambar Flowchart Yang Telah saya Buat, 

Terlihat Pada Gambar Di Flowchart Bahwa Kesalahan Input atau Invalid Input akan Mengulang Ke Login User dan

Jika Sudah masuk Bagian Menu User baik Admin Dan Fans Maka Invalid Input Akan Terulang Pada Bagian Menu Input

### Penjelasan Kode

<img width="505" height="142" alt="image" src="https://github.com/user-attachments/assets/8d3d8367-6b25-4976-9707-1a7531f61435" />

Library yang saya pakai ada 4 yaitu, Library Os, Library Time, Library pwinput dan Library Prettytable

library os Berguna untuk Membuat Clear Layar Pada Output terminal

Library Time Berguna Untuk Memberikan Jeda Waktu Ekseskusi

Library pwinput Berguna untuk Menyembunyikan Karakter Saat Mengetik Password

Library prettytable Bertujuan agar Saya dapat Membuat Bentuk table dengan rapi

---

<img width="562" height="90" alt="image" src="https://github.com/user-attachments/assets/76a58c5d-4ee8-4d6e-aa83-59313a9f6197" />

data User yang Menggunakan Fungsi Nested Dictionary yang Bertujuan Untuk Membedakan User 

Terdapat Dua user yaitu admin dan fans

---

<img width="1031" height="118" alt="image" src="https://github.com/user-attachments/assets/0b2e08ea-dfb7-43b3-84dd-f678862525e6" />

Jadwal Pertandingan yang menggunakan fungsi dari Nested Dictionary dengan Meyimpan Hasil jadwal

menggunakan Key/Kunci yang Unik dengan contoh J-01

---

<img width="540" height="85" alt="image" src="https://github.com/user-attachments/assets/fb4f527b-f2e7-4bfe-a4e0-e0f4963c7d59" />


kode diatas merupakan penggunaan library OS Untuk Penggunaan Clear Screen

---

<img width="986" height="343" alt="image" src="https://github.com/user-attachments/assets/f5a2848e-12c5-4844-8143-c660fb93daa9" />

Program pertama-tama mengecek apakah dictionary jadwal_pertandingan kosong; jika kosong, 

program akan mencetak pemberitahuan dan langsung mengakhiri fungsi menggunakan return.

Jika data tersedia, fungsi mendefinisikan objek PrettyTable dan menetapkan nama-nama kolomnya.

Program kemudian melakukan perulangan for untuk membedah setiap kunci dan isi detail dari dictionary, 

memasukkannya sebagai baris tabel (add_row), lalu mencetak tabel tersebut ke layar.  


---

<img width="785" height="652" alt="image" src="https://github.com/user-attachments/assets/ea0e9f5a-9700-4e74-a313-3bef81cbfd56" />

Fungsi meminta pengguna memasukkan ID Jadwal dan langsung divalidasi dengan dua kondisi pencegahan error: 

menolak input jika dikosongkan, dan menolak input jika ID tersebut sudah ada (mencegah duplikasi kunci pada dictionary).   

Setelah lolos validasi, program meminta input nama pertandingan, liga, dan waktu, lalu menyimpannya sebagai dictionary baru ke dalam 

jadwal_pertandingan dengan ID yang diinputkan tadi sebagai kuncinya.   

---

<img width="865" height="612" alt="image" src="https://github.com/user-attachments/assets/ce5ce062-1215-4357-a552-36acc6a75fa6" />

Fungsi ini diawali dengan menampilkan seluruh tabel data, kemudian meminta input ID dari jadwal yang ingin direvisi.   

Terdapat pengecekan kondisi: jika ID yang dicari ada di dalam jadwal_pertandingan, 

program akan meminta detail inputan terbaru dan memperbarui/menimpa isi dictionary pada ID tersebut. 

Jika tidak ditemukan, program melompat ke blok else dan memberi tahu bahwa jadwal tidak ada.   

---

<img width="1200" height="470" alt="image" src="https://github.com/user-attachments/assets/4cfc6fc6-62b9-47fb-8e0d-6985a98eced5" />

Sama halnya dengan pengubahan data, fungsi ini meminta input ID jadwal terlebih dahulu.   

Saat data ditemukan, program memberikan lapis keamanan tambahan berupa konfirmasi penghapusan ("y/n"). Jika pengguna mengetik 'y', 

perintah del dieksekusi untuk menghapus elemen spesifik dari dictionary berdasarkan kuncinya.   

---

<img width="922" height="362" alt="image" src="https://github.com/user-attachments/assets/6fd95e81-320a-4b20-a809-ded53348c5af" />

Dibungkus dengan perulangan while True, fungsi ini akan terus mengulang tampilan login sampai pengguna berhasil masuk.   

Input password direkam menggunakan library eksternal pwinput agar karakter yang diketik tidak terlihat di layar.   

Program memvalidasi apakah username ada di data_users dan mengecek kecocokan kata sandinya; jika benar, 

fungsi mengembalikan nilai (return) berupa 'role' (hak akses) akun tersebut untuk diproses di tahap selanjutnya.

---

<img width="1095" height="822" alt="image" src="https://github.com/user-attachments/assets/7e1cdd6b-e882-4b07-bc2b-0f31cc7ddb49" />

Parameter role digunakan untuk memfilter tampilan antarmuka. Hanya pengguna dengan peran "admin" yang dapat melihat dan mengakses opsi tambah, ubah, dan hapus.

Program menerapkan Error Handling (try-except ValueError) saat menerima konversi input angka int(). 

Ini memastikan bahwa jika pengguna keliru memasukkan karakter huruf, program tidak akan crash, 

melainkan memunculkan notifikasi dan mengulang proses (continue).   

Percabangan if-elif di bagian akhir bertugas memanggil kembali fungsi-fungsi pengolahan data berdasarkan input angka yang valid dari pengguna.   

---

<img width="297" height="100" alt="image" src="https://github.com/user-attachments/assets/e31e3481-c085-4310-a86e-0c83a3d20374" />

Bagian kode ini adalah blok eksekusi utama (titik awal jalannya program) yang menggerakkan keseluruhan sistem Anda secara terus-menerus.  

while True: digunakan untuk membuat perulangan tanpa henti (infinite loop). 

Fungsinya adalah untuk memastikan bahwa setelah seorang pengguna keluar (logout) atau memilih menu "Keluar",

program tidak akan langsung tertutup dan berhenti, melainkan akan terus hidup dan otomatis mengulang kembali ke tampilan layar awal.   

role_aktif = login() bertugas memanggil fungsi login() ke layar. Saat pengguna memasukkan kombinasi yang benar, 

fungsi tersebut akan memberikan hasil akhir (return value) berupa hak akses (contohnya "admin" atau "user"), 

yang nilainya langsung ditangkap dan disimpan ke dalam variabel role_aktif.  

main_menu(role_aktif) bertugas memanggil fungsi menu utama dengan memasukkan variabel role_aktif yang didapat dari proses login sebelumnya sebagai argumen. 

Data hak akses ini dikirim ke dalam fungsi menu agar program tahu dan bisa membedakan 

fasilitas menu apa saja yang boleh diakses oleh orang yang sedang login saat itu.   

---

### Output Program

<img width="510" height="202" alt="image" src="https://github.com/user-attachments/assets/759ac1fa-0209-4b0c-b9eb-6beeae584922" />


<img width="387" height="175" alt="image" src="https://github.com/user-attachments/assets/6cebd97c-c6b4-4c20-aa4d-b0a82cf7ffbf" />

#### ADMIN

<img width="372" height="152" alt="image" src="https://github.com/user-attachments/assets/c63cde07-ff28-4a3f-b098-9bc01dc98a90" />

#### FANS

Program dapat mendeteksi kredensial yang tidak valid, contohnya saat diinput username "jay" program akan menolak akses dan meminta pengguna mencoba lagi.

Sebaliknya, login akan berhasil jika menggunakan akun yang terdaftar pada dictionary, seperti akun "admin" atau akun "fans"

---

<img width="357" height="205" alt="image" src="https://github.com/user-attachments/assets/fa782f1f-fd0b-4f89-84ef-5a5fc846f965" />

Setelah login, program menampilkan antarmuka Menu Utama dengan pilihan 1 hingga 4 dan 0 untuk keluar.

---

<img width="765" height="437" alt="image" src="https://github.com/user-attachments/assets/186a991b-139c-4a6e-ba98-6ad5e16ef04c" />

Saat memilih menu 1, program berhasil menampilkan dictionary jadwal pertandingan ke dalam bentuk 

tabel ASCII yang rapi (berkat library PrettyTable) berisi data awal J-01 dan J-02.

---

