from django.shortcuts import render

# Create your views here.


def helloDjango(request):

    return render(request, 'hello.html')

def hellopython(request):

    return render(request,'why.html')