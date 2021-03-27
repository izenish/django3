from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html',{"password":"randomNumbersandcharactersinrandomsequence"})

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')

    len=int(request.GET.get('length',12))
    #('length',x)---> here x is the default value if none is received
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('specicalCharacters'):
        characters.extend(list('!"#$%&()*+,-./:;<=>?@[]^_`{|}~'))
    
    if request.GET.get('number'):
        characters.extend(list('0123456789'))


    key=''
    for x in range(len):
        key+=random.choice(characters)
    return render(request, 'generator/password.html',{'password':key})
    

def about(request):
    return render(request,'generator/about.html')