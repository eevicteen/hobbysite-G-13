from django.shortcuts import render

# Create your views here.
def home_view(request):
    apps = {
        'merchstore':[
            {'name':'merchstore',
             'url':'merchstore:product-list'
             }
        ],
        'wiki':[
            {'name':'wiki',
             'url':'wiki:articles_list'
             }
        ],
        'blog':[
            {'name':'blog',
             'url':'blog:blog_list'
             }
        ],
        'commissions':[
            {'name':'commissions',
             'url':'commissions-list'
             }
        ],
    }
