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
       volume = models.IntegerField()
    
       @property
       def price_per_ml(self):
           return self.price / self.volume if self.volume > 0 else 0
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
    Project telah dideploy di PWS melalui [ http://adelya-amanda-glowify.pbp.cs.ui.ac.id/ ]

### Jawaban dari Pertanyaan Tugas 2
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

## Tugas 3
### Implementasi Form pada Django
1. Membuat `forms.py` di direktori `main` dengan isi:
   ```bash
   from django import forms
   from .models import Product
   
   class ProductForm(forms.ModelForm):
       class Meta:
           model = Product
           fields = ['name', 'price', 'description', 'volume']
3. Menambahkan fungsi `create_product` untuk menambha entri database di `views.py` di direktori main:
   ```bash
   def create_product(request):
       form = ProductForm(request.POST or None)
   
       if form.is_valid():
           form.save()
           return redirect('main:show_main')
       
       context = {'form': form}    
       return render(request, "create_product.html", context)
4. Mengimplementasikan form yang sudah dibuat ke dalam laman baru dengan template html yang baru `create_product.html`:
   ```bash
   {% extends 'base.html' %} 
   {% block content %}
   
   <h1>Add new product!</h1>
   <form method="POST">
       {% csrf_token %}
       <table>
           {{form.as_table}}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add product" />
               </td>
           </tr>
       </table>
   </form>
   
   {% endblock %}
5. Routing URL ke page yang sesuai di `urls.py` pada adirektori `main`:
   ```bash
   urlpatterns = [
       ...
       path('create-product', create_product, name='create_product'),
       ...
   ]
6. Menambahkan folder `templates` di direktori utama dan `base.html` sebagai base dari halaman-halaman lainnya.
7. Menambahkan lokasi folder `templates` ke `settings.py` di direktori `glowify`:
   ```bash
   ...
   'DIRS': [BASE_DIR / 'templates'],
   ...
8. Mengimplementasikan database ke dalam halaman utama `main.html`, yang juga menjadi perpanjangan dari `base.html` di direktori utama:
   ```bash
   {% if not products %}
   <p>Product not found T_T</p>
   {% else %}
   <table>
       <tr>
           <th>Product Name</th>
           <th>Price</th>
           <th>Description</th>
           <th>Volume (ml)</th>
       </tr>
   
       {% for product in products %}
       <tr>
           <td>{{ product.name }}</td>
           <td>{{ product.price }}</td>
           <td>{{ product.description }}</td>
           <td>{{ product.volume }}</td>
       </tr>
       {% endfor %}
   </table>
   {% endif %}
   
   <br />
   
   <a href="{% url 'main:create_product' %}">
       <button>Add new product!</button>
   </a>
9. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML, baik secara keseluruhan ataupun berdasarkan PK entri database yang sesuai di `views.py`
   ```bash
   def show_xml(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
   
   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize('json', data), content_type='application/json')
   
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
   
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize('json', data), content_type='application/json')    
10. Melakukan routing kembali URL yang sesuai i file `urls.py`:
   ```bash
   urlpatterns = [
       ...
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>', show_json_by_id, name='show_json_by_id')
   ]
11. Melakukan test aplikasi pada localhost, cek apakah ada error. Cek juga endpoint yang sesuai, baik tidak ataupun menggunakan PK:
   ```bash
   python manage.py runserver

### Test di Postman
1. JSON
![image](https://github.com/user-attachments/assets/a24d8e4f-f3a3-4275-b51b-91f0e7a87f49)

2. JSON by PK
![image](https://github.com/user-attachments/assets/1e40ca32-c143-4bfc-a23c-ad67b789f415)

3. XML
![image](https://github.com/user-attachments/assets/a76119a7-401d-4c11-90e7-9d63e24e602e)

4. XML by PK
![image](https://github.com/user-attachments/assets/77247af3-3ab5-46bb-a25c-668f576ab0e4)

### Jawaban dari Pertanyaan Tugas 3
#### 1. Mengapa memerlukan data delivery dalam mengimplementasikan platform
Misalkan untuk user e-commerce `glowify`, user akan expect untuk mendapatkan lists dari produk terbaru dan melihat  stok barang yang tersedia. Misalkan saya, sebagai salah satu seller dari `glowify`, tentu saya ingin menuliskan deskripsi produk up-to-date agar pembeli saya mendapatkan review produk yang paling relevan, atau terus mengupdate harga dari produk yang saya jual seiring waktu. Saya juga perlu mengupdate stok yang tersedia di inventori saya. Dengan demikian, data delivery berguna untuk user experience. User memerlukan update data yang dinamis, jadi data perlu diperbaharui secara terus menerus, menyanggupi request yang masuk.
Melalui data delivery, setiap produk yang saya update di `glowify` telah memiliki identitas (ID) nya sendiri. Namun saya dapat merasa nyaman sebagai penjual, karena tahu ID nya bukanlah semata desimal yang mudah dienumerate, tapi sebuah unique ID yang dipastikan berbeda untuk setiap barang yang saya jual. Dengan demikian, data delivery juga berfungsi sebagai data protection.

#### 2. JSON vs. XML?
Meskipun keduanya merupakan form of data delivery yang paling umum digunakan, saya bisa mengerti mengapa JSON lebih populer. Secara awam, JSON akan jauh lebih mudah dipahami karena hanya berupa key and value pair, juga lebih 'sedikit' untuk ditulis (less verbose). Dengan penulisan yang lebih sedikit (simple) tetapi merepresentasikan data delivery yang sama, tentu JSON akan lebih menjadi pilihan. Selain itu, JSON juga didukung oleh Javascript, yang merupakan 'most used web programming language` (Statista, 2024). Ketika pertama kali mempelajari web development, saya juga lebih dulu diperkenalkan dengan Javascript, sehingga jauh lebih familiar untuk menggunakan JSON. Ketika mempelajari RESTful APIs pun, JSOn akan digunakan untuk data interchange, ditambah JSON didukung oleh built-in method yang berguna seperti `JSON.parse()` dan `JSON.stringify()`. JSON juga mensupport penggunaan array, tidak dengan XML. Tetapi, semua kembali ke konteks penggunaan. Bagaimanapun, XML juga memberikan hierarki yang lebih jelas dan descriptive.

### 3. `is_valid()` pada Form Django
![image](https://github.com/user-attachments/assets/2effd8e3-4716-4abb-b32b-2b79dfe3cd2b)

Ketika saya mencoba mengisi form bagian field `price` dan `volume` dengan alphabet, tulisannya tidak akan bisa muncul. Hal ini disebabkan saya telah mendefine field form tersebut dengan Integer. 




   


   
