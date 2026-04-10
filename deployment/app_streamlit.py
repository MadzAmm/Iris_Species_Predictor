import streamlit as st
import pickle
import pandas as pd

# 1. Konfigurasi Halaman (Harus dipanggil paling pertama)
st.set_page_config(
    page_title="Iris Predictor",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Custom CSS untuk mempercantik tampilan UI
st.markdown(
    """
    <style>
    .main-title {
        font-size: 6rem;
        color: #4B4B4B;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #6C757D;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
        transform: scale(1.02);
    }
    </style>
""",
    unsafe_allow_html=True,
)


# 3. Fungsi memuat model dengan Cache
@st.cache_resource
def load_model():
    try:
        # Ganti 'model_iris.pkl' dengan nama file pickle Anda
        with open("model_pandas.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"⚠️ Gagal memuat model: {e}")
        return None


model = load_model()

# 4. Bagian Header (Layar Utama)
st.markdown(
    '<p class="main-title">🌸 Iris Species Predictor</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-title">Sistem Klasifikasi Cerdas Berbasis Machine Learning</p>',
    unsafe_allow_html=True,
)

st.write("---")

# 5. Bagian Sidebar (Untuk Input Pengguna)
st.sidebar.header("Parameter Input")
st.sidebar.write("Geser slider di bawah untuk mengatur karakteristik bunga.")


def user_input_features():
    # Rentang nilai disesuaikan dengan dataset asli Iris
    sepal_length = st.sidebar.slider("Panjang Sepal (cm)", 4.3, 7.9, 5.4, step=0.1)
    sepal_width = st.sidebar.slider("Lebar Sepal (cm)", 2.0, 4.4, 3.4, step=0.1)
    petal_length = st.sidebar.slider("Panjang Petal (cm)", 1.0, 6.9, 1.3, step=0.1)
    petal_width = st.sidebar.slider("Lebar Petal (cm)", 0.1, 2.5, 0.2, step=0.1)

    data = {
        "Sepal Length": sepal_length,
        "Sepal Width": sepal_width,
        "Petal Length": petal_length,
        "Petal Width": petal_width,
    }
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()

# 6. Menampilkan Input Pengguna dengan Layout Kolom
st.subheader("Data Karakteristik Bunga")
st.write("Berikut adalah parameter yang Anda masukkan melalui sidebar:")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Sepal Length", f"{input_df['Sepal Length'][0]} cm")
col2.metric("Sepal Width", f"{input_df['Sepal Width'][0]} cm")
col3.metric("Petal Length", f"{input_df['Petal Length'][0]} cm")
col4.metric("Petal Width", f"{input_df['Petal Width'][0]} cm")

st.write("")  # Spasi kosong

# 7. Proses Prediksi
if st.button("Prediksi Spesies Sekarang"):
    if model is not None:
        with st.spinner("Menganalisis data..."):
            # Konversi input DataFrame ke array untuk model
            input_array = input_df.values
            prediction = model.predict(input_array)

            # Asumsi output model Anda adalah integer 0, 1, 2 (Label Encoding)
            # Jika model Anda langsung mengeluarkan string ('setosa', dll),
            # Anda bisa langsung menggunakan hasil prediksinya tanpa mapping ini.
            species_mapping = {
                0: "Iris Setosa",
                1: "Iris Versicolor",
                2: "Iris Virginica",
            }

            # Sesuaikan dengan format output model Anda
            # Jika output string: predicted_species = prediction[0]
            predicted_species = species_mapping.get(prediction[0], prediction[0])

            st.success(f"### 🎉 Hasil Prediksi: **{predicted_species}**")
            st.balloons()  # Efek balon saat prediksi berhasil

            # Tampilkan informasi tambahan berdasarkan spesies
            with st.expander("Info lebih lanjut tentang spesies ini"):
                if "Setosa" in str(predicted_species):
                    st.write(
                        "Iris Setosa adalah spesies yang mudah dibedakan secara visual karena ukurannya yang lebih kecil dan mahkota yang khas."
                    )
                elif "Versicolor" in str(predicted_species):
                    st.write(
                        "Iris Versicolor memiliki ukuran menengah, sering ditemukan di padang rumput basah."
                    )
                elif "Virginica" in str(predicted_species):
                    st.write(
                        "Iris Virginica biasanya merupakan spesies terbesar di antara ketiganya dengan kelopak yang lebar."
                    )
                else:
                    st.write("Spesies berhasil diklasifikasikan.")
    else:
        st.error("Model tidak tersedia. Pastikan file pickle sudah benar.")

# Footer info
st.sidebar.markdown("---")
st.sidebar.info(
    "Dibuat menggunakan [Streamlit](https://streamlit.io/) oleh Thinker Muumoo"
)
