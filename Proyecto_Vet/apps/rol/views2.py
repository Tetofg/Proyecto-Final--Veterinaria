from django.shortcuts import render

def adminlte(request):
    return render(request, "rol/top-nav.html")