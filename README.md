# Data Produksi Management
Program ini digunakan untuk mengelola data produksi, termasuk menambah, memperbarui, dan memeriksa data produksi berdasarkan Batch No. Data produksi terdiri dari informasi mengenai operator, mesin, tanggal pengerjaan, material, tipe produk, ukuran produk, dan kualitas produk yang dihasilkan.

# Data Description
Berikut deskripsi kolom:
| No | Nama Kolom | Variabel Kode | Tipe Data | Deskripsi |
| -- | -- | -- | -- | -- |
| 1 | `Batch No.` | `batch_no` | `str` | Nomor batch yang unik untuk setiap produksi. Digunakan sebagai pengenal utama untuk melacak setiap batch. |
| 2 | `ID Operator` | `id_operator` | `str` | ID Operator yang bertanggung jawab pada batch tersebut. Merupakan pengenal unik untuk operator dalam proses produksi. |
| 3 | `Machine ID` | `machine_id` | `str` | ID dari mesin yang digunakan dalam produksi. Setiap mesin memiliki ID unik yang mempermudah identifikasi. |
| 4 | `Tanggal Pengerjaan` | `tanggal_pengerjaan` | `datetime` | Tanggal pengerjaan produk dalam format hari-bulan-tahun. Menunjukkan kapan batch tersebut diproduksi. |
| 5 | `Raw Material` | `raw_material` | `str` | Material yang digunakan sebagai bahan baku dalam produksi batch ini. Berisi nama atau kode bahan baku yang digunakan. |
| 6 | `Product Type` | `product_type` | `str` | Jenis produk yang dihasilkan dari batch tersebut. Menyatakan kategori atau tipe produk yang dibuat. |
| 7 | `Product Size` | `product_size` | `str` | Ukuran produk yang dihasilkan dari batch tersebut. Bisa berupa ukuran fisik atau berat produk. |
| 8 | `Quality` | `quality` | `str` | Kualitas akhir dari produk yang dihasilkan. Berisi nilai 'Good' atau 'Not Good' untuk menilai kualitas produk. |

# Fitur Utama

1. **Login Sistem**
   - User diharuskan login sebelum mengakses aplikasi.
   - Terdapat dua peran yang tersedia:
     - **Administrator**: `adm` / `adm123`
     - **Operator**: `op` / `op123`
   - Setiap peran memiliki hak dan wewenang yang berbeda.

2. **Main Menu**
   - Main Menu **Administrator** memiliki fitur CRUD dan juga tambahan fitur untuk sorting dan filtering data.
   - Main Menu **Operator** hanya terbatas pada fitur Read dan Create.

3. **Menu Data Produksi**
   - User dapat melihat data hasil produksi dalam bentuk tabel yang diformat rapi menggunakan modul `PrettyTable`.
   - **Sorting** (pengurutan data) tersedia berdasarkan kolom seperti Batch No., ID Operator, Tanggal Pengerjaan, dan lainnya, dengan opsi ascending atau descending.
   - **Filtering** (penyaringan data) tersedia berdasarkan kolom tertentu untuk memudahkan pencarian data yang spesifik.

4. **Mengedit/Update Data Produksi**
   - **Administrator** dapat mengedit data pada batch tertentu, seperti Batch No., ID Operator, Tanggal Pengerjaan, dll.
   - Validasi input dilakukan untuk memastikan format data yang benar, terutama pada tanggal dengan format (`DDMMYYY`) dan pilihan Quality (`GOOD`/`NOT GOOD`).

5. **Menambah Input Produksi**
   - User dapat menambahkan data baru, dengan validasi input pada format tanggal dan pilihan Quality yang valid.

6. **Menghapus Data Produksi**
   - **Administrator** dapat menghapus data berdasarkan Batch No. tertentu.

7. **Logout dan Keluar Program**
   - User dapat logout dari sistem dan kembali ke menu login.
   - User juga dapat keluar dari aplikasi sepenuhnya.

# Hak dan Wewenang User

- **Administrator** dapat mengelola data hasil produksi (sort,filter dan update), termasuk menambah, mengedit, dan menghapus data yang sudah ada.
- **Operator** dibatasi hanya dapat melihat data hasil produksi tanpa fitur tambahan sort dan filter serta menginput data.

# Requirement
- Visual Studio Code 1.93.1
- Python 3.12.4
- Tabulate 0.9.0

# Flow Chart
  ![](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/1.%20Menu%20Login.png)
   ![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/2.%20Main%20Menu%20Administrator.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/3.%20Main%20Menu%20Operator.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/4.%20Menu%20Data%20Produksi.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/5.%20Menu%20Sorting.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/6.%20Sort%20By.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/7.%20Menu%20Filter.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/8.%20Update%20Data.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/9.%20Create%20Data.png)
![ ](https://raw.githubusercontent.com/satriaym/capstone-project-m1/main/docs/99.%20Remove%20Data.png)
