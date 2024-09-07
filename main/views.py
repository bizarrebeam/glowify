from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165616',
        'name': 'Adelya Amanda',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
