from django.shortcuts import render
from formexample.forms import FormExample
# Create your views here.

def staticExample(request):
    return render(request, 'static_example.html')


def form_example(request):
    formobj =  FormExample()
    #print(request.POST)
    #print(request.GET)
    if request.method =='POST':
        formobj=FormExample(request.POST)

        if formobj.is_valid():
            print(request.POST)
            pass

    return render(request,'form_example.html', {'form':formobj})
