from django.urls import reverse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    apps = [
        {'name': 'Merchstore',
         'url': reverse('merchstore:product-list'),
         'image_url': 'home/images/bryce.jpg',
         'creator': 'BRYCE RIVERO'
         },
        {'name': 'Wiki',
         'url':  reverse('wiki:article_list'),
         'image_url': 'home/images/lego.jpg',
         'creator': 'LEGO SAMILLANO'
         },
        {'name': 'Blog',
         'url': reverse('blog:blog_list'),
         'image_url': 'home/images/syd.jpg',
         'creator': 'SYD PAGUIO'
         },
        {'name': 'Commissions',
         'url': reverse('commissions:commissions-list'),
         'image_url': 'home/images/bayani.jpg',
         'creator': 'ROUEL BERNOS'
         },
    ]
    honorable_mentions = {
        'name':'FRANCISCO LEGASPI',
        'image_url':'home/images/chino.jpg',
    }
    banner_url = 'home/images/ctc.jpg'
    ctx = {
        'apps':apps,
        'honorable_mentions':honorable_mentions,
        'banner_url': banner_url
    }

    return render(request,'home.html',ctx)

