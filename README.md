# Glowify - A Django Project for Skincare E-commerce
`Glowify` adalah proyek Django sederhana sebagai tugas semester 3 mata kuliah Pemrograman Berbasis Platform oleh Adelya Amanda (2306165616). Proyek ini di buat dengan sistem operasi Windows.

## Tugas 2
### Proses Pembuatan Proyek Django
1. Membuat sebuah repository lokal yang sudah terkoneksi dengan repository Github bernama `glowify`
2. Di direktori `glowify`, membuat virtual environment Python baru dengan command:
   ```python
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
   ```python
   python -m pip install -r requirements.txt
6. Membuat proyek Django baru dengan command:
   ```bash
   django-admin startproject glowify .
7. Mengubah ALLOWED_HOSTS di file `settings.py ` agar dapat berjalan di localhost dengan menambahkan:
   ```python
   ...
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ...
8. Membuat aplikasi bernama main dengan command:
   ```python
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
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
11. Mengubah `models.py`dengan `class Product`, lalu isi dengan datatype sesuai kriteria:
    ```python
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
    ```python
    python manage.py makemigrations
    python manage.py migrate
13. Membuat direktori template di aplikasi main, lalu isi dengan `index.html` untuk laman main:
    ```html
    <h1>Glowify your skin!</h1>

      <h5>Name: </h5>
      <p>{{ name }}<p>
      <h5>NPM: </h5>
      <p>{{ npm }}<p>
      <h5>Class: </h5>
      <p>{{ class }}<p>
14. Menambahkan fungsi untuk me-render laman main pada file `views.py`:
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'npm' : '2306165616',
            'name': 'Adelya Amanda',
            'class': 'PBP A'
        }
    
        return render(request, "main.html", context)
15. Melakukan routing pada aplikasi `main` pada file `urls.py` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
16. Test aplikasi pada localhost dengan command:
    ```python
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
   ```python
   from django import forms
   from .models import Product
   
   class ProductForm(forms.ModelForm):
       class Meta:
           model = Product
           fields = ['name', 'price', 'description', 'volume']
   ```
   
3. Menambahkan fungsi `create_product` untuk menambha entri database di `views.py` di direktori main:
   ```python
   def create_product(request):
       form = ProductForm(request.POST or None)
   
       if form.is_valid():
           form.save()
           return redirect('main:show_main')
       
       context = {'form': form}    
       return render(request, "create_product.html", context)
   ```
   
4. Mengimplementasikan form yang sudah dibuat ke dalam laman baru dengan template html yang baru `create_product.html`:
   ```python
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
   ```
   
5. Routing URL ke page yang sesuai di `urls.py` pada adirektori `main`:
   ```python
   urlpatterns = [
       ...
       path('create-product', create_product, name='create_product'),
       ...
   ]
   ```
   
6. Menambahkan folder `templates` di direktori utama dan `base.html` sebagai base dari halaman-halaman lainnya.
   
7. Menambahkan lokasi folder `templates` ke `settings.py` di direktori `glowify`:
   ```python
   ...
   'DIRS': [BASE_DIR / 'templates'],
   ...
   ```
   
8. Mengimplementasikan database ke dalam halaman utama `main.html`, yang juga menjadi perpanjangan dari `base.html` di direktori utama:
   ```html
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
   ```

9. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML, baik secara keseluruhan ataupun berdasarkan PK entri database yang sesuai di `views.py`:
   ```python
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
   ```

10. Melakukan routing kembali URL yang sesuai di file `urls.py`:
   ```python
   urlpatterns = [
       ...
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>', show_json_by_id, name='show_json_by_id')
   ]
   ```

11. Melakukan test aplikasi pada localhost, cek apakah ada error. Cek juga endpoint yang sesuai, baik tidak ataupun menggunakan PK:
   ```bash
   python manage.py runserver
   ```

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
Misalkan untuk user e-commerce `glowify`, user akan expect untuk mendapatkan lists dari produk terbaru dan melihat stok barang yang tersedia. Misalkan saya, sebagai salah satu seller dari `glowify`, tentu saya ingin menuliskan deskripsi produk up-to-date agar pembeli saya mendapatkan review produk yang paling relevan, atau terus mengupdate harga dari produk yang saya jual seiring waktu. Saya juga perlu mengupdate stok yang tersedia di inventori saya. Dengan demikian, data delivery berguna untuk user experience. User memerlukan update data yang dinamis, jadi data perlu diperbaharui secara terus menerus, menyanggupi request yang masuk.
Melalui data delivery, setiap produk yang saya update di `glowify` telah memiliki identitas (ID) nya sendiri. Namun saya dapat merasa nyaman sebagai penjual, karena tahu ID nya bukanlah semata desimal yang mudah dienumerate, tapi sebuah unique ID yang dipastikan berbeda untuk setiap barang yang saya jual. Dengan demikian, data delivery juga berfungsi sebagai data protection.

#### 2. JSON vs. XML?
Meskipun keduanya merupakan form of data delivery yang paling umum digunakan, saya bisa mengerti mengapa JSON lebih populer. Secara awam, JSON akan jauh lebih mudah dipahami karena hanya berupa key and value pair, juga lebih 'sedikit' untuk ditulis (less verbose). Dengan penulisan yang lebih sedikit (simple) tetapi merepresentasikan data delivery yang sama, tentu JSON akan lebih menjadi pilihan. Selain itu, JSON juga didukung oleh Javascript, yang merupakan 'most used web programming language' (Statista, 2024). Ketika pertama kali mempelajari web development, saya juga lebih dulu diperkenalkan dengan Javascript, sehingga jauh lebih familiar untuk menggunakan JSON. Ketika mempelajari RESTful APIs pun, JSON akan digunakan untuk data interchange, ditambah JSON didukung oleh built-in method yang berguna seperti `JSON.parse()` dan `JSON.stringify()` yang dapat langsung mentranslasi data dalam bentuk objek. Bandingkan dengan XML yang perlu berhadapan dengan parsing text secara manual. JSON juga mensupport penggunaan array, tidak dengan XML. Tetapi, semua kembali ke konteks penggunaan. Bagaimanapun, XML juga memberikan hierarki yang lebih jelas dan descriptive.

### 3. `is_valid()` pada Form Django
![image](https://github.com/user-attachments/assets/2effd8e3-4716-4abb-b32b-2b79dfe3cd2b)

`is_valid()` merupakan built-in method dari Django. Ketika memanggil `is_valid()`, Django akan melakukan validasi untuk setiap field di form. Validasi berupa: apakah tipe dari field sesuai dengan yang didefinisikan di `models.py`, apakah semua field terisi, ataupun custom logic lainnya. 
Mengapa membutuhkan method `is_valid()`? Jika validasi gagal, yang berarti data yang diinput user tidak seusai kriteria, field akan me-return `false` dan memunculkan pesan error, sehingga user dapat langsung menyadari kesalahan dari input dan segera membetulkan pengisian input fieldnya. Jika `is_valid()` me-return `true`, form akan emiliki `cleaned_data` yang dapat digunakan untuk logika selanjutnya dalam aplikasi Django. 
Jika tidak melalui validasi, data yang masuk ke database dengan tipe `IntegerField` bisa saja berupa alphabet, sehingga database (umumnya SQL) akan segera mereturn error, yang berujung rumit jika harus membetulkannya manual dari sisi database. Sehingga, dengan method `is_valid()`, ketika saya mencoba mengisi  field `price` dan `volume` dengan alphabet, tulisannya tidak akan bisa muncul, akibat saya telah mendefine field form tersebut dengan Integer.

### 4. CSRF (Cross-Site Request Forgery) `csrf_token` pada template Django
CSRF merupakan jenis serangan di mana attacker melakukan tindakan yang tidak sah, atas nama pengguna yang sah, tanpa sepengetahuan mereka. Tindakan yang tidak sah dalam konteks aplikasi bisa berupa mengubah kata sandi, mengirim pesan atas nama pengguna yang sah, melakukan transaksi tidak sah, hingga mengubah data. Dalam konteks `glowify`, serangan bisa berupa penghapusan produk atau perubahan informasi mengenai produk yang dijual.
Contoh mekanismenya, attacker dapat membuat form tersembunyi yang mengirimkan `POST` request ke aplikasi Django saya, `glowify`. Pengguna `glowify` yang mengira mereka sedang mengisi form di situs `glowify` asli, akan mengisi data penting mengenai pembelian mereka pada form palsu, lalu submit form tersebut. Submit request akan tampak sah bagi `glowify` dikarenakan berasal dari browser pengguna yang sah. 
`csrf_token` membantu menghasilkan token unik yang disertakan dalam form. Token ini yang hanya akan lolos oleh verifikasi server saat form disubmit, jika token tersebut sesuai dengan yang dihasilkan server. Sehingga, hanya form sah `glowify` yang akan diterima oleh server.

## Tugas 4

### Implementasi Autentikasi, Cookie & Session, dan Menghubungkan Model `Product` dengan `User`

#### 1. Membuat Fungsionalitas Registrasi

- Buat fungsi `register` di `views.py` untuk menangani registrasi pengguna baru menggunakan `UserCreationForm`.
- Tambahkan halaman `register.html` di dalam `main/templates` untuk form pendaftaran.
- Tambahkan routing untuk `register` di `urls.py`.

```python
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    return render(request, 'register.html', {'form': form})
```

```html
<!-- register.html -->
{% extends 'base.html' %}
{% block content %}
<div class="login">
  <h1>Register</h1>
  <form method="POST">{% csrf_token %}
    <table>{{ form.as_table }}</table>
    <input type="submit" name="submit" value="Daftar" />
  </form>
