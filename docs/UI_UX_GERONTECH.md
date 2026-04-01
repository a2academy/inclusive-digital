# SafeGuard AI — Gerontechnology UI/UX Redesign

**Role framing:** Senior UX/UI for older adults (gerontechnology): prioritize clarity, contrast, forgiving targets, and emotional reassurance through color and layout—not decoration alone.

This document records the **redesign plan**, **style guide**, **Scam Academy flow**, and **SOS implementation notes** aligned with WCAG 2.1 AA (minimum **4.5:1** contrast for normal text).

---

## 1. Home screen — UI component list

| Component | Purpose |
|-----------|---------|
| **Hero band** | Brand, one-line value, primary CTA (“Check a message”). Gradient background for warmth without low-contrast text. |
| **Quick-action strip** | Three **large card buttons**: Help (blue), Learn (green), Family (orange)—color-coded “happy” regions with icons + title + short description. |
| **Help section (blue)** | Narrative + links to emergency help and official numbers; background `#E3F2FD`, text `#0D47A1` (AA on light blue). |
| **Learn section (green)** | CTA to Scam Academy; background `#E8F5E9`, text `#1B5E20`. |
| **Family section (orange)** | Family Link + check message; background `#FFF3E0`, text `#BF360C`. |
| **Executive summary & below** | Standard content sections (problem, solution, features, etc.) on neutral background for long-form reading. |
| **Header nav** | Persistent wayfinding; sticky optional. |
| **Footer** | Meta and summit line. |
| **Senior Mode toggle** | Top-right; increases base type and control size via **reflow** (see below). |
| **SOS control** | Fixed bottom-left, circular red, white “SOS” (see §4). |

---

## 2. Style guide

### Colors (WCAG AA–oriented pairings)

Use **dark text on pastel section fills** for body copy (reliable 4.5:1+). Avoid white text on light pastels.

| Token / use | Background | Foreground (body) | Notes |
|---------------|------------|-------------------|--------|
| **Help (blue)** | `#E3F2FD` | `#0D47A1` | Primary headings/links on section |
| **Help muted** | — | `#1565C0` | Supporting text |
| **Learn (green)** | `#E8F5E9` | `#1B5E20` | |
| **Learn muted** | — | `#2E7D32` | |
| **Family (orange)** | `#FFF3E0` | `#BF360C` | |
| **Family muted** | — | `#E65100` | |
| **Primary actions (navy)** | `#1A237E` | `#FFFFFF` | Buttons; white on navy ≥ AA for large text; use ≥18px or bold for small buttons |
| **SOS red** | `#D32F2F` → `#B71C1C` gradient | `#FFFFFF` | “SOS” label bold |

*(Automated contrast checks in CI or design tools are recommended for any future token changes.)*

### Typography

| Element | Default | Senior Mode |
|---------|---------|-------------|
| **Body** | 18px | **≥24px** (`--font-size-base: 24px`) |
| **H1 / hero** | `clamp` | **≥30px** (`clamp(1.875rem, …)`) |
| **H2 / page titles** | 1.75rem | **≥30px** via `clamp` |
| **Font families** | **Roboto** (UI), **Roboto Slab** (display headings) | Same |

### Buttons & targets

- **Minimum touch target:** **80×80px** where specified (SOS, Senior Mode–aware primary controls).
- **Quiz topic cards:** Large hit areas, `min-height` ~120px (larger in Senior Mode).
- **Reflow:** Increase **font size and padding**; use **vertical scroll**. Do **not** scale the whole page with CSS `transform: scale()` (avoids blur and odd hit areas).

---

## 3. Scam Academy — user flow (topic-first)

1. User opens **Scam Academy**.
2. User sees **six topic cards** (Phishing, SMS, Government, Prize, Banking, Romance)—each with **icon + title + short concrete hint**.
3. User **taps one topic** → quiz loads **only questions for that category** (server-side JSON grouped by category).
4. User answers one question at a time → **Next** → progress bar updates.
5. At end → **score** for that topic + optional **another topic** or **same topic again**.
6. **Back to topics** returns to the grid without forcing a fixed sequence across all six.

This replaces a single forced 10-question mixed sequence with **self-directed topic choice**.

---

## 4. Persistent SOS button — design & technical behavior

### Design

- **Shape:** Circle (`border-radius: 50%`).
- **Size:** **80×80px** minimum (`--sos-size: 80px`).
- **Label:** **“SOS”** in **bold white sans-serif** (Roboto).
- **Placement:** `position: fixed`; `bottom` + `left` with `env(safe-area-inset-*)` for notched devices.
- **Stacking:** `z-index: 400` so it stays above main content and header.

### Behavior

- Same **anchor** on **every** Django template that extends `base.html` → one component in `base.html`, visible on all routes.
- **Hover/focus:** Slight `translateY(-2px)` and stronger shadow—**avoid** `transform: scale()` on the whole UI (reduces “stretch” feeling).

### Avoiding overlap with content

- **`main`** uses **`padding-left`** (and safe-area) so body text does not run under the left-fixed SOS. Approximate rule: `padding-left ≥ SOS width + margin` (e.g. `--sos-safe-left`).
- **`padding-bottom`** on `main` reserves space above bottom UI so the last lines of content are not hidden behind the button when scrolling.
- For **keyboard** users: SOS is focusable; focus ring should remain visible (consider `:focus-visible` outline).

---

## 5. Django implementation map

| Area | Implementation |
|------|----------------|
| Home layout | `website/templates/website/home.html` + `style.css` |
| SOS | `base.html` + `.floating-sos` in `style.css` |
| Senior Mode | `body.senior-mode` in `style.css` + `localStorage` in `base.html` |
| Quiz by topic | `quiz_data.get_quiz_by_category()` → `views.scam_academy` → JSON → `scam_academy.html` |

---

*Last updated with the gerontechnology home refresh, topic-based Scam Academy, SOS restyle, and Senior Mode typography reflow.*
