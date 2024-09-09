# Glowify - A Django Project for Skincare E-commerce
`Glowify` adalah proyek Django sederhana sebagai tugas semester 3 mata kuliah Pemrograman Berbasis Platform oleh Adelya Amanda (2306165616). Proyek ini di buat dengan sistem operasi Windows.

## Tugas 2
### Proses Pembuatan Proyek Django
1. Membuat sebuah repository lokal yang sudah terkoneksi dengan repository Github bernama `glowify`
2. Di direktori `glowify`, membuat virtual environment Python baru dengan command:
   ```bash
   python -m venv env
3. Menyalakan virtual environment Python baru dengan command:
   ```bash
   env\Scripts\activate
4. Mempersiapkan `requirements.txt` di direktori yang sama, berisi daftar modul requirements:
   ```bash
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
5. Meng-install modul requirements dengan pip:
   ```bash
   python -m pip install -r requirements.txt
6. Membuat proyek Django baru dengan command:
   ```bash
   django-admin startproject glowify .
7. Mengubah ALLOWED_HOSTS di file `settings.py ` agar dapat berjalan di localhost dengan menambahkan:
   ```bash
   ...
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ...
8. Membuat aplikasi bernama main dengan command:
   ```bash
   python manage.py startapp main
9. Menambahkan nama aplikasi ke `INSTALLED_APPS` pada file `settings.py` di direktori `glowify`
    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
   ]
10. Me-routing url pada file `urls.py` di direktori `glowify` sehingga isi file `urls.py` menjadi:
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
11. Mengubah `models.py`dengan `class Product`, lalu isi dengan datatype sesuai kriteria:
    ```bash
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255) 
        price = models.IntegerField()  
        description = models.TextField()
12. Melakukan migrasi dengan command:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
13. Membuat direktori template di aplikasi main, lalu isi dengan `index.html` untuk laman main:
    ```bash
    <h1>Glowify your skin!</h1>

      <h5>Name: </h5>
      <p>{{ name }}<p>
      <h5>NPM: </h5>
      <p>{{ npm }}<p>
      <h5>Class: </h5>
      <p>{{ class }}<p>
14. Menambahkan fungsi untuk me-render laman main pada file `views.py`:
    ```bash
    from django.shortcuts import render

    def show_main(request):
        context = {
            'npm' : '2306165616',
            'name': 'Adelya Amanda',
            'class': 'PBP A'
        }
    
        return render(request, "main.html", context)
15. Melakukan routing pada aplikasi `main` pada file `urls.py` di direktori main:
    ```bash
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
16. Test aplikasi pada localhost dengan command:
    ```bash
    python manage.py runserver
17. Melakukan deploy app ke Pacil Web Server (PWS).

### Jawaban dari Pertanyaan
#### 1. Arsitektur MTV Django
![urls py (1)](https://github.com/user-attachments/assets/2375606a-f322-456b-85d3-db53d7dddc91)
Ketika user mengirimkan request melalui browser, request tersebut pada pertama kali akan diterima oleh `urls.py`. File ini berfungsi untuk menentukan URL mana yang cocok dengan request yang dikirim, kemudian mengarahkannya ke fungsi view yang sesuai di `views.py`. Setiap URL telah dipetakan ke fungsi tertentu di `views.py`.
   
Di dalam `views.py`, logic web app dijalankan, seperti memvalidasi data, mengambil informasi dari database, atau memproses input dari user. Jika perlu berinteraksi dengan database, `views.py` akan menggunakan `models.py` -- representasi data yang disimpan dalam database. Setelah data diambil atau diproses, view akan menggunakan file template HTML dari folder templates untuk menyajikan tampilan yang user lihat. Akhirnya, halaman HTML yang dirender tersebut dikirim kembali ke browser user sebagai response. Dengan demikian, `urls.py`, `views.py`, `models.py`, dan template HTML bekerja sama untuk memproses request & response dalam aplikasi Django.

#### 2. Fungsi git di pengembangan software
Git adalah alat version control yang umum digunakan dalam software development. Fungsinya untuk membantu developer melacak perubahan pada kode secara terorganisir. Dengan Git, setiap perubahan dalam proyek akan tersimpan di dalam repositori, sehingga developer dapat melihat riwayat perubahan, membandingkan versi kode yang berbeda, melakukan eksperimen pada kodenya, dan mengembalikan kode ke versi sebelumnya jika diperlukan. Fitur ini membuat kolaborasi antar tim menjadi mlebih mudah, karena setiap anggota tim dapat bekerja pada versi kode yang sama tanpa harus menyatukan perubahan secara manual.

Fitur unggulan lainnya dari Git adalah kemampuan untuk membuat cabang (branch) dari proyek utama. Dengan branch, developer dapat bekerja pada fitur atau perbaikan bug secara terpisah tanpa mengganggu kode utama yang sudah diyakini stabil. Setelah pekerjaan pada cabang selesai, cabang tersebut bisa digabungkan kembali ke proyek utama. Dengan git, setiap orang dapat fokus pada bagian mereka tanpa memengaruhi pekerjaan orang lain.

#### 3. Mengapa Django untuk permulaan pembelajaran software?
Dari pengalaman saya menggunakan framework full-stack seperti Node.js, saya merasa Django lebih menawarkan kepraktisan. Salah satu alasan utama adalah karena Django menggunakan Python, yang sering menjadi bahasa pertama bagi banyak orang yang ingin belajar pemrograman. Dengan Python yang terkenal readable seperti pseudocode dan juga beginner-friendly, Django menjadi pilihan yang natural bagi pemula yang ingin mencoba terjun ke web development

Selain itu, setup untuk membuat aplikasi web penuh di Django relatif jauh lebih cepat dibandingkan Node.js. Django sudah menyediakan banyak fitur bawaan, seperti sistem autentikasi, routing, dan manajemen database, sehingga developer dapat langsung fokus pada logika tanpa harus menyiapkan banyak komponen dari awal. Django juga menggabungkan back-end dan front-end dalam satu framework, sehingga tidak perlu menggunakan dua framework terpisah untuk full-stack development. Poin ini menghemat waktu dan tenaga dalam hal setup, terutama bagi yang baru memulai belajar software development.

### 4. Mengapa model pada Django disebut ORM?
Model dalam Django adalah representasi data yang ada di dalam database. Model biasanya berbentuk kelas Python yang mendefinisikan struktur data relasional, seperti kolom, tipe data, dan aturan-aturan terkait datanya. Model berfungsi sebagai penghubung antara logika web app dengan data yang disimpan di database.

Django menggunakan ORM (Object Relational Mapping) karena model memetakan objek Python (seperti kelas dan konsep OOP) dengan tabel di database. ORM ini berbeda dengan pengalaman saya menggunakan bahasa dan framework lain, di mana untuk berinteraksi dengan database saya harus menulis perintah SQL secara langsung untuk melakukan operasi CRUD. Django dapat melakukan manipulasi database menggunakan kode Python tanpa perlu menulis query SQL secara manual. ORM membantu proses pengelolaan data tanpa perlu memahami detail bahasa SQL.




   


   
