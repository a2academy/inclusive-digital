/**
 * Rule-based scam risk analysis (runs in the browser; no random scores).
 */
(function (global) {
    'use strict';

    var PATTERNS = [
        {
            test: function (t) {
                return /within\s+\d+\s*hours?|24\s*hours?|48\s*hours?|immediately|urgent|act\s+now|prompt\s+attention|time\s+is\s+running/i.test(t);
            },
            weight: 28,
            reason: 'Uses artificial urgency or a tight deadline—common in phishing and scams.'
        },
        {
            test: function (t) {
                return /click\s+(here|the\s+link|below)|link\s+below|clicking\s+the\s+link|follow\s+the\s+link|review\s+your\s+account|restore.*by\s+clicking/i.test(t);
            },
            weight: 26,
            reason: 'Asks you to click a link to verify, restore, or secure an account—classic phishing.'
        },
        {
            test: function (t) {
                return /dear\s+(user|customer|valued\s+customer|member)\b/i.test(t);
            },
            weight: 16,
            reason: 'Generic greeting ("Dear User") often signals mass phishing, not a real personal message.'
        },
        {
            test: function (t) {
                return /unusual\s+activity|account.*(?:limited|locked|suspended|restricted|compromised)|temporarily\s+limited/i.test(t);
            },
            weight: 22,
            reason: 'Claims unusual activity or limits on your account to create fear and get you to act.'
        },
        {
            test: function (t) {
                return /gift\s*card|wire\s+transfer|bitcoin|cryptocurrency|send\s+money\s+via/i.test(t);
            },
            weight: 32,
            reason: 'Requests payment via gift cards, wire, or crypto—almost never legitimate from banks or agencies.'
        },
        {
            test: function (t) {
                return /verify\s+your\s+(?:password|pin|ssn|social\s+security)|enter\s+your\s+credentials/i.test(t);
            },
            weight: 24,
            reason: 'Asks for passwords, PINs, or SSN by message—legitimate services do not do this.'
        },
        {
            test: function (t) {
                return /security\s+team(?!\s+from)|\bTEST\s+MESSAGE\b|for\s+application\s+testing/i.test(t);
            },
            weight: 14,
            reason: 'Vague "Security Team" sign-off or test wording still matches common phishing templates.'
        },
        {
            test: function (t) {
                return /(?:irs|social\s+security|medicare).*(?:gift\s+card|prepaid|bitcoin)|arrest.*unless\s+you\s+pay/i.test(t);
            },
            weight: 30,
            reason: 'Government impersonation combined with payment pressure is a scam pattern.'
        },
        {
            test: function (t) {
                return /look[-\s]?alike|misspelled\s+domain|fake\s+bank|phishing/i.test(t);
            },
            weight: 10,
            reason: 'Message references fake domains or phishing tactics.'
        }
    ];

    function analyzeUrl(urlStr) {
        var reasons = [];
        var score = 0;
        try {
            var u = new URL(urlStr.indexOf('http') === 0 ? urlStr : 'https://' + urlStr);
            var host = u.hostname.toLowerCase();
            if (/^www\.example\.com$|^example\.com$/i.test(host) || /\.example\.com$/i.test(host)) {
                score += 35;
                reasons.push('example.com is a placeholder—real services use their own verified domain.');
            }
            if (/-secure-|-verify-|login-secure|account-update/i.test(host)) {
                score += 25;
                reasons.push('Domain looks like a fake "secure login" or "verify" site.');
            }
            if (/^\d+\.\d+\.\d+\.\d+$/.test(host)) {
                score += 30;
                reasons.push('Link uses a raw IP address instead of a company domain—very suspicious.');
            }
            if (/bit\.ly|tinyurl|t\.co|short\.link/i.test(host)) {
                score += 22;
                reasons.push('Shortened URL—scammers often hide the real destination.');
            }
        } catch (e) {
            score += 15;
            reasons.push('URL could not be parsed cleanly—treat with caution.');
        }
        return { score: Math.min(100, score), reasons: reasons };
    }

    function analyzeText(text) {
        var t = text || '';
        var reasons = [];
        var score = 0;
        for (var i = 0; i < PATTERNS.length; i++) {
            var p = PATTERNS[i];
            if (p.test(t)) {
                score += p.weight;
                reasons.push(p.reason);
            }
        }
        var urlMatches = t.match(/https?:\/\/[^\s<>"']+/gi);
        if (urlMatches) {
            var seen = {};
            for (var j = 0; j < urlMatches.length; j++) {
                if (seen[urlMatches[j]]) continue;
                seen[urlMatches[j]] = true;
                var u = analyzeUrl(urlMatches[j]);
                score += u.score;
                for (var k = 0; k < u.reasons.length; k++) {
                    if (reasons.indexOf(u.reasons[k]) === -1) reasons.push(u.reasons[k]);
                }
            }
        }
        score = Math.min(100, score);
        if (reasons.length === 0) {
            reasons.push('Fewer typical scam signals detected—but stay cautious with links and urgent requests.');
        }
        return { score: score, reasons: reasons };
    }

    global.SafeGuardAnalyzer = {
        analyzeText: analyzeText,
        analyzeUrl: analyzeUrl
    };
})(typeof window !== 'undefined' ? window : this);
