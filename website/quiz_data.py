"""
Scam Academy quiz data - 6 categories, randomized questions.
"""
import random

SCAM_CATEGORIES = [
    ("phishing", "Phishing Emails"),
    ("sms", "SMS Scams"),
    ("government", "Government Impersonation"),
    ("prize", "Prize & Lottery Scams"),
    ("banking", "Banking Fraud"),
    ("romance", "Romance Scams"),
]

QUIZ_POOL = [
    # Phishing
    {
        "category": "phishing",
        "question": "You get an email from 'support@amaz0n-sales.com' saying your account will be suspended unless you click a link to verify. What do you do?",
        "options": [
            ("A", "Click the link to verify your account", False),
            ("B", "Ignore it and log into Amazon directly via the official app or website", True),
            ("C", "Reply to the email asking for more details", False),
            ("D", "Forward it to a friend to check", False),
        ],
    },
    {
        "category": "phishing",
        "question": "An email says 'Your Netflix subscription expired. Update payment now.' The sender is 'billing@netfl1x-support.net'. Is this safe?",
        "options": [
            ("A", "Yes, update your payment to avoid service interruption", False),
            ("B", "No, Netflix uses @netflix.com. This is a fake domain.", True),
            ("C", "Maybe—call the number in the email to verify", False),
            ("D", "Forward the email to Netflix support", False),
        ],
    },
    # SMS
    {
        "category": "sms",
        "question": "A text says: 'You've won $10,000! Reply YES to claim. Fee: $50 processing.' What is this?",
        "options": [
            ("A", "A legitimate prize notification", False),
            ("B", "A scam—real prizes don't require upfront fees", True),
            ("C", "Maybe real—$50 is a small fee for $10,000", False),
            ("D", "A marketing survey", False),
        ],
    },
    {
        "category": "sms",
        "question": "Text: 'URGENT: Your bank card is locked. Verify at secure-bank-verify.com.' What should you do?",
        "options": [
            ("A", "Click the link immediately to unlock your card", False),
            ("B", "Call your bank using the number on the back of your card", True),
            ("C", "Reply to the text with your card number", False),
            ("D", "Ignore it—your card probably still works", False),
        ],
    },
    # Government
    {
        "category": "government",
        "question": "A call claims to be from the IRS. They say you owe back taxes and must pay with gift cards or face arrest. Is this real?",
        "options": [
            ("A", "Yes, the IRS can demand immediate payment", False),
            ("B", "No—the IRS never demands gift cards or threatens arrest by phone", True),
            ("C", "Maybe—pay to be safe", False),
            ("D", "Ask for a callback number to verify", False),
        ],
    },
    {
        "category": "government",
        "question": "You get a letter from 'Social Security Administration' asking you to confirm your SSN via a provided link. What do you do?",
        "options": [
            ("A", "Click the link and enter your SSN", False),
            ("B", "Contact SSA directly at ssa.gov or 1-800-772-1213 to verify", True),
            ("C", "Ignore it—SSA never contacts by mail", False),
            ("D", "Reply to the return address on the letter", False),
        ],
    },
    # Prize
    {
        "category": "prize",
        "question": "You get a call: 'Congratulations! You won a Caribbean cruise! Pay a $200 port fee to claim.' Is this legitimate?",
        "options": [
            ("A", "Yes—port fees are normal", False),
            ("B", "No—you can't win a contest you never entered, and real prizes don't require fees", True),
            ("C", "Maybe—ask for written confirmation first", False),
            ("D", "Pay the fee—it's a good deal", False),
        ],
    },
    {
        "category": "prize",
        "question": "An email says you won a foreign lottery. To receive the prize, you must wire $500 for 'international transfer fees.' What is this?",
        "options": [
            ("A", "A legitimate lottery payout process", False),
            ("B", "A scam—legitimate lotteries don't require upfront fees", True),
            ("C", "A tax requirement", False),
            ("D", "A processing fee—pay it to get your winnings", False),
        ],
    },
    # Banking
    {
        "category": "banking",
        "question": "You get an alert: 'Suspicious activity on your account. Click here to secure it.' The link goes to 'chase-secure-login.com'. What do you do?",
        "options": [
            ("A", "Click the link to secure your account", False),
            ("B", "Log into Chase directly at chase.com—this domain is fake", True),
            ("C", "Call the number in the email", False),
            ("D", "Reply to the email with your account number", False),
        ],
    },
    {
        "category": "banking",
        "question": "A text says your debit card was used for $800 at a store you don't recognize. It asks you to text 'STOP' or 'FRAUD' to block. Is this safe?",
        "options": [
            ("A", "Text FRAUD immediately", False),
            ("B", "Call your bank's number from your card or statement—don't use links or numbers from the text", True),
            ("C", "Ignore it—your card probably wasn't used", False),
            ("D", "Reply with your PIN to verify identity", False),
        ],
    },
    # Romance
    {
        "category": "romance",
        "question": "Someone you met online says they love you but needs $2,000 for an emergency surgery before they can visit. What should you do?",
        "options": [
            ("A", "Send the money—they need help", False),
            ("B", "Be suspicious—romance scammers often invent emergencies to get money", True),
            ("C", "Send half now and half later", False),
            ("D", "Ask for a video call to verify their identity", False),
        ],
    },
    {
        "category": "romance",
        "question": "An online romantic interest asks you to receive a package and forward it, or to open a bank account for 'their business.' What is this?",
        "options": [
            ("A", "A normal request from a partner", False),
            ("B", "A scam—you could be used for money laundering or fraud", True),
            ("C", "A test of your loyalty", False),
            ("D", "A legitimate business arrangement", False),
        ],
    },
    # Legitimate (safe) scenarios
    {
        "category": "phishing",
        "question": "You get an email from 'no-reply@paypal.com' with a subject 'Receipt for your purchase.' You recently bought something with PayPal. What do you do?",
        "options": [
            ("A", "Click any link in the email to view the receipt", False),
            ("B", "Log into PayPal directly at paypal.com to check your activity", True),
            ("C", "Delete the email—it's probably fake", False),
            ("D", "Reply to the email to confirm", False),
        ],
    },
    {
        "category": "government",
        "question": "You receive a letter from the IRS at your home address with a notice number and instructions to respond by mail. The return address is an official IRS address. What should you do?",
        "options": [
            ("A", "Ignore it—all IRS mail is a scam", False),
            ("B", "Review it and respond via the official IRS channels listed", True),
            ("C", "Call any number printed on the letter", False),
            ("D", "Throw it away", False),
        ],
    },
]


