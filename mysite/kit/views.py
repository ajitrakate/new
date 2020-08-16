from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Node

# Create your views here.
def home(request):
    k = Node.objects.all()
    l=k[0]
    g = l.light1_status
    f = open('kit/static/kit/kit.txt', "w")
    f.write(g)
    print(l)
    param = {"l":l}
    return render(request, 'kit/base.html', param)
    

def change(request):
    j = request.POST['kitnum']
    k = Node.objects.all()
    l=k[0]
    print(j)
    if j == "Room1":
        g = l.light1_status
        print(g)
        if g == "ON":
            l.light1_status = "OFF"
            l.save()
        elif g == "OFF":
            l.light1_status = "ON"
            l.save()
        else:
            print("Something went wrong inside")
    elif j == "Room2":
        g = l.light2_status
        print(g)
        if g == "ON":
            l.light2_status = "OFF"
            l.save()
        elif g == "OFF":
            l.light2_status = "ON"
            l.save()
        else:
            print("Something went wrong inside") 
    else:
        print("Something went wrong outside")

    param = {"l": l}
    return HttpResponseRedirect(reverse('kit:home'))