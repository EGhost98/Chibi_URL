from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Shortener
from .forms import ShortenerForm, SearchForm
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class IndexView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    template_name = 'tinyurl/home.html'
    form_class = ShortenerForm
    def get(self, request):
        context = {'form': self.form_class()}
        if request.user.is_authenticated:
            cache_key = f"last4:{request.user.id}"
            last_entries = cache.get(cache_key)
            if not last_entries:
                last_entries = Shortener.objects.filter(user_name=request.user).order_by('-created')[:3]
                cache.set(cache_key, last_entries)
            context['last4'] = last_entries
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            shortened_object = form.save(commit=False)
            if request.user.is_authenticated:
                shortened_object.user_name = request.user
            if shortened_object.url_alias:
                if Shortener.objects.filter(url_alias=shortened_object.url_alias).exists():
                    form.errors.setdefault('url_alias', ErrorList()).append("URL Alias Already Exists.")
                else:
                    shortened_object.short_url = shortened_object.url_alias

            if not form.errors:
                shortened_object.save()
                context['cur'] = shortened_object
        else:
            context['errors'] = form.errors
        if request.user.is_authenticated:
            cache_key = f"last4:{request.user.id}"
            cache.delete(cache_key) 
            if not form.errors:
                last_entries = Shortener.objects.filter(user_name=request.user).order_by('-created')[1:4]
                cache.set(cache_key, last_entries)
            else:
                last_entries = Shortener.objects.filter(user_name=request.user).order_by('-created')[:3]
                cache.set(cache_key, last_entries)
            context['last4'] = last_entries
        return render(request, self.template_name, context)


def redirect_url(request, shortened_part):
    cache_key = f"short_url:{shortened_part}"
    cached_url = cache.get(cache_key)
    if cached_url:
        return HttpResponseRedirect(cached_url)
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1
        shortener.save()
        cache.set(cache_key, shortener.long_url)
        return HttpResponseRedirect(shortener.long_url)
    except Shortener.DoesNotExist:
        return render(request, 'tinyurl/404.html', status=404)


@login_required
def myurls(request):
    template = 'tinyurl/myurls.html'
    context = {}
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            all_urls = Shortener.objects.filter(user_name=request.user).filter(url_index__icontains=query) | Shortener.objects.filter(user_name=request.user).filter(long_url__icontains=query) | Shortener.objects.filter(user_name=request.user).filter(short_url__icontains=query)
        else:
            all_urls = Shortener.objects.filter(user_name=request.user)
    else:
        all_urls = Shortener.objects.filter(user_name=request.user)

    # Pagination
    paginator = Paginator(all_urls, 6) 
    page_number = request.GET.get('page')
    urls_page = paginator.get_page(page_number)
    context['search_form'] = search_form
    context['myurls'] = urls_page
    return render(request, template, context)


@login_required
def delete_item(request, id):
    itm = Shortener.objects.get(id=id)
    if request.method == 'POST':
        if request.user.is_superuser or request.user == itm.user_name:
            itm.delete()
            return redirect('myurls')
        else:
            return render(request,'tinyurl/403.html',status=403)  # Return 403 Forbidden response
    context = {'itm': itm}
    return render(request, 'tinyurl/delete.html', context)


@cache_page(CACHE_TTL)
def about_Chibi(request):
    return render(request,'tinyurl/abt.html')

@cache_page(CACHE_TTL)
def handler404(request, exception):
    return render(request, 'tinyurl/404.html', status=404)