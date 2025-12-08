data = []

def autosave():
    try:
        with open("mindcare_log.txt", "w") as f:
            for d in data:
                f.write(str(d) + "\n")
            print("Data berhasil disimpan")
    except:
        print("Gagal menyimpan data.")

def motivasi_mood(mood):
    if mood == "happy":
        return "Senang melihat kamu bahagia! Pertahankan ya 😁"
    elif mood == "sad":
        return "Tidak apa-apa merasa sedih. Kamu kuat, dan ini akan berlalu 🤍"
    elif mood == "anxious":
        return "Tarik napas pelan... kamu aman di sini. You’re doing your best 🌿"
    elif mood == "stress":
        return "Kamu sudah berusaha keras. Istirahat sebentar, kamu tidak sendirian 🤝"
    else:
        return "Hari yang netral juga baik. Jaga dirimu dan tetap positif ✨"

def motivasi_stres(level):
    if 1 <= level <= 3:
        return "Stressmu rendah, bagus! Tetap jaga keseimbangan ya 🌱"
    elif 4 <= level <= 6:
        return "Kamu terlihat sedikit lelah. Coba istirahat sebentar atau minum air hangat ☕"
    elif 7 <= level <= 8:
         return "Stressmu cukup tinggi. Ambil waktu untuk rileks, kamu layak istirahat 🧘"
    elif 9 <= level <= 10:
        return "Stress sangat tinggi! Tolong beri dirimu waktu untuk tenang dan jangan memaksakan diri 🤍"
    else:
        return ""

def tambah():
    print("\n=== Tambah Catatan Mental ===")
   
    while True:
        tgl = input("Tanggal (dd/mm/yyyy: ").strip()
        try:
            if len(tgl) == 10 and tgl[2] == "/" and tgl[5] == "/":
                hari = tgl[:2]
                bulan = tgl[3:5]
                tahun = tgl[6:]
                if hari.isdigit() and bulan.isdigit() and tahun.isdigit():
                    hari = int(hari)
                    bulan = int(bulan)
                    if 1 <= hari <= 31 and 1 <= bulan <= 12:
                        break
            raise ValueError
        except ValueError:
            print("❌ Format tanggal salah! Gunakan format dd/mm/yyyy & hanya angka. Contoh: 08/12/2025")
    mood = input("Mood (happy/sad/anxious/stress/neutral): ").lower().strip()

    try:
        stres = int(input("Tingkat stress (1-10): "))
        if stres < 1 or stres > 10:
            raise ValueError
    except ValueError:
        print("Stres harus angka 1–10!")
        return

    catatan = input("Catatan singkat: ").strip()

    entry = {
        "tgl": tgl,
         "mood": mood,
        "stres": stres,
        "catatan": catatan
    }

    data.append(entry)
    autosave()
    print("\nCatatan berhasil ditambah!")
    print("Pesan untukmu:", motivasi_mood(mood))
    print("Level stres:", motivasi_stres(stres))

def tampil():
    print("\n=== Semua Catatan Mental ===")
    if not data:
        print("Belum ada catatan.")
        return

    for i, d in enumerate(data, 1):
        print(f"\nData {i}")
        print(f"Tanggal : {d['tgl']}")
        print(f"Mood    : {d['mood']}")
        print(f"Stres   : {d['stres']}/10")
        print(f"Catatan : {d['catatan']}")
        print("Pesan Mood :", motivasi_mood(d["mood"]))
        print("Pesan Stres:", motivasi_stres(d["stres"]))

def cari():
    print("\n===Cari Jurnal===")
    q = input("Masukkan tanggal atau mood: ").strip().lower()

    found = False
    for d in data:
        if d["tgl"].lower() == q or d["mood"].lower() == q:
            print("\nDitemukan:")
            print(f"Tanggal : {d['tgl']}")
            print(f"Mood    : {d['mood']}")
            print(f"Stres   : {d['stres']}/10")
            print(f"Catatan : {d['catatan']}")
            found = True

    if not found:
        print("Tidak ada yang cocok.")
        
def edit():
    print("\n=== Edit Catatan ===")
    tgl = input("Masukkan tanggal catatan yang ingin diedit: ").strip()

    for d in data:
        if d["tgl"] == tgl:
            print("Kosongkan input jika tidak ingin mengubah.")

            mood_baru = input("Mood baru: ").lower().strip()
            stres_baru = input("Tingkat stres baru (1-10): ")
            catatan_baru = input("Catatan baru: ")

            if mood_baru != "":
                d["mood"] = mood_baru

            if stres_baru != "":
                try:
                    stres_val = int(stres_baru)
                    if 1 <= stres_val <= 10:
                        d["stres"] = stres_val
                except:
                    print("Input stres tidak valid.")

            if catatan_baru != "":
                d["catatan"] = catatan_baru

            autosave()

            print("\nCatatan berhasil diperbarui!")
            print("Pesan Mood :", motivasi_mood(d["mood"]))
            print("Pesan Stres:", motivasi_stres(d["stres"]))
            return

    print("Tanggal tidak ditemukan.")

def hapus():
    print("\n=== Hapus Catatan ===")
    tgl = input("Masukkan tanggal: ").strip()
    for d in data:
        if d["tgl"] == tgl:
            data.remove(d)
            autosave()
            print("Catatan berhasil dihapus!")
            return

    print("Tanggal tidak ditemukan.")

def menu():
    while True:
        print("\n========= MINDCARE JOURNAL =========")
        print("1. Tambah Catatan")
        print("2. Lihat Semua Catatan")
        print("3. Cari Catatan")
        print("4. Edit Catatan")
        print("5. Hapus Catatan")
        print("6. Keluar")

        
        pilih = input("Pilih menu: ").strip()

        
        if pilih == "1":
            tambah()
        elif pilih == "2":
            tampil()
        elif pilih == "3":
            cari()
        elif pilih == "4":
            edit()
        elif pilih == "5":
            hapus()
        elif pilih == "6":
            print("Terima kasih! Jaga kesehatan mental ya 🤍")
            break
        else:
            print("Pilihan tidak valid.")

menu()

