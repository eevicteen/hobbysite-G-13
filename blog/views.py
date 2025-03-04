from django.shortcuts import render

def blog_list(request):
    blog = Blog.objects.all()
    ctx = {
        "blogs": blog,

    }
    return render(request, 'blog_list.html', ctx)


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    ctx = {
        "blog": blog
    }
    return render(request, 'blog_details.html', ctx)
