from django.shortcuts import render

# Create your views here.
def student_info(request):

    d1={

        'name':'xyz',
        'email':'xyz@gmail.com',
        'l1':[1,2,3,4,5],
        'd2':{'city':'banglore','address':'btm'}
    }
    return render(request, 'studentinfo.html',d1)