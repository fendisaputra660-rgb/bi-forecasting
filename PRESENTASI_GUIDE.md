# 📊 PANDUAN PRESENTASI - BI FORECASTING DASHBOARD

## 🎯 RINGKAS UNTUK PEMBACA

Anda akan menampilkan **Dashboard BI Forecasting** yang terintegrasi dengan **Jupyter Notebook dataset** dan menampilkan **9 interactive Bokeh charts** dengan login authentication.

---

## ⚡ QUICK START (5 Menit)

### **LANGKAH 1: Buka Terminal PowerShell**
```powershell
cd C:\Users\fendi\Documents\UTS_BI\TA\bi_forecasting
```

### **LANGKAH 2: Aktivasi Virtual Environment**
```powershell
.\.venv\Scripts\Activate.ps1
```
✅ Anda seharusnya melihat `(.venv)` di terminal

### **LANGKAH 3: Jalankan Flask App**
```powershell
python bi_app/run.py
```

**OUTPUT YANG DIHARAPKAN:**
```
 * Running on http://127.0.0.1:5000
 * DEBUG mode: ON
```

### **LANGKAH 4: Buka Browser**
```
http://127.0.0.1:5000
```

---

## 🔐 LOGIN CREDENTIALS

| Field | Value |
|-------|-------|
| **Username** | `admin` |
| **Password** | `admin123` |

---

## 📖 ALUR PRESENTASI STEP-BY-STEP

### **SLIDE 1: Introduction (1 menit)**
> "Ini adalah BI Dashboard yang terintegrasi dengan Jupyter notebook dataset. Dashboard ini menampilkan 9 interactive charts untuk business analytics dan forecasting."

**Yang ditampilkan:**
- Buka halaman login

### **SLIDE 2: Login & Authentication (1 menit)**
> "Dashboard dilindungi dengan authentication system. User hanya bisa akses jika sudah login dengan username dan password yang benar."

**Demo:**
1. Input `admin` di username field
2. Input `admin123` di password field
3. Klik tombol "Sign In"

**Keunggulan:**
- ✅ Secure password hashing
- ✅ Session management
- ✅ Role-based access control

### **SLIDE 3: Dashboard Overview (2 menit)**
Setelah login, user akan masuk ke dashboard yang menampilkan 4 cards dengan metrics:

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ 762         │ 2 Years     │ 13          │ 9           │
│ Total       │ Date        │ Features    │ Charts      │
│ Records     │ Range       │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

**Penjelasan:**
- **762 Records** = Dataset dari Jupyter notebook (762 hari)
- **2 Years** = Data range 2022-2023
- **13 Features** = 13 variabel data yang dianalisis
- **9 Charts** = 9 visualisasi interaktif Bokeh

### **SLIDE 4: Chart 1 - Units Sold Over Time (1 menit)**
> "Chart pertama menunjukkan trend penjualan per hari selama 2 tahun. Ini adalah KPI (Key Performance Indicator) utama bisnis."

**Interactive Features:**
- Hover mouse → lihat nilai exact di tooltip
- Scroll wheel → zoom in/out
- Klik & drag → pan (geser chart)
- Icon 🔄 → reset ke view original
- Icon 💾 → download sebagai PNG

**Demo Action:**
1. Hover ke beberapa titik data → lihat tooltip muncul
2. Scroll untuk zoom in (lihat detail periode tertentu)
3. Drag untuk pan ke bulan lain
4. Klik reset untuk kembali

### **SLIDE 5: Chart 2-4 - Time Series Trends (1 menit)**
Scroll down untuk melihat 3 chart time series lainnya:

