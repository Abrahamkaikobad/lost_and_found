from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import FoundItem, LostItem, Category
from django.db.models import Q

# Create your views here.


def home(request):
   return HttpResponse("Home_Filter")


class SearchView(TemplateView):
    template_name = "search/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        print(kw)
        if kw:
         results = FoundItem.objects.filter(Q(name__icontains=kw) | Q(
             description__icontains=kw) | Q(location__icontains=kw))
         context['results'] = results
        else:
          print("Nothing")
        return context




def filter(request, category_id):
    category = Category.objects.get(id=category_id)
    lostitem = LostItem.objects.filter(category=category)
    data = {"lostitem": lostitem, "category": Category.objects.all()}
    return render(request, 'search/filter.html', data)
