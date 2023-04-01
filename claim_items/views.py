from django.shortcuts import render,HttpResponse
from search.models import LostItem
from .forms import ContactForm
from .models import Contact
# Create your views here.

def render_lost_Items(request):
    lost_items = LostItem.objects.all()
    return render(request,'claim/claimItems.html',{'lostitems':lost_items})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact object and save it to the database
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                description=form.cleaned_data['description'],
                location=form.cleaned_data['location'],
            )
            contact.save()
            # Redirect to the success page
            return render(request, 'claim/claim_successful.html')
    else:
        form = ContactForm()
    return render(request, 'claim/claim_form.html', {'form': form})