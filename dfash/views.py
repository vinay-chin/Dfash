from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def started(request):
    return render(request, 'inner-page.html')