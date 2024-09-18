from datetime import datetime
from prettytable import PrettyTable
import pyinputplus as pyip

# List data produksi
data = [
    {'Batch No.': 'H3-TS-0824-1', 'ID Operator': '001', 'Machine ID': 'M001', 'Tanggal Pengerjaan': datetime.strptime('16082024', '%d%m%Y'), 'Raw Material': 'TS-51H', 'Product Type': 'HEXAGONAL', 'Product Size': '3 M', 'Quality': 'GOOD'},
    {'Batch No.': 'S4-UTS-0824-1', 'ID Operator': '002', 'Machine ID': 'M002', 'Tanggal Pengerjaan': datetime.strptime('17082024', '%d%m%Y'), 'Raw Material': 'UTS-50', 'Product Type': 'SQUARE', 'Product Size': '4 M', 'Quality': 'GOOD'},
    {'Batch No.': 'H3-TS-0824-2', 'ID Operator': '003', 'Machine ID': 'M001', 'Tanggal Pengerjaan': datetime.strptime('18082024', '%d%m%Y'), 'Raw Material': 'TS-51H', 'Product Type': 'HEXAGONAL', 'Product Size': '3 M', 'Quality': 'NOT GOOD'},
    {'Batch No.': 'S4-UTS-0824-2', 'ID Operator': '001', 'Machine ID': 'M002', 'Tanggal Pengerjaan': datetime.strptime('19082024', '%d%m%Y'), 'Raw Material': 'UTS-50', 'Product Type': 'SQUARE', 'Product Size': '4 M', 'Quality': 'GOOD'},
    {'Batch No.': 'H3-TS-0824-3', 'ID Operator': '003', 'Machine ID': 'M002', 'Tanggal Pengerjaan': datetime.strptime('20082024', '%d%m%Y'), 'Raw Material': 'TS-51H', 'Product Type': 'HEXAGONAL', 'Product Size': '3 M', 'Quality': 'NOT GOOD'},
    {'Batch No.': 'S4-UTS-0824-3', 'ID Operator': '002', 'Machine ID': 'M001', 'Tanggal Pengerjaan': datetime.strptime('21082024', '%d%m%Y'), 'Raw Material': 'UTS-50', 'Product Type': 'SQUARE', 'Product Size': '4 M', 'Quality': 'NOT GOOD'},
    {'Batch No.': 'H3-TS-0824-4', 'ID Operator': '001', 'Machine ID': 'M002', 'Tanggal Pengerjaan': datetime.strptime('22082024', '%d%m%Y'), 'Raw Material': 'TS-51H', 'Product Type': 'HEXAGONAL', 'Product Size': '3 M', 'Quality': 'GOOD'},
    {'Batch No.': 'S4-UTS-0824-4', 'ID Operator': '003', 'Machine ID': 'M001', 'Tanggal Pengerjaan': datetime.strptime('16082024', '%d%m%Y'), 'Raw Material': 'UTS-50', 'Product Type': 'SQUARE', 'Product Size': '4 M', 'Quality': 'GOOD'},
    {'Batch No.': 'H3-TS-0824-5', 'ID Operator': '002', 'Machine ID': 'M002', 'Tanggal Pengerjaan': datetime.strptime('17082024', '%d%m%Y'), 'Raw Material': 'TS-51H', 'Product Type': 'HEXAGONAL', 'Product Size': '3 M', 'Quality': 'GOOD'},
    {'Batch No.': 'S4-UTS-0824-5', 'ID Operator': '001', 'Machine ID': 'M001', 'Tanggal Pengerjaan': datetime.strptime('18082024', '%d%m%Y'), 'Raw Material': 'UTS-50', 'Product Type': 'SQUARE', 'Product Size': '4 M', 'Quality': 'GOOD'},
    {'Batch No.': 'H3-TS-0824-6', 'ID Operator': '003', 'Machine ID': 'M002', 'Tanggal Pengerjaan': datetime.strptime('19082024', '%d%m%Y'), 'Raw Material': 'TS-51H', 'Product Type': 'HEXAGONAL', 'Product Size': '3 M', 'Quality': 'NOT GOOD'},
    {'Batch No.': 'S4-UTS-0824-6', 'ID Operator': '002', 'Machine ID': 'M001', 'Tanggal Pengerjaan': datetime.strptime('20082024', '%d%m%Y'), 'Raw Material': 'UTS-50', 'Product Type': 'SQUARE', 'Product Size': '4 M', 'Quality': 'NOT GOOD'},
]
# Fungsi untuk mencetak data dalam format tabel
def print_formatted_data(data):  
    table = PrettyTable()
    table.field_names = ['Batch No.', 'ID Operator', 'Machine ID', 'Tanggal Pengerjaan', 'Raw Material', 'Product Type', 'Product Size', 'Quality']
    
    for item in data:
        table.add_row([
            item['Batch No.'],
            item['ID Operator'],
            item['Machine ID'],
            item['Tanggal Pengerjaan'].strftime('%d-%m-%Y'),
            item['Raw Material'],
            item['Product Type'],
            item['Product Size'],
            item['Quality']
        ])
    return table

