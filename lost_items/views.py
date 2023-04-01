from django.shortcuts import render, get_object_or_404,redirect
from .models import LostItem
from .forms import LostItemForm
from django.contrib import messages

def lost_item_detail(request, id):
    lost_item = get_object_or_404(LostItem, id=id, owner=request.user)
    form = LostItemForm(instance=lost_item)
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES, instance=lost_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lost item report updated successfully.')
            return redirect('lost_item_detail', id=id)
    return render(request, 'lost_items/detail.html', {'lost_item': lost_item, 'form': form})


def search(request):
    lost_items = LostItem.objects.filter(is_found=False)
    # Apply filters based on user inputs
    return render(request, 'lost_items/search.html', {'lost_items': lost_items})

def search_results(request):
    query = request.GET.get('q')
    lost_items = LostItem.objects.filter(name__icontains=query, is_found=False)
    return render(request, 'lost_items/search_results.html', {'lost_items': lost_items})

