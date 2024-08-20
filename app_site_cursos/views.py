from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_cursos(request):
    return render(request, 'cursos/add_cursos.html')

def popup_view(request):
    return render(request, 'popup/popup_content.html')