</div>
{% endblock %}
```

```python
# urls.py
from main.views import register

urlpatterns = [
    ...
    path('register/', register, name='register'),
]
```

#### 2. Membuat Fungsionalitas Login

- Buat fungsi `login_user` untuk menangani autentikasi pengguna. Setelah berhasil login, set cookie `last_login`.
- Buat halaman `login.html`.
- Tambahkan routing untuk login di `urls.py`.

```python
# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
import datetime

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```

```html
<!-- login.html -->
{% extends 'base.html' %}
{% block content %}
<div class="login">
  <h1>Back to Glowify!</h1>
  <form method="POST">{% csrf_token %}
    <table>{{ form.as_table }}</table>
    <input type="submit" value="Login" />
  </form>
  <a href="{% url 'main:register' %}">Register Now</a>
</div>
{% endblock %}
```

```python
# urls.py
urlpatterns = [
    ...
    path('login/', login_user, name='login'),
]
```

#### 3. Membuat Fungsionalitas Logout

- Buat fungsi `logout_user` untuk logout dan menghapus cookie `last_login`.
- Tambahkan routing untuk logout di `urls.py`.

```python
# views.py
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

```html
<!-- main.html -->
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

```python
# urls.py
from main.views import logout_user

urlpatterns = [
    ...
    path('logout/', logout_user, name='logout'),
]
```

#### 4. Membatasi Akses ke Halaman `main`

Tambahkan decorator `login_required` untuk membatasi akses ke halaman `main` hanya untuk pengguna yang sudah login.

```python
# views.py
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'npm': '2306165616',
        'class': 'PBP-A',
        'products': products,
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'main.html', context)
```

#### 5. Menghubungkan Model `Product` dengan `User`

Sesuaikan model `Product` untuk terhubung dengan `User` melalui `ForeignKey`, dan pastikan setiap produk terhubung ke pengguna yang membuatnya.

```python
# models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    volume = models.IntegerField()

    @property
    def price_per_ml(self):
        return self.price / self.volume if self.volume > 0 else 0
```

Tambahkan logika untuk menyimpan produk baru yang terkait dengan pengguna yang sedang login.

```python
# views.py
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    return render(request, 'create_product.html', {'form': form})
```

#### 6. Melakukan Migrasi

Membuat dan menerapkan migrasi:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Mengedit `settings.py` untuk Produksi

Tambahkan pengecekan environment production dengan menggunakan variabel `os`.

```python
# settings.py
import os

PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

#### 8. Menjalankan Server

Cek apakah semuanya aman dengan menjalankan perintah:

```bash
python manage.py runserver
```
aman:D