# Fungsi untuk sort data
def sort_data(data, sort_by, ascending=True):
    return sorted(data, key=lambda x: x[sort_by], reverse=not ascending)

# Fungsi untuk filter data
def filter_data(data, filter_by, filter_value):
    return [item for item in data if str(item.get(filter_by, '')).upper() == filter_value.upper()]

# Process Sort (Menu Sorting)
def process_sorting(data):
    while True:
        print('\n=== Menu Sorting ===')
        print('1. Batch No.')
        print('2. ID Operator')
        print('3. Machine ID')
        print('4. Tanggal Pengerjaan')
        print('5. Raw Material')
        print('6. Product Type')
        print('7. Product Size')
        print('8. Quality')
        print('0. Menu Data Produksi')

        pilihan_sorting = input('Masukan pilihan sorting anda: ')
        sort_options = {
            '1': 'Batch No.',
            '2': 'ID Operator',
            '3': 'Machine ID',
            '4': 'Tanggal Pengerjaan',
            '5': 'Raw Material',
            '6': 'Product Type',
            '7': 'Product Size',
            '8': 'Quality'
        }

        if pilihan_sorting in sort_options:
            sort_by = sort_options[pilihan_sorting]
            
            while True:
                print('\nSort by:')
                print('1. Ascending')
                print('2. Descending')
                print('0. Menu Data Produksi')

                pilihan_batch_sort = input('Sort by: ')

                if pilihan_batch_sort == '1':
                    ascending = True
                    break  
                elif pilihan_batch_sort == '2':
                    ascending = False
                    break 
                elif pilihan_batch_sort == '0':
                    return 
                else:
                    print('Input tidak valid. Silakan coba lagi.')

            sorted_data = sort_data(data, sort_by, ascending=ascending)
            print('\nData Hasil Produksi setelah Sorting:')
            print(print_formatted_data(sorted_data))

        elif pilihan_sorting == '0':
            break
        else:
            print('Input tidak valid. Masukan input kembali.')

# Process Filter (Menu Filter)
def process_filtering(data):
    while True:
        print('\n=== Menu Filter ===')
        print('1. Batch No.')
        print('2. ID Operator')
        print('3. Machine ID')
        print('4. Tanggal Pengerjaan')
        print('5. Raw Material')
        print('6. Product Type')
        print('7. Product Size')
        print('8. Quality')
        print('0. Kembali ke Menu Data Produksi')

        pilihan_filter = input('Masukan pilihan filter anda: ')
        filter_options = {
            '1': 'Batch No.',
            '2': 'ID Operator',
            '3': 'Machine ID',
            '4': 'Tanggal Pengerjaan',
            '5': 'Raw Material',
            '6': 'Product Type',
            '7': 'Product Size',
            '8': 'Quality'
        }

        if pilihan_filter in filter_options:
            filter_by = filter_options[pilihan_filter]
            filter_value = input(f'Masukan {filter_by} yang ingin difilter: ')

            if filter_by == 'Tanggal Pengerjaan':
                while True:
                    try:
                        datetime.strptime(filter_value, '%d%m%Y')
                        break
                    except ValueError:
                        print('Format tanggal tidak valid. Harap masukkan tanggal dengan format DDMMYYYY.')
                        filter_value = input(f'Masukan {filter_by} yang ingin difilter: ')

            filtered_data = filter_data(data, filter_by, filter_value)
            if filtered_data:
                print('\nData yang sesuai filter:')
                print(print_formatted_data(filtered_data))
            else:
                print(f'Tidak ada data yang sesuai dengan {filter_by} "{filter_value}"')
        elif pilihan_filter == '0':
            break
        else:
            print('Input tidak valid. Masukan input kembali.')

