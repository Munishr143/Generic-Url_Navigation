from django.shortcuts import render

# Create your views here.
def Url(request):
    return render(request, 'url_nav.html')


def Url2(request):
    return render(request, 'munish.html')