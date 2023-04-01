from django.shortcuts import render,HttpResponse,redirect
from .forms import ContactForm
# Create your views here.
from search.models import FoundItem,LostItem,Category

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

def test(request):
    if request.method=="POST":
      form=ContactForm(request.POST)

      if form.is_valid():
          name=form.cleaned_data['name']
          email=form.cleaned_data['email']
          content=form.cleaned_data['content']
          items_name=FoundItem.objects.all().values()

          #item_location=FoundItem.objects.values_list('location', flat=True)
          #item_description=FoundItem.objects.values_list('description', flat=True)
          html=render_to_string('notification/email.html',{
              'name':name,
              'email':email,
              'content':items_name
              
              
          })
      send_mail(
         'Subject-Testing',
         'Body',
         'akaikobad6716@gmail.com',
         [email],
         html_message=html)
      return redirect ('notification')
       
    else:
          form=ContactForm()

    return render(request,'notification/base.html',{'form':form})

def success(request):


      send_mail(
         'Subject-Testing',
         'ANy default message',
         'akaikobad6716@gmail.com',
         ['abrahamkaikobad@gmail.com'],
      )
      return render(request,'notification/email.html')
   


