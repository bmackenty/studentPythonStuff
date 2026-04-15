import csv
import math
import random
from datetime import datetime, timedelta


# ============================================================
# Synthetic House Sales Generator
# ------------------------------------------------------------
# Generates realistic-ish house sale data with correlated fields:
# - location
# - country
# - size_sqm
# - number_of_rooms
# - convenience_facilities
# - constructed_year
# - transportation
# - floor_number
# - economic
# - crime
# - sale_price
# - sale_date
#
# Output:
#   synthetic_house_sales.csv
#
# Notes:
# - This is synthetic data, not real market data.
# - The script tries to make the data internally consistent:
#   larger homes usually cost more, better transport helps value,
#   higher crime tends to reduce value, older homes may be cheaper
#   unless located in premium cities, etc.
# ============================================================


random.seed(42)


COUNTRIES = {
    "Poland": {
        "currency": "PLN",
        "base_price_per_sqm": 11500,
        "economic_base": 67,
        "crime_base": 34,
        "urban_share": 0.58,
        "cities": [
            ("Warsaw", 1.35),
            ("Krakow", 1.20),
            ("Wroclaw", 1.12),
            ("Gdansk", 1.15),
            ("Poznan", 1.08),
            ("Lodz", 0.92),
            ("Lublin", 0.88),
            ("Bialystok", 0.84),
        ],
    },
    "Germany": {
        "currency": "EUR",
        "base_price_per_sqm": 5200,
        "economic_base": 84,
        "crime_base": 28,
        "urban_share": 0.66,
        "cities": [
            ("Berlin", 1.22),
            ("Munich", 1.65),
            ("Hamburg", 1.35),
            ("Frankfurt", 1.42),
            ("Cologne", 1.18),
            ("Leipzig", 0.92),
            ("Dresden", 0.90),
            ("Essen", 0.88),
        ],
    },
    "France": {
        "currency": "EUR",
        "base_price_per_sqm": 5100,
        "economic_base": 82,
        "crime_base": 33,
        "urban_share": 0.67,
        "cities": [
            ("Paris", 1.85),
            ("Lyon", 1.28),
            ("Marseille", 1.10),
            ("Toulouse", 1.14),
            ("Nice", 1.32),
            ("Lille", 0.98),
            ("Bordeaux", 1.22),
            ("Nantes", 1.08),
        ],
    },
    "Spain": {
        "currency": "EUR",
        "base_price_per_sqm": 3300,
        "economic_base": 75,
        "crime_base": 31,
        "urban_share": 0.61,
        "cities": [
            ("Madrid", 1.45),
            ("Barcelona", 1.55),
            ("Valencia", 1.14),
            ("Seville", 1.02),
            ("Malaga", 1.08),
            ("Bilbao", 1.12),
            ("Zaragoza", 0.94),
            ("Alicante", 0.97),
        ],
    },
    "Italy": {
        "currency": "EUR",
        "base_price_per_sqm": 3400,
        "economic_base": 73,
        "crime_base": 36,
        "urban_share": 0.60,
        "cities": [
            ("Milan", 1.60),
            ("Rome", 1.42),
            ("Florence", 1.28),
            ("Bologna", 1.16),
            ("Turin", 1.00),
            ("Naples", 0.92),
            ("Palermo", 0.84),
            ("Bari", 0.87),
        ],
    },
    "United Kingdom": {
        "currency": "GBP",
        "base_price_per_sqm": 6100,
        "economic_base": 81,
        "crime_base": 35,
        "urban_share": 0.69,
        "cities": [
            ("London", 1.95),
            ("Manchester", 1.20),
            ("Birmingham", 1.12),
            ("Edinburgh", 1.28),
            ("Bristol", 1.26),
            ("Leeds", 1.02),
            ("Liverpool", 0.96),
            ("Glasgow", 0.98),
        ],
    },
    "United States": {
        "currency": "USD",
        "base_price_per_sqm": 4200,
        "economic_base": 83,
        "crime_base": 39,
        "urban_share": 0.64,
        "cities": [
            ("New York", 2.05),
            ("San Francisco", 2.10),
            ("Seattle", 1.52),
            ("Austin", 1.25),
            ("Chicago", 1.12),
            ("Denver", 1.20),
            ("Atlanta", 1.08),
            ("Cleveland", 0.82),
        ],
    },
    "Canada": {
        "currency": "CAD",
        "base_price_per_sqm": 5000,
        "economic_base": 82,
        "crime_base": 24,
        "urban_share": 0.68,
        "cities": [
            ("Toronto", 1.75),
            ("Vancouver", 1.92),
            ("Montreal", 1.22),
            ("Calgary", 1.12),
            ("Ottawa", 1.15),
            ("Edmonton", 0.96),
            ("Halifax", 1.00),
            ("Winnipeg", 0.86),
        ],
    },
    "Japan": {
        "currency": "JPY",
        "base_price_per_sqm": 680000,
        "economic_base": 86,
        "crime_base": 12,
        "urban_share": 0.72,
        "cities": [
            ("Tokyo", 1.85),
            ("Osaka", 1.35),
            ("Yokohama", 1.42),
            ("Kyoto", 1.28),
            ("Nagoya", 1.18),
            ("Sapporo", 1.00),
            ("Fukuoka", 1.06),
            ("Sendai", 0.92),
        ],
    },
    "Netherlands": {
        "currency": "EUR",
        "base_price_per_sqm": 5600,
        "economic_base": 85,
        "crime_base": 22,
        "urban_share": 0.71,
        "cities": [
            ("Amsterdam", 1.78),
            ("Rotterdam", 1.18),
            ("Utrecht", 1.32),
            ("The Hague", 1.26),
            ("Eindhoven", 1.14),
            ("Groningen", 0.96),
            ("Leiden", 1.08),
            ("Maastricht", 0.98),
        ],
    },
}


