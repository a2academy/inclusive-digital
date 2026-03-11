from django.shortcuts import render


def home(request):
    """Home page with SafeGuard AI overview."""
    return render(request, 'website/home.html')
