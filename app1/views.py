from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,'index.html', {'form':'django','link':'https://www.google.co.in/'})


# def Profile(request):
#     return HttpResponse("Profiel page")

def expretion(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = a + b
    return render(request,'output.html',{'return':c})
