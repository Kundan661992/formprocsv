from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from first.forms import DeveloperForm
from first.function import handle_uploaded_file


def index(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('File Uploaded successfully')

        '''try:
            return redirect('/')
        except:
            pass'''
    else:
        form = DeveloperForm()
    return render(request, 'index.html', {'form': form})
