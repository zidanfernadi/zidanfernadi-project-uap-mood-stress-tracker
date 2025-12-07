data = []

def autosave():
    try:
        with open("mindcare_log.txt", "w") as f:
            for d in data:
                f.write(str(d) + "\n")
            print("Data berhasil disimpan")")
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
