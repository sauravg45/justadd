from django.shortcuts import render
from django.utils import timezone
from .forms import PostForm
from .models import Advertise
def post_list(request):
    adverts = Advertise.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'advert/post_list.html', {'adverts':adverts})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.brand = request.user
            advert.published_date = timezone.now()
            advert.save()
    else:
        form = PostForm()
    return render(request, 'advert/post_edit.html', {'form': form})
# Create your views here.
