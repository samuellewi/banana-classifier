# README Model Klasifikasi Pisang

## 📚 Penjelasan Konsep (Bahasa Sederhana)

### Apa yang Dilakukan Program Ini?

Program ini **melatih komputer untuk mengenali pisang busuk atau segar** dari foto. Seperti mengajari anak kecil membedakan apel merah dan hijau, kita ajari komputer membedakan pisang busuk dan segar dengan menunjukkan banyak foto contoh.

---

## 🧠 Konsep-Konsep Penting (Dijelaskan Sangat Sederhana)

### 1. **Transfer Learning (Belajar dari yang Sudah Pintar)**
**Analogi:** Seperti kamu tidak perlu belajar dari nol untuk mengenali jenis mobil baru. Karena kamu sudah tahu apa itu roda, kaca, pintu, kamu tinggal belajar ciri khas mobil itu saja.

**Di Program:** Kita pakai MobileNetV2 yang sudah dilatih dengan jutaan gambar. Dia sudah pintar mengenali garis, bentuk, warna, dan pola. Kita tinggal ajari dia mengenali ciri khas pisang busuk vs segar.

### 2. **MobileNetV2 (Otak Pintar yang Ringan)**
**Apa itu:** Model kecerdasan buatan yang sudah dilatih oleh Google dengan jutaan gambar.

**Kenapa Pakai Ini:**
- Sudah pintar mengenali bentuk dan pola
- Ringan (tidak berat untuk komputer)
- Cepat belajar hal baru
- Cocok untuk perangkat dengan resource terbatas

### 3. **Mixed Precision Training (Latihan Cepat dengan Angka Campuran)**
**Analogi:** Seperti matematika. Kadang kamu pakai angka bulat (1, 2, 3), kadang pakai desimal (1.5, 2.7). Angka bulat lebih cepat dihitung.

**Di Program:** Kita pakai campuran angka presisi tinggi (float32) dan rendah (float16) agar latihan lebih cepat, terutama di komputer dengan GPU modern atau Apple Silicon.

### 4. **Image Size 224×224 (Ukuran Gambar)**
**Kenapa 224×224:**
- Ukuran standar yang MobileNetV2 sudah biasa pakai
- Lebih kecil = lebih cepat diproses
- Masih cukup detail untuk mengenali pisang

**Analogi:** Seperti thumbnail foto. Tidak perlu foto full HD untuk tahu itu foto siapa.

### 5. **Data Augmentation (Bikin Variasi Gambar)**
**Apa itu:** Kita "putar-putar" dan "balik-balik" gambar pisang saat latihan.

**Kenapa:** Agar model tidak kaget kalau pisangnya miring, terbalik, atau dari sudut berbeda.

**Teknik yang dipakai:**
- `RandomFlip`: Balik gambar horizontal/vertical (seperti cermin)
- `RandomRotation`: Putar gambar sampai 20% (72 derajat)

### 6. **Batch Size 32 (Belajar 32 Gambar Sekaligus)**
**Analogi:** Seperti belajar dengan flashcard. Daripada lihat 1 kartu lalu mikir lama, lebih baik lihat 32 kartu dulu, baru mikir sekaligus.

**Kenapa 32:** Balance yang bagus antara kecepatan dan keakuratan untuk komputer biasa.

### 7. **Epochs 8 (Ulang 8 Kali)**
**Apa itu:** Berapa kali komputer "membaca ulang" semua gambar untuk belajar.

**Analogi:** Seperti baca buku pelajaran 8 kali sampai hafal. Kalau cuma baca 1 kali, belum paham betul.

### 8. **Binary Classification (Pilihan 2: Busuk atau Segar)**
**Apa itu:** Komputer cuma jawab 2 kemungkinan:
- 0 = Segar 🍌
- 1 = Busuk 🍌💀

**Kenapa Binary:** Masalah kita sederhana, cuma 2 kategori. Tidak perlu rumit-rumit.

### 9. **Sigmoid Activation (Fungsi Jawaban 0-1)**
**Apa itu:** Fungsi matematika yang mengubah angka apapun menjadi nilai antara 0 dan 1.

**Analogi:** Seperti nilai ujian dalam persen (0%-100%). Lebih dari 50% = lulus (busuk), kurang dari 50% = tidak lulus (segar).

### 10. **Frozen Base Model (Kunci Otak Dasar)**
**Apa itu:** Kita "kunci" bagian MobileNetV2 yang sudah pintar mengenali bentuk dan pola umum.

**Kenapa:** Supaya tidak lupa pelajaran dasarnya. Kita cuma latih bagian atas yang spesifik untuk pisang.

---

## 🏗️ Arsitektur Model (Susun Lapisan)

```
Input (Gambar 224×224) 
    ↓
Data Augmentation (Putar & Balik)
    ↓
Rescaling (Ubah 0-255 jadi 0-1)
    ↓
MobileNetV2 Base (Otak Pintar - Dikunci)
    ↓
GlobalAveragePooling (Ringkas Info)
    ↓
Dense 128 (Pikir Lebih Dalam)
    ↓
Dropout 0.5 (Buang 50% - Cegah Hafalan)
    ↓
Dense 1 + Sigmoid (Jawaban: 0-1)
```

