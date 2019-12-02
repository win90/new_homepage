import requests
import random
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
# from .model import Contact




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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=100)
    Message = forms.CharField(widget=forms.Textarea)

    
    




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
    context = {}
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']


        if '@' not in email:
            context['error_message'] = 'bad email'
            return render(request, 'add_sitter.html', context)

        if len(phone) < 9:
            context['error_message'] = 'phone number is too short'
            return render(request, 'add_sitter.html', context)

        if '-' not in phone:
            context['error_message'] = 'phone number is weird'
            return render(request, 'add_sitter.html', context)

        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            phone=phone,
        )

        
    return render(request,'contact.html',context)



def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

