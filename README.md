# Management Data Hasil Produksi
Program ini digunakan untuk mengelola data produksi, termasuk menambah, memperbarui, dan memeriksa data produksi berdasarkan Batch No. Data produksi terdiri dari informasi mengenai operator, mesin, tanggal pengerjaan, material, tipe produk, ukuran produk, dan kualitas produk yang dihasilkan.

# Data Description  
Berikut deskripsi kolom:
| No | Nama Kolom | Type | Deskripsi |
| -- | -- | -- | -- |
| 1 | `Batch No.` | `str` | Nomor batch yang unik untuk setiap produksi |
| 2 | `ID Operator` | `str` | ID Operator yang bertanggung jawab pada batch tersebut |
| 3 | `Machine ID` | `str` | ID dari mesin yang digunakan dalam produksi |
| 4 | `Tanggal Pengerjaan` | `datetime` | Tanggal pengerjaan produk dalam format hari-bulan-tahun |
| 5 | `Raw Material` | `str` | Material yang digunakan sebagai bahan baku |
| 6 | `Product Type` | `str` | Jenis produk yang dihasilkan dari batch tersebut |
| 7 | `Product Size` | `str` | Ukuran produk yang dihasilkan |
| 8 | `Quality` | `str` | Kualitas akhir dari produk (Good atau Not Good) |

# Fitur Utama

1. **Login Sistem**
   - Pengguna diharuskan login sebelum mengakses aplikasi.
   - Terdapat dua peran yang tersedia:
     - **Administrator**: `adm` / `adm123`
     - **Operator**: `op` / `op123`
   - Setiap peran memiliki hak dan wewenang yang berbeda.  

2. **Menu Data Produksi**
   - Pengguna dapat melihat data hasil produksi dalam bentuk tabel yang diformat rapi menggunakan modul `PrettyTable`.
   - **Sorting** (pengurutan data) tersedia berdasarkan kolom seperti Batch No., ID Operator, Tanggal Pengerjaan, dan lainnya, dengan opsi ascending atau descending.
   - **Filtering** (penyaringan data) tersedia berdasarkan kolom tertentu untuk memudahkan pencarian data yang spesifik.

3. **Mengedit Data Produksi**
   - Administrator dapat mengedit data pada batch tertentu, seperti Batch No., ID Operator, Tanggal Pengerjaan, dll.
   - Validasi input dilakukan untuk memastikan format data yang benar, terutama pada tanggal dengan format (`DDMMYYY`) dan pilihan Quality (`GOOD`/`NOT GOOD`).

4. **Menambah Input Produksi**
   - Pengguna dapat menambahkan data baru, dengan validasi input pada format tanggal dan pilihan Quality yang valid.

5. **Menghapus Data Produksi**
   - Administrator dapat menghapus data berdasarkan Batch No. tertentu.

6. **Logout dan Keluar Program**
   - Pengguna dapat logout dari sistem dan kembali ke menu login.
   - Pengguna juga dapat keluar dari aplikasi sepenuhnya.

## Hak dan Wewenang User

- **Administrator** dapat mengelola data hasil produksi, termasuk menambah, mengedit, dan menghapus data yang sudah ada.
- **Operator** hanya dapat melihat data hasil produksi dan menginput data.
