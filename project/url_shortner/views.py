from random import random
from django.shortcuts import redirect, render
import random
from url.models import Url

def index(request):
    if request.method == "POST":
        link = request.POST.get("link")
        
        short_link= ""
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']

        for i in range(1,7):
            latters = random.randint(1,len(alpha) + 1)

            let = alpha[latters]
            short_link += let
        print(short_link)
        print(link)

        url = Url(link=link,short_link = short_link)
        url.save()


    return render(request,"index.htm")

def shorten(request,id):
    url = Url.objects.filter(short_link = id)
    link = ""
    for i in url:
        link = i.link
    return redirect(link)