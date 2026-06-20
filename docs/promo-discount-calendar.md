# Elite Ti — Go-To-Market Promo & Discount Calendar

**Purpose:** define *what we market, to whom, when, and at what price* — with **time-boxed
discount codes** that go live only for the campaign window and **expire automatically**. Every
code below has a hard start and end date. Nothing runs open-ended.

> Companion document: **Marketing Execution Plan** (who posts what, where, and how the AI agent
> distributes). This report is the *offer & calendar*; that one is the *operations*.

---

## 1. Positioning principles

1. **Discipline over depth.** We sell premium titanium & carbon at a ~$1,000 AOV. We do **not**
   train buyers to wait for 30% off. Most promos are **10–15%**, often with a **minimum spend**
   so margin and AOV are protected.
2. **Time-boxed = urgency + safety.** Every code has start + end dates. Scarcity converts this
   audience; auto-expiry protects margin.
3. **Get in front of *buyers*, not browsers.** Each promo is pushed to the people most likely to
   buy *that* platform: past buyers/abandoners of that model (Klaviyo), that model's FB/IG groups
   and forums, and retargeting of that model's collection viewers. (Mechanics in §6.)
4. **Group buys ≠ discount codes.** Group buys use **tiered pre-order pricing**, not coupons
   (see the Group Buy Playbook). They're listed here for calendar coordination only.
5. **Match the moment.** Anchor to dates this audience already cares about (Sevens Day, SEMA,
   Tokyo Auto Salon) and proven retail spikes (Black Friday, tax-refund season).

---

## 2. The discount toolkit (types we'll use)

| Type | Depth | Structure | When |
|---|---|---|---|
| **Model Day** | 10–15% | Scoped to one model collection + min spend | Signature days (Sevens Day, GTR, etc.) |
| **Seasonal retail** | 10% | Sitewide + min spend | Labor Day, Memorial Day, New Year |
| **Black Friday / Cyber** | 15% (or tiered 10/15/20) | Sitewide; biggest event of year | Late Nov |
| **Gift / holiday** | 10% + gift cards | Accessories/apparel/universal titanium | December |
| **Clearance / container** | 15–20% | Curated clearance collection only | Year-end + on container arrival |
| **Group buy (pre-order)** | Tiered pricing | Not a code — pre-order page | Quarterly |

---

## 3. Master promo calendar (next 12 months)

> Dates are inclusive. Codes expire 11:59 PM on the end date. "Scope" = which collection the code
> applies to (sitewide = no collection). All depths are **proposals pending your approval.**

| # | Campaign | Window | Models / Scope | Code | Offer | Type |
|---|---|---|---|---|---|---|
| 1 | **SC300/SC400 Door Trim + Card Group Buy** | Launches late June | SC300/400 / Soarer | — | Tiered pre-order (~$900 trims / ~$1,400 cards) | Group buy |
| 2 | **Sevens Day** | Jul 5–9, 2026 | RX-7 (FD3S) | `SEVENS` | 15% off RX-7, min $1,000 | Model Day |
| 3 | **Summer Show Season** | Aug 7–16, 2026 | Aero/Body kits — GT86, Evo, GTR | `SHOWSEASON` | 10% off, min $1,500 | Model Day |
| 4 | **Labor Day** | Sep 4–7, 2026 | Sitewide | `LABORDAY` | 10% off, min $500 | Seasonal |
| 5 | **Godzilla Days (GTR)** | Sep 25 – Oct 4, 2026 | Nissan GTR R32–R35 | `GODZILLA` | 12% off, min $1,000 | Model Day |
| 6 | **Carbon October / Blackout** | **Oct 12–31, 2026** | Rotary — RX-7 + RX-8 | `BLACKOUT` | 12% off, min $750 | Model Day |
| 7 | **SEMA Week** | Nov 3–7, 2026 | Supra (MK4/MK5) + featured builds | `SEMA` | 10% off, min $1,000 | Event tie-in |
| 8 | **Black Friday → Cyber Monday** | Nov 25 (VIP) · 27–30 public · ext. to Dec 1 | Sitewide | `BF2026` | **15% sitewide** (or tiered 10/15/20) + free shipping | Sitewide |
| 9 | **Holiday Gift** | Dec 8–24, 2026 | Apparel, accessories, universal titanium + gift cards | `GIFT` | 10% off, free shipping | Gift |
| 10 | **Year-End Clearance** | Dec 26–31, 2026 | Clearance collection only | `YEAREND` | 15% off | Clearance |
| 11 | **Tokyo Auto Salon / New Year** | Jan 8–18, 2027 | JDM heroes — Supra, RX-7, GTR, Evo | `TAS2027` | 12% off, min $1,000 | Event tie-in |
| 12 | **Valentine's "Treat Your Build"** | Feb 11–15, 2027 | Interior / trim products | `BUILDLOVE` | 10% off | Model Day |
| 13 | **Tax-Refund Kickoff** | Feb 20 – Mar 8, 2027 | Sitewide + flagship group buy | `REFUND` | 10% off, min $1,000 | Seasonal (big) |
| 14 | **Mad March Feature** | Mar 13–22, 2027 | Top-selling model of the season | `MARCH` | 12% off, min $1,000 | Model Day |
| 15 | **Spring Drop** | Apr 10–19, 2027 | New-product collection | `SPRING` | 10% off, min $750 | Seasonal |
| 16 | **Memorial Day** | May 21–25, 2027 | Sitewide | `MEMORIAL` | 10% off, min $500 | Seasonal |
| — | **Container / Restock sales** | On arrival (~quarterly) | The arriving model lines | `CONTAINER` | 12–15% off that line, 5–7 days | Container |

