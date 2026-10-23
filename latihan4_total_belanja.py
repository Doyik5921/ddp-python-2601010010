

nama_barang = "buku"
harga_barang = 25000
jumlah_barang = 3

subtotal = harga_barang * jumlah_barang
ppn = subtotal * 11 / 100
total = subtotal + ppn

print(f"Subtotal {subtotal}, PPN {ppn}, Total {total}")