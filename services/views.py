from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request,'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    font = request.GET.get('font')
    string = request.GET.get('string')
    context = {'print': requests.get('http://artii.herokuapp.com/make?text={}&font={}'.format(string,font)).text}
    return render(request, 'services/artii_result.html', context)

# import sys
# sys.stdin.readline()
# => input() 