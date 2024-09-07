# Glowify - A Django Project for Skincare E-commerce
Glowify adalah proyek Django sederhana sebagai tugas mata kuliah Pemrograman Berbasis Platform 2024/2025 oleh Adelya Amanda (2306165616). Proyek ini di buat dengan sistem operasi Windows.

## Tugas 2
### Proses Pembuatan Proyek Django
1. Membuat sebuah repository lokal yang sudah terkoneksi dengan repository Github bernama `glowify`
2. Di direktori `glowify`, buat virtual environment Python baru dengan command:
   ```bash
   python -m venv env
3. Menyalakan virtual environment Python baru dengan command:
   ```bash
   env\Scripts\activate
4. Mempersiapkan requirements.txt di direktori yang sama, berisi:
   ```bash
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
5. Meng-install requirements dengan pip:
   ```bash
   python -m pip install -r requirements.txt
6. Membuat proyek Django baru dengan command:
   ```bash
   django-admin startproject glowify .
7. Mengubah ALLOWED_HOSTS di file `settings.py `dengan menambahkan:
   ```bash
   ...
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ...
8. Membuat aplikasi main dengan command:
   ```bash
   python manage.py startapp main
9. Me-routing url pada file `urls.py` di direktori glowify sehingga isi file `urls.py` menjadi:
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
10. Mengubah `models.py` menjadi:
    ```bash
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255) 
        price = models.IntegerField()  
        description = models.TextField()
11. Membuat direktori template di aplikasi main, lalu isi dengan `index.html` untuk laman main:
    ```bash
    <h5>NPM: </h5>
    <p>{{ npm }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
12. Menambahkan fungsi untuk me-render laman main pada file `views.py`:
    ```bash
    from django.shortcuts import render

    def show_main(request):
        context = {
            'npm' : '2306165616',
            'name': 'Adelya Amanda',
            'class': 'PBP A'
        }
    
        return render(request, "main.html", context)
13. Melakukan routing pada aplikasi main pada file `urls.py` di direktori main:
    ```bash
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
14. Mengetest aplikasi pada localhost dengan command:
    ```bash
    python manage.py runserver
15. Melakukan deploy app ke Pacil Web Server (PWS).

    
