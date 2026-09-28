# Aplikasi Web Klasifikasi Pisang

Web app modern yang menggunakan kecerdasan buatan untuk mengklasifikasikan pisang sebagai "Segar" atau "Busuk" secara real-time menggunakan webcam kamu.

## 🌟 Fitur

- **Klasifikasi Real-time**: Arahkan kamera ke pisang dan dapatkan hasil instan
- **UI Modern**: Desain bersih dan responsif untuk desktop dan mobile
- **Integrasi Webcam**: Akses kamera langsung melalui browser
- **Error Handling**: Penanganan yang baik untuk izin kamera dan masalah jaringan
- **Ringan**: Dibangun dengan vanilla JavaScript untuk performa optimal

## 🚀 Cara Menjalankan (Windows)

### Prasyarat

- Windows 10/11
- Python 3.8+
- Webcam (built-in atau eksternal)
- Model yang sudah dilatih (lihat di bawah)

### Instalasi

1. **Buka Command Prompt atau PowerShell**
   - Tekan `Win + R`
   - Ketik `cmd` atau `powershell`
   - Enter

2. **Masuk ke folder app**
   ```bash
   cd path\ke\banana_image_classifier\app
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Pastikan model sudah ada**
   
   File model harus ada di: `../model/rotten_banana_mobilenet_224_model.h5`
   
   Jika belum ada, latih modelnya dulu:
   ```bash
   cd ..\model
   python main.py
   cd ..\app
   ```

5. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

6. **Buka browser**
   - Buka Chrome, Firefox, atau Edge
   - Ketik di address bar: `http://localhost:5000`
   - Izinkan akses kamera ketika diminta
   - Arahkan kamera ke pisang
   - Klik tombol "📸 Capture"
   - Lihat hasilnya!

## 📋 Requirements

```
Flask>=2.0.0
tensorflow>=2.0.0
Pillow>=8.0.0
numpy>=1.19.0
```

## 🏗️ Arsitektur (Cara Kerja)

### Backend (Flask - Python)

**Penjelasan Sederhana:** Ini adalah "otak" di belakang layar yang menerima foto dan memberitahu apakah pisang busuk atau segar.

**Komponen:**
- **Model Loading**: Muat model AI saat aplikasi start
- **Image Processing**: Proses gambar (resize ke 224×224, konversi RGB)
- **Prediction API**: Endpoint `/predict` untuk terima foto dan kasih jawaban
- **Error Handling**: Tangani error jika ada masalah

**Cara Kerja:**
1. User upload foto dari browser
2. Flask terima foto
3. Resize foto ke 224×224 piksel
4. Masukkan ke model AI
5. Model kasih jawaban: 0-1 (di atas 0.5 = busuk, di bawah = segar)
6. Flask kirim jawaban balik ke browser

### Frontend (Vanilla JavaScript)

**Penjelasan Sederhana:** Ini adalah tampilan yang kamu lihat di browser, mengontrol kamera dan menampilkan hasil.

**Komponen:**
- **Camera Access**: Akses webcam menggunakan `navigator.mediaDevices.getUserMedia()`
- **Real-time Video**: Tampilkan video langsung dari kamera
- **Image Capture**: Ambil foto dari video menggunakan canvas
- **State Management**: Atur kondisi UI (loading, ready, processing, hasil)
- **Responsive Design**: Tampilan menyesuaikan ukuran layar

**Cara Kerja:**
1. Minta izin akses kamera
2. Tampilkan video stream
3. User klik tombol capture
4. Ambil frame dari video, simpan ke canvas
5. Convert canvas ke file gambar (JPEG)
6. Kirim ke server (backend)
7. Terima hasil
8. Tampilkan "Segar" atau "Busuk"

## 🔧 Detail Teknis

### Spesifikasi Model
- **Input**: Gambar 224×224 RGB
- **Arsitektur**: MobileNetV2 dengan transfer learning
- **Output**: Klasifikasi binary (Segar/Busuk)
- **Preprocessing**: Rescaling built-in (tidak perlu normalisasi manual)

### API Endpoints

#### `GET /`
Menampilkan halaman web utama.

#### `POST /predict`
Menerima gambar dan mengembalikan hasil klasifikasi.

**Request:**
- Content-Type: `multipart/form-data`
- Body: field `image` berisi data gambar JPEG/PNG

**Response:**
```json
{
  "result": "Segar",
  "confidence": 0.92,
  "is_rotten": false
}
```