**Result:** 1–2 promotable offers every month, loaded heaviest into the proven spike windows
(Black Friday and Feb–March tax season), with group buys and container sales filling the gaps.

---

## 4. Black Friday — the one to get right

BF/CM is our biggest single retail window (~$25K last year with no real plan). Two options:

- **Option A (simple): 15% sitewide + free shipping.** Easy to communicate, one code, strong
  enough to convert without gutting margin on $1K+ carbon/titanium.
- **Option B (margin-smart): tiered "spend more, save more"** — 10% over $500 / 15% over $1,500
  / 20% over $3,000. Rewards full builds, protects small-order margin, lifts AOV. Requires an
  **automatic discount** (set via GraphQL) or three stacked-threshold codes.

**Recommendation:** Option B as an automatic tiered discount — it fits a high-AOV build audience
and industry data shows threshold tiers lift basket size more than a flat % on big-ticket parts.
Run **VIP early access** (high-value segment) 48 hrs before public.

---

## 5. Discount code spec sheet (ready for Shopify prefill)

Hand these straight to setup. **I will prefill these in Shopify only after you approve**, each
with the start/end below so they cannot run past their window. Eligibility = all customers
unless noted. Model scope uses these collections:

| Model | Collection GID |
|---|---|
| Mazda RX-7 (FD3S) | `gid://shopify/Collection/467566100761` |
| Mazda RX-8 | `gid://shopify/Collection/476770599193` |
| Toyota Supra MKIV | `gid://shopify/Collection/467589693721` |
| Nissan GTR (R32 / R33 / R34 / R35) | `467589890329` / `467589792025` / `467591233817` / `467614761241` |
| GT86 / FT86 | `gid://shopify/Collection/486336659737` |
| Evo 8/9 | `gid://shopify/Collection/496729325849` |
| Universal Titanium | `gid://shopify/Collection/472386437401` |
| Toyota / Lexus (SC/Soarer) | `gid://shopify/Collection/513420820761` |

| Code | % | Min spend | Scope | Starts | Ends |
|---|---|---|---|---|---|
| `SEVENS` | 15 | $1,000 | RX-7 collection | 2026-07-05 | 2026-07-09 |
| `SHOWSEASON` | 10 | $1,500 | Aero/body-kit (campaign collection) | 2026-08-07 | 2026-08-16 |
| `LABORDAY` | 10 | $500 | Sitewide | 2026-09-04 | 2026-09-07 |
| `GODZILLA` | 12 | $1,000 | GTR (campaign collection) | 2026-09-25 | 2026-10-04 |
| `BLACKOUT` | 12 | $750 | Rotary RX-7 + RX-8 (campaign collection) | 2026-10-12 | 2026-10-31 |
| `SEMA` | 10 | $1,000 | Supra collection | 2026-11-03 | 2026-11-07 |
| `BF2026` | 15 (or tiered) | — | Sitewide | 2026-11-27 | 2026-12-01 |
| `GIFT` | 10 | — | Apparel/accessories/titanium | 2026-12-08 | 2026-12-24 |
| `YEAREND` | 15 | — | Clearance collection | 2026-12-26 | 2026-12-31 |
| `TAS2027` | 12 | $1,000 | JDM-hero (campaign collection) | 2027-01-08 | 2027-01-18 |
| `BUILDLOVE` | 10 | — | Interior/trim (campaign collection) | 2027-02-11 | 2027-02-15 |
| `REFUND` | 10 | $1,000 | Sitewide | 2027-02-20 | 2027-03-08 |
| `MARCH` | 12 | $1,000 | Feature model | 2027-03-13 | 2027-03-22 |
| `SPRING` | 10 | $750 | New-products collection | 2027-04-10 | 2027-04-19 |
| `MEMORIAL` | 10 | $500 | Sitewide | 2027-05-21 | 2027-05-25 |

