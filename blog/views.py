
# Create your views here.
from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse



# Create your views here.
#creating function home to handle the traffic from home page
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)
    #render object takes request as first argument second argument template name

def about(request):
    return render(request,"blog/about.html", {'title':"About"}
    
    )
 
#blog -> templates -> blog -> template.html

