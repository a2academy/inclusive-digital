import json
from django.shortcuts import render

from .quiz_data import get_quiz_by_category


def home(request):
    """Home page with SafeGuard AI overview."""
    return render(request, 'website/home.html')


def check_message(request):
    """Multi-modal scam detection - text, screenshot, voice, URL."""
    return render(request, 'website/check_message.html')


def scam_academy(request):
    """Interactive quiz: users pick a scam category, then answer questions for that topic."""
    quiz_by_category = get_quiz_by_category()
    quiz_by_category_json = json.dumps(quiz_by_category)
    return render(request, 'website/scam_academy.html', {'quiz_by_category_json': quiz_by_category_json})


def emergency_help(request):
    """Emergency 'I Need Help' panic button module."""
    return render(request, 'website/emergency_help.html')


def family_link(request):
    """Family Link / Trusted Contact dashboard."""
    return render(request, 'website/family_link.html')


def official_verification(request):
    """Official verification directory - IRS, SSA, banks."""
    return render(request, 'website/official_verification.html')
