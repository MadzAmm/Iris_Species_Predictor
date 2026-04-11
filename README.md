<img width="1920" height="948" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/d22a1ae2-6663-468f-bbad-2c3fde22da1d" />
# 🌸 Iris Species Predictor

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56.0-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-F7931E.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Linear%20SVC-brightgreen)

Sistem Klasifikasi Cerdas Berbasis Machine Learning untuk memprediksi spesies bunga Iris (Setosa, Versicolor, atau Virginica) berdasarkan ukuran Sepal dan Petal. Aplikasi ini dibalut dengan antarmuka web interaktif yang dibangun menggunakan **Streamlit**.

---

## 🚀 Fitur Aplikasi

- **Antarmuka Interaktif:** Pengguna dapat memasukkan parameter ukuran bunga menggunakan _slider_ yang intuitif.
- **Prediksi Real-time:** Hasil klasifikasi spesies bunga langsung ditampilkan dalam hitungan detik.
- **UI Modern:** Dilengkapi dengan _custom CSS_, visualisasi metrik, dan efek animasi dari Streamlit.
- **Informasi Spesies:** Menampilkan deskripsi singkat mengenai spesies bunga yang berhasil diprediksi.

---

## 🧠 Arsitektur Model Machine Learning

Model _Machine Learning_ yang digunakan dalam aplikasi ini dilatih menggunakan dataset legendaris **Iris Dataset**. Arsitektur pemodelan dibangun menggunakan arsitektur **Pipeline** yang bersih dan efisien dari Scikit-Learn, terdiri dari dua tahap utama:

1. **Pre-processing (StandardScaler):**
   Data input (Panjang/Lebar Sepal dan Petal) distandarisasi terlebih dahulu sehingga memiliki _mean_ = 0 dan _standard deviation_ = 1. Hal ini sangat penting karena algoritma berbasis jarak/margin seperti SVC sangat sensitif terhadap skala data.
2. **Classifier (Linear SVC):**
   Setelah diskalakan, data diproses menggunakan algoritma **Linear Support Vector Classification (LinearSVC)** untuk menemukan _hyperplane_ terbaik yang memisahkan ketiga kelas spesies bunga Iris.

Model yang telah dilatih kemudian diekspor ke dalam format `.pkl` (Pickle) agar dapat dimuat dengan cepat di aplikasi web tanpa perlu melatih ulang (_retraining_).

---

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Python
- **Web Framework:** Streamlit
- **Machine Learning:** Scikit-Learn
- **Data Manipulasi:** Pandas & NumPy

---

## 💻 Cara Menjalankan Aplikasi Secara Lokal

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di komputer Anda:

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/MadzAmm/Iris_Species_Predictor.git
   cd data_iris_ml
   ```

2. **Buat Virtual Environment (Opsional namun disarankan):**

   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # Mac/Linux
   source env/bin/activate
   ```

3. **Instal pustaka (dependencies) yang dibutuhkan:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit:**

   ```bash
   streamlit run app_streamlit.py
   ```

5. **Buka di Browser:**
   Aplikasi akan otomatis terbuka di browser Anda, atau kunjungi `http://localhost:8501`.

---

_Dibuat dengan ❤️ menggunakan Streamlit oleh thinkermuumoo_
