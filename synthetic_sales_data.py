"""
Synthetic Sales Data Generator (CSV)
- Generates 15k–17k rows of sales across 100–200 stores
- Adds weekend uplift (both more transactions and slightly larger baskets)
- Includes extra fields that make dashboards more interesting

Output: synthetic_sales.csv
"""

import csv
import random
import math
from datetime import datetime, timedelta, time
from pathlib import Path


# -----------------------------
# Configuration
# -----------------------------
# random.seed(42)  # remove or change for a different dataset

N_ROWS = 16000          # between 15k and 17k
N_STORES = 150          # between 100 and 200
N_CUSTOMERS = 5500
N_PRODUCTS = 1200

START_DATE = datetime(2025, 9, 1)
END_DATE = datetime(2026, 2, 28)

OUTPUT_PATH = Path("synthetic_sales.csv")

TAX_RATE = 0.23  # adjust if you want


# -----------------------------
# Helper functions
# -----------------------------
def weighted_choice(items_with_weights):
    """
    items_with_weights: list of (value, weight) where weights sum to ~1.0
    returns one value according to weight
    """
    r = random.random()
    cumulative = 0.0
    for value, w in items_with_weights:
        cumulative += w
        if r <= cumulative:
            return value
    return items_with_weights[-1][0]


def daterange_days(start, end):
    days = []
    d = start.date()
    while d <= end.date():
        days.append(d)
        d = (datetime.combine(d, time()) + timedelta(days=1)).date()
    return days


def weekend_amount_multiplier(d):
    """
    Makes basket totals slightly higher on weekends.
    This is separate from the increased weekend transaction frequency.
    """
    wd = datetime.combine(d, time()).weekday()  # 0=Mon ... 6=Sun
    if wd == 5:  # Sat
        return 1.10
    if wd == 6:  # Sun
        return 1.07
    if wd == 4:  # Fri
        return 1.03
    return 1.00


def store_size_multiplier(size):
    return {"Small": 0.92, "Medium": 1.00, "Large": 1.12}[size]


def promo_probability(d):
    """
    Mild seasonality: more promos in Nov/Dec, and near month-end.
    """
    month = d.month
    day = d.day
    base = 0.12
    if month in (11, 12):
        base += 0.07
    if day >= 25:
        base += 0.05
    return min(base, 0.30)


def discount_rate(is_promo, segment):
    """
    Promo discounts vary by segment (budget customers tend to take larger discounts).
    """
    if not is_promo:
        return 0.0
    if segment == "Budget":
        return random.uniform(0.05, 0.22)
    if segment == "Mainstream":
        return random.uniform(0.03, 0.18)
    return random.uniform(0.02, 0.12)


def sample_time_of_day(channel):
    """
    In-store sales cluster during shopping hours; online is more spread out.
    """
    if channel == "InStore":
        hour = int(random.triangular(9, 20, 15))
    else:
        hour = int(random.triangular(0, 23, 20))
    minute = random.randrange(0, 60)
    second = random.randrange(0, 60)
    return hour, minute, second


def sample_unit_price(category, category_price):
    """
    Log-uniform-ish distribution: many cheap items, occasional expensive ones.
    """
    lo, hi = category_price[category]
    price = math.exp(random.uniform(math.log(lo), math.log(hi)))
    return round(price, 2)


def sample_units(category, category_units):
    """
    Skew toward smaller quantities.
    """
    lo, hi = category_units[category]
    if hi <= 2:
        return random.randint(lo, hi)
    return max(lo, int(random.triangular(lo, hi, lo + 1)))


# -----------------------------
# Domain "flavor"
# -----------------------------
categories = [
    ("Grocery", 0.32),
    ("Apparel", 0.14),
    ("Home", 0.12),
    ("Beauty", 0.10),
    ("Electronics", 0.09),
    ("Sports", 0.08),
    ("Toys", 0.07),
    ("Office", 0.08),
]

payment_methods = [("Card", 0.62), ("Cash", 0.14), ("MobilePay", 0.18), ("GiftCard", 0.06)]
channels = [("InStore", 0.82), ("Online", 0.18)]
customer_segments = [("Budget", 0.35), ("Mainstream", 0.45), ("Premium", 0.20)]
loyalty_tiers = [("None", 0.48), ("Bronze", 0.25), ("Silver", 0.18), ("Gold", 0.09)]
regions = ["North", "South", "East", "West", "Central"]
cities = ["Warsaw", "Krakow", "Gdansk", "Wroclaw", "Poznan", "Lodz", "Szczecin", "Lublin", "Katowice", "Bialystok"]

category_price = {
    "Grocery": (2.0, 30.0),
    "Apparel": (20.0, 140.0),
    "Home": (10.0, 220.0),
    "Beauty": (8.0, 90.0),
    "Electronics": (60.0, 1800.0),
    "Sports": (12.0, 250.0),
    "Toys": (6.0, 120.0),
    "Office": (3.0, 80.0),
}

category_units = {
    "Grocery": (1, 12),
    "Apparel": (1, 4),
    "Home": (1, 3),
    "Beauty": (1, 5),
    "Electronics": (1, 2),
    "Sports": (1, 3),
    "Toys": (1, 4),
    "Office": (1, 8),
}

