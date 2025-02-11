# -*- coding: utf-8 -*-
"""Visualization_Stress-Lysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11nHzlpYonMXJ4AXBSYYlDgIx_Ozobemy

# Import
"""

import pandas as pd
from google.colab import files
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

file = files.upload()

data = pd.read_csv("Stress-Lysis.csv")

"""# -- Data Understanding"""

data.head()

# Menampilkan data dictionary
data.info()

data.describe()

"""# -- Data Preparation dan Preprocessing

## Eksplorasi Awal
"""

data.head()

# Statistik deskriptif
data.describe()

"""## Menghilangkan nilai null"""

# Menghitung jumlah nilai null di setiap kolom
null_counts = data.isnull().sum()

# Menampilkan jumlah nilai null di setiap kolom
print("Jumlah nilai null di setiap kolom:")
print(null_counts)

# Menampilkan jumlah baris sebelum penghapusan
print("Jumlah baris sebelum penghapusan:", len(data))

# Menghapus baris yang mengandung nilai null
data_preprocessed = data.dropna()

# Menampilkan jumlah baris setelah penghapusan
print("Jumlah baris setelah penghapusan:", len(data_preprocessed))

"""# -- EDA"""

# Eksplorasi awal
data.head()

# Statistik deskriptif
data.describe()

"""## Eksplorasi Deskriptif

---

### Bagaimana Persebaran kelas yang ada dalam dataset?
"""

# Visualisasi distribusi data
data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

"""Distribusi kelas dalam data ini cukup baik untuk tujuan klasifikasi. Kelas-kelas stres rendah, sedang, dan tinggi memiliki frekuensi yang relatif seimbang, sehingga model pembelajaran mesin dapat mempelajari setiap kelas dengan representasi yang memadai.

###Bagaimana Persebaran stress level pada setiap faktor/variabel independen (Humidity, Temperature, Step-count)?
"""

# Membuat plot histogram frekuensi Humidity dengan membedakan warna untuk setiap level stress
sns.histplot(data=data, x='Humidity', hue='Stress Level', multiple='dodge', palette='colorblind', kde=False)
plt.title('Histogram of Humidity by Stress Level')
plt.show()

# Membuat plot histogram frekuensi Temperature dengan membedakan warna untuk setiap level stress
sns.histplot(data=data, x='Temperature', hue='Stress Level', multiple='dodge', palette='colorblind', kde=False)
plt.title('Histogram of Temperature by Stress Level')
plt.show()

# Membuat plot histogram frekuensi Step count dengan membedakan warna untuk setiap level stress
sns.histplot(data=data, x='Step count', hue='Stress Level', multiple='dodge', palette='colorblind', kde=False)
plt.title('Histogram of Step count by Stress Level')
plt.show()

"""1. Korelasi antara tingkat stres (0, 1, dan 2) dengan variabel kelembaban, suhu, dan jumlah langkah terlihat jelas dalam histogram ini.
2. Kelembaban rendah (10-15) dan suhu rendah (80-85 derajat) cenderung dikaitkan dengan tingkat stres 0, sementara kelembaban tinggi (25-30) dan suhu tinggi (95-100 derajat) lebih sering terkait dengan tingkat stres 2.
3. Jumlah langkah juga memainkan peran, dengan tingkat stres 0 terjadi pada jumlah langkah rendah (0-75) dan tingkat stres 2 pada jumlah langkah tinggi (150-200).
4. Data ini menyoroti pentingnya memahami bagaimana faktor lingkungan seperti kelembaban, suhu, dan tingkat aktivitas fisik dapat mempengaruhi tingkat stres seseorang.

## eksplorasi diagnostic

Apakah ada nilai outlier atau nilai yang jauh berbeda dari nilai-nilai lainnya yang terdapat dalam dataset
"""

# Box Plot untuk identifikasi outlier
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.title('Outlier Data')
plt.xticks(rotation=45)
plt.show()

"""Dari grafik ini, kita bisa melihat rentang data, nilai tengah (median), dan penyebaran data untuk masing-masing variabel. Untuk kelembaban, rentangnya berkisar antara 10 hingga 30 dengan beberapa data yang mendekati nilai maksimum. Suhu berkisar antara 80 hingga 100, menunjukkan distribusi yang lebih sempit dibanding kelembaban. Jumlah langkah memiliki penyebaran yang paling luas, dengan rentang dari 0 hingga hampir 200, mencerminkan variasi besar dalam aktivitas fisik. Tingkat stres memiliki rentang yang sangat kecil, mengindikasikan bahwa datanya lebih terfokus pada nilai-nilai tertentu, tanpa banyak variasi. Tidak ada outlier yang jelas terlihat dalam grafik ini, menunjukkan bahwa semua data berada dalam batasan yang diharapkan untuk masing-masing variabel.

###Apakah ada korelasi signifikan secara statistik antara variabel-variabel dalam dataset?
"""