PROPERTY_TYPES = [
    ("apartment", 0.46),
    ("house", 0.36),
    ("townhouse", 0.10),
    ("duplex", 0.08),
]

TRANSPORT_OPTIONS = {
    "excellent": 1.22,
    "good": 1.10,
    "average": 1.00,
    "poor": 0.86,
}

LOCATION_TYPES = {
    "urban_core": 1.30,
    "suburban": 1.05,
    "rural": 0.78,
}

ECONOMIC_LABELS = [
    (0, 39, "weak"),
    (40, 54, "fragile"),
    (55, 69, "stable"),
    (70, 84, "strong"),
    (85, 100, "very_strong"),
]

CRIME_LABELS = [
    (0, 19, "very_low"),
    (20, 34, "low"),
    (35, 49, "moderate"),
    (50, 69, "high"),
    (70, 100, "very_high"),
]


def weighted_choice(items):
    """
    items: list of tuples (value, weight)
    """
    total = sum(weight for _, weight in items)
    r = random.uniform(0, total)
    upto = 0
    for value, weight in items:
        if upto + weight >= r:
            return value
        upto += weight
    return items[-1][0]


def clamp(value, low, high):
    return max(low, min(high, value))


def score_to_label(score, bands):
    for low, high, label in bands:
        if low <= score <= high:
            return label
    return bands[-1][2]