# used to compute estimated cost/profit (dashboard depth)
category_margin = {
    "Grocery": 0.18,
    "Apparel": 0.48,
    "Home": 0.40,
    "Beauty": 0.52,
    "Electronics": 0.22,
    "Sports": 0.38,
    "Toys": 0.42,
    "Office": 0.35,
}


# -----------------------------
# Build store metadata
# -----------------------------
store_meta = {}
for sid in range(1, N_STORES + 1):
    size = weighted_choice([("Small", 0.45), ("Medium", 0.40), ("Large", 0.15)])
    store_meta[sid] = {
        "store_size": size,
        "region": random.choice(regions),
        "city": random.choice(cities),
    }


# -----------------------------
# Build date weights (more transactions on weekends)
# -----------------------------
all_days = daterange_days(START_DATE, END_DATE)

day_weights = []
for d in all_days:
    wd = datetime.combine(d, time()).weekday()  # 0=Mon ... 6=Sun
    if wd == 5:       # Saturday
        w = 1.60
    elif wd == 6:     # Sunday
        w = 1.45
    elif wd == 4:     # Friday
        w = 1.18
    else:
        w = 1.00
    day_weights.append(w)

total_w = sum(day_weights)
day_probs = [w / total_w for w in day_weights]


def sample_day():
    r = random.random()
    cumulative = 0.0
    for d, p in zip(all_days, day_probs):
        cumulative += p
        if r <= cumulative:
            return d
    return all_days[-1]


# -----------------------------
# Generate sales
# -----------------------------
fieldnames = [
    "sale_id",
    "sale_timestamp",
    "sale_date",
    "day_of_week",
    "is_weekend",
    "store_id",
    "store_size",
    "region",
    "city",
    "customer_id",
    "customer_segment",
    "loyalty_tier",
    "channel",
    "payment_method",
    "category",
    "product_id",
    "units",
    "unit_price",
    "subtotal",
    "promo_applied",
    "discount_rate",
    "discount_amount",
    "tax_rate",
    "tax_amount",
    "total_amount",
    "estimated_cost",
    "estimated_profit",
    "returned_flag",
]

weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

rows = []

for i in range(1, N_ROWS + 1):
    d = sample_day()
    channel = weighted_choice(channels)
    hour, minute, second = sample_time_of_day(channel)
    ts = datetime(d.year, d.month, d.day, hour, minute, second)

    store_id = random.randint(1, N_STORES)
    sm = store_meta[store_id]

    segment = weighted_choice(customer_segments)
    tier = weighted_choice(loyalty_tiers)

    category = weighted_choice(categories)
    product_id = f"P{random.randint(1, N_PRODUCTS):04d}"

    units = sample_units(category, category_units)
    unit_price = sample_unit_price(category, category_price)

    # Base subtotal
    subtotal = units * unit_price

    # Weekend uplift + store size uplift + noise
    subtotal *= weekend_amount_multiplier(d)
    subtotal *= store_size_multiplier(sm["store_size"])
    subtotal *= random.uniform(0.90, 1.12)

    # Promotions and discounts
    promo = random.random() < promo_probability(d)
    disc = discount_rate(promo, segment)
    discount_amount = subtotal * disc
    after_discount = subtotal - discount_amount

    # Tax + total
    tax_amount = after_discount * TAX_RATE
    total = after_discount + tax_amount

    # Cost/profit estimation
    margin = category_margin[category]
    cost = after_discount * (1.0 - margin) * random.uniform(0.97, 1.03)
    profit = after_discount - cost

    # Returns: rare, more likely online and for apparel/electronics
    return_base = 0.008
    if channel == "Online":
        return_base += 0.010
    if category in ("Apparel", "Electronics"):
        return_base += 0.008
    returned = 1 if random.random() < return_base else 0

    wd = ts.weekday()
    rows.append({
        "sale_id": f"S{i:06d}",
        "sale_timestamp": ts.isoformat(sep=" "),
        "sale_date": d.isoformat(),
        "day_of_week": weekday_names[wd],
        "is_weekend": 1 if wd in (5, 6) else 0,
        "store_id": store_id,
        "store_size": sm["store_size"],
        "region": sm["region"],
        "city": sm["city"],
        "customer_id": f"C{random.randint(1, N_CUSTOMERS):05d}",
        "customer_segment": segment,
        "loyalty_tier": tier,
        "channel": channel,
        "payment_method": weighted_choice(payment_methods),
        "category": category,
        "product_id": product_id,
        "units": units,
        "unit_price": f"{unit_price:.2f}",
        "subtotal": f"{subtotal:.2f}",
        "promo_applied": 1 if promo else 0,
        "discount_rate": f"{disc:.4f}",
        "discount_amount": f"{discount_amount:.2f}",
        "tax_rate": f"{TAX_RATE:.2f}",
        "tax_amount": f"{tax_amount:.2f}",
        "total_amount": f"{total:.2f}",
        "estimated_cost": f"{cost:.2f}",
        "estimated_profit": f"{profit:.2f}",
        "returned_flag": returned,
    })


# -----------------------------
# Write CSV
# -----------------------------
with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {OUTPUT_PATH.resolve()}")