### Bukti Pembuatan 2 Akun & Masing-Masing 3 Data Dummy
![image](https://github.com/user-attachments/assets/adf928b2-dd0c-42e5-948f-61e39d9208d4)
![image](https://github.com/user-attachments/assets/4bf76d3f-6d51-479e-b0ce-092d1e44431a)


### Jawaban dari Pertanyaan Tugas 4
#### 1. Perbedaan antara `HttpResponseRedirect()` dengan `redirect()`
Dalam `views.py` di direktori `main`, terdapat penggunaan dari kedua fungsi tersebut.
##### Penggunaan `redirect`:
- Merupakan `function` di Django yang membantu routing menjadi lebih sederhana, dikarenakan fungsi ini langsung menerima berbagai jenis argumen seperti nama view hingga objek model. Detail URL akan diurus oleh Django.
   ```python
   def register(request):
       form = UserCreationForm()
   
       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
      ...
   ```
- Pada function `register`, digunakan `redirect()` dikarenakan saya hanya ingin langsung mengarahkan user untuk ke halaman login setelah selesai mendaftarkan akunnya. Saya tidak perlu memberikan detail URL tertentu yang tepat atau mekanisme tambahan. Kode akan jadi lebih mudah dibaca, karena fungsionalitas yang saya butuhkan hanya switch laman saja.
##### Penggunaan `HttpResponseRedirect()`
- Merupakan `kelas` di Django untuk mengembalikan respons HTTP yang juga mengarahkan pengguna ke URL tertentu secara manual. Diperlukan pemberian URL tujuan sebagai argumen. Penggunaan kelas ini membantu kontrol lebih terhadap respons HTTP, terutama jika perlu melakukan mekanisme tambahan sebelum mengirimkan respons. Jadi, yang dilakukan tidak hanya sekedar switch laman.
```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
      ...
```
- Pada function `login_user`, digunakan `HttpResponseRedirect()` dikarenakan saya ingin menambahkan cookie ke dalam respons sebelum mengembalikannya. Dengan demikian, terjadi modifikasi response sebelum dikirim balik ke pengguna (dikembalikan ke laman `show_main`), dilihat dari bagaimana kelas dipanggil dengan cara disimpan ke variabel `response` terlebih dahulu.

#### 2. Cara kerja menghubungkan model `Product` dengan `User`
- Menambahkan ForeignKey ke dalam model `Product` agar setiap produk akan terkait dengan satu pengguna dari model `User` bawaan Django. Setiap entri produk yang dibuat pengguna akan disimpan dengan informasi siapa yang membuatnya. Jika pengguna dihapus, produk yang terkait juga akan dihapus secara otomatis melalui `on_delete=models.CASCADE`
```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
- Tentu best practice e-commerce adalah menampilkan produk sesuai dengan pengguna yang sedang login. Sehingga di bagian `view`, gunakan filter untuk menampilkan produk yang hanya dimiliki oleh pengguna yang terautentikasi. Pada `show_main`, filter produk dengan `request.user`.
```python
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    ...
```
- Saat pengguna membuat produk baru, produk akan otomatis terkait dengan pengguna yang sedang login dikarenakan telah ditambahkan properti `user` pada instance produk sebelum disimpan.
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user  # Menghubungkan produk dengan user
        product.save() # Baru simpan
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```
#### 3. Implementasi authentication dan authorization oleh Django
- Autentikasi adalah proses memverifikasi identitas user. Proses ini memastikan bahwa pengguna yang mencoba mengakses aplikasi sesuai dengan 'field pengguna' yang diklaim. Proses ini biasanya meminta username dan password. Saat pengguna berhasil login, berarti proses autentikasi berhasil. 
Otorisasi adalah proses memberi izin, 'apa saja yang boleh dilakukan oleh pengguna yang sudah terautentikasi'? Otorisasi menentukan halaman atau data apa saja yang bisa diakses oleh pengguna tersebut.
- Misal, saya pernah mendaftar ke `glowify` dengan username bizarrebeam. Autentikasi akan menanyakan, 'apakah ini benar-benar bizarrebeam?'. Otorisasi, di lain sisi, akan menanyakan, 'apakah bizarrebeam berhak untuk mengakses halaman admin ecommerce, atau mengedit data produk?'
- Django menangani autentikasi dengan modul `django.contrib.auth`. Django telah menyediakan form login bawaan yang menangani pengecekan kredensial pengguna. Pada `views.py` saya:
```python
form = AuthenticationForm(data=request.POST)
if form.is_valid():
    user = form.get_user()
    login(request, user)
```
- Django menangani otorisasi dengan decorator seperti `@login_required`, sehingga hanya pengguna yang telah login yang bisa mengakses halaman tertentu. Pada `views.py` saya:
```python
@login_required(login_url='/login')
def show_main(request):
```

#### 4. Bagaimana Django mengingat pengguna yang telah login, kegunaan lain dari cookies, apakah semua cookies aman digunakan
##### Bagaimana Django mengingat pengguna yang telah login
- Setelah pengguna login, Django menggunakan sesi untuk mengingat pengguna tersebut. Informasi sesi disimpan di server. Browser pengguna hanya menyimpan session ID dalam bentuk cookie. Saat pengguna melakukan permintaan (request) ke server, browser mengirimkan session ID ini, dan Django akan mencocokkannya dengan informasi yang ada di server untuk mengidentifikasi pengguna. Proses ini terjadi setiap kali pengguna membuka halaman baru tanpa perlu login ulang.
- Setelah login, Django mengirim cookie dengan session ID ke browser. Django mengakses informasi sesi menggunakan cookie ini. Jika pengguna membuka halaman lain di situs, browser akan mengirim cookie ini dalam setiap permintaan, sehingga Django bisa mengenali pengguna yang telah login. 
- Django secara default akan mengingat pengguna selama sesi berlangsung. Jika pengguna menutup browser atau jika durasi sesi habis, pengguna harus login kembali. Namun, Django juga bisa dikonfigurasi untuk mengingat pengguna lebih lama, misalnya dengan fitur "remember me" yang membuat sesi bertahan lebih lama.
##### Kegunaan lain dari cookies
- Cookie umum diminta untuk menyimpan preferensi pengguna, seperti bahasa yang dipilih, light/dark mode.
- Cooies dapat digunakan untuk melacak aktivitas pengguna di situs web, misal mengingat halaman yang dikunjungi, atau produk yang ditambahkan ke keranjang belanja (dalam konteks ecommerce).
- Third-party cookies dapat digunakan layanan iklan untuk menampilkan iklan yang lebih personalize. Cookies ini digunakan untuk menargetkan iklan berdasarkan perilaku pengguna di internet.
- Cookies juga dapat digunakan untuk mengumpulkan data statistik tentang kunjungan pengguna, lalu digunakan untuk menganalisis performa situs web.
##### Apakah semua cookies aman digunakan
Ada beberapa hal yang harus diperhatikan, sebab belum tentu semua cookies aman jika tidak dikonfigurasi dengan baik.
- Cookies yang mengandung informasi penting, seperti session ID, harus memiliki atribut HttpOnly. Atribut ini mencegah cookies tersebut diakses oleh JavaScript, sehingga mengurangi risiko serangan cross-site scripting (XSS).
- Cookies yang dikirim melalui koneksi yang aman (HTTPS) harus diberi atribut `Secure` yang memastikan cookies hanya dikirim melalui koneksi yang terenkripsi. Tanpa atribut ini, cookies bisa dicuri jika pengguna mengakses situs melalui koneksi yang tidak aman.
- Atribut `SameSite` mencegah cookies dikirimkan dalam permintaan lintas situs, yang melindungi dari serangan cross-site request forgery (CSRF), seperti yang telah dijelaskan pada README Tugas 3.
- Cookies pihak ketiga yang digunakan untuk iklan atau pelacakan sering kali dianggap 'invasif' karena melacak aktivitas pengguna di berbagai situs, sehingga menjadi concern privasi. Beberapa browser telah mulai memblokir third-party cookies secara default.



## Tugas 5
### Implementasi Styling dan Fitur CRUD Produk

#### 1. Menambahkan Tailwind ke Aplikasi

1. File `base.html` di folder templates di root project:
   - Menambahkan tag `<meta name="viewport">` a
   - Menambahkan script CDN Tailwind di bagian `<head>`.

    ```html
    <head>
        {% block meta %}
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
        {% endblock meta %}
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    ```

#### 2. Menambahkan Fitur Edit Produk

1. File`views.py` di subdirektori main:
   - Menambahkan fungsi `edit_product`.

    ```python
    def edit_product(request, id):

		product = Product.objects.get(pk=id)
		form = ProductForm(request.POST or None, request.FILES or None, instance=product)
	
		if form.is_valid() and request.method == "POST":
			form.save()
			return HttpResponseRedirect(reverse('main:show_main'))
		
		context = {'form': form}
		return render(request, "edit_product.html", context)
    ```

2. Membuka `urls.py` di subdirektori main:
   - Menambahkan path URL untuk fungsi `edit_product`.

    ```python
    from main.views import delete_product

    urlpatterns = [
        # URL patterns lainnya
        path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    ]
    ```

2. Membuka `urls.py` di subdirektori main:
   - Menambahkan path URL untuk fungsi `delete_product`.

    ```python
    from main.views import delete_product

    urlpatterns = [
        # URL patterns lainnya
        path('delete-product/<uuid:id>', delete_product, name='delete_product'),
    ]
    ```

#### 3. Menampilkan Produk di Halaman Utama

1. Membuka `main.html` di subdirektori templates:
   - Menambahkan tabel untuk menampilkan daftar produk.
   - Menambahkan tombol untuk mengedit dan menghapus produk.

    ```html
    <table>
        <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Volume (ml)</th>
            <th>Image</th>
            <th>Actions</th>
        </tr>
        {% for product in products %}
        <tr>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.description }}</td>
            <td>{{ product.volume }}</td>
            <td>
                {% if product.image %}
                <img src="{{ product.image.url }}" alt="{{ product.name }}" style="max-width: 100px; max-height: 100px;">
                {% else %}
                <p>No image available</p>
                {% endif %}
            </td>
            <td>
                <a href="{% url 'main:edit_product' product.pk %}">
                    <button>Edit</button>
                </a>
                <a href="{% url 'main:delete_product' product.pk %}">
                    <button>Delete</button>
                </a>
            </td>
        </tr>
        {% endfor %}
    </table>
    ```

#### 4. Menambahkan Styling dengan Tailwind

1. Styling di `base.html`**:
   - Menambahkan script CDN Tailwind dan menghubungkannya dengan `global.css`.

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
      </head>
      <body>
        {% block content %} {% endblock content %}
      </body>
    </html>
    ```

2. Styling di `global.css`:
   - Menambahkan custom styling di `global.css`

3. Menambahkan styling di page lainnya:
   - `login.html`
   - `register.html`
   - `main.html`
   - `navbar.html`
   - `footer.html`
   - `card_product.html`
   - `add_product.html`
   - `edit_product.html`

#### 4. Menambahkan Navigation Bar

1. Membuat `navbar.html` di folder templates
```html
{% load static %}

<nav class="bg-[#333333] fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-14 sm:h-16 md:h-20">

	<!-- Logo Title -->
      <div class="flex items-center">
        <a href="{% url 'main:show_main' %}">
          <img src="{% static 'image/glowify-logo.png' %}" alt="glowify logo" class="h-4 sm:h-5 md:h-6">
        </a>
      </div>
      
      <!-- Navbar Links -->
      <div class="hidden md:flex items-center space-x-8">
        <a href="{% url 'main:show_main' %}" class="text-[#F5F3EE] hover:opacity-60">Home</a>
        <a href="#" class="text-[#F5F3EE] hover:opacity-60">Products</a>
        <a href="#" class="text-[#F5F3EE] hover:opacity-60">Categories</a>
        <a href="#" class="text-[#F5F3EE] hover:opacity-60">Cart</a>

        <!-- Logout Button -->
        <a href="{% url 'main:logout' %}" class="text-center border border-[#F5F3EE] hover:bg-gray-200 hover:text-[#333333] text-[#F5F3EE] font-bold py-2 px-4 rounded transition duration-300">
          Logout
        </a>
      </div>

      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 text-[#F5F3EE]" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full">
    <div class="py-2 space-y-1">
      <a href="#" class="block text-[#F5F3EE] hover:opacity-60 py-2">Home</a>
      <a href="#" class="block text-[#F5F3EE] hover:opacity-60 py-2">Products</a>
      <a href="#" class="block text-[#F5F3EE] hover:opacity-60 py-2">Categories</a>
      <a href="#" class="block text-[#F5F3EE] hover:opacity-60 py-2">Cart</a>

	<!-- Logout Button for Mobile -->
      <a href="{% url 'main:logout' %}" class="block text-center border border-[#F5F3EE] hover:bg-gray-200 hover:text-[#333333] text-[#F5F3EE] font-bold py-2 px-4 rounded transition duration-300 mt-2">
        Logout
      </a>
    </div>
  </div>
</nav>
<script>

const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});

</script>
```

#### 5. Konfigurasi Static Files

1. Di file `settings.py`:
   - Menambahkan middleware WhiteNoise.

    ```python
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',  # Tambahkan tepat di bawah SecurityMiddleware
        # Middleware lainnya
    ]
    ```

2. Konfigurasi Static Files di `settings.py`:

    ```python
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static'  # merujuk ke /static root project pada mode development
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static'  # merujuk ke /static root project pada mode production
    ```

#### 6. Menambahkan Footer

1. Membuat`footer.html` di folder templates:
```html
{% load static %}