**Note on multi-model promos** (GTR, rotary, JDM-hero, aero, interior): Shopify's quick discount
tool scopes to **one** collection. For these I'll either (a) create a small temporary
**"Campaign" collection** for the promo, or (b) set them up via GraphQL to target multiple
collections. Single-model and sitewide codes are straightforward. Flag your preference.

### Prefill status (live in Shopify)

**Staged & scheduled (inactive until their window):**
`SEVENS` · `SHOWSEASON` · `LABORDAY` · `GODZILLA` · `BLACKOUT` · `SEMA` · `GIFT` · `TAS2027` ·
`BUILDLOVE` · `REFUND` · `MEMORIAL` — all created as scheduled discounts; they will not apply to
any order before their start date and auto-expire at the end date. Six are scoped to **temporary
campaign collections**:
- *Campaign — Godzilla (GTR R32–R35)* — 224 products, curated from the R32/R33/R34/R35 GTR collections.
- *Campaign — Blackout (Rotary RX-7 + RX-8)* — 134 products, curated from Mazda RX7 + RX8.
- *Campaign — Holiday Gifts (Titanium & Swag)* — 66 products, curated from Titanium + Shirts/Swag + Shift Knobs.
- *Campaign — Showseason (Aero & Body)* — ~1,300 products, **smart** (title rules: Body Kit/Wing/Diffuser/Hood/Bumper/…). Broad; trim if a tighter aero set is wanted.
- *Campaign — Buildlove (Interior & Trim)* — ~99 products, **smart** (title rules: Interior/Dash/Door Card/Console/Seat/…).
- *Campaign — TAS Heroes (JDM Icons)* — ~700 products, **smart** (title rules: Supra/RX-7/R34/350Z/GT86/Evo).
"Campaign —" collections are clearly labeled and safe to delete after each promo.

**`BF2026` — Black Friday tiered (staged):** built as **three scheduled automatic discounts**
(10% over $500 · 15% over $1,500 · 20% over $3,000), set *not to combine with each other* so
Shopify applies only the single best-qualifying tier per cart. ⚠️ **Verify before go-live:** run a
test/draft cart at each threshold ($800, $1,800, $3,200) to confirm only one tier applies and the
tiers don't stack. If bulletproof tiering is required, replace with a single Shopify Discount Function.

**Housekeeping done:** two stray open-ended ACTIVE 10% codes (`NT8YMY9VFZNB`, `JBQ4A9VWGZFJ`)
that had no expiry were expired.

**Still pending — only these need Nate's manual curation (catalog can't supply them):**
- `YEAREND` (clearance) — no clearance collection; flag which items are clearance, then I'll stage it.
- `SPRING` (new products) — no unified "new arrivals" collection (only per-brand "New" dumps); confirm a source.
- `MARCH` (feature model) — pick the season's bestselling model closer to the date.

---

## 6. Getting each promo in front of *actual buyers*

Every promo fires through four buyer-focused channels, not a generic blast:

1. **Klaviyo segments** — the model's past buyers + browse/cart abandoners + the high-value list
   first (VIP early access). This is the "people who already want it" layer.
2. **Model-specific FB/IG groups + forums** — AI agent reshares the human's creative into the
   exact-platform communities (RX-7 promo → RX-7 groups/rx7club, GTR promo → GTR groups, etc.).
3. **Meta retargeting** — serve the offer to people who viewed that model's collection/products
   in the last 30–60 days. Warm traffic, high intent.
4. **Native social** — human posts the announcement on IG/FB/TikTok; AI adds UTM links.

This is the difference between "5,000 random impressions" and "the 400 people building that exact
car who saw it in their group and their inbox the same day."

---

## 7. Discount-depth rationale (industry-informed)

- **10–15% is the conversion sweet spot** for premium aftermarket: enough to trigger a purchase,
  not so deep it signals "the real price is lower" or erodes brand on titanium/carbon.
- **Minimum-spend thresholds** push AOV up and keep small orders from eroding margin — they fit a
  build audience that buys in sets (hood + interior + hardware).
- **Black Friday is the exception** where 15–20% (tiered) is expected and shoppers actively
  compare — going too shallow here leaves money on the table; tiering captures big builds.
- **Clearance/container 15–20%** is fine because it's curated overstock, not core catalog — it
  moves aged inventory and funds the next container without discounting the everyday range.
- **Never discount during group buys** — pre-order tier pricing already *is* the incentive;
  stacking a code on top destroys the model.

---

## 8. What I need from you to activate
1. **Approve depths/dates** above (or edit them).
2. Confirm **Black Friday Option A (flat 15%) vs B (tiered)**.
3. Confirm **multi-model handling** (temporary campaign collections vs GraphQL multi-collection).
4. On approval, I'll **prefill the codes in Shopify** with the exact start/end dates — scheduled,
   not live early, and auto-expiring. Nothing goes live until you say go.
