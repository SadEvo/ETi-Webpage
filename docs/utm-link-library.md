# Elite Ti — UTM Link Library

> The single highest-leverage, zero-cost fix for "we don't know what's working." Tag **every**
> link we share so Shopify's generic "$117K social" becomes **per-platform, per-campaign**
> revenue. Implements §5 of the distribution plan.

## The standard format

> **Store domain: `myeliteti.com`** (confirmed live from Shopify).

```
https://myeliteti.com/PRODUCT-OR-PAGE?utm_source=SOURCE&utm_medium=MEDIUM&utm_campaign=CAMPAIGN
```

| Parameter | Meaning | Allowed values (keep this list tight) |
|---|---|---|
| `utm_source` | The platform/place the link lives | `instagram`, `instagram_story`, `instagram_bio`, `facebook_page`, `facebook_group`, `rx7club`, `clublexus`, `sc300org`, `supraforums`, `mkiv`, `reddit`, `tiktok`, `youtube`, `email`, `sms`, `discord` |
| `utm_medium` | The *type* of channel | `social`, `forum`, `email`, `sms`, `referral`, `bio`, `qr` |
| `utm_campaign` | The event (one slug per event, reused everywhere) | see campaign slugs below |

> **Rules:** all lowercase, no spaces (use hyphens), reuse the **exact same** values every time
> or the data fragments. Never share a bare link in a post — always UTM it.

---

## Campaign slugs (lock these — reuse all year)

| Event | `utm_campaign` slug |
|---|---|
| SC300/SC400/Soarer Door Trim + Door Card Group Buy | `sc-doorcard-gb` |
| Sevens Day (RX-7, 7/7) | `sevens-day-2026` |
| Summer build-season flash | `summer-build-2026` |
| Black Friday / Cyber Monday | `bfcm-2026` |
| Tax-refund season group buy (2027) | `tax-season-gb-2027` |
| Always-on / no specific event | `evergreen` |

---

## Ready-to-copy links — Event #1: SC300/SC400 Door Card Group Buy

> **Note:** the dedicated SC300/SC400 door-card/door-trim product page isn't live yet (the group
> buy launches end of June). Links below point to the **`toyota-lexus` collection** as an interim
> landing spot — **swap in the real product/landing URL the moment the GB page is published**, and
> keep the same `?utm_...` query string.

| Where you're posting | Copy-paste link |
|---|---|
| Instagram feed/Reel | `https://myeliteti.com/collections/toyota-lexus?utm_source=instagram&utm_medium=social&utm_campaign=sc-doorcard-gb` |
| Instagram story | `https://myeliteti.com/collections/toyota-lexus?utm_source=instagram_story&utm_medium=social&utm_campaign=sc-doorcard-gb` |
| Link in bio | `https://myeliteti.com/collections/toyota-lexus?utm_source=instagram_bio&utm_medium=bio&utm_campaign=sc-doorcard-gb` |
| Facebook Group post | `https://myeliteti.com/collections/toyota-lexus?utm_source=facebook_group&utm_medium=social&utm_campaign=sc-doorcard-gb` |
| ClubLexus thread | `https://myeliteti.com/collections/toyota-lexus?utm_source=clublexus&utm_medium=forum&utm_campaign=sc-doorcard-gb` |
| SC300.org thread | `https://myeliteti.com/collections/toyota-lexus?utm_source=sc300org&utm_medium=forum&utm_campaign=sc-doorcard-gb` |
| Email blast | `https://myeliteti.com/collections/toyota-lexus?utm_source=email&utm_medium=email&utm_campaign=sc-doorcard-gb` |
| SMS blast | `https://myeliteti.com/collections/toyota-lexus?utm_source=sms&utm_medium=sms&utm_campaign=sc-doorcard-gb` |

## Ready-to-copy links — Event #2: Sevens Day (RX-7)

> Pointed at the live **`rx7` collection** (105 products). Swap to a dedicated Sevens Day sale
> page if one is built; keep the query string.

| Where you're posting | Copy-paste link |
|---|---|
| Instagram feed/Reel | `https://myeliteti.com/collections/rx7?utm_source=instagram&utm_medium=social&utm_campaign=sevens-day-2026` |
| Instagram story | `https://myeliteti.com/collections/rx7?utm_source=instagram_story&utm_medium=social&utm_campaign=sevens-day-2026` |
| Link in bio | `https://myeliteti.com/collections/rx7?utm_source=instagram_bio&utm_medium=bio&utm_campaign=sevens-day-2026` |
| RX-7 Facebook Group | `https://myeliteti.com/collections/rx7?utm_source=facebook_group&utm_medium=social&utm_campaign=sevens-day-2026` |
| rx7club.com thread | `https://myeliteti.com/collections/rx7?utm_source=rx7club&utm_medium=forum&utm_campaign=sevens-day-2026` |
| r/rx7 | `https://myeliteti.com/collections/rx7?utm_source=reddit&utm_medium=social&utm_campaign=sevens-day-2026` |
| Email blast | `https://myeliteti.com/collections/rx7?utm_source=email&utm_medium=email&utm_campaign=sevens-day-2026` |
| SMS blast | `https://myeliteti.com/collections/rx7?utm_source=sms&utm_medium=sms&utm_campaign=sevens-day-2026` |

---

## How to make new links fast

1. Take the product/landing URL.
2. Append `?utm_source=…&utm_medium=…&utm_campaign=…` using the tables above.
3. For forums/bio, shorten it (Bitly/Dub) so it looks clean — the UTMs still track.
4. **For each new event, copy the Event #1 block and swap the slug + URL.**

## How to read the results (monthly)

- Shopify → Analytics → Sessions/Sales **by UTM campaign** and **by source**.
- Expect to learn that **Facebook Groups + Email** convert far above their post volume, while the
  Facebook *Page* and raw IG likes underperform. Then **reallocate effort accordingly.**

---

*Companion: `engagement-diagnosis.md`, `facebook-group-forum-sop.md`. Source: distribution plan §5.*
