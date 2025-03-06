from django.http import HttpResponse
from django.shortcuts import render
from django import utils


def index(request):

    return render(request, "index.html",)



def aboutus(request):
   

    return render(request,"about.html",)

def service(request):
    return render(request,"service.html")

def team(request):
    
    return render(request,"team.html",)

def testimonial(request):
    return render( request,"testimonial.html")

def room(request):
   
    return render(request,"room.html",)

def contact(request):
    # if request.method == "POST":
    #     Name = request.POST.get("name")
    #     Email = request.POST.get("email")
    #     Subject = request.POST.get("subject")
    #     Message = request.POST.get("message")
    #     formData = ContactForm(NAME=Name,EMAIL=Email,SUBJECT=Subject,MESSAGE=Message)
    #     formData.save()
    return render(request, "contact.html")

def booking(request):
    return render(request, "booking.html")