**Penjelasan Response:**
- `result`: "Segar" atau "Busuk"
- `confidence`: Angka 0-1 (tingkat keyakinan model)
- `is_rotten`: `true` jika busuk, `false` jika segar

### Kompatibilitas Browser
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 11+
- ✅ Edge 79+

**Catatan:** Akses kamera memerlukan HTTPS (kecuali di localhost).

## 🎨 Status UI (Tampilan)

1. **Camera Loading**: Spinner saat inisialisasi webcam
2. **Ready to Capture**: Video stream aktif dengan tombol capture
3. **Processing**: Spinner saat analisis gambar
4. **Results**: Hasil klasifikasi ditampilkan
5. **Error**: Pesan error yang ramah pengguna

## 🛠️ Struktur Project

```
app/
├── app.py              # Aplikasi Flask (backend)
├── requirements.txt    # Dependencies Python
├── templates/
│   └── index.html      # Frontend (HTML + CSS + JavaScript)
└── README.md          # File ini
```

## 🎓 Penjelasan Kode Penting

### File: `app.py`

```python
# Muat model saat aplikasi start
model = tf.keras.models.load_model(MODEL_PATH)
```
**Penjelasan:** Baca file model .h5 dan siapkan untuk prediksi.

```python
# Resize gambar ke 224×224
img = img.resize((224, 224))
```
**Penjelasan:** Model dilatih dengan gambar 224×224, jadi input harus sama.

```python
# Prediksi
prediction = model.predict(img_array)
confidence = float(prediction[0][0])
is_rotten = confidence > 0.5
```
**Penjelasan:** 
- Model kasih angka 0-1
- Di atas 0.5 = busuk
- Di bawah 0.5 = segar

### File: `index.html` (JavaScript)

```javascript
// Akses kamera
const stream = await navigator.mediaDevices.getUserMedia({
    video: { width: 640, height: 480 }
});
```
**Penjelasan:** Minta browser akses kamera dengan resolusi 640×480.

```javascript
// Ambil foto dari video
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
```
**Penjelasan:** Gambar frame saat ini dari video ke canvas (seperti screenshot).

```javascript
// Kirim ke server
const formData = new FormData();
formData.append('image', blob, 'capture.jpg');
const response = await fetch('/predict', {
    method: 'POST',
    body: formData
});
```
**Penjelasan:** Bungkus gambar dalam FormData dan kirim ke endpoint `/predict`.

## 🔒 Keamanan

- ✅ Akses kamera memerlukan izin user
- ✅ Gambar diproses lokal di server (tidak disimpan)
- ✅ Tidak ada penyimpanan data
- ⚠️ Untuk production, gunakan HTTPS

## 💡 Tips Penggunaan

1. **Pencahayaan:** Pastikan pencahayaan cukup
2. **Jarak:** Posisikan pisang mengisi 50-80% frame
3. **Fokus:** Tunggu kamera fokus sebelum capture
4. **Background:** Background polos lebih baik
5. **Sudut:** Foto dari berbagai sudut untuk hasil terbaik

## 🐛 Troubleshooting

### Kamera tidak muncul
1. Cek izin browser untuk akses kamera
2. Pastikan kamera tidak dipakai aplikasi lain
3. Refresh halaman (F5)
4. Coba browser lain

### Error "Model not loaded"
1. Pastikan file model ada di `../model/rotten_banana_mobilenet_224_model.h5`
2. Latih model dulu jika belum ada

### Prediksi tidak akurat
1. Pastikan pencahayaan cukup
2. Pisang harus terlihat jelas
3. Jangan terlalu jauh atau dekat
4. Coba dari sudut berbeda

### Port sudah digunakan
```bash
# Ubah port di app.py baris terakhir:
app.run(debug=True, port=5001)  # Ganti 5000 ke 5001
```

## 🚀 Mode Development vs Production

### Development (Saat ini)
```python
app.run(debug=True)  # Auto-reload, error messages detail
```

### Production (Deployment)
```python
# Gunakan WSGI server seperti Gunicorn
# Jangan gunakan debug=True
# Aktifkan HTTPS
```

---

## 📱 Fitur Masa Depan (Ide)

- [ ] Upload foto dari galeri (tidak hanya webcam)
- [ ] Riwayat klasifikasi
- [ ] Batch processing (banyak gambar sekaligus)
- [ ] Export hasil ke CSV
- [ ] Multi-language support
- [ ] Dark mode

---

**Selamat mengklasifikasi pisang! 🍌✨**
