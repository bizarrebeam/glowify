from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'sebuah barang',
        'price': '10',
        'description': 'oke bgt'
    }

    return render(request, "main.html", context)