# Periksa korelasi antar kolom
correlation_matrix = data.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Reds', fmt='.2f', linewidths=0.5)
plt.title('Matrix Korelasi')
plt.show()

"""semua fitur (Humidity, Temperature, dan Step count) memiliki korelasi yang kuat dengan tingkat stres (Stress Level). Terutama, kelembaban tubuh (Humidity) dan suhu tubuh (Temperature) menunjukkan korelasi yang sangat tinggi dengan tingkat stres. Hal ini mengindikasikan bahwa perubahan pada kelembaban dan suhu tubuh dapat menjadi indikator yang sangat baik dalam menentukan tingkat stres seseorang. Jumlah langkah yang diambil juga berhubungan erat dengan tingkat stres, meskipun tidak sekuat dua fitur lainnya.

###Apakah terdapat korelasi positif atau negatif antara variabel dengan tingkat stres?
"""

# Scatter plot dengan fit garis regresi
data_encoded = data.copy()
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
sns.regplot(x='Humidity', y='Stress Level', data=data_encoded, scatter_kws={'s': 50}, order=1)
plt.title('Humidity vs Stress Level')

plt.subplot(1, 3, 2)
sns.regplot(x='Temperature', y='Stress Level', data=data_encoded, scatter_kws={'s': 50}, order=1)
plt.title('Temperature vs Stress Level')

plt.subplot(1, 3, 3)
sns.regplot(x='Step count', y='Stress Level', data=data_encoded, scatter_kws={'s': 50}, order=1)
plt.title('Step count vs Stress Level')

plt.tight_layout()
plt.show()

"""Hasil scatterplot dengan garis regresi menunjukkan bahwa terdapat hubungan positif antara setiap fitur (Humidity, Temperature, Step count) dan tingkat stres (Stress Level). Secara spesifik, kelembaban (Humidity) memiliki korelasi positif yang jelas dengan tingkat stres, dengan dua kelompok data yang terpisah menunjukkan batasan tertentu dalam nilai kelembaban yang membedakan tingkat stres rendah, sedang, dan tinggi. Suhu (Temperature) juga menunjukkan tren positif, meskipun data lebih tersebar, menunjukkan bahwa tingkat stres cenderung meningkat dengan kenaikan suhu, meskipun korelasinya mungkin lebih lemah dibandingkan dengan kelembaban. Sementara itu, jumlah langkah (Step count) menunjukkan tren positif yang sangat jelas, menandakan bahwa semakin banyak langkah yang diambil, semakin tinggi tingkat stres, dengan kelompok data yang jelas untuk setiap tingkat stres.

### Variabel manakah yang mungkin menjadi pengaruh terbesar dalam klasifikasi tingkat stres?
"""

from sklearn.ensemble import RandomForestClassifier

X = data.drop('Stress Level', axis=1)
y = data['Stress Level']

model = RandomForestClassifier()
model.fit(X, y)

importances = model.feature_importances_
feature_importances = pd.Series(importances, index=X.columns)

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_importances.index, palette='viridis')
plt.title('Feature Importance')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()

"""Berdasarkan grafik "Feature Importance" yang dihasilkan oleh model machine learning seperti Random Forest, terlihat bahwa fitur "Humidity" memiliki pengaruh terbesar terhadap prediksi "Stress Level", diikuti oleh "Temperature" dan "Step count". Hal ini menunjukkan bahwa kelembaban tubuh merupakan indikator paling signifikan dalam menentukan tingkat stres seseorang. Suhu tubuh juga memberikan kontribusi penting, sementara jumlah langkah yang diambil meskipun lebih rendah pengaruhnya, tetap berperan dalam prediksi stres. Model ini mengungkapkan betapa pentingnya kondisi fisik dalam memahami dan memprediksi tingkat stres, dengan kelembaban tubuh menjadi faktor dominan.

###Bagaimana hubungan antara suhu dan kelembaban mempengaruhi tingkat stres?
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Asumsikan dataset sudah di-load ke dalam variabel `dataset`

# Drop kolom "Stress Level" untuk mendapatkan fitur numerik saja
numerical_features = data.drop("Stress Level", axis=1)

# Menambahkan kolom "Stress Level" ke dalam dataframe fitur numerik
numerical_features["Stress Level"] = data["Stress Level"]

# Membuat grid scatter plot dengan pairplot
plt.figure(figsize=(15, 10))
sns.pairplot(numerical_features, hue="Stress Level", palette="viridis")
plt.suptitle("Pair Plot of Numerical Features Colored by Stress Level", y=1.02)
plt.show()

"""Grafik tersebut merupakan pair plot yang menampilkan hubungan antara tiga fitur numerik yaitu kelembaban (Humidity), suhu (Temperature), dan jumlah langkah (Step count) dengan tingkat stres yang ditandai oleh warna berbeda: ungu untuk stres level 0, biru untuk stres level 1, dan kuning untuk stres level 2. Dari grafik ini, terlihat bahwa setiap tingkat stres memiliki rentang kelembaban, suhu, dan jumlah langkah yang berbeda. Stres level 0 cenderung terjadi pada kelembaban rendah (sekitar 10-15%), suhu rendah (sekitar 80-85 derajat), dan jumlah langkah yang rendah (0-100). Stres level 1 terjadi pada rentang menengah untuk ketiga fitur tersebut, sementara stres level 2 terjadi pada kelembaban tinggi (25-30%), suhu tinggi (95-100 derajat), dan jumlah langkah yang tinggi (150-200). Hubungan linier yang kuat antara suhu dan kelembaban serta pola blok pada grafik jumlah langkah menunjukkan bahwa faktor-faktor lingkungan ini sangat mempengaruhi tingkat stres seseorang, dengan tingkat stres meningkat seiring dengan peningkatan suhu dan kelembaban, serta peningkatan jumlah langkah.

