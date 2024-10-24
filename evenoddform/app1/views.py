from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    print(request.GET)
    if request.method=="POST":
        a=int(request.POST.get('num'))
        if a%2==0:
            result=True
        else:
            result=False

    return render(request,'index.html',{'res':result})
