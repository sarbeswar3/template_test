from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'webapp/home.html')

# about
def about(request):
    return render(request, 'webapp/about.html')

# contact
def contact(request):
    return render(request, 'webapp/contact.html')
