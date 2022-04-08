from django.shortcuts import render


def home_view(request):
    context = {
    'salom' : "Assalomu alaykum"
    }
    return render(request, 'index.html', context)