# -- Modeling

### SVM
"""

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# Pisahkan atribut dan label
X = data.drop('Stress Level', axis=1)
y = data['Stress Level']

# Bagi dataset menjadi data pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definisikan hyperparameter grid
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf', 'linear', 'poly', 'sigmoid']
}

# Inisialisasi model SVM
svm_model = SVC()

# Buat objek GridSearchCV
grid_search = GridSearchCV(estimator=svm_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Latih model pada dataset dengan GridSearch
grid_search.fit(X_train, y_train)

# Print hasil pencarian grid
print("Best Parameters:", grid_search.best_params_)
print("Best Estimator:", grid_search.best_estimator_)

# Evaluasi model terbaik
best_model = grid_search.best_estimator_
svm_y_pred = best_model.predict(X_test)

# Hitung dan print hasil evaluasi
accuracy = accuracy_score(y_test, svm_y_pred)
precision = precision_score(y_test, svm_y_pred, average='weighted')
recall = recall_score(y_test, svm_y_pred, average='weighted')
f1 = f1_score(y_test, svm_y_pred, average='weighted')

print("Accuracy SVM:", accuracy)
print("Precision SVM:", precision)
print("Recall SVM:", recall)
print("F1 Score SVM:", f1)
print("Classification Report:\n", classification_report(y_test, svm_y_pred))

import matplotlib.pyplot as plt
import seaborn as sns

# Membuat Confusion Matrix
conf_matrix = confusion_matrix(y_test, svm_y_pred)

# Membuat plot Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
            xticklabels=['Low Stress', 'Normal Stress', 'High Stress'],
            yticklabels=['Low Stress', 'Normal Stress', 'High Stress'])
plt.title('Accuracy Test SVM')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

"""### Naive Bayes"""

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# Pisahkan atribut dan label
X = data.drop('Stress Level', axis=1)
y = data['Stress Level']

# Bagi dataset menjadi data pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inisialisasi model Naive Bayes
nb_model = GaussianNB()

# Definisikan hyperparameter grid (tidak ada hyperparameter yang dapat dioptimalkan untuk Naive Bayes)
param_grid = {}

# Buat objek GridSearchCV
grid_search = GridSearchCV(estimator=nb_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Latih model pada dataset dengan GridSearch
grid_search.fit(X_train, y_train)

# Print hasil pencarian grid (karena tidak ada hyperparameter yang dioptimalkan, hanya mencetak model default)
print("Best Estimator:", grid_search.best_estimator_)

# Evaluasi model terbaik
best_model = grid_search.best_estimator_
nb_y_pred = best_model.predict(X_test)

# Print hasil evaluasi
accuracy = accuracy_score(y_test, nb_y_pred)
precision = precision_score(y_test, nb_y_pred, average='weighted')
recall = recall_score(y_test, nb_y_pred, average='weighted')
f1 = f1_score(y_test, nb_y_pred, average='weighted')

print("Accuracy Naive Bayes:", accuracy)
print("Precision Naive Bayes:", precision)
print("Recall Naive Bayes:", recall)
print("F1 Score Naive Bayes:", f1)
print("Classification Report:\n", classification_report(y_test, nb_y_pred))

import matplotlib.pyplot as plt
import seaborn as sns

# Membuat Confusion Matrix
conf_matrix = confusion_matrix(y_test, nb_y_pred)

# Membuat plot Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
            xticklabels=['Low Stress', 'Normal Stress', 'High Stress'],
            yticklabels=['Low Stress', 'Normal Stress', 'High Stress'])
plt.title('Accuracy Test Naive Bayes')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

