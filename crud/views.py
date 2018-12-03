from django.shortcuts import render, redirect
from crud.forms import CollageForm
from formexample.models import Collage
from django.db.transaction import connections
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def create(request):

    form = CollageForm()

    if request.method == 'POST':
        form = CollageForm(request.POST)

        if form.is_valid():
            #form.save()
            collage = Collage()
            collage.collage_name = form.cleaned_data['collage_email'].split('@')[0]
            collage.collage_email = form.cleaned_data['collage_email']
            collage.collage_address = form.cleaned_data['collage_address']
            collage.collage_city = form.cleaned_data['collage_city']
            collage.save()
            return redirect(index)
    return render(request,'crud/create.html',{'form':form})

def update(request):
    id = request.GET['id']
    data = Collage.objects.get(id=id)
    form = CollageForm(instance=data)

    if request.method == 'POST':
        form = CollageForm(request.POST,instance=data)
        if form.is_valid():
            #form.save()
            collage = Collage()
            collage.id = id
            collage.collage_name = form.cleaned_data['collage_email'].split('@')[0]
            collage.collage_email = form.cleaned_data['collage_email']
            collage.collage_address = form.cleaned_data['collage_address']
            collage.collage_city = form.cleaned_data['collage_city']
            print(form.cleaned_data)
            collage.save()
            return redirect(index)
    return render(request, 'crud/update.html', {'form': form})


def delete(request):
    id = request.GET['id']
    data = Collage.objects.get(id=id)
    data.delete()
    return redirect(index)

def view(request):
    id = request.GET['id']
    print(id)
    data = Collage.objects.get(id=id)
    return render(request, 'crud/view.html',{'data':data})

@login_required(login_url='/login')
def index(request):

    data = Collage.objects.all()
   #data = Collage.objects.raw("select * from collage")(in case for raw queries)
    return render(request, 'crud/index.html', {'data':data})