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




   


   
