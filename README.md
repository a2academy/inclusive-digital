# SafeGuard AI — Inclusive Digital Protection

**Youth & AI Innovation Summit 2026**

An AI-powered security suite designed to bridge the digital safety gap for seniors and persons with disabilities. By combining real-time scam detection with advanced accessibility features, SafeGuard AI empowers vulnerable populations to navigate the digital world without fear of financial exploitation.

## Tech Stack

- **Framework:** Django 5.x
- **Python:** 3.10+

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

## Project Structure

```
inclusive-digital/
├── manage.py
├── requirements.txt
├── safeguard_ai/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── website/               # Main app
    ├── templates/
    │   └── website/
    │       ├── base.html
    │       └── home.html
    ├── static/
    │   └── website/
    │       └── css/
    │           └── style.css
    ├── views.py
    └── urls.py
```

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