<footer class="bg-[#333333] text-[#F5F3EE] py-6 sm:py-8 md:py-10 text-xs sm:text-sm md:text-base">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col space-y-4 sm:space-y-6 md:space-y-8">

	<!-- Logo -->
      <div class="flex justify-start">
        <img src="{% static 'image/glowify-logo.png' %}" alt="glowify logo" class="h-4 sm:h-5 md:h-6">
      </div>

      <!-- Divider -->
      <div class="w-full border-t border-[#F5F3EE]"></div>

      <!-- Links and Copyright -->
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center w-full space-y-2 sm:space-y-0">

        <!-- Copyright -->
        <div class="text-left">
          <p class="text-xs sm:text-sm md:text-base">&copy; 2024, bizarrebeams.</p>
        </div>

        <!-- Links -->
        <div class="flex flex-col sm:flex-row space-y-1 sm:space-y-0 sm:space-x-3 md:space-x-4 text-left sm:text-right">
          <a href="#" class="hover:underline text-xs sm:text-sm md:text-base">Privacy Policy</a>
          <a href="#" class="hover:underline text-xs sm:text-sm md:text-base">Terms of Service</a>
        </div>
      </div>
    </div>
  </div>
</footer>
```

#### 7. Menambahkan Card untuk Produk

1. Membuat `card_product.html` di folder templates:
```html
{% load humanize %}

<div class="bg-[#F5F5F5] p-4 sm:p-5 md:p-6 rounded shadow-md">

    <!-- Product Image -->
    <div class="bg-[#E7E5E0] p-3 sm:p-4 rounded">
        <img src="{{ product.image.url }}" class="mx-auto object-cover h-36 sm:h-44 md:h-52 w-auto" alt="{{ product.name }}">
    </div>

	<!-- Product Details -->
    <div class="text-left mt-3 sm:mt-4">
        <h3 class="text-sm sm:text-base md:text-lg text-[#333333] mb-1 sm:mb-2">{{ product.name }}</h3>
        <p class="text-xs sm:text-sm md:text-base text-[#818181] mb-2 sm:mb-3">{{ product.description }}</p>
        <p class="text-base sm:text-lg md:text-xl font-bold text-[#333333] inline-block mb-1 sm:mb-2">Rp{{ product.price|intcomma }}</p>
        <p class="text-xxs sm:text-xs md:text-sm text-[#818181] inline-block ml-1 mb-1 sm:mb-2"> /{{ product.volume }} mL</p>
    </div>

    <!-- Actions -->
    <div class="mt-2 sm:mt-3 md:mt-4 flex justify-end space-x-2 sm:space-x-3 md:space-x-4">
        <a href="{% url 'main:edit_product' product.pk %}">
            <button class="bg-[#333333] text-white py-1 sm:py-1.5 md:py-2 px-2 sm:px-3 md:px-4 text-[10px] sm:text-xs md:text-sm rounded hover:bg-[#818181] hover:text-black transition duration-300">EDIT</button>
        </a>
        <a href="{% url 'main:delete_product' product.pk %}">
            <button class="bg-[#F5F5F5] text-[#333333] border border-[#333333] py-1 sm:py-1.5 md:py-2 px-2 sm:px-3 md:px-4 text-[10px] sm:text-xs md:text-sm rounded hover:bg-[#818181] hover:text-black transition duration-300">DELETE</button>
        </a>
    </div>
</div>
```

#### 8. Menambahkan Halaman Register

1. Membuat `register.html` di folder templates:
```html
{% extends 'base.html' %}
{% load static %}
{% block meta %}

<title>Register</title>
{% endblock meta %}
{% block content %}

<div class="flex h-screen">

  <!-- Left side with image and text -->
  <div class="w-1/2 relative hidden sm:block">
    <img src="{% static 'image/login-photo.png' %}" alt="Register Photo" class="object-cover w-full h-full">
    <div class="absolute inset-0 flex justify-center items-end pb-4 sm:pb-8 md:pb-16 lg:pb-24">
      <p class="text-white text-lg sm:text-xl md:text-2xl lg:text-3xl text-center drop-shadow-md">
        Discover your radiant glow.<br>One product at a time.
      </p>
    </div>
  </div>

  <!-- Right side with register form -->
  <div class="w-full sm:w-1/2 flex flex-col justify-center items-center bg-[#F5F3EE] p-4 sm:p-8 md:p-16 lg:p-24">

    <!-- Logo -->
    <img src="{% static 'image/glowify-logo-black.png' %}" alt="Glowify Logo" class="mb-4 sm:mb-8 md:mb-16 lg:mb-24 h-6 sm:h-7 md:h-8 w-auto">

    <!-- Title -->
    <h1 class="text-[#333333] text-xl sm:text-2xl md:text-3xl font-semibold mb-4 sm:mb-6 md:mb-8">Create your account</h1>

    <!-- Register Form -->
    <form method="POST" action="" class="w-full max-w-xs sm:max-w-sm">
      {% csrf_token %}
      <div class="mb-3 sm:mb-4">
        <label for="id_username" class="block text-[#333333] text-xs sm:text-sm md:text-base mb-1 sm:mb-2">Username</label>
        <input id="id_username" name="username" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10 text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="Enter your username">
      </div>
      <div class="mb-3 sm:mb-4">
        <label for="id_password1" class="block text-[#333333] text-xs sm:text-sm md:text-base mb-1 sm:mb-2">Password</label>
        <input id="id_password1" name="password1" type="password" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10 text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="Enter your password">
      </div>

      <div class="mb-3 sm:mb-4">
        <label for="id_password2" class="block text-[#333333] text-xs sm:text-sm md:text-base mb-1 sm:mb-2">Confirm Password</label>
        <input id="id_password2" name="password2" type="password" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10 text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="Confirm your password">
      </div>

      <div class="mb-4 sm:mb-6 md:mb-8">
        <input class="btn login_btn w-full bg-[#333333] text-[#F5F3EE] py-1 sm:py-2 md:py-3 px-4 rounded transition duration-300 hover:opacity-80 text-xs sm:text-sm md:text-base cursor-pointer" type="submit" value="Register" />
      </div>
    </form>
    
    <!-- Login Link -->
    <p class="text-xs sm:text-sm md:text-base text-[#333333]">Already have an account?
      <a href="{% url 'main:login' %}" class="font-bold hover:opacity-80">Login here</a>
    </p>
  </div>