1. **Price Trend Over Time** (Chart 2)
   - Menunjukkan evolusi harga produk per hari
   - Warna merah (#e74c3c)

2. **Inventory Level Tracking** (Chart 3)
   - Menunjukkan jumlah stok barang di gudang
   - Warna hijau (#2ecc71)

3. **Demand Analysis** (Chart 4)
   - Menunjukkan pola permintaan pasar
   - Warna orange (#f39c12)

**Insight:**
> "Ketiga chart ini menunjukkan trend sepanjang waktu. Kita bisa lihat seasonality, peaks, dan valleys yang terjadi dalam bisnis."

### **SLIDE 6: Chart 5-8 - Correlation Analysis (2 menit)**
Lanjut scroll untuk melihat 4 scatter plots yang menunjukkan **hubungan antar variabel**:

#### **Chart 5: Price vs Units Sold (Warna Ungu)**
> "Scatter plot ini menunjukkan hubungan antara harga dan jumlah penjualan. Semakin rendah harga, semakin banyak units terjual (negative correlation)."

**Demo:**
- Hover ke beberapa titik → lihat kombinasi Price dan Units
- Semakin jauh ke kanan = harga lebih tinggi
- Semakin jauh ke atas = units terjual lebih banyak

#### **Chart 6: Inventory vs Units Ordered (Warna Cyan)**
> "Hubungan antara stok yang ada dengan jumlah pemesanan. Saat stok rendah, pemesanan lebih banyak."

#### **Chart 7: Discount vs Units Sold (Warna Orange)**
> "Discount memiliki pengaruh positif terhadap penjualan. Semakin besar discount, semakin banyak units terjual."

#### **Chart 8: Promotion vs Units Sold (Warna Merah Tua)**
> "Promosi juga berdampak positif terhadap penjualan. Campaign marketing yang efektif meningkatkan volume penjualan."

### **SLIDE 7: Chart 9 - LSTM Forecast Model (2 menit)**
> "Chart terakhir menampilkan hasil dari machine learning model (LSTM - Long Short-Term Memory) yang kami train pada Jupyter notebook."

**Penjelasan:**
- **Garis Biru** = Actual Units Sold (nilai sebenarnya dari data historis)
- **Garis Orange Putus-putus** = Predicted Units Sold (prediksi dari model LSTM)
- **Kedekatannya** = Akurasi model (semakin dekat = semakin akurat)

**Demo:**
- Hover ke overlap area → lihat actual vs predicted
- Zoom ke periode tertentu untuk lihat performa model lebih detail
- Explain: Model ini bisa digunakan untuk forecast demand bulan depan

---

## 💡 KEY TALKING POINTS

### **Architecture:**
```
Frontend: Bootstrap 5 + Bokeh 3.8.1
Backend:  Flask 3.1.1 dengan Blueprint pattern
Database: SQLite (user authentication)
Data:     CSV (762 rows × 14 features)
ML:       LSTM model untuk forecasting
```

### **Tech Stack:**
- **Backend:** Flask, Flask-Login, SQLAlchemy
- **Frontend:** Bootstrap 5, Font Awesome, Bokeh
- **Data Processing:** Pandas, NumPy
- **ML:** TensorFlow/Keras (LSTM model)

### **Features Unggulan:**
✅ **Secure Authentication** - Login dengan hashing password
✅ **Interactive Charts** - 9 Bokeh visualizations
✅ **Real Data Integration** - Dari Jupyter notebook dataset
✅ **Responsive Design** - Works di desktop/tablet
✅ **ML Integration** - LSTM forecast model
✅ **Professional UI** - AdminLTE-inspired styling
✅ **Hover Tooltips** - Detail values on hover
✅ **Export Charts** - Download as PNG

---

## 🔍 TECHNICAL DETAILS (Untuk Pembaca Teknis)

### **Data Source:**
```
data/processed/
├── daily_features.csv (762 rows, 14 columns)
│   ├── Date
│   ├── Units Sold (KPI utama)
│   ├── Price
│   ├── Inventory Level
│   ├── Units Ordered
│   ├── Discount
│   ├── Promotion
│   ├── Competitor Pricing
│   ├── Epidemic
│   ├── Demand
│   ├── Category
│   ├── Region
│   ├── Weather Condition
│   └── Seasonality
│
└── lstm_forecast_results.csv (154 rows, 3 columns)
    ├── Date
    ├── Actual Units Sold
    └── Predicted Units Sold
```

### **Flask Routes:**
```python
GET  /login              # Login page
POST /login              # Login submission
GET  /logout             # Logout
GET  /charts/dashboard   # Main dashboard dengan 9 charts
GET  /charts/analytics   # Analytics page (optional)
```

### **Chart Generation:**
```python
def get_bokeh_plots():
    # Load CSV files
    df = pd.read_csv('data/processed/daily_features.csv')
    df_forecast = pd.read_csv('data/processed/lstm_forecast_results.csv')
    
    # Generate 9 plots
    plots = [
        plot1_units_sold(),
        plot2_price_trend(),
        plot3_inventory(),
        plot4_demand(),
        plot5_price_vs_units(),
        plot6_inventory_vs_ordered(),
        plot7_discount_impact(),
        plot8_promotion_impact(),
        plot9_lstm_forecast()
    ]
    
    # Embed ke HTML
    script, divs = components(plots)
    return script, divs
```

---

## ⚠️ TROUBLESHOOTING

### **Error 1: "ModuleNotFoundError: No module named 'bokeh'"**
```powershell
pip install -r bi_app/requirements.txt
```

### **Error 2: "Address already in use 0.0.0.0:5000"**
```powershell
# Kill existing process
Get-Process python | Stop-Process -Force
```

### **Error 3: "CSV files not found"**
✅ Pastikan file ada di: `data/processed/daily_features.csv`
✅ Dan: `data/processed/lstm_forecast_results.csv`

### **Error 4: Dashboard blank / charts tidak muncul**
- Refresh page (Ctrl + F5)
- Clear browser cache
- Buka Chrome DevTools (F12) untuk lihat error di console

---

## 📝 CHECKLIST SEBELUM PRESENTASI

- [ ] Aktivasi `.venv`
- [ ] Jalankan `python bi_app/run.py`
- [ ] Cek port 5000 accessible: `http://127.0.0.1:5000`
- [ ] Test login dengan `admin` / `admin123`
- [ ] Semua 9 charts muncul di dashboard
- [ ] Test interactive features (hover, zoom, pan)
- [ ] Jika offline: download screenshots atau cache browser
- [ ] Siapkan PowerPoint/slides di samping browser
- [ ] Test microphone jika online
- [ ] Matikan notifications agar tidak mengganggu demo

---

## 🎬 DURASI PRESENTASI

| Bagian | Durasi |
|--------|--------|
| Intro & Login | 2 menit |
| Overview & Metrics | 1 menit |
| Time Series Charts (1-4) | 3 menit |
| Correlation Charts (5-8) | 3 menit |
| LSTM Forecast Chart (9) | 2 menit |
| Q&A | 4 menit |
| **TOTAL** | **~15 menit** |

---

## 🎤 SCRIPT PRESENTASI

**Opening:**
> "Assalamualaikum, nama saya [nama]. Hari ini saya akan menunjukkan BI Forecasting Dashboard yang merupakan aplikasi web terintegrasi dengan Jupyter notebook untuk business analytics dan forecasting. Dashboard ini menampilkan 9 interactive visualizations dari dataset real yang sudah kami proses dan clean."

**Demo Start:**
> "Mari kita lihat langsung aplikasinya. Pertama, dashboard dilindungi dengan login system untuk security. Saya akan login dengan username admin dan password admin123."

**After Login:**
> "Setelah login, kita masuk ke dashboard yang menampilkan 4 metrics utama: 762 records dari 2 tahun, dengan 13 features yang kami analisis menjadi 9 interactive charts."

**Time Series Section:**
> "Mari kita lihat 4 chart pertama yang menunjukkan time series trends. Chart pertama adalah Units Sold - Key Performance Indicator utama kami. Anda bisa lihat trend penjualan naik turun sepanjang tahun. Kalau saya hover, bisa melihat nilai exact tanggal tersebut."

**Correlation Section:**
> "Selanjutnya adalah 4 scatter plots yang menunjukkan hubungan antar variabel. Misalnya di chart ini, price vs units sold. Terlihat ada negative correlation - saat harga turun, penjualan naik. Ini sesuai dengan economic law of demand."

**ML Section:**
> "Chart terakhir adalah hasil dari LSTM machine learning model yang kami train. Garis biru adalah actual data, garis orange adalah prediksi model. Semakin dekat keduanya, semakin akurat model. Model ini bisa kami gunakan untuk forecast demand bulan depan."

**Closing:**
> "Jadi singkatnya, dashboard ini mengintegrasikan data processing, data visualization, dan machine learning dalam satu aplikasi web yang user-friendly. Terima kasih, siap untuk pertanyaan."

---

## 📱 TIPS PRESENTASI

✅ **Persiapan Teknis:**
- Jangan lupa activate virtual environment
- Start Flask app minimal 2 menit sebelum presentasi dimulai
- Test semua charts muncul dengan baik
- Siapkan laptop backup kalau yang utama error

✅ **During Presentation:**
- Speak slowly dan clearly
- Jangan terburu-buru klik-klik
- Beri waktu audience untuk pahami chart
- Hover tooltips sebagai visual aid
- Explain insights dari setiap chart

✅ **After Presentation:**
- Siap jawab technical questions
- Siap tunjukkan code kalau ditanya architecture
- Siap jelaskan data source dan methodology

---

## 🚀 BONUS: LIVE CODE DEMO (Optional)

Jika penonton penasaran dengan kode:

**Show the structure:**
```powershell
tree bi_app\apps\charts
```

**Show the route:**
```powershell
# Open apps/charts/routes.py
code bi_app\apps\charts\routes.py
```

**Show the data:**
```powershell
# Show first few rows
python -c "import pandas as pd; df = pd.read_csv('data/processed/daily_features.csv'); print(df.head(10))"
```

**Show the template:**
```powershell
# Open HTML template
code bi_app\templates\charts\index.html
```

---

## 📞 CONTACT / FOLLOW-UP

Jika ada yang error atau ingin improve:
1. Check error logs di console
2. Lihat browser console (F12) untuk JS errors
3. Restart Flask app dengan Ctrl+C kemudian jalankan lagi

---

**Good luck sa presentation! 🍀**

Anda siap menampilkan BI Dashboard dengan confidence! 💪