def random_sale_date():
    """
    Random date within the last 4 years.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=4 * 365)
    delta_days = (end_date - start_date).days
    return (start_date + timedelta(days=random.randint(0, delta_days))).date().isoformat()


def choose_country():
    weights = []
    for country_name, info in COUNTRIES.items():
        # Mildly bias toward larger/commonly modeled markets
        city_count = len(info["cities"])
        weight = city_count
        if country_name in ("United States", "Germany", "United Kingdom", "France", "Japan"):
            weight += 2
        weights.append((country_name, weight))
    return weighted_choice(weights)


def choose_location(country_info):
    city_name, city_multiplier = random.choice(country_info["cities"])

    r = random.random()
    if r < country_info["urban_share"]:
        location_type = "urban_core"
    elif r < 0.90:
        location_type = "suburban"
    else:
        location_type = "rural"

    return city_name, city_multiplier, location_type


def choose_property_type(location_type):
    adjusted = []
    for ptype, weight in PROPERTY_TYPES:
        w = weight
        if location_type == "urban_core":
            if ptype == "apartment":
                w *= 1.8
            if ptype == "house":
                w *= 0.65
        elif location_type == "rural":
            if ptype == "house":
                w *= 1.9
            if ptype == "apartment":
                w *= 0.45
        adjusted.append((ptype, w))
    return weighted_choice(adjusted)


def generate_size(property_type, location_type, country):
    """
    Approximate sizes in square meters.
    """
    if property_type == "apartment":
        if country == "Japan":
            size = random.gauss(58, 18)
        elif location_type == "urban_core":
            size = random.gauss(72, 22)
        else:
            size = random.gauss(86, 25)

    elif property_type == "house":
        if country == "United States":
            size = random.gauss(185, 55)
        elif country == "Canada":
            size = random.gauss(170, 45)
        elif location_type == "rural":
            size = random.gauss(165, 50)
        else:
            size = random.gauss(140, 40)

    elif property_type == "townhouse":
        size = random.gauss(120, 28)

    else:  # duplex
        size = random.gauss(135, 35)

    return int(clamp(round(size), 28, 420))


def infer_rooms(size_sqm, property_type):
    """
    Strong correlation between size and room count, with noise.
    """
    base = max(1, round(size_sqm / 28 + random.choice([-1, 0, 0, 0, 1])))
    if property_type == "apartment":
        base = clamp(base, 1, 6)
    elif property_type == "house":
        base = clamp(base, 2, 10)
    else:
        base = clamp(base, 2, 8)
    return int(base)


def generate_constructed_year(location_type, city_multiplier):
    """
    Distribution with some older stock in premium cities and urban cores.
    """
    current_year = datetime.now().year
    r = random.random()

    if location_type == "urban_core" and city_multiplier > 1.25:
        if r < 0.30:
            year = random.randint(1900, 1945)
        elif r < 0.62:
            year = random.randint(1946, 1989)
        elif r < 0.88:
            year = random.randint(1990, 2014)
        else:
            year = random.randint(2015, current_year)
    else:
        if r < 0.15:
            year = random.randint(1950, 1975)
        elif r < 0.45:
            year = random.randint(1976, 1999)
        elif r < 0.82:
            year = random.randint(2000, 2016)
        else:
            year = random.randint(2017, current_year)

    return year


def choose_transport(location_type):
    if location_type == "urban_core":
        return weighted_choice([
            ("excellent", 0.48),
            ("good", 0.34),
            ("average", 0.14),
            ("poor", 0.04),
        ])
    elif location_type == "suburban":
        return weighted_choice([
            ("excellent", 0.15),
            ("good", 0.38),
            ("average", 0.33),
            ("poor", 0.14),
        ])
    else:
        return weighted_choice([
            ("excellent", 0.03),
            ("good", 0.14),
            ("average", 0.35),
            ("poor", 0.48),
        ])


def generate_floor_number(property_type, location_type):
    if property_type == "house":
        return 0
    if property_type in ("townhouse", "duplex"):
        return random.randint(0, 3)

    # apartment
    if location_type == "urban_core":
        return random.randint(0, 25)
    elif location_type == "suburban":
        return random.randint(0, 12)
    else:
        return random.randint(0, 5)


def generate_convenience_facilities(location_type, transport, size_sqm):
    """
    Integer score from 0 to 10 representing amenities/convenience:
    shops, schools, clinics, parks, gyms, daily services, etc.
    """
    base = {
        "urban_core": 7.0,
        "suburban": 5.5,
        "rural": 3.0,
    }[location_type]

    transport_bonus = {
        "excellent": 1.6,
        "good": 0.8,
        "average": 0.0,
        "poor": -0.9,
    }[transport]

    size_bonus = 0.4 if size_sqm > 150 else 0.0
    noise = random.gauss(0, 1.1)

    score = round(base + transport_bonus + size_bonus + noise)
    return int(clamp(score, 0, 10))


def generate_economic_score(country_info, city_multiplier, location_type):
    base = country_info["economic_base"]
    city_bonus = (city_multiplier - 1.0) * 18
    loc_bonus = {
        "urban_core": 4,
        "suburban": 1,
        "rural": -3,
    }[location_type]
    score = round(base + city_bonus + loc_bonus + random.gauss(0, 6))
    return int(clamp(score, 0, 100))


def generate_crime_score(country_info, location_type, city_multiplier):
    base = country_info["crime_base"]
    loc_shift = {
        "urban_core": 6,
        "suburban": -2,
        "rural": -5,
    }[location_type]

    # Premium cities can still have some higher urban crime
    city_shift = 2 if city_multiplier > 1.35 and location_type == "urban_core" else 0

    score = round(base + loc_shift + city_shift + random.gauss(0, 8))
    return int(clamp(score, 0, 100))


def age_penalty_or_premium(constructed_year, location_type, city_multiplier):
    age = datetime.now().year - constructed_year

    # Newer buildings often command a premium.
    if age <= 5:
        return 1.12
    if age <= 15:
        return 1.07
    if age <= 30:
        return 1.02

    # Older premium-city urban stock may retain value.
    if age > 70 and location_type == "urban_core" and city_multiplier > 1.30:
        return 1.05

    if age > 70:
        return 0.88
    if age > 45:
        return 0.94
    return 0.98


def floor_effect(property_type, floor_number, transport):
    if property_type != "apartment":
        return 1.0

    # Mid floors often slightly preferred; very high floors depend on quality area.
    if floor_number == 0:
        factor = 0.95
    elif 1 <= floor_number <= 3:
        factor = 1.00
    elif 4 <= floor_number <= 8:
        factor = 1.03
    elif 9 <= floor_number <= 18:
        factor = 1.01
    else:
        factor = 0.98

    if transport == "excellent" and floor_number >= 8:
        factor += 0.01

    return factor


def rooms_effect(size_sqm, rooms):
    ideal_rooms = max(1, round(size_sqm / 30))
    gap = abs(rooms - ideal_rooms)

    if gap == 0:
        return 1.03
    if gap == 1:
        return 1.00
    if gap == 2:
        return 0.96
    return 0.92


def convenience_effect(convenience_facilities):
    return 0.90 + (convenience_facilities * 0.025)


def economic_effect(economic_score):
    return 0.85 + (economic_score / 100.0) * 0.35


def crime_effect(crime_score):
    return 1.08 - (crime_score / 100.0) * 0.30


def price_noise():
    return random.uniform(0.90, 1.12)


def generate_sale_price(
    country_info,
    city_multiplier,
    location_type,
    size_sqm,
    rooms,
    convenience_facilities,
    constructed_year,
    transport,
    floor_number,
    economic_score,
    crime_score,
    property_type
):
    base_ppsqm = country_info["base_price_per_sqm"]

    location_multiplier = LOCATION_TYPES[location_type]
    transport_multiplier = TRANSPORT_OPTIONS[transport]
    age_multiplier = age_penalty_or_premium(constructed_year, location_type, city_multiplier)
    floor_multiplier = floor_effect(property_type, floor_number, transport)
    room_multiplier = rooms_effect(size_sqm, rooms)
    convenience_multiplier = convenience_effect(convenience_facilities)
    economic_multiplier = economic_effect(economic_score)
    crime_multiplier = crime_effect(crime_score)
    noise_multiplier = price_noise()

    # Large houses sometimes have lower price per sqm than smaller premium units.
    size_scale = 1.0
    if property_type == "house" and size_sqm > 220:
        size_scale = 0.94
    elif property_type == "apartment" and size_sqm < 55 and location_type == "urban_core":
        size_scale = 1.08

    ppsqm = (
        base_ppsqm
        * city_multiplier
        * location_multiplier
        * transport_multiplier
        * age_multiplier
        * floor_multiplier
        * room_multiplier
        * convenience_multiplier
        * economic_multiplier
        * crime_multiplier
        * size_scale
        * noise_multiplier
    )

    price = size_sqm * ppsqm

    # Round to a realistic market increment.
    if country_info["currency"] in ("EUR", "GBP", "USD", "CAD", "PLN"):
        price = round(price / 1000) * 1000
    else:
        price = round(price / 10000) * 10000

    return int(max(price, 25000))


def generate_record(record_id):
    country = choose_country()
    country_info = COUNTRIES[country]

    city, city_multiplier, location_type = choose_location(country_info)
    property_type = choose_property_type(location_type)
    size_sqm = generate_size(property_type, location_type, country)
    rooms = infer_rooms(size_sqm, property_type)
    constructed_year = generate_constructed_year(location_type, city_multiplier)
    transport = choose_transport(location_type)
    floor_number = generate_floor_number(property_type, location_type)
    convenience_facilities = generate_convenience_facilities(location_type, transport, size_sqm)
    economic_score = generate_economic_score(country_info, city_multiplier, location_type)
    crime_score = generate_crime_score(country_info, location_type, city_multiplier)

    sale_price = generate_sale_price(
        country_info=country_info,
        city_multiplier=city_multiplier,
        location_type=location_type,
        size_sqm=size_sqm,
        rooms=rooms,
        convenience_facilities=convenience_facilities,
        constructed_year=constructed_year,
        transport=transport,
        floor_number=floor_number,
        economic_score=economic_score,
        crime_score=crime_score,
        property_type=property_type,
    )

    economic_label = score_to_label(economic_score, ECONOMIC_LABELS)
    crime_label = score_to_label(crime_score, CRIME_LABELS)

    return {
        "sale_id": record_id,
        "sale_date": random_sale_date(),
        "country": country,
        "location": city,
        "location_type": location_type,
        "property_type": property_type,
        "size_sqm": size_sqm,
        "number_of_rooms": rooms,
        "convenience_facilities": convenience_facilities,
        "constructed_year": constructed_year,
        "transportation": transport,
        "floor_number": floor_number,
        "economic_score": economic_score,
        "economic": economic_label,
        "crime_score": crime_score,
        "crime": crime_label,
        "currency": country_info["currency"],
        "sale_price": sale_price,
    }


def generate_dataset(n=7000, output_file="synthetic_house_sales.csv"):
    fieldnames = [
        "sale_id",
        "sale_date",
        "country",
        "location",
        "location_type",
        "property_type",
        "size_sqm",
        "number_of_rooms",
        "convenience_facilities",
        "constructed_year",
        "transportation",
        "floor_number",
        "economic_score",
        "economic",
        "crime_score",
        "crime",
        "currency",
        "sale_price",
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, n + 1):
            writer.writerow(generate_record(i))

    print(f"Generated {n} synthetic house sales into {output_file}")


if __name__ == "__main__":
    generate_dataset(n=7000)
