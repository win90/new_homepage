import requests
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     # This is similar to ones we have done before. Instead of keeping
#     # the HTML / template in a separate directory, we just reply with
#     # the HTML embedded here.
#     return HttpResponse('''
#         <h1>Welcome to my home page!</h1>
#         <a href="/my-blog">My Blog</a> <br/>
#         <a href="/my-projects">My Projects</a><br/>
#         <a href="/contact-me">Contact me</a> <br />
        
#     ''')



def base (request):
    # content_html = open ('contact.html').read()
    context = {
        # "contact":content_html
    }

    return render (request,'base.html',context)

def blog(request):
    # content_html = open("blog.html").read()
    context = {
        # "content": content_html

    }
    return render(request, 'blog.html', context)

def projects(request):
    context = {

    }
    return render(request,'projects.html',context)

def contact(request):
    context = {

    }
    return render(request,'contact.html',context)



def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

