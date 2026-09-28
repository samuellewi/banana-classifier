# 🍌 Banana Image Classifier

Aplikasi web berbasis kecerdasan buatan (AI) untuk mengklasifikasikan pisang sebagai **Segar** atau **Busuk** menggunakan webcam secara real-time.

## 📖 Deskripsi

Project ini terdiri dari 2 bagian utama:
1. **Model AI (Machine Learning)**: Otak yang mengenali pisang busuk atau segar
2. **Web App (Flask)**: Aplikasi web untuk menggunakan model tersebut dengan webcam

## 🎯 Cara Kerja (Penjelasan Sederhana)

Bayangkan kamu mengajari anak kecil membedakan pisang segar dan busuk:
1. Tunjukkan 1000+ foto pisang segar dan busuk
2. Anak belajar ciri-cirinya (warna, tekstur, bintik-bintik)
3. Setelah belajar, anak bisa mengenali pisang baru

Komputer juga begitu! Kita latih dengan ribuan foto pisang, lalu dia bisa mengenali pisang baru dari webcam.

## 🚀 Quick Start (Windows)

### Langkah 1: Persiapan

**Install Python:**
1. Download Python dari [python.org](https://www.python.org/downloads/)
2. Install dengan centang "Add Python to PATH"
3. Buka Command Prompt, ketik: `python --version` (harus muncul versi Python)

**Clone atau Download Project:**
```bash
# Jika pakai git:
git clone [url-repo-ini]
cd banana_image_classifier

# Atau download ZIP, lalu extract
```

### Langkah 2: Latih Model AI (5-15 menit)

```bash
# Masuk ke folder model
cd model

# Install dependencies
pip install -r requirements.txt

# Jalankan training
python main.py

# Tunggu sampai selesai (akan muncul "Final Test Accuracy: 97.69%")
# File rotten_banana_mobilenet_224_model.h5 akan dibuat
```

**Apa yang terjadi:**
- Program download dataset pisang dari internet
- Melatih model AI dengan 8 epoch (8x ulang)
- Menghasilkan file model (.h5) yang siap pakai
- Akurasi: 97.69% (sangat bagus!)

### Langkah 3: Jalankan Web App

```bash
# Kembali ke folder utama
cd ..

# Masuk ke folder app
cd app

# Install dependencies
pip install -r requirements.txt

# Jalankan web app
python app.py
```

**Apa yang terjadi:**
- Flask server akan jalan di port 5000
- Buka browser, ketik: `http://localhost:5000`
- Izinkan akses kamera
- Arahkan ke pisang, klik capture
- Lihat hasilnya!

## 📁 Struktur Project

```
banana_image_classifier/
├── model/                          # Folder untuk training AI
│   ├── main.py                     # Script training model
│   ├── README.md                   # Penjelasan detail konsep AI
│   └── rotten_banana_mobilenet_224_model.h5  # Model hasil training (9MB)
│
├── app/                            # Folder aplikasi web
│   ├── app.py                      # Backend Flask
│   ├── requirements.txt            # Dependencies Python
│   ├── templates/
│   │   └── index.html              # Frontend (HTML + JS)
│   └── README.md                   # Penjelasan detail web app
│
├── .gitignore                      # File yang tidak di-commit
└── README.md                       # File ini
```

## 🎓 Penjelasan Komponen

### 1. Model AI (`model/`)

**Apa itu:** Program yang melatih komputer mengenali pisang.

**Teknologi:**
- **TensorFlow**: Library untuk machine learning
- **MobileNetV2**: Model AI ringan yang sudah pintar mengenali gambar
- **Transfer Learning**: Teknik belajar dari model yang sudah pintar
- **Mixed Precision**: Teknik untuk training lebih cepat

**Input:** Gambar pisang 224×224 piksel  
**Output:** File model `.h5` (9MB)  
**Akurasi:** 97.69%

**Baca detail:** [model/README.md](model/README.md)

### 2. Web App (`app/`)

**Apa itu:** Aplikasi web untuk pakai model AI dengan webcam.

**Teknologi:**
- **Flask**: Framework Python untuk web server
- **TensorFlow**: Untuk load dan pakai model AI
- **Vanilla JavaScript**: Kontrol kamera dan UI di browser
- **HTML5 Canvas**: Ambil foto dari video

**Input:** Video dari webcam  
**Output:** Label "Segar" atau "Busuk"

**Baca detail:** [app/README.md](app/README.md)

## 🎯 Fitur Utama

### Model AI
- ✅ Transfer learning dengan MobileNetV2
- ✅ Data augmentation (flip, rotate)
- ✅ Mixed precision training
- ✅ Akurasi 97.69%
- ✅ Model ringan (9MB)

### Web App
- ✅ Real-time classification dengan webcam
- ✅ UI modern dan responsif
- ✅ Loading states yang jelas
- ✅ Error handling
- ✅ Tidak perlu build tools

## 📊 Performa

| Metrik | Nilai |
|--------|-------|
| Akurasi Model | 97.69% |
| Ukuran Model | ~9 MB |
| Waktu Training | 5-15 menit |
| Waktu Prediksi | <1 detik |
| Browser Support | Chrome, Firefox, Edge, Safari |

## 🔧 Requirements

### Hardware Minimum:
- **CPU**: Intel i3 atau setara
- **RAM**: 4GB (8GB recommended)
- **Storage**: 500MB free space
- **Webcam**: Resolusi minimal 640×480
- **Internet**: Untuk download dataset (pertama kali)

### Software:
- **OS**: Windows 10/11
- **Python**: 3.8 atau lebih baru
- **Browser**: Chrome 60+, Firefox 55+, Edge 79+, Safari 11+

## 🛠️ Troubleshooting

### Problem: "Python not found"
**Solusi:**
```bash
# Download dan install Python dari python.org
# Pastikan centang "Add Python to PATH" saat install
```

### Problem: "pip not found"
**Solusi:**
```bash
python -m ensurepip --upgrade
```

### Problem: Training sangat lambat
**Solusi:**
- Tutup aplikasi berat lainnya
- Kurangi BATCH_SIZE di `model/main.py` (dari 32 ke 16)
- Pastikan ada koneksi internet stabil

### Problem: Kamera tidak muncul
**Solusi:**
1. Cek izin browser untuk akses kamera
2. Tutup aplikasi lain yang pakai kamera (Zoom, Teams, dll)
3. Restart browser
4. Coba browser lain

### Problem: Error saat import tensorflow
**Solusi:**
```bash
pip uninstall tensorflow
pip install tensorflow
```

### Problem: Model tidak ditemukan
**Solusi:**
- Pastikan file `rotten_banana_mobilenet_224_model.h5` ada di folder `model/`
- Jika belum ada, jalankan `python main.py` di folder `model/`

## 📚 Belajar Lebih Lanjut

### Untuk Pemula:
1. Baca [model/README.md](model/README.md) - Penjelasan konsep AI dengan bahasa sangat sederhana
2. Baca [app/README.md](app/README.md) - Penjelasan cara kerja web app

### Konsep Yang Dipelajari:
- Machine Learning & Deep Learning
- Transfer Learning (belajar dari model yang sudah pintar)
- Computer Vision (komputer lihat gambar)
- Convolutional Neural Networks (CNN)
- Binary Classification (2 kategori)
- Flask Web Development
- Webcam API di browser
- REST API

## 🎨 Screenshots

### 1. Tampilan Awal
```
╔══════════════════════════════╗
║   🍌 Banana Classifier      ║
║   Point camera and capture  ║
╠══════════════════════════════╣
║                              ║
║     [Video from Webcam]      ║
║                              ║
║      📸 Capture Button       ║
╚══════════════════════════════╝
```

### 2. Hasil Klasifikasi
```
╔══════════════════════════════╗
║         SEGAR! ✅           ║
╚══════════════════════════════╝
```
atau
```
╔══════════════════════════════╗
║         BUSUK! ⚠️           ║
╚══════════════════════════════╝
```

## 🚀 Deployment (Opsional)

Untuk deploy ke internet (bukan localhost):

1. **Heroku** (Free tier):
   - Add `Procfile`: `web: gunicorn app:app`
   - Install: `pip install gunicorn`
   - Push ke Heroku

2. **PythonAnywhere**:
   - Upload files
   - Setup Flask app di dashboard
   - Set webcam permissions

3. **Docker**:
   ```dockerfile
   FROM python:3.9
   COPY . /app
   WORKDIR /app
   RUN pip install -r app/requirements.txt
   CMD ["python", "app/app.py"]
   ```

**Catatan:** Webcam hanya bisa diakses via HTTPS (bukan HTTP) kecuali di localhost.

## 🤝 Contributing

Kontribusi welcome! Silakan:
1. Fork repo ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 License

Project ini untuk tujuan edukasi dan pembelajaran.

## 👥 Credits

- Dataset: [Kaggle - Banana Ripeness Classification](https://www.kaggle.com/datasets/shahriar26s/banana-ripeness-classification-dataset)
- Model Architecture: MobileNetV2 (Google)
- Framework: TensorFlow, Flask

## 📞 Support

Jika ada pertanyaan atau masalah:
1. Baca README di folder `model/` dan `app/`
2. Cek bagian Troubleshooting
3. Buka issue di GitHub (jika repo di GitHub)

---

## 🎓 Summary (TL;DR)

**Untuk yang buru-buru:**

```bash
# 1. Training model (tunggu 5-15 menit)
cd model
pip install tensorflow kagglehub matplotlib
python main.py

# 2. Jalankan web app
cd ..\app
pip install -r requirements.txt
python app.py

# 3. Buka browser: http://localhost:5000
# 4. Arahkan kamera ke pisang, klik capture
# 5. Done! 🎉
```

---

**Happy classifying! 🍌✨**

Made with ❤️ for learning AI and Computer Vision