# Fungsi untuk update data
def update_data(data):
    while True:
        batch_no = input('\nMasukkan Batch No. yang ingin diupdate: ').upper()
        
        # Cek apakah batch_no ada dalam data
        item_found = False
        for item in data:
            if item['Batch No.'] == batch_no:
                item_found = True
                item_to_update = item
                break

        if not item_found:
            print(f'Batch No. {batch_no} tidak ditemukan. Silakan masukkan Batch No. yang valid.')
            continue
        
        while True:
            print('\nPilih kolom yang ingin diupdate:')
            print('1. Batch No.')
            print('2. ID Operator')
            print('3. Machine ID')
            print('4. Tanggal Pengerjaan')
            print('5. Raw Material')
            print('6. Product Type')
            print('7. Product Size')
            print('8. Quality')
            
            pilihan_to_update = input('Masukkan field yang ingin diupdate: ')
            
            update_options = {
                '1': 'Batch No.',
                '2': 'ID Operator',
                '3': 'Machine ID',
                '4': 'Tanggal Pengerjaan',
                '5': 'Raw Material',
                '6': 'Product Type',
                '7': 'Product Size',
                '8': 'Quality'
            }
            
            if pilihan_to_update in update_options:
                field = update_options[pilihan_to_update]
                new_input = input(f'Masukkan nilai baru untuk {field}: ').strip()
                
                if field == 'Tanggal Pengerjaan':
                    while True:
                        if len(new_input) != 8:
                            print('Input harus terdiri dari 8 digit (Format: DDMMYYYY).')
                            new_input = input(f'Masukkan tanggal baru untuk {field} (Format: DDMMYYYY): ').strip()
                        else:
                            try:
                                item_to_update[field] = datetime.strptime(new_input, '%d%m%Y').date()
                                break
                            except ValueError:
                                print('Format tanggal salah. Gunakan Format DDMMYYYY.')
                                new_input = input(f'Masukkan tanggal baru untuk {field} (Format: DDMMYYYY): ').strip()
                else:
                    item_to_update[field] = new_input.upper()

                print(f'\nField {field} telah diperbaru dengan nilai: {new_input}')
                return data
            else:
                print('Pilihan tidak valid. Masukkan nomor kolom yang benar.')
        
# Fungsi untuk menambah data baru
def add_data(data):
    print('\nTambah Data Produksi Baru')

    # Cek apakah batch_no sudah ada
    while True:
        batch_no = input('Masukan Batch No.: ').upper()
        duplicate = False
        for entry in data:
            if entry['Batch No.'] == batch_no:
                print(f'Batch No. {batch_no} sudah ada. Masukkan batch baru.')
                duplicate = True
                break
        if not duplicate:
            break

    id_operator = input('Masukan ID Operator: ').upper()
    machine_id = input('Masukan Machine ID: ').upper()

    # Cek format tanggal
    while True:
        tanggal_pengerjaan = input('Masukan Tanggal Pengerjaan (format: DDMMYYYY): ')
        if len(tanggal_pengerjaan) != 8:
            print('Input tidak valid. Harap mengisi dengan 8 digit (Format: DDMMYYYY).')
        else:
            try:
                tanggal_pengerjaan = datetime.strptime(tanggal_pengerjaan, '%d%m%Y')
                break
            except ValueError:
                print('Format tanggal tidak valid. Gunakan (format: DDMMYYYY).')

    raw_material = input('Masukan Raw Material: ').upper()
    product_type = input('Masukan Product Type: ').upper()
    product_size = input('Masukan Product Size: ').upper()

    # Cek input quality
    while True:
        quality = input('Masukan Quality (GOOD/NOT GOOD): ').upper()
        if quality in ['GOOD', 'NOT GOOD']:
            break
        else:
            print('Input tidak valid. Harap masukkan "GOOD" atau "NOT GOOD".')

    # Tambahkan data baru
    new_entry = {
        'Batch No.': batch_no,
        'ID Operator': id_operator,
        'Machine ID': machine_id,
        'Tanggal Pengerjaan': tanggal_pengerjaan,
        'Raw Material': raw_material,
        'Product Type': product_type,
        'Product Size': product_size,
        'Quality': quality
    }

    data.append(new_entry)
    print('\nData berhasil ditambahkan!')
    return data


