from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
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


def show_profile(request):

    profile=Contact.objects.all()
    return render(request,'claim/show_claimers.html',{'Profile':profile})


#Extra code --Edit later ---url comment out also ---
def delete_item(request, item_id):
    item = get_object_or_404(Contact, id=item_id)
    item.delete()
    return redirect('profile-show') 



def edit_item(request, item_id):
    item = get_object_or_404(Contact, id=item_id)

    if request.method == 'POST':
        form = Contact(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('profile-show')
    else:
        form = Contact(instance=item)

    return render(request, 'claim/edit_item.html', {'form': form})
