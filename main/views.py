from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Adelya Amanda',
        'npm': '2306165616',
        'class': 'PBP-A'
    }

    return render(request, "main.html", context)
