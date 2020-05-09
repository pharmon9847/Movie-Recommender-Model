from django.shortcuts import render
from django.http import HttpResponse
from .forms import movie_choices_form

# Create your views here.
def movies(request):
    form = movie_choices_form()

    if request.method == 'POST':
        print(request.POST)
        form = movie_choices_form(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form':form,
    }
    return render(request,'index.html',context)