### Penjelasan Tiap Lapisan:

1. **Input:** Terima gambar 224×224 piksel
2. **Data Augmentation:** Variasi gambar (flip, rotate)
3. **Rescaling:** Ubah nilai warna dari 0-255 menjadi 0-1 (standarisasi)
4. **MobileNetV2:** Ekstrak fitur penting (garis, bentuk, tekstur)
5. **GlobalAveragePooling:** Ringkas semua info jadi 1 vektor
6. **Dense 128:** Layer pemikiran dengan 128 neuron
7. **Dropout 0.5:** Matikan 50% neuron random saat latihan (cegah overfitting)
8. **Dense 1 + Sigmoid:** Satu neuron output dengan fungsi sigmoid (0=segar, 1=busuk)

---

## 📊 Cara Kerja Training

### Langkah 1: Download Dataset
```python
path = kagglehub.dataset_download("shahriar26s/banana-ripeness-classification-dataset")
```
**Apa yang terjadi:** Unduh ribuan foto pisang dari Kaggle.

### Langkah 2: Bagi Data
- **Train (80%):** Data untuk belajar
- **Valid (10%):** Data untuk cek selama belajar
- **Test (10%):** Data untuk ujian akhir

**Analogi:** Seperti belajar ujian. 80% soal untuk latihan, 10% untuk try-out, 10% untuk ujian asli.

### Langkah 3: Label Data
```python
# 1.0 jika folder 'rotten', 0.0 untuk yang lain
is_rotten = tf.equal(labels, rotten_idx)
```
**Apa yang terjadi:** Tandai semua foto di folder "rotten" dengan label 1, sisanya 0.

### Langkah 4: Optimasi Data
```python
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
```
**Penjelasan:**
- `cache()`: Simpan di memory agar tidak load ulang dari disk
- `shuffle()`: Acak urutan (agar tidak belajar berurutan)
- `prefetch()`: Siapkan data berikutnya selagi model masih proses yang sekarang

### Langkah 5: Compile Model
```python
model.compile(
    optimizer='adam',      # Algoritma belajar (cerdas & adaptif)
    loss='binary_crossentropy',  # Fungsi hitung kesalahan
    metrics=['accuracy']   # Ukur akurasi (berapa persen benar)
)
```

### Langkah 6: Training
```python
model.fit(train_ds, validation_data=val_ds, epochs=8)
```
**Apa yang terjadi:** Model belajar 8 kali putaran penuh melihat semua gambar.

### Langkah 7: Evaluasi
```python
test_loss, test_acc = model.evaluate(test_ds)
```
**Apa yang terjadi:** Uji model dengan data yang belum pernah dilihat. Hasil: **97.69% akurat!**

### Langkah 8: Simpan Model
```python
model.save('rotten_banana_mobilenet_224_model.h5')
```
**Apa yang terjadi:** Simpan "otak" yang sudah pintar ke file .h5

---

## 🚀 Cara Menjalankan (Windows)

### Prasyarat
- Windows 10/11
- Python 3.8 atau lebih baru
- Koneksi internet (untuk download dataset)

### Langkah-langkah:

1. **Buka Command Prompt atau PowerShell**
   - Tekan `Win + R`
   - Ketik `cmd` atau `powershell`
   - Enter

2. **Masuk ke folder model**
   ```bash
   cd path\ke\banana_image_classifier\model
   ```

3. **Install dependencies (jika belum)**
   ```bash
   pip install tensorflow kagglehub matplotlib
   ```

4. **Jalankan training**
   ```bash
   python main.py
   ```

5. **Tunggu proses selesai**
   - Training akan memakan waktu 5-15 menit tergantung spesifikasi PC
   - GPU akan mempercepat proses

6. **Hasil**
   - File `rotten_banana_mobilenet_224_model.h5` akan dibuat
   - Model siap digunakan untuk aplikasi web

---

## 📈 Hasil yang Diharapkan

- **Akurasi Training:** ~97-98%
- **Akurasi Validasi:** ~96-97%
- **Akurasi Test:** ~97-98%
- **Ukuran Model:** ~9-10 MB
- **Waktu Training:** 5-15 menit (tergantung hardware)

---

## 🎯 Keunggulan Pendekatan Ini

1. ✅ **Cepat:** Transfer learning membuat training 10x lebih cepat
2. ✅ **Akurat:** 97.69% akurasi sangat bagus
3. ✅ **Ringan:** Model hanya ~9MB, cocok untuk web
4. ✅ **Efisien:** Mixed precision mengoptimalkan resource
5. ✅ **Stabil:** Data augmentation mencegah overfitting

---

## 🔧 Troubleshooting

### Error: "Module not found"
```bash
pip install tensorflow kagglehub matplotlib
```

### Error: "Out of memory"
- Turunkan BATCH_SIZE dari 32 ke 16 atau 8
- Tutup aplikasi lain yang berat

### Training sangat lambat
- Pastikan TensorFlow terinstall dengan GPU support
- Check: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

---

**Selamat mencoba! 🍌🎓**
