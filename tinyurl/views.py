from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm, SearchForm
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# @method_decorator(login_required, name='dispatch')
class index(View):
    template_name = 'tinyurl/home.html'
    form_class = ShortenerForm

    def get(self, request):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            shortened_object = form.save(commit=False)
            if request.user.is_authenticated:
                shortened_object.user_name = request.user
            shortened_object.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
        else:
            context['errors'] = form.errors
        return render(request, self.template_name, context)


def redirect_url(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
    except Shortener.DoesNotExist:
        return render(request, 'tinyurl/404.html', status=404) # Custom 404 Errors

def myurls(request):
    template = 'tinyurl/myurls.html'
    context = {}
    # Process the search form
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        # Filter the queryset based on the search query
        if query:
            all_urls = Shortener.objects.filter(user_name=request.user).filter(url_index__icontains=query) | Shortener.objects.filter(user_name=request.user).filter(long_url__icontains=query) | Shortener.objects.filter(user_name=request.user).filter(short_url__icontains=query)
        else:
            all_urls = Shortener.objects.filter(user_name=request.user)
    else:
        all_urls = Shortener.objects.filter(user_name=request.user)
    context['search_form'] = search_form
    context['myurls'] = all_urls
    return render(request, template, context)

def delete_item(request, id):
    itm = Shortener.objects.get(id=id)
    if request.method == 'POST':
        itm.delete()
        return redirect('myurls')
    context = {'itm': itm}
    return render(request, 'tinyurl/delete.html', context)