</div>

{% endblock content %}
```

#### 9. Menambahkan Halaman Edit Produk

1.  Membuat `edit_product.html` di folder templates:
```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
{% include 'navbar.html' %}

<div class="bg-[#F5F3EE] min-h-screen flex items-center justify-center py-10 sm:py-16 md:py-20 px-10 sm:px-6 lg:px-8">
  <div class="w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl bg-white shadow-md rounded-md p-4 sm:p-6 md:p-8 my-6 sm:my-8 md:my-12">
    <h1 class="text-xl sm:text-2xl md:text-3xl font-semibold text-center text-[#333333] mb-4 sm:mb-6 md:mb-8">Edit product</h1>
    <form method="POST" enctype="multipart/form-data" class="space-y-3 sm:space-y-4 md:space-y-5">
      {% csrf_token %}
      <div>
        <label for="id_name" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Product name</label>
        <input id="id_name" name="name" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="E.g. COSRX Snail Mucin" value="{{ form.name.value }}">
      </div>
      <div>
        <label for="id_price" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Price</label>
        <input id="id_price" name="price" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="In Rupiah, e.g. 150000" value="{{ form.price.value }}">
      </div>
      <div>
        <label for="id_description" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Description</label>
        <textarea id="id_description" name="description" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="E.g. An essence to calm down the skin.">{{ form.description.value }}</textarea>
      </div>
      <div>
        <label for="id_volume" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Volume</label>
        <input id="id_volume" name="volume" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="In ml, e.g. 150" value="{{ form.volume.value }}">
      </div>
      <div>
        <label for="id_image" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Product Image</label>
        <input id="id_image" name="image" type="file" class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border border-gray-300 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 text-xs sm:text-sm md:text-base bg-[#E7E5E0]">
      </div>
      <div>
        <input type="submit" value="Edit product" class="w-full bg-[#333333] text-[#F5F3EE] py-2 sm:py-2.5 md:py-3 px-4 rounded transition duration-300 hover:bg-gray-200 hover:text-black text-xs sm:text-sm md:text-base cursor-pointer mt-2 sm:mt-3 md:mt-4">

      </div>
    </form>
  </div>
</div>

{% include 'footer.html' %}

{% endblock content %}
```

#### 10. Menambahkan Halaman Tambah Produk

1.  Membuat `create_product.html` di folder templates:
```html
{% extends 'base.html' %}
{% load static %}

  
{% block content %}
{% include 'navbar.html' %}

<div class="bg-[#F5F3EE] min-h-screen flex items-center justify-center py-10 sm:py-16 md:py-20 px-10 sm:px-6 lg:px-8">
  <div class="w-full max-w-sm sm:max-w-md md:max-w-lg lg:max-w-xl bg-white shadow-md rounded-md p-4 sm:p-6 md:p-8 my-6 sm:my-8 md:my-12">
    <h1 class="text-xl sm:text-2xl md:text-3xl font-semibold text-center text-[#333333] mb-4 sm:mb-6 md:mb-8">Add a new product</h1>
    <form method="POST" enctype="multipart/form-data" class="space-y-3 sm:space-y-4 md:space-y-5">
      {% csrf_token %}
      <div>
        <label for="id_name" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Product name</label>
        <input id="id_name" name="name" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="E.g. COSRX Snail Mucin">
      </div>
      <div>
        <label for="id_price" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Price</label>
        <input id="id_price" name="price" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="In Rupiah, e.g. 150000">
      </div>
      <div>
        <label for="id_description" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Description</label>
        <textarea id="id_description" name="description" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="E.g. An essence to calm down the skin."></textarea>
      </div>
      <div>
        <label for="id_volume" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Volume</label>
        <input id="id_volume" name="volume" type="text" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border placeholder-[#818181] text-gray-900 focus:outline-none focus:ring-[#333333] focus:border-[#333333] focus:z-10text-xs sm:text-sm md:text-base bg-[#E7E5E0]" placeholder="In ml, e.g. 150">
      </div>
      <div>
        <label for="id_image" class="block text-xs sm:text-sm md:text-base text-[#333333] mb-1 sm:mb-2">Product Image</label>
        <input id="id_image" name="image" type="file" required class="appearance-none rounded-md relative block w-full px-2 sm:px-3 py-1.5 sm:py-2 md:py-3 border border-gray-300 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 text-xs sm:text-sm md:text-base bg-[#E7E5E0]">
      </div>
      <div>
        <input type="submit" value="Add product" class="w-full bg-[#333333] text-[#F5F3EE] py-2 sm:py-2.5 md:py-3 px-4 rounded transition duration-300 hover:bg-gray-200 hover:text-black text-xs sm:text-sm md:text-base cursor-pointer mt-2 sm:mt-3 md:mt-4">
      </div>
    </form>
  </div>
</div>

{% include 'footer.html' %}

{% endblock content %}
```

### Jawaban dari Tugas 5

#### 1. Urutan prioritas CSS selector
1. Inline Styles
   - CSS yang ditulis langsung pada atribut `style` di elemen HTML memiliki prioritas tertinggi.
     ```html
     <p style="color: red;">This is a paragraph.</p>
     ```

2. ID Selectors
   - Selector yang menggunakan ID memiliki prioritas lebih tinggi dibandingkan class, attribute, dan type selectors.
     ```css
     #myId {
       color: blue;
     }
     ```

3. Class, Attribute, dan Pseudo-class Selectors
   - Selector yang menggunakan class, attribute, atau pseudo-class memiliki prioritas lebih tinggi dibandingkan type selectors.
     ```css
     .myClass {
       color: green;
     }
     [type="text"] {
       color: yellow;
     }
     :hover {
       color: orange;
     }
     ```

4. Type Selectors dan Pseudo-element Selectors
   - Selector yang menggunakan type (tag) atau pseudo-element memiliki prioritas lebih rendah dibandingkan ID, class, dan attribute selectors.
     ```css
     p {
       color: purple;
     }
     ::before {
       content: "Prefix";
     }
     ```

5. Universal Selector
   - Selector yang menggunakan `*` memiliki prioritas paling rendah.
     ```css
     * {
       color: black;
     }
     ```

6. Important Rule
   - Deklarasi yang menggunakan `!important` akan mengesampingkan semua aturan lainnya, kecuali aturan lain yang juga menggunakan `!important`.
   - Contoh:
     ```css
     p {
       color: blue !important;
     }
     ```

#### 2. Responsive design
Mengapa penting? Misalkan saya tidak menerapkan responsive design pada `glowify` saya:

- Design `glowify` pada website
  <br>
  ![image](https://github.com/user-attachments/assets/051d4f19-ae0d-4156-af5a-b1135a8289c5)
  <br>
  (oke :D)

- Design `glowify` pada tab
  <br>
  ![image](https://github.com/user-attachments/assets/fc1729bc-f098-4e0c-b552-5785e192b9e6)
  <br>
  (masih boleh lah ya.... sesek dikit)

- Design `glowify` pada mobile:
  <br>
  ![image](https://github.com/user-attachments/assets/81e18c9c-6b85-4b32-9bf4-d9e49ed9cc8a)
  <br>
  (sesek bgt..... apa yang mau diliat)

##### Mengapa responsive design penting?
- Memberi pengalaman pengguna yang lebih baik
- Website dapat diakses dari berbagai jenis perangkat, mau layarnya 'besar' ataupun lebih kecil
- Hanya membuat satu website, tetapi sudah diset agar mampu menghandle display design untuk berbagai perangkat (dibandingkan membuat website untuk tipe desktop, tab, dan hp....). Pengelolaan website akan lebih mudah.

##### Contoh aplikasi yang sudah menerapkan responsive design
1. `glowify` tentunya:D
   <br>
   ![image](https://github.com/user-attachments/assets/5fbfee55-2e17-4d18-9d4a-16971b52ee1b)
   <br>
   ![image](https://github.com/user-attachments/assets/694cda18-ea99-4337-be96-fa9cae37a187)
   <br>
   ![image](https://github.com/user-attachments/assets/82b2e829-477a-492d-a47a-516d9178748a)
   <br>
2. Github
   <br>
   ![image](https://github.com/user-attachments/assets/8694a345-eecb-4eda-ab73-cdef60c254ba)
   <br>
   ![image](https://github.com/user-attachments/assets/7f5b9e77-6e05-4327-a07b-4abcd518f720)
   <br>
   ![image](https://github.com/user-attachments/assets/873795e8-deac-4da0-81a7-198e39902b99)
   <br>

##### Contoh aplikasi yang belum menerapkan responsive design 
1. SIAKNG :D
   Baru tampilan website saja, login formnya menyediakan banyak empty space yang tidak terisi. Empty space umum di login form, namun akan lebih baik jika main utility webistenya (form) diletakkan di tengah sebagai center of attention.
   <br>
   ![image](https://github.com/user-attachments/assets/8fca083c-28b6-4a5a-b23e-457386efea0b)
   <br>
   Untuk mobile screen size, pengguna harus zoom page secara manual dikarenakan teks sangat kecil.
   <br>
   ![image](https://github.com/user-attachments/assets/66144559-ba55-4aab-90e7-b421afb6b7e1)
   <br>
   Banyak space kosong tersedia di bawah, padahal design bisa dibuat agar layoutnya menyesuaikan mobile screen size
   <br>
   ![image](https://github.com/user-attachments/assets/35c2272d-b269-41d6-91b9-2f24a00c6ff5)
   <br>


#### 3. Perbedaan dan Implementasi dari Margin, Border, dan Padding
1. Margin
   - Ruang di luar elemen yang memisahkan elemen tersebut dari elemen lain di sekitarnya. Margin tidak memiliki warna atau gaya, hanya ruang kosong.
   - Digunakan untuk mengatur jarak antara elemen-elemen di halaman web.
     ```css
     .example {
       margin: 20px; /* Memberikan jarak 20px di semua sisi elemen */
     }
     ```

2. Border
   - Garis yang mengelilingi elemen. Border dapat memiliki warna, ketebalan, dan gaya (seperti solid, dashed, atau dotted).
   - Digunakan untuk memberikan batas visual pada elemen, sehingga elemen tersebut lebih menonjol atau terpisah dari elemen lain.
     ```css
     .example {
       border: 2px solid black; /* Memberikan border hitam solid dengan ketebalan 2px */
     }
     ```

3. Padding
   - Ruang di dalam elemen yang memisahkan konten elemen dari border elemen tersebut. Padding tidak memiliki warna atau gaya, hanya ruang kosong.
   - Digunakan untuk memberikan ruang di dalam elemen, sehingga konten tidak terlalu dekat dengan border.
     ```css
     .example {
       padding: 10px; /* Memberikan ruang 10px di dalam elemen di semua sisi */
     }
     ```


#### 4. Flexbox dan Grid Layout
##### Flexbox
Adalah model layout **satu dimensi** yang digunakan untuk mengatur tata letak elemen dalam satu baris atau satu kolom. Flexbox umum digunakan untuk membua layout yang responsif (mampu adjust di beda breakpoint ukuran screen) dikarenakan konsepnya berupa 'flexible box'.

Flexbox berguna untuk:
- Mengatur elemen dalam satu baris (horizontal) atau adlam satu kolom (vertikal)
- Membantu pengaturan spasi antara elemen dan perataan elemen di dalam container
- Membantu elemen untuk menyesuaikan ukuran dan posisi berdasarkan ukuran container
##### Grid Layout
Adalah model layout **dua dimensi** yang digunakan untuk mengatur tata letak elemen dalam baris dan kolom. Grid Layout sangat berguna untuk membuat tata letak yang lebih terstruktur.

Grid berguna untuk:
- Mengatur elemen dalam baris dan kolom dengan design yang lebih 'terstruktur' dikarenakan memiliki grid lines
- Mengatur ukuran dan posisi elemen dengan lebih presisi.

## Tugas 6
### Implementasi  Javascript dan AJAX

#### 1. Menambahkan Pesan Error pada Login

- Menambahkan pesan error untuk menampilkan validasi kesalahan pada form login.

```html
{% if form.errors %}
    <div class="text-red-500 text-xs mt-1">
        {{ form.errors }}
    </div>
{% endif %}
```

#### 2. Membuat Fungsi untuk Menambahkan Produk dengan AJAX

- Membuat view baru `create_product_ajax` untuk menangani permintaan POST menggunakan AJAX.

```python
@csrf_exempt
@require_POST
def create_product_ajax(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({
            "message": "Product created successfully",
            "product": {
                "id": str(product.id),
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "volume": product.volume,
                "image": product.image.url if product.image else None
            }
        }, status=201)
    else:
        return JsonResponse({"errors": form.errors}, status=400)
```

#### 3. Menambahkan Routing untuk Fungsi `create_product_ajax`

- Menambahkan path baru untuk view `create_product_ajax`.

```python
urlpatterns = [
    path('create-product-ajax', create_product_ajax, name='create_product_ajax'),
]
```

#### 4. Menampilkan Data Produk dengan fetch() API

- Membuat fungsi `refreshProducts` untuk mengambil dan menampilkan data produk menggunakan AJAX GET.

```html
<script>
    async function getProducts() {
        return fetch("{% url 'main:show_json' %}").then((res) => res.json());
    }

    async function refreshProducts() {
        const productCardsContainer = document.getElementById("product_cards");
        const products = await getProducts();
        let htmlString = "";

        if (products.length === 0) {
            htmlString = `
                <div class="col-span-full text-center py-8 sm:py-10 md:py-12">
                    <h3 class="text-lg sm:text-xl md:text-2xl font-semibold text-[#333333]">We couldn't find anything.</h3>
                    <p class="text-base sm:text-lg md:text-xl text-[#333333] mt-2">Drop yours here, one product at a time.</p>
                </div>
            `;
        } else {
            products.forEach((product) => {
                const name = DOMPurify.sanitize(product.fields.name);
                const description = DOMPurify.sanitize(product.fields.description);
                const price = DOMPurify.sanitize(product.fields.price.toString());
                const volume = DOMPurify.sanitize(product.fields.volume.toString());
                const image = product.fields.image ? DOMPurify.sanitize(product.fields.image) : '{% static "image.png" %}';

                htmlString += `
                    <div class="bg-[#F5F5F5] p-4 sm:p-5 md:p-6 rounded shadow-md">
                        <div class="bg-[#E7E5E0] p-3 sm:p-4 rounded">
                            <img src="${image}" class="mx-auto object-cover h-36 sm:h-44 md:h-52 w-auto" alt="${name}">
                        </div>
                        <div class="text-left mt-3 sm:mt-4">
                            <h3 class="text-sm sm:text-base md:text-lg text-[#333333] mb-1 sm:mb-2">${name}</h3>
                            <p class="text-xs sm:text-sm md:text-base text-[#818181] mb-2 sm:mb-3">${description}</p>
                            <p class="text-base sm:text-lg md:text-xl font-bold text-[#333333] inline-block mb-1 sm:mb-2">Rp${parseInt(price).toLocaleString()}</p>
                            <p class="text-xxs sm:text-xs md:text-sm text-[#818181] inline-block ml-1 mb-1 sm:mb-2"> /${volume} mL</p>
                        </div>
                        <div class="mt-2 sm:mt-3 md:mt-4 flex justify-end space-x-2 sm:space-x-3 md:space-x-4">
                            <a href="/edit-product/${product.pk}">
                                <button class="bg-[#333333] text-white py-1 sm:py-1.5 md:py-2 px-2 sm:px-3 md:px-4 text-[10px] sm:text-xs md:text-sm rounded hover:bg-[#818181] hover:text-black transition duration-300">EDIT</button>
                            </a>
                            <a href="/delete/${product.pk}">
                                <button class="bg-[#F5F5F5] text-[#333333] border border-[#333333] py-1 sm:py-1.5 md:py-2 px-2 sm:px-3 md:px-4 text-[10px] sm:text-xs md:text-sm rounded hover:bg-[#818181] hover:text-black transition duration-300">DELETE</button>
                            </a>
                        </div>
                    </div>
                `;
            });
        }

        productCardsContainer.innerHTML = htmlString;
    }

    refreshProducts();
</script>
```

#### 5. Membuat Modal Sebagai Form untuk Menambahkan Produk

- Menambahkan modal form untuk menambahkan produk baru menggunakan AJAX POST.

```html
<!-- Modal -->
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
  <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
    <!-- Modal header -->
    <div class="flex items-center justify-between p-4 border-b rounded-t">
      <h3 class="text-xl font-semibold text-gray-900">
        Add New Product
      </h3>
      <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Close modal</span>
      </button>
    </div>
    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
      <form id="productForm">
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700">Product name</label>
          <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="E.g. COSRX Snail Mucin" required>
        </div>
        <div class="mb-4">
          <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
          <input type="text" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="In Rupiah, e.g. 150000" required>
        </div>
        <div class="mb-4">
          <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
          <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2" placeholder="E.g. An essence to calm down the skin." required></textarea>
        </div>
        <div class="mb-4">
          <label for="volume" class="block text-sm font-medium text-gray-700">Volume</label>
          <input type="text" id="volume" name="volume" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="In ml, e.g. 150" required>
        </div>
        <div class="mb-4">
          <label for="image" class="block text-sm font-medium text-gray-700">Product Image</label>
          <input type="file" id="image" name="image" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required>
        </div>
      </form>
    </div>
    <!-- Modal footer -->
    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
      <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
      <button type="submit" id="submitProduct" form="productForm" class="bg-[#333333] hover:bg-gray-200 hover:text-black text-white font-bold py-2 px-4 rounded-lg">Save</button>
    </div>
  </div>
</div>

<script>
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        modal.classList.remove('hidden'); 
        setTimeout(() => {
            modalContent.classList.remove('opacity-0', 'scale-95');
            modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);

    document.getElementById("productForm").addEventListener("submit", async function(event) {
        event.preventDefault();
        const formData = new FormData(this);

        const response = await fetch("{% url 'main:create_product_ajax' %}", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": "{{ csrf_token }}",
            },
        });

        if (response.ok) {
            hideModal();
            refreshProducts();
            document.getElementById("productForm").reset(); 
        } else {
            const data = await response.json();
            const errors = data.errors;
            for (const [field, messages] of Object.entries(errors)) {
                const input = document.getElementById(field);
                const errorContainer = document.createElement('p');
                errorContainer.className = 'text-red-500 text-xs mt-1';
                errorContainer.innerText = messages.join(', ');
                input.parentNode.appendChild(errorContainer);
            }
        }
    });
</script>
```

#### 6. Menambahkan Data Produk dengan AJAX

- Menambahkan fungsi untuk menangani pengiriman form menggunakan AJAX POST.

```html
<script>
    document.getElementById("productForm").addEventListener("submit", async function(event) {
        event.preventDefault();
        const formData = new FormData(this);

        const response = await fetch("{% url 'main:create_product_ajax' %}", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": "{{ csrf_token }}",
            },
        });

        if (response.ok) {
            hideModal();
            refreshProducts();
            document.getElementById("productForm").reset(); 
        } else {
            const data = await response.json();
            const errors = data.errors;
            for (const [field, messages] of Object.entries(errors)) {
                const input = document.getElementById(field);
                const errorContainer = document.createElement('p');
                errorContainer.className = 'text-red-500 text-xs mt-1';
                errorContainer.innerText = messages.join(', ');
                input.parentNode.appendChild(errorContainer);
            }
        }
    });
