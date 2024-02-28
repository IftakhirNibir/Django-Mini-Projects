from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        a = request.POST.get('text1','')
        b = request.POST.get('text2','')
        c = request.POST.get('text3','')
        d = request.POST.get('text4','')
        e = request.POST.get('text5','')
        f = request.POST.get('text6','')
    else:
        a = b = c = d = e = f = ''
    context = {
        'A' : a,
        'B' : b,
        'C' : c,
        'D' : d,
        'E' : e,
        'F' : f,
    }
    return render(request,'index.html',context)