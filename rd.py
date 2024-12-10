undo_stack = ["menjalankan office word", "membuka google chrome", "menjalankan visual studio code"]
redo_stack = []

def aksi(item):
    undo_stack.append(item)
    redo_stack.clear()
    print ("tambahkan aksi =>", item)
    print("aksi setelah ditambahkan:", undo_stack)

def undo():
    if undo_stack:
        item = undo_stack.pop()
        redo_stack.append(item)
        print ("Undo =>", item)
        print("aksi setelah di-Undo Stack:", undo_stack)
    else:
        print ("Tidak ada tindakan yang bisa dilakukan!")


def redo():
    if redo_stack:
        item = redo_stack.pop()
        undo_stack.append(item)
        print ("Redo =>", item)
        print("aksi setelah di-redo Stack:", undo_stack)
    else:
        print ("Tidak ada tindakan yang bisa dilakukan!")

def hasil_stack():
    print ("Undo Stack =>", undo_stack)
    print ("Redo Stack =>", redo_stack)  

while True:
    print ()
    print ("pilih opsii :")
    print ("1. Tambahkan aksi")
    print ("2. Tindakan Undo")
    print ("3. Tindakan Redo")
    print ("4. lihat stack undo dan redo")
    print ("5. Keluar")
    
    pilihan = input("Pilih Tindakan : ")
    if pilihan == '1':
        item = input ("Masukan item uji coba => ")
        aksi (item)
    elif pilihan == '2' :
        undo ()
    elif pilihan == '3' :
        redo ()
    elif pilihan == '4' :
        hasil_stack()
    elif pilihan == '5' :
        print ("Keluar dari program")
        break
    else :
        print ("Pilihan tidak ada dalam daftar!")
