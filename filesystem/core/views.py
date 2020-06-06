from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.core.files.storage import FileSystemStorage

# Create your views here.
def HomeView(request):
    if request.user.is_authenticated:
        documents = Document.objects.all()
        return render(request, 'home.html', {
            'documents': documents
        })
    else: 
        return redirect('/accounts/login/')

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def upload1(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
    return render(request, 'upload.html')