def _shuffle_option_letters(options_raw):
    """Shuffle order so the correct answer is not always B; reassign A–D."""
    opts = [{"letter": o[0], "text": o[1], "correct": o[2]} for o in options_raw]
    random.shuffle(opts)
    letters = ["A", "B", "C", "D"]
    for i, o in enumerate(opts):
        o["letter"] = letters[i]
    return opts


def get_quiz_questions(count=10):
    """
    Build a quiz with up to `count` questions.
    Ensures at least one question from each of the 6 scam categories when the pool allows,
    then fills remaining slots from the rest of the pool.
    """
    categories = ["phishing", "sms", "government", "prize", "banking", "romance"]
    picked = []
    picked_ids = set()

    for cat in categories:
        pool = [q for q in QUIZ_POOL if q["category"] == cat]
        if pool:
            choice = random.choice(pool)
            picked.append(choice)
            picked_ids.add(id(choice))

    rest = [q for q in QUIZ_POOL if id(q) not in picked_ids]
    random.shuffle(rest)
    for q in rest:
        if len(picked) >= count:
            break
        picked.append(q)

    random.shuffle(picked)
    picked = picked[: min(count, len(picked))]

    result = []
    for i, q in enumerate(picked):
        item = {
            "id": i,
            "category": q["category"],
            "question": q["question"],
            "options": _shuffle_option_letters(q["options"]),
        }
        result.append(item)
    return result
