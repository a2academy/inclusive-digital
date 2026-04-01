# SafeGuard AI — Inclusive Digital Protection

**Youth & AI Innovation Summit 2026**

This repository is a **Python [Django](https://www.djangoproject.com/)** web application. The server renders HTML with Django templates, routes every URL through Django’s URLconf and views, and serves static assets (CSS, JavaScript) via Django’s static files system. There is no separate frontend framework; the UI is Django templates plus browser JavaScript for OCR, speech, and client-side checks.

An AI-powered security suite designed to bridge the digital safety gap for seniors and persons with disabilities. By combining real-time scam detection with advanced accessibility features, SafeGuard AI empowers vulnerable populations to navigate the digital world without fear of financial exploitation.

## Tech Stack

| Layer | Technology |
|--------|------------|
| **Web framework** | **Django 5.x** (`manage.py`, `safeguard_ai/settings.py`, WSGI/ASGI) |
| **Language** | Python 3.10+ |
| **Templates** | Django Template Language (`website/templates/`) |
| **Database** | SQLite (default in `settings.py`; swap for Postgres/MySQL in production) |
| **Static files** | `website/static/` (collected with `collectstatic` in production) |

## Quick Start

1. **Create and activate a virtual environment:**

   ```bash
   cd inclusive-digital
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   If port 8000 is already in use by another app, use a different port:

   ```bash
   python manage.py runserver 8001
   ```

4. **Open in browser:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (or `:8001` if you used that port)

## Project Structure (Django)

```
inclusive-digital/
├── manage.py                 # Django CLI entry point
├── requirements.txt          # pip: Django and dependencies
├── safeguard_ai/             # Django project package
│   ├── settings.py           # INSTALLED_APPS, DATABASES, STATIC_URL, etc.
│   ├── urls.py               # Root URLconf → includes website.urls
│   ├── wsgi.py
│   └── asgi.py
└── website/                  # Django app (listed in INSTALLED_APPS)
    ├── apps.py
    ├── views.py              # Python view functions → render templates
    ├── urls.py               # App URL patterns (home, check/, scam-academy/, …)
    ├── quiz_data.py          # Server-side quiz question data
    ├── templates/website/      # Django HTML templates
    └── static/website/       # CSS, JS (scam_analyzer.js, …)
```

Run **`python manage.py runserver`** to start the Django development server. Use **`python manage.py check`** to validate configuration.

## Features (from proposal)

- **Check Message** — Multi-modal input: paste text, screenshot OCR, voice dictation, URL scanner
- **Scam Risk Meter** — Semi-circular 0-100 gauge with "Why" section and "Read to Me" audio
- **Senior Mode** — Toggle for single-column layout, 80×80px tap targets, 7:1 contrast (WCAG AAA)
- **Scam Academy** — Interactive quiz with 10 randomized questions across 6 scam categories; Safety Badges & Shield Levels
- **I Need Help** — Emergency module: "I gave my password", "I sent money", "I feel overwhelmed" with direct links and hotlines
- **Family Link** — Invite Guardian via SMS; one-touch SOS to alert trusted contact
- **Official Verification** — Directory of real IRS, SSA, Medicare, FTC, and major bank fraud numbers
- **Calm & Secure Design** — Navy (#1A237E), Emerald (#2E7D32), Amber (#FFC107), Crimson (#D32F2F); 18pt base font, Roboto

## License

See [LICENSE](LICENSE) for details.