# Fungsi untuk menghapus data
def delete_data(data, batch_no):
    deleted = False
    for item in data:
        if item['Batch No.'] == batch_no.upper():
            data.remove(item)
            deleted = True
            print(f'\nData dengan Batch No. {batch_no} berhasil dihapus.')
            break
    if not deleted:
        print(f'\nBatch No. {batch_no} tidak ditemukan.')
    return data

# Fungsi login
def login(role):
    users = [
    {'username': 'adm', 'password': 'adm123', 'role': 'admin'},
    {'username': 'op', 'password': 'op123', 'role': 'operator'}
]
    while True:
        username = input('\nMasukkan username: ')
        password = pyip.inputPassword(prompt='Masukkan password: ')
        
        # Periksa apakah username dan password cocok
        user_found = False
        for user in users:
            if user['username'] == username and user['password'] == password:
                user_found = True
                if user['role'] == role:
                    print(f'\nSelamat datang, {username}!')
                    return True
                else:
                    print(f'\nAnda tidak memiliki akses sebagai {role.capitalize()}.')
                    return False
        
        if not user_found:
            print('Username atau password salah.')
        
        # Pilihan untuk mencoba login lagi atau keluar
        choice = input('Apakah Anda ingin mencoba lagi? (Y/N): ').strip().upper()
        if choice != 'Y':
            print('Login dibatalkan.')
            return False

# Menu Login
while True:
    print('\n=== Account Login ===')
    print('1. Administrator')
    print('2. Operator')
    print('0. Exit Program')
    login_akun = input('Masukan pilihan anda:')

    if login_akun == '1':
        if login('admin'):
            # Main Menu
            while True:
                print('\n=== Main Menu ===')
                print('1. Menu Data Produksi')
                print('2. Mengedit hasil produksi')
                print('3. Menambah input produksi')
                print('4. Menghapus data produksi')
                print('0. Logout Account')

                pilihan = input('Masukan pilihan menu anda:')

                if pilihan == '1':
                    # Menu Hasil Produksi
                    while True:
                        print('\n==== Menu Data Produksi ====')
                        print('1. Menampilkan Semua Data Hasil Produksi')
                        print('2. Sort Data Produksi')
                        print('3. Filter Data Produksi')
                        print('0. Main Menu')

                        pilihan_data_produksi = input('Masukan pilihan menu produksi anda:')
                        
                        if pilihan_data_produksi == '1':
                            print('\nData Hasil Produksi')
                            print(print_formatted_data(data))

                        elif pilihan_data_produksi == '2':
                            process_sorting(data)

                        elif pilihan_data_produksi == '3':
                            process_filtering(data)

                        elif pilihan_data_produksi == '0':
                            break
                        else:
                            print('Input tidak valid. Masukan input kembali.')

                elif pilihan == '2':
                    updated_data = update_data(data)
                    print(print_formatted_data(updated_data))

                elif pilihan == '3':
                    data = add_data(data)

                elif pilihan == '4':
                    print(print_formatted_data(data))
                    batch_no = input('\nMasukkan Batch No. yang ingin dihapus: ').upper()
                    data = delete_data(data, batch_no)

                elif pilihan == '0':
                    break
                else:
                    print('Input tidak valid. Masukan input kembali.')
                    continue

    elif login_akun == '2':
        if login('operator'):
            while True:
                print('\n=== Main Menu Operator ===')
                print('1. Menampilkan Data Produksi')
                print('2. Menambah Data Produksi')
                print('0. Logout Account')

                pilihan_operator = input('Masukan pilihan menu anda:')
                
                if pilihan_operator == '1':
                    print('\nData Hasil Produksi')
                    print(print_formatted_data(data))

                elif pilihan_operator == '2':
                    data = add_data(data)

                elif pilihan_operator == '0':
                    break
                else:
                    print('Input tidak valid. Masukan input kembali.')
                    continue

    elif login_akun == '0':
        print('\nKeluar Dari Program. \nSafety First!\n')
        break

    else:
        print('Input tidak valid. Masukan input kembali.')