</script>
```

#### 7. Melindungi Aplikasi dari Cross Site Scripting (XSS)

- Menggunakan DOMPurify untuk membersihkan data yang diambil dari server sebelum ditampilkan di halaman.

```html
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
<script>
    async function refreshProducts() {
        const productCardsContainer = document.getElementById("product_cards");
        const products = await getProducts();
        let htmlString = "";

        if (products.length === 0) {
            htmlString = `
                <div class="col-span-full text-center py-8 sm:py-10 md:py-12">
                    <h3 class="text-lg sm:text-xl md:text-2xl font-semibold text-[#333333]">We couldn't find anything.</h3>
                    <p class="text-base sm:text-lg md:text-xl text-[#333333] mt-2">Drop yours here, one product at a time.</p>
                </div>
            `;
        } else {
            products.forEach((product) => {
                const name = DOMPurify.sanitize(product.fields.name);
                const description = DOMPurify.sanitize(product.fields.description);
                const price = DOMPurify.sanitize(product.fields.price.toString());
                const volume = DOMPurify.sanitize(product.fields.volume.toString());
                const image = product.fields.image ? DOMPurify.sanitize(product.fields.image) : '{% static "image.png" %}';

                htmlString += `
                    <div class="bg-[#F5F5F5] p-4 sm:p-5 md:p-6 rounded shadow-md">
                        <div class="bg-[#E7E5E0] p-3 sm:p-4 rounded">
                            <img src="${image}" class="mx-auto object-cover h-36 sm:h-44 md:h-52 w-auto" alt="${name}">
                        </div>
                        <div class="text-left mt-3 sm:mt-4">
                            <h3 class="text-sm sm:text-base md:text-lg text-[#333333] mb-1 sm:mb-2">${name}</h3>
                            <p class="text-xs sm:text-sm md:text-base text-[#818181] mb-2 sm:mb-3">${description}</p>
                            <p class="text-base sm:text-lg md:text-xl font-bold text-[#333333] inline-block mb-1 sm:mb-2">Rp${parseInt(price).toLocaleString()}</p>
                            <p class="text-xxs sm:text-xs md:text-sm text-[#818181] inline-block ml-1 mb-1 sm:mb-2"> /${volume} mL</p>
                        </div>
                        <div class="mt-2 sm:mt-3 md:mt-4 flex justify-end space-x-2 sm:space-x-3 md:space-x-4">
                            <a href="/edit-product/${product.pk}">
                                <button class="bg-[#333333] text-white py-1 sm:py-1.5 md:py-2 px-2 sm:px-3 md:px-4 text-[10px] sm:text-xs md:text-sm rounded hover:bg-[#818181] hover:text-black transition duration-300">EDIT</button>
                            </a>
                            <a href="/delete/${product.pk}">
                                <button class="bg-[#F5F5F5] text-[#333333] border border-[#333333] py-1 sm:py-1.5 md:py-2 px-2 sm:px-3 md:px-4 text-[10px] sm:text-xs md:text-sm rounded hover:bg-[#818181] hover:text-black transition duration-300">DELETE</button>
                            </a>
                        </div>
                    </div>
                `;
            });
        }

        productCardsContainer.innerHTML = htmlString;
    }

    refreshProducts();
