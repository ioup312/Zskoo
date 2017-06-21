from django.shortcuts import render

# Create your views here.

def main(request):
    context = 'lalalalalal'
    return render(request,'index.html',{'zhaoxu':context})
