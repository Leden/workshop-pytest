from django.shortcuts import render

from .forms import ShortUrlForm


def shorten(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
    else:
        form = ShortUrlForm()

    return render('shorts/index.html', {'form': form})