</script>
```

#### 8. Membersihkan Data dengan DOMPurify
- Menggunakan DOMPurify untuk membersihkan data yang diambil dari server sebelum ditampilkan di halaman.

```html
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
<script>
    async function getProducts() {
        return fetch("{% url 'main:show_json' %}").then((res) => res.json());
    }

    async function refreshProducts() {
        const productCardsContainer = document.getElementById("product_cards");
        const products = await getProducts();
        let htmlString = "";

        if (products.length === 0) {
            htmlString = `
                <div class="col-span-full text-center py-8 sm:py-10 md:py-12">
                    <h3 class="text-lg sm:text-xl md:text-2xl font-semibold text-[#333333]">We couldn't find anything.</h3>
                    <p class="text-base sm:text-lg md:text-xl text-[#333333] mt-2">Drop yours here, one product at a time.</p>
                </div>
            `;
        } else {
            products.forEach((product) => {
                const name = DOMPurify.sanitize(product.fields.name);
                const description = DOMPurify.sanitize(product.fields.description);
                const price = DOMPurify.sanitize(product.fields.price.toString());
                const volume = DOMPurify.sanitize(product.fields.volume.toString());
                const image = DOMPurify.sanitize(product.fields.image || '{% static "image.png" %}');

                ...
</script>
```

### Jawaban dari Tugas 6
#### 1. Manfaat penggunaan JavaScript dalam web development
- Membuat halaman web menjadi lebih interaktif. Misalnya, di `glowify`, JS digunakan untuk membuka dan menutup modal form saat menambahkan produk baru.

    ```html
    <script>
        function showModal() {
            document.getElementById('crudModal').classList.remove('hidden');
        }

        function hideModal() {
            document.getElementById('crudModal').classList.add('hidden');
        }
    </script>
    ```

-  AJAX (Asynchronous JavaScript and XML) membantu mengambil dan mengirim data ke server tanpa perlu me-refresh halaman. 
    ```html
    <script>
        async function refreshProducts() {
            const response = await fetch('/path/to/api');
            const products = await response.json();
            // Menampilkan produk di halaman
        }
    </script>
    ```

- JS membantu validasi form di sisi klien sebelum data dikirim ke server. Di `glowify`, dapat dipastikan dulu bahwa semua field diisi dengan benar sebelum mengirim data produk baru.

    ```html
    <script>
        document.getElementById("productForm").addEventListener("submit", function(event) {
            event.preventDefault();
            // Validasi form di sini
            // Jika valid, kirim data ke server
        });
    </script>
    ```

- JS membuat pengalaman pengguna yang lebih responsif. Misalnya, di `glowify`, setelah produk baru ditambahkan, daftar produk diperbarui secara otomatis tanpa perlu me-refresh halaman. Dari sisi penggunaan akan terasa lebih responsif dan mudah digunakan.

#### 2. Fungsi `await` ketika menggunakan `fetch`
Fungsi adalah untuk menunggu hingga permintaan HTTP selesai dan responsnya diterima sebelum melanjutkan eksekusi kode berikutnya. Dalam `glowify`, misalnya saat mengambil data produk dari server, gunakan `await` agar JavaScript menunggu hingga data produk benar-benar diterima sebelum mencoba memproses dan menampilkan data tersebut di halaman.

Jika tidak menggunakan `await`, maka JavaScript tidak akan menunggu respons dari `fetch()` dan langsung melanjutkan eksekusi kode berikutnya. Program berpotensi mencoba memproses data yang belum diterima, yang akan menyebabkan kesalahan atau data yang tidak lengkap ditampilkan. Misalnya, di `glowify`, jika tidak menggunakan `await` saat mengambil data produk, program mencoba menampilkan daftar produk sebelum data tersebut benar-benar tersedia, sehingga halaman bisa menampilkan data yang kosong atau tidak lengkap.

 `await` memastikan bahwa data produk sudah siap sebelum ditampilkan, sehingga pengalaman pengguna menjadi lebih baik.

#### 3. Mengapa diperlukan _decorator_ `csrf_exempt` pada _view_ yang akan digunakan untuk AJAX `POST`
Dikarenakan decorator ini menonaktifkan perlindungan CSRF (Cross-Site Request Forgery) untuk view tersebut. Dalam `glowify`, misalnya saat membuat view untuk menambahkan produk baru menggunakan AJAX POST, gunakan `csrf_exempt` agar permintaan AJAX dari klien dapat diterima oleh server tanpa memerlukan token CSRF.

CSRF adalah jenis serangan di mana penyerang dapat membuat permintaan yang tidak sah atas nama pengguna yang sah (seperti penjelasan pada Tugas 2). Django secara default melindungi aplikasi dari serangan ini dengan memeriksa token CSRF pada setiap permintaan POST. Namun, ketika menggunakan AJAX untuk mengirim data, token CSRF mungkin tidak selalu tersedia atau dikirim dengan benar, terutama jika tidak dikonfigurasi dengan benar di JavaScript.

`csrf_exempt`menonaktifkan pemeriksaan token CSRF untuk view tertentu, sehingga permintaan AJAX dapat diterima tanpa masalah. Menonaktifkan perlindungan CSRF dapat membuka celah keamanan jika tidak digunakan dengan hati-hati. Oleh karena itu, perlu dipastikan bahwa view yang menggunakan `csrf_exempt` hanya menerima permintaan dari sumber yang tepercaya.

#### Mengapa pembersihan data _input_ pengguna dilakukan di belakang (_backend_) juga, tidak dilakukan di _frontend_ saja?
Untuk memastikan bahwa data yang diterima oleh server adalah valid dan aman. Dalam `glowify`, pembersihan data digunakan untuk mencegah serangan seperti Cross-Site Scripting (XSS) seperti yang dijelaskan pada tutorial. tidak hanya sekedar tampilan frontend, tetapi juga memastikan bahwa data yang disimpan di database (sisi yang diurusi backend) adalah data yang sesuai dengan yang diharapkan.

Misalnya, ketika pengguna mengirimkan data produk baru melalui form, data tersebut akan diproses oleh view di backend. Di sini, Django Forms digunakan untuk memvalidasi dan membersihkan data input. Django Forms secara otomatis akan memeriksa apakah data yang dimasukkan sesuai dengan tipe data yang diharapkan dan akan membersihkan data dari karakter-karakter yang tidak diinginkan.

Contoh pada `glowify` adalah ketika pengguna menambahkan produk baru melalui form. Data yang dikirimkan oleh pengguna akan diterima oleh view `create_product_ajax`. Di view ini,  `ProductForm` akan memvalidasi dan membersihkan data. Jika data valid, produk akan disimpan ke dalam database. Jika tidak, pesan error akan dikembalikan ke pengguna.

```python
@csrf_exempt
@require_POST
def create_product_ajax(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({"message": "Product created successfully"}, status=201)
    else:
        return JsonResponse({"errors": form.errors}, status=400)
```



   


   
