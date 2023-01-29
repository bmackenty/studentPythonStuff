# This file was written by a student
import textwrap
import random

# -------------------------------------------------------------------------------------------------
# COUNTRY NAME

vowels = ["a", "e", "i", "o", "u"]
country_beginning_options = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W", "Y", "Z", "Br", "Cl", "Cr", "Dr", "Fr", "Tr", "Fl", "Gl", "Gr", "Pl", "Pr", "Sl", "Sp", "St", "Ch", "Sc", "Sh", "Th", "Ph", "Ar", "Ang", "Or", "E", "Syra", ""]
country_middle_options = ["a", "e", "i", "o", "u", "uls", "aris", "acra", "oma", "esa", "oka", "emo", "en", "ara", "era", "ed", "arl", "ithu", "er", "ica", "ash", "ark", "aling", "il", "ub", "otts", "al", "eni", "are", "ins", "oren", "ace", "an", "or", "ef", "ad", "abe", "ong", "uri", "itri", "obou", "astri", "ocu", "ego", "aho", "ose", "ean", "ine", "uco", "yti", "yl", "oya", "one"]
country_end_options = ["more", "min", "ville", "no", "kee", "ta", "co", "worth", "son", "go", "notte", "lotte", "ton", "mis", "nia", "sfield", "cas", "das", "dus", "lus", "tus", "mus", "nor", "ver", "phis", "que", "mento", "land", "lina", "see", "side", "mont", "kane", "dale", "ster", "llin", "wood", "cord", "ley", "ridge", "well", "tura", "vina", "bank", "walk", "ford", "cuse", "vale", "heim", "mark", "stan", "nam", "tu", "bia", "lot", "can", ""]

chosen_country_beginning = random.choice(country_beginning_options)

if chosen_country_beginning != "":
    # if a string ending with "l" is chosen as the beginning, the middle can’t be "uls", "arl", "aling", "al", or "il"
    if chosen_country_beginning[-1] == "l":
        unwanted_middle = {"uls", "arl", "aling", "al", "il"}
        country_middle_options = [ele for ele in country_middle_options if ele not in unwanted_middle]

    # if a string ending with "r" is chosen as the beginning, the middle can’t be "or", "uri", "arl", "er", "aris", "are", "ark", "ara", "era", or "oren"
    if chosen_country_beginning[-1] == "r":
        unwanted_middle = {"or", "uri", "arl", "er", "aris", "are", "ark", "ara", "era", "oren"}
        country_middle_options = [ele for ele in country_middle_options if ele not in unwanted_middle]

chosen_country_middle = random.choice(country_middle_options)

# if “ ” is chosen as the beginning, the first letter of middle has to be capitilized and an end has to be chosen
if chosen_country_beginning == "":
    chosen_country_middle = chosen_country_middle.capitalize()
    country_end_options.remove("")

# if “Syra” is chosen as the beginning, don’t choose a middle
if chosen_country_beginning == "Syra":
    chosen_country_middle = ""

# if "Ar", "Or", or "E" are chosen as the beginning, the vowel at the start of the middle is removed
if chosen_country_beginning in ["Ar", "Or", "E"]:
    chosen_country_middle = chosen_country_middle[1:]

# if a vowel is chosen as the middle, an end has to be chosen
if chosen_country_middle in vowels:
    country_end_options.remove("")

chosen_country_end = random.choice(country_end_options)

# if "Ang" is chosen as the beginning, don’t choose an end
if chosen_country_beginning == "Ang":
    chosen_country_end = ""

country_name = chosen_country_beginning + chosen_country_middle + chosen_country_end

# -------------------------------------------------------------------------------------------------
# CITY NAME

country_middle_options = ["a", "e", "i", "o", "u", "uls", "aris", "acra", "oma", "esa", "oka", "emo", "en", "ara", "era", "ed", "arl", "ithu", "er", "ica", "ash", "ark", "aling", "il", "ub", "otts", "al", "eni", "are", "ins", "oren", "ace", "an", "or", "ef", "ad", "abe", "ong", "uri", "itri", "obou", "astri", "ocu", "ego", "aho", "ose", "ean", "ine", "uco", "yti", "yl", "oya", "one"]
country_end_options = ["more", "min", "ville", "no", "kee", "ta", "co", "worth", "son", "go", "notte", "lotte", "ton", "mis", "nia", "sfield", "cas", "das", "dus", "lus", "tus", "mus", "nor", "ver", "phis", "que", "mento", "land", "lina", "see", "side", "mont", "kane", "dale", "ster", "llin", "wood", "cord", "ley", "ridge", "well", "tura", "vina", "bank", "walk", "ford", "cuse", "vale", "heim", "mark", "stan", "nam", "tu", "bia", "lot", "can", ""]

chosen_city_beginning = random.choice(country_beginning_options)

if chosen_city_beginning != "":
    # if a string ending with "l" is chosen as the beginning, the middle can’t be "uls", "arl", "aling", "al", or "il"
    if chosen_city_beginning[-1] == "l":
        unwanted_middle = {"uls", "arl", "aling", "al", "il"}
        country_middle_options = [ele for ele in country_middle_options if ele not in unwanted_middle]

    # if a string ending with "r" is chosen as the beginning, the middle can’t be "or", "uri", "arl", "er", "aris", "are", "ark", "ara", "era", or "oren"
    if chosen_city_beginning[-1] == "r":
        unwanted_middle = {"or", "uri", "arl", "er", "aris", "are", "ark", "ara", "era", "oren"}
        country_middle_options = [ele for ele in country_middle_options if ele not in unwanted_middle]

chosen_city_middle = random.choice(country_middle_options)

# if “ ” is chosen as the beginning, the first letter of middle has to be capitilized and an end has to be chosen
if chosen_city_beginning == "":
    chosen_city_middle = chosen_city_middle.capitalize()
    country_end_options.remove("")

# if “Syra” is chosen as the beginning, don’t choose a middle
if chosen_city_beginning == "Syra":
    chosen_city_middle = ""

# if "Ar", "Or", or "E" are chosen as the beginning, the vowel at the start of the middle is removed
if chosen_city_beginning in ["Ar", "Or", "E"]:
    chosen_city_middle = chosen_city_middle[1:]

# if a vowel is chosen as the middle, an end has to be chosen
if chosen_city_middle in vowels:
    country_end_options.remove("")

chosen_city_end = random.choice(country_end_options)

# if "Ang" is chosen as the beginning , don’t choose an end
if chosen_city_beginning == "Ang":
    chosen_city_end = ""

city_name = chosen_city_beginning + chosen_city_middle + chosen_city_end
if city_name == country_name:
    city_name += " city"

# -------------------------------------------------------------------------------------------------
# BORDERING COUNTRIES
# reduced list for bordering countries so fewer conditionals are needed
country_middle_options = ["a", "e", "i", "o", "u", "acra", "oma", "esa", "oka", "emo", "en", "ed", "ithu", "ica", "ash", "ark", "ub", "otts", "eni", "ins", "ace", "an", "ef", "ad", "abe", "ong", "itri", "obou", "astri", "ocu", "ego", "aho", "ose", "ean", "ine", "uco", "yti", "yl", "oya", "one"]
country_end_options = ["more", "min", "ville", "no", "kee", "ta", "co", "worth", "son", "go", "notte", "lotte", "ton", "mis", "nia", "sfield", "cas", "das", "dus", "lus", "tus", "mus", "nor", "ver", "phis", "que", "mento", "land", "lina", "see", "side", "mont", "kane", "dale", "ster", "llin", "wood", "cord", "ley", "ridge", "well", "tura", "vina", "bank", "walk", "ford", "cuse", "vale", "heim", "mark", "stan", "nam", "tu", "bia", "lot", "can"]

bordering_countries = []
for i in range(random.randint(0, 7)):
    bordering_country_beginning = random.choice(country_beginning_options)
    bordering_country_middle = random.choice(country_middle_options)
    bordering_country_end = random.choice(country_end_options)

    if bordering_country_beginning == "":
        bordering_country_middle = bordering_country_middle.capitalize()
    if bordering_country_middle == "Syra":
        bordering_country_middle = ""
    if bordering_country_beginning in ["Ar", "Or", "E"]:
        bordering_country_middle = bordering_country_middle[1:]
    
    bordering_country = bordering_country_beginning + bordering_country_middle + bordering_country_end
    if (bordering_country not in bordering_countries) and (bordering_country != country_name) and (bordering_country != city_name):
        bordering_countries.append(bordering_country)
# -------------------------------------------------------------------------------------------------
# COUNTRY DEMONYM 

demonym_end = random.choice(["ish", "ian", "an", "ese"])
demonym = country_name

# gets rid of any vowels at the end of country name
for letter in reversed(demonym):
    if letter in vowels:
        demonym = demonym[:-1]
    else:
        break

demonym = demonym + demonym_end

# -------------------------------------------------------------------------------------------------
# GOVERNMENT TYPE 

government_type_options = ["Triarchy", "Communism", "Representative Democracy", "Direct Democracy", "Democratic Republic", "Socialism", "Theocracy", "Absolute Monarchy", "Oligarchy", "Autocracy", "Provisional", "Republic", "Constitutional Monarchy"]
government_type = random.choice(government_type_options)

# -------------------------------------------------------------------------------------------------

print("\n\033[36m" + "\033[1m" + "General Information:" + "\033[0m" + "\033[00m")
print("\033[1m" + "Country Name: " + "\033[0m" + country_name)
print("\033[1m" + "City Name: " + "\033[0m" + city_name)
print("\033[1m" + "Bordering Countries: " + "\033[0m")
if len(bordering_countries) == 0:
    print(country_name + " is an island, there are no bordering countries.")
else:
    for i in range(1, len(bordering_countries) + 1):
        print("\t" + str(i) + ". " + bordering_countries[i - 1])
print("\033[1m" + "Demonym: " + "\033[0m" + demonym)
print("\033[1m" + "Government Type: " + "\033[0m" + government_type)

# -------------------------------------------------------------------------------------------------
# UNEMPLOYMENT AND EMPLOYMENT RATE

employment_rate = (random.randint(0,10000))/100
unemployment_rate = round(100 - employment_rate, 2)

# -------------------------------------------------------------------------------------------------
# POVERTY RATE

poverty_rate = (random.randint(0, 3000))/100

# -------------------------------------------------------------------------------------------------
# CURRENCY NAME

currency_beginning_options = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "W", "Y", "Z", "Br", "Cl", "Cr", "Dr", "Fr", "Tr", "Fl", "Gl", "Gr", "Pl", "Pr", "Sl", "Sp", "St", "Ch", "Sc", "Sh", "Th"]
currency_middle_options = ["a", "e", "i", "o", "u", "ei", "oo", "ou"]
currency_end_options = [ "min", "no", "pee", "ta", "co", "son", "go", "mis", "dus", "los", "tus", "nor", "ver", "nit", "tu", "can", "ng", "n", "ra", "t", "p", "pin", "nt", "d", "din", "ck"]

# makes sure that the currency name is not the same as the country or city name
currency_name = country_name
while currency_name == country_name or currency_name == city_name:
    currency_name = random.choice(currency_beginning_options) + random.choice(currency_middle_options) + random.choice(currency_end_options)

# -------------------------------------------------------------------------------------------------
# GDP
# random GDP is chosen from 10 billion to 90 trillion

gdp_in_billions = random.randint(10, 1090)
billion = True

# if the GDP is equal or over to 1000, it is converted into trillions 
if gdp_in_billions == 1000:
    gdp = 1
    billion = False
if gdp_in_billions > 1000:
    gdp = str(gdp_in_billions)[2:]
    billion = False

if billion == True:
    gdp = str(gdp_in_billions) + " billion"
if billion == False:
    gdp = str(gdp) + " trillion"

gdp = gdp + " " + currency_name

# -------------------------------------------------------------------------------------------------
# AVERAGE GROSS SALARY

avg_gross_salary = random.randint(20, 10000)
avg_gross_salary = str(avg_gross_salary) + " " + currency_name

# -------------------------------------------------------------------------------------------------
# LABOR FORCE BY OCCUPATION

labor_force_split1 = random.randint(0, 10000)
labor_force_split2 = random.randint(labor_force_split1 + 1, 10000)

services = (labor_force_split1)/100
industry = (labor_force_split2 - labor_force_split1)/100
agriculture = (10000 - labor_force_split2)/100

# -------------------------------------------------------------------------------------------------
# IMPORTS AND EXPORTS

imports_and_exports = ["Pharmaceutical Products", "Refined Petroleum", "Vehicle Parts", "Crude Petroleum", "Gold", "Plastics, plastic articles", "Footwear", "Computers", "Telephones", "Broadcasting Equipment", "Chemical Products", "Articles of Iron or Steel", "Tea", "Tobacco", "Wood", "Fish", "Coffee", "Vanilla", "Cosmetic Products", "Aluminum", "Corn", "Nuts", "Wheat", "Rice", "Dairy Products", "Seafood", "Textiles", "Copper", "Silver", "Fruits and Vegetables", "Confectionery", "Livestock"]
random.shuffle(imports_and_exports)
imports = imports_and_exports[:5]
exports = imports_and_exports[5:10]

# -------------------------------------------------------------------------------------------------

print("\n\033[32m" + "\033[1m" + "Economy:" + "\033[0m" + "\033[00m")
print("\033[1m" + "Employment Rate: " + "\033[0m" + str(employment_rate) + "%")
print("\033[1m" + "Unemployment Rate: " + "\033[0m" + str(unemployment_rate) + "%")
print("\033[1m" + "Poverty Rate: " + "\033[0m" + str(poverty_rate) + "%")
print("\033[1m" + "Currency Name: " + "\033[0m" + currency_name)
print("\033[1m" + "GDP: " + "\033[0m" + gdp)
print("\033[1m" + "Average Gross Salary (monthly): " + "\033[0m" + avg_gross_salary)
print("\033[1m" + "Labor Force by Occupation: " + "\033[0m")
print(f"\tServices: {services}%")
print(f"\tIndustry: {industry}%")
print(f"\tAgriculture: {agriculture}%")
print("\033[1m" + "Top Imports: " + "\033[0m")
for item in imports:
    print("\t" + str((imports.index(item) + 1)) + ". " + item)
print("\033[1m" + "Top Exports: " + "\033[0m")
for item in exports:
    print("\t" + str((exports.index(item) + 1)) + ". " + item)

# -------------------------------------------------------------------------------------------------
# AREA

area = random.randint(50, 15000000)
area_counter = 1

# adds commas to the random area
area_commas = ""
for num in reversed(str(area)):
    area_commas += num
    if area_counter % 3 == 0 and area_counter != len(str(area)):
        area_commas += ","
    area_counter += 1
area_commas = area_commas[::-1] + " kilometers squared"

# -------------------------------------------------------------------------------------------------
# CLIMATE/WEATHER

climate_type_options = ["tropical", "dry", "temperate", "continental", "polar"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
country_region = ["North", "East", "South", "West", "central regions"]
climate_type = random.choice(climate_type_options)
climate_sentence1 = country_name + " has a primarily " + climate_type + " climate. "

if climate_type == "tropical":
    additional = ["There is also very high humidity during the wet season. ", "However, percipitation tends to occur solely during the wet season. ", "The average temperature in every month exceeds " + str(random.randint(18, 20)) + " degrees celcius. "]
    avg_temp = random.randint(25, 30)
    climate_sentence2 = "Due to the high exposure to the sun for tropic countries, " + country_name + " is warm all year, averaging at " + str(avg_temp) + " degrees Celcius. "
    month_chosen_index = random.randint(0, 11)
    climate_sentence3 = country_name + " doesn't experience seasons like other countries, however, there is a wet and dry season. The wet season is from " + months[month_chosen_index] + " to " + months[(month_chosen_index + 17) % 12] + ", and the dry season is from " + months[(month_chosen_index + 18) % 12] + " to " + months[(month_chosen_index + 23) % 12] + ". "
    climate_sentence4 = random.choice(additional)
    climate_sentence5 = "Additionally, annual percipitation is high. It averages at " + str(random.randint(180, 250)) + " centimeters of rain a year and rainfall is typically the highest in the " + random.choice(country_region) + ". "
    climate = climate_sentence1 + climate_sentence2 + climate_sentence3 + climate_sentence4 + climate_sentence5
    climate = textwrap.fill(climate, 90)

if climate_type == "dry":
    dry_climate_type_options = ["arid", "semi-arid"]
    dry_climate_type = random.choice(dry_climate_type_options)
    climate_sentence2 = "There is high evaporation and so land in " + country_name + "is very dry. "
    avg_temp = random.randint(25, 30)
    additional = ["There tends to be a big temperature difference from night to day throughout the entire year. ", "Summers tend to be extremely hot and winter days tend to be cool and warm during the day and colder at night. ", "Although there is summer and winter, dry climates have yearly period of low precipitation. "]
    climate_sentence3 = "The average temperature is " + str(avg_temp) + " degrees Celcius. " + random.choice(additional)
    climate_sentence4 = "Additionally, " + country_name + "'s type of dry climate is " + dry_climate_type + ". "
    if dry_climate_type == "arid":
        climate_sentence5 = "This means that " + country_name + " has a desert climate and receives severe excess of evaporation over precipitation. " + country_name + " receives on average " + str(random.randint(5, 25)) + " centimeters of rain a year. "
    if dry_climate_type == "semi-arid":
        semi_arid_plant_options = ["creosote bush", "bur sage", "white thorn", "cat claw", "mesquite", "brittle bushes", "lyciums", "jujube"]
        random.shuffle(semi_arid_plant_options)
        climate_sentence5 = "Also known as a steppe climate, this means that " + country_name + " receives light rainfall, averaging at approximately " + str(random.randint(26, 50)) + " centimeters of rain a year. The climate is unable to support forests or large vegetation, however, common plants in " + country_name + " includes " + semi_arid_plant_options[0] + ", " + semi_arid_plant_options[1] + ", and " + semi_arid_plant_options[2] + ". "
    climate = climate_sentence1 + climate_sentence2 + climate_sentence3 + climate_sentence4 + climate_sentence5
    climate = textwrap.fill(climate, 90)

if climate_type == "temperate":
    avg_temp = random.randint(0, 18)
    climate_sentence2 = "Temperate climates are moderate climates and so " + country_name + " doesn't have any particularly extreme weather and it cycles through all four seasons. The average temperature is " + str(avg_temp) + " degrees Celcius and the amount of rainfall averages at " + str(random.randint(70, 170)) + " centimeters of rain a year. "
    summer_options = ["mild", "warm"]
    summer_type = random.choice(summer_options)
    if summer_type == "mild":
        summer_temp = random.randint(21, 25)
    else:
        summer_temp = random.randint(25, 30)
    winter_options = ["cool", "cold"]
    winter_type = random.choice(winter_options)
    if winter_type == "cool":
        winter_temp = random.randint(-5, 0)
    else:
        winter_temp = random.randint(-10, -5)
    climate_sentence3 = "There is a large temperature change from summer to winter. Summers tend to be " + summer_type + " and temperatures in the summer average at " + str(summer_temp) + " degrees Celcius. Winters tend to be " + random.choice(winter_options) + " and temperatures in the winter average at " + str(winter_temp) + " degrees Celcius. "
    climate = climate_sentence1 + climate_sentence2 + climate_sentence3
    climate = textwrap.fill(climate, 90)

if climate_type == "continental":
    avg_percipitation = random.randint(60, 120)
    percipitation_spread = random.choice(["well distributed throughout the year", "mostly concentrated in the warmer months"])
    if percipitation_spread == "mostly concentrated in the warmer months":
        warm_month_index = random.randint(3,7)
        warm_months = months[warm_month_index] + " and " + months[warm_month_index + 1]
        percipitation_spread += " which is in " + warm_months
    climate_sentence2 = country_name + "'s climate is a transition zone between mild and polar climates. There is a moderate amount of percipitation that is " + percipitation_spread + " and is mostly in the form of snow. The average percipitaion is " + str(avg_percipitation) + " centimeters a year. "
    climate_sentence3 = "The average temperature in the summer is " + str(random.randint(14, 21)) + " degrees celcius and the average temperature in the winter is " + str(random.randint(-12, -1)) + " degrees celcius. "
    winter_characteristics = ["dry and sunny days with periods of snowfall", "high layers of ice and regular snowstorms", "bitter and cold days with frequent, heavy snowfall", "regular below-freezing temperatures and strong winds", "dry temperatures and shorter days and longer nights"]
    climate_sentence4 = "Winters are much longer than summer and winter in " + country_name + " is typically characterized by " + random.choice(winter_characteristics) + ". "
    climate = climate_sentence1 + climate_sentence2 + climate_sentence3 + climate_sentence4
    climate = textwrap.fill(climate, 90)

if climate_type == "polar":
    avg_temp = random.randint(-20, 5)
    polar_characteristics = ["has strong winds and regular snowstorms", "permananet ice sheets covering the land", "a very dry climate due to the lack of moisture", "treeless tundra, glaciers, and regular and heavy snowfall"]
    climate_sentence2 = "Polar climates don't have warm summers and temperatures never exceed 10 degrees celcius. The average temperature is " + str(avg_temp) + " degrees celcius. "
    climate_sentence3 = country_name + " also has " + random.choice(polar_characteristics) + ". "
    animal_life = ["scarce animal life", "no animal life"]
    climate_sentence4 = "Rainfall is low with the annual amount of rain received averaging at " + str(random.randint(5, 25)) + " centimeters. Due to the harsh conditions, there is " + random.choice(animal_life) + " and minimal plant life. "
    coldest_month_index = random.randint(-2, 1)
    coldest_months = months[coldest_month_index] + " and " + months[coldest_month_index + 1]
    warmest_month_index = random.randint(4, 6)
    warmest_months = months[warmest_month_index] + " and " + months[warmest_month_index + 1]
    climate_sentence5 = "The lowest temperatures are typically in " + coldest_months + " and the warmest temperatures are typically in " + warmest_months + "."
    climate = climate_sentence1 + climate_sentence2 + climate_sentence3 + climate_sentence4 + climate_sentence5
    climate = textwrap.fill(climate, 90)

# -------------------------------------------------------------------------------------------------
# LANDFORMS

landforms = {
    'tropical_landforms': ["rainforest mountains", "valleys", "rivers", "wetlands", "dense forests", "hills", "beaches", "floodplains", "karsts", "waterfalls", "bays", "volcanos", "isthmuses", "cliffs", "swamps", "lakes", "marshes", "plains", "peninsulas"],
    'dry_landforms': ["plains", "wadis", "sand dunes", "mesas", "buttes", "gullies", "plateaus", "canyons", "isthmuses", "peninsulas"],
    'temperate_landforms': ["mountains", "plains", "lakes", "rivers", "plateaus", "peninsulas", "waterfalls", "bays", "volcanos", "isthmuses", "canyons", "cliffs", "forests", "swamps", "marshes", "valleys", "wetlands", "beaches", "floodplains", "hills", "karsts"],
    'continental_landforms': ["plains", "plateaus", "hills", "mountains", "volcanos", "glaciers", "isthmuses", "forests", "lakes", "marshes", "peninsulas", "valleys", "beaches", "taiga"],
    'polar_landforms': ["plateaus", "mountains", "valleys", "plains", "continental glaciers", "tundra", "peninsulas", "alpine glaciers"]
}

# only shuffles appropriate landforms list
landforms_cat = climate_type + "_landforms"
for i in landforms.keys():
    if i == landforms_cat:
        random.shuffle(landforms[i])
random.shuffle(country_region)

landforms = "In " + country_name + ", common landforms/landscapes in the " + country_region[0] + " include " + landforms[landforms_cat][0] + ", " + landforms[landforms_cat][1] + ", and " + landforms[landforms_cat][2] + ". In the rest of " + country_name + ", the most common landforms are " + landforms[landforms_cat][3] + ", " + landforms[landforms_cat][4] + ", and " + landforms[landforms_cat][5] + ". There are very few to no " + landforms[landforms_cat][6] + " and " + landforms[landforms_cat][7] + " are generally limited to the " + country_region[1] + ". "
landforms = textwrap.fill(landforms, 90)

# -------------------------------------------------------------------------------------------------

print("\n\033[35m" + "\033[1m" + "Geography:" + "\033[0m" + "\033[00m")
print("\033[1m" + "Area: " + "\033[0m" + area_commas)
print("\033[1m" + "Climate: " + "\033[0m")
print(climate)
print("\033[1m" + "Landforms/Landscapes: " + "\033[0m")
print(landforms)

# -------------------------------------------------------------------------------------------------
# POPULATION
# weighted random choices for population
population = random.choices([random.randint(800, 100000), random.randint(100000, 1000000), random.randint(1000000, 100000000), random.randint(100000000, 800000000), random.randint(800000000, 1400000000)], [2, 2, 6, 1, 1])[0]

pop_counter = 1
# adds commas to random population
population_commas = ""
for num in reversed(str(population)):
    population_commas += num
    if pop_counter % 3 == 0 and pop_counter != len(str(population)):
        population_commas += ","
    pop_counter += 1
population_commas = population_commas[::-1]

# -------------------------------------------------------------------------------------------------
# MALE AND FEMALE PERCENTAGE

male_pct = (random.randint(4000,6000))/100
female_pct = round(100 - male_pct, 2)

# -------------------------------------------------------------------------------------------------
# MALE AND FEMALE LIFE EXPECTANCY

male_expectancy = (random.randint(5500,8500))/100
female_expectancy = (random.randint(5500,8500))/100

# -------------------------------------------------------------------------------------------------
# FERTILITY RATE
# weighted random choices for fertility rate
fertility_rate = (random.choices([random.randint(8, 16), random.randint(16, 26), random.randint(26, 40), random.randint(40, 70)], [1, 6, 2, 1])[0])/10

# -------------------------------------------------------------------------------------------------
# POPULATION DENSITY

population_split1 = random.randint(0, 10000)
population_split2 = random.randint(population_split1 + 1, 10000)

urban = (population_split1)/100
suburban = (population_split2 - population_split1)/100
rural = (10000 - population_split2)/100

# -------------------------------------------------------------------------------------------------
# LARGEST RELIGION PARAGRAPH DESCRIPTION

religion_name = ["Catholicism", "Judaism", "Buddhism", "Atheism", "Agnosticism", "Hinduism", "Confucianism", "Sikhism", "Gnosticism", "Jainism", "Orthodoxy", "Protestantism", "Shintoism", "Taoism", "The Bahá'í Faith", "The Druze Faith", "Islam"]
religion_adj =  ["Catholic", "Jewish", "Buddhist", "Atheist", "Agnostic", "Hindu", "Confucianist", "Sikh", "Gnostic", "Jain", "Orthodox", "Protestant", "Shinto", "Taoist", "Bahá'í", "Druze", "Muslim"]

# shuffles religion_name and religion_adj in the same order
temp = list(zip(religion_name, religion_adj))
random.shuffle(temp)
religion_name_rdm, religion_adj_rdm = zip(*temp)
religion_name_rdm, religion_adj_rdm = list(religion_name_rdm), list(religion_adj_rdm)

# weighted random choices for top religion percentage
top_rlgn_pct = (random.choices([random.randint(200, 490), random.randint(500, 740), random.randint(750, 990), 1000], [3, 4, 3, 2])[0])/10

if (top_rlgn_pct * 10) == 1000:
    top_rlgn_sentence = "There is a single religion in " + country_name + " with 100 % of the population identifying as " + str(religion_adj_rdm[0]) + ". "
    range = 4
if 750 <= (top_rlgn_pct * 10) < 1000:
    top_rlgn_sentence = "The overwhelming majority of the " + demonym + " population is " + str(religion_adj_rdm[0]) + " with an estimated " + str(top_rlgn_pct) + " % of the population identifying as " + str(religion_adj_rdm[0]) + ". "
    range = 3
if 500 <= (top_rlgn_pct * 10) < 750:
    top_rlgn_sentence = "Most of the " + demonym + " population belongs to the religion of " + str(religion_name_rdm[0]) + " with an estimated " + str(top_rlgn_pct) + " % of the population identifying as " + str(religion_adj_rdm[0]) + ". "
    range = 2
if 200 <= (top_rlgn_pct * 10) < 500:
    top_rlgn_sentence = "In " + country_name + ", there is no religion that makes up the majority of the poupulation. The largest religion is " + str(religion_name_rdm[0]) + " which " + str(top_rlgn_pct) + " % of the population identifies as. "
    range = 1

religion_sentences = {
'rlgn_pct_range1': ["Religion greatly varies depending on the country region with " + str(religion_name_rdm[0]) + " being significantly more common in the " + random.choice(country_region) + ". ", "Freedom of religion is constitutionally ensured regardless of one's faith so long as its practices do not harm others. ", "Festivals, celebrations, and such organizations are commonly organized by different religious groups in " + country_name + " to celebrate and publicize certain reglious beliefs. ", "Many religions in " + country_name + " came from and were influenced by religions from other countries with people like immigrants and missionaries coming to " + country_name + " bringing new religous ideas. ", random.choice(["Places of worship are very common and can be found all over the country. ", "Places of worhsip are limited to more populated areas, particularly the capital city. "]), str(religion_name_rdm[0]) + " has been the largest religion in " + country_name + " for just over " + str(random.randint(5, 100)) + " years. "],
'rlgn_pct_range2': ["Religion greatly varies depending on the country region with " + str(religion_name_rdm[0]) + " being significantly more common in the " + random.choice(country_region) + ". ", "Freedom of religion is constitutionally ensured regardless of one's faith so long as its practices do not harm others. ", "Festivals, celebrations, and such organizations are commonly organized by different religious groups, especially by " + str(religion_adj_rdm[0]) + "s to celebrate and publicize certain reglious beliefs. ", "The current religions in " + country_name + " were highly influenced by religions from bordering countries. ", random.choice(["Places of worship are very common and can be found all over the country. ", "Places of worhsip are limited to more populated areas, particularly the capital city. "]), str(religion_name_rdm[0]) + " has been the largest religion in " + country_name + " for just over " + str(random.randint(5, 100)) + " years. "],
'rlgn_pct_range3': ["There is high pressure from the government and society to be " + str(religion_adj_rdm[0]) + ". ", "The citizens have little exposure to other religions. ", str(religion_adj_rdm[0]) + " teachings are mandated in public schools and also highly encouraged in private schools. ", "Religion greatly varies depending on the country region with " + str(religion_name_rdm[0]) + " being significantly more common in the " + random.choice(country_region) + ". ", "Freedom of religion is constitutionally ensured regardless of one's faith so long as its practices do not harm others. ", "The presence of " + str(religion_name_rdm[0]) + " in " + country_name + " is historically and culturally pervasive. ", "Festivals, celebrations, and such organizations are common in " + country_name + " to celebrate and publicize " + str(religion_adj_rdm[0]) + " beliefs. The current religion in " + country_name + " was highly influenced by religions from bordering countries. ", random.choice(["Places of worship are very common and can be found all over the country. ", "Places of worhsip are limited to more populated areas, particularly the capital city. "]), str(religion_name_rdm[0]) + " has been the largest religion in " + country_name + " for just over " + str(random.randint(5, 100)) + " years. "],
'rlgn_pct_range4': ["There is extremely high pressure from the government and society to be " + str(religion_adj_rdm[0]) + ". ", "The citizens have little exposure to other religions. ", str(religion_adj_rdm[0]) + " teachings are mandated at both public and private schools. ", "There is no freedom of religion in " + country_name + " with " + str(religion_adj_rdm[0]) + " practices being mandated and regularly enforced. ", "The presence of " + str(religion_name_rdm[0]) + " in " + country_name + " is incredibly historically and culturally pervasive. ", "Festivals, celebrations, and such organizations are common in " + country_name + " to celebrate and publicize " + str(religion_name_rdm[0]) + " and " +   str(religion_adj_rdm[0]) + " beliefs. ", "The current religion in " + country_name + " was highly influenced by religions from bordering countries. ", random.choice(["Places of worship are very common and can be found all over the country. ", "Places of worhsip are limited to more populated areas, particularly the capital city. "]), str(religion_name_rdm[0]) + " has been the largest religion in " + country_name + " for just over " + str(random.randint(5, 100)) + " years. "]
}

# only shuffles appropriate religion list
religion_sentences_name = "rlgn_pct_range" + str(range)
for i in religion_sentences.keys():
    if i == religion_sentences_name:
        random.shuffle(religion_sentences[i])

# description is top_rlgn_sentenc and 3 randomly chosen sentences from the appropriate list
full_religion_descr = top_rlgn_sentence + religion_sentences[religion_sentences_name][0] + religion_sentences[religion_sentences_name][1] + religion_sentences[religion_sentences_name][2]
full_religion_descr = textwrap.fill(full_religion_descr, 90)

# -------------------------------------------------------------------------------------------------
# RELIGION PERCENTAGE DISTRIBUTION

religion_percentages = {
religion_name_rdm[0]: top_rlgn_pct, 
}

# continues adding religions with random percentages to the dictionary until total percentage exceds 95%
religion_counter = 1
religion_pct_sum = top_rlgn_pct * 10
while religion_pct_sum < 950:
    current_religion = religion_name_rdm[religion_counter]
    religion_counter += 1
    current_religion_pct = random.randint(50, 1000 - religion_pct_sum)
    while (current_religion_pct/10) > top_rlgn_pct:
        current_religion_pct = random.randint(50, 1000 - religion_pct_sum)
    religion_pct_sum += current_religion_pct
    religion_percentages[current_religion] = current_religion_pct/10

if religion_pct_sum != 1000:
    religion_percentages['Other'] = (1000 - religion_pct_sum)/10

# -------------------------------------------------------------------------------------------------

print("\n\033[31m" + "\033[1m" + "Population:" + "\033[0m" + "\033[00m")
print("\033[1m" + "Population: " + "\033[0m" + population_commas)
print("\033[1m" + "Male Percentage: " + "\033[0m" + str(male_pct) + " %")
print("\033[1m" + "Female Percentage: " + "\033[0m" + str(female_pct) + " %")
print("\033[1m" + "Male Life Expectancy: " + "\033[0m" + str(male_expectancy) + " years")
print("\033[1m" + "Female Life Expectancy: " + "\033[0m" + str(female_expectancy) + " years")
print("\033[1m" + "Fertility Rate: " + "\033[0m" + str(fertility_rate) + " births per woman")
print("\033[1m" + "Population Density: " + "\033[0m")
print(f"\tUrban: {urban}%")
print(f"\tSuburban: {suburban}%")
print(f"\tRural: {rural}%")
print("\033[1m" + "Largest Religion: " + "\033[0m")
print(full_religion_descr)
print("\033[1m" + "Religions by Percentages: " + "\033[0m")
for i in religion_percentages.items():
    print(f"\t{i[0]}: {i[1]}%")

# -------------------------------------------------------------------------------------------------
# TRADITIONS/CUSTOMS

tradition_aspects = {
'tradition_group_options': ["for kids", "for adults", "for teenagers", "for the elderly", "for women", "for men", "for everyone"],
'tradition_options': ["carve/decorate " + random.choice(["pumpkins", "radishes", "skulls", "apples", "trees", "eggs"]), random.choice(["cut", "dye", "trim", "shave", "curl", "braid", "freeze"]) + " their hair", "perform a " + random.choice(["self-made", "traditional"]) + " dance", "learn how to play a new " + random.choice(["instrument", "piano", "violin", "guitar", "drum"]) + " piece", "go " + random.choice(["swimming", "on a run", "to the airport", "to the beach", "hunting"]), random.choice(["avoid ", "increase "]) + random.choice(["salt", "sugar", "meat", "fish", "dairy", "sweets", "chocolate"]) + " in the food they eat", "sit in the " + random.choice(["middle car seat", "trunk of the car"]), "greet people with a " + random.choice(["nod", "high five", "spin", "clap", "snap"]), "receive " + random.choice(["flowers", "gifts", "fruits", "vegetables"]) + " from their " + random.choice(["parents", "relatives", "siblings"]), "write with their " + random.choice(["non-dominant hand", "feet", "elbows"]), "point at others with their " + random.choice(["thumb", "middle finger", "pinkie", "ring finger", "feet"]), "throw " + random.choice(["oranges", "apples"]) + " at one another", "get " + random.choice(["pinched", "sprayed with water", "punched", "up before sunrise", "up at sunset"]), "bake " + random.choice(["money", "a figurine", "a coin", "a ribbon", "a string", "a ring"]) + " into a traditional dish", "avoid " + random.choice(["speaking", "exercising", "tying their shoelaces", "showering", "getting wet", "producing trash", "eating breakfast"]), "wear " + random.choice(["traditional clothing", "scary costumes", "formal clothing", "black", "white", "green", "hats", "animal costumes"]), "release " + random.choice(["lanterns", "balloons"]) + " into the sky", "launch " + random.choice(["rockets", "fireworks"]), "drink " + random.choice(["beer", "wine", "alcohol", "vodka"]), "burn " + random.choice(["a piece of clothing", "plants", "stacks of paper", "planks of wood"]), "eat " + random.choice(["fruit seeds", "insects", "only animals"]), "mount " + random.choice(["hills", "horses", "trees", "flights of stairs"])],
'tradition_frequency': ["once a month", "on their birthday", "on the" + random.choice([" first ", " last "]) + "day of " + random.choice(months), "on the" + random.choice([" first ", " last "]) + "day of " + random.choice(["spring", "winter", "autumn", "summer"]), "on New Years Eve", "during " + random.choice(months)]
}

for i in tradition_aspects.values():
        random.shuffle(i)

tradition1 = f"It is tradition {tradition_aspects['tradition_group_options'][0]} to {tradition_aspects['tradition_options'][0]} {tradition_aspects['tradition_frequency'][0]}."
tradition2 = f"It is tradition {tradition_aspects['tradition_group_options'][1]} to {tradition_aspects['tradition_options'][1]} {tradition_aspects['tradition_frequency'][1]}."
tradition3 = f"It is tradition {tradition_aspects['tradition_group_options'][2]} to {tradition_aspects['tradition_options'][2]} {tradition_aspects['tradition_frequency'][2]}."

# -------------------------------------------------------------------------------------------------
# ARCHITECTURE

arch_types = ["modern", "classical", "Gothic", "Victorian", "neoclassical", "Byzantine", "industrial"]
arch_types_features = [["asymmetrical designs", "walls of glass", "large windows", "a mix of modern and traditional building materials", "flat roofs", "neutral color palettes", "an emphasis on rectangular forms and horizontal/vertical lines", "open floorplans"], ["symmetrical designs", "rectangular windows", "strudy/durable materials (e.g., stone, brick, concrete, marble, terracotta tile)", "an emphasis on symmetry, proportion, and harmony", "structures such as columns, pediments, arches, and domes", "front porches"], ["large stained glass windows", "pointed arches", "vaulted ceilings", "flying buttresses", "spires", "designs made of stone or iron", "ornate stone decorations", "gargoyles", "grand and tall designs", "large doors"], ["structures with two to three stories", "wooden or stone exteriors", "complicated and asymmetrical designs", "decorative trims", "textured wall surfaces", "steep and multi-faceted roofs", "one-story porches", "towers and turrets", "vibrant colors", "small gardens"], ["grand designs", "simple geometric shapes", "structures such as columns, pediments, arches, and domes", "blank walls", "flat roofs", "strudy/durable materials (e.g., stone, brick, concrete, marble, terracotta tile)", "domed roofs", "repeated classical patterns"], ["massive domes with square bases", "rounded arches", "spires", "lofty and towering interior spaces", "strucutures made of brick, stone, and marble", "rich colors", "arch windows"], ["large and open floor plans", "high ceilings", "raw rough materials used (e.g., conrete, brick, metal)", "minimalist designs", "lots of natural light", "monochromatic colors"]]
arch_mats = ["wood", "stone", "sand", "steel", "concrete", "plastic", "glass", "brick", "bamboo", "fabric", "terracotta", "marble"]
random.shuffle(arch_mats)

# shuffles arch_types and arch_types_features in the same order
temp = list(zip(arch_types, arch_types_features))
random.shuffle(temp)
arch_types_rdm, arch_types_features_rdm = zip(*temp)
arch_types_rdm, arch_types_features_rdm = list(arch_types_rdm), list(arch_types_features_rdm)

# shuffles each list in arch_types_features list
for arch_type in arch_types_features_rdm:
    random.shuffle(arch_type)

arch_types_distr_options = ["is typically described as " + arch_types_rdm[0] + " architecture. ", "is characterized as a mix between " + arch_types_rdm[0] + " and " + arch_types_rdm[1] + " architecture. ", "is most commonly said to be " + arch_types_rdm[0] + " architecture, however, he architecture does tend to vary from city to city. ", "greatly varies from region to region and you will easily find " + arch_types_rdm[0] + ", " + arch_types_rdm[1] + ", and " + arch_types_rdm[2] + " architecture all around the country. "]
arch_types_distr = random.choice(arch_types_distr_options)

# gets index of chosen architecture distribution
for option in arch_types_distr_options:
    if arch_types_distr == option:
        arch_types_index = arch_types_distr_options.index(arch_types_distr)

arch_other_features = [demonym + " architecture is well integrated into the natural setting. ", "There has recently been a new emphasis put on preserving the environment with the architecture. ", demonym + " architecture has greatly changed in the last " + str(random.randint(5,20)) + " years with there being an emphasis put on " + arch_types_rdm[0] + " architecture. ", "It is oftentimes said to be distinct and instantly recognizable. ", "It is meant to be representative of the country and its people while still being conventional and sustainable. ", "There can be some variation with the architecture style from region to region, however, for the most part, the architecture imitates that of the Victorian era. ", "It is often appreciated for its structure and attention to detail in the design. ", "Today, new homes are regularly being built across the country that reinterpret past building methods and construction techniques. ", "The architecture has been greatly influenced by different historical periods along with other countries' architectural designs. ", demonym + " architecture also reflects the country's origins, bringing to life the culture and personality of the nation. "]
random.shuffle(arch_other_features)

# different sentence structure depending on the architecture distribution and other architectural details that fit with the chosen architecture type(s)
if arch_types_index == 0:
     arch_features = f"You will easily find {arch_types_features_rdm[0][0]}, {arch_types_features_rdm[0][1]}, and {arch_types_features_rdm[0][2]}. "
if arch_types_index == 1:
    arch_features = f"Particularly in the {random.choice(country_region)}, you will see influences of {arch_types_rdm[0]} architecture. In these areas, you will easily find {arch_types_features_rdm[0][0]}, {arch_types_features_rdm[0][1]}, and {arch_types_features_rdm[0][2]}. In the rest of {country_name}, you will largely see {arch_types_rdm[1]} architecture. Here, you will most likely find {arch_types_features_rdm[1][0]}, {arch_types_features_rdm[1][1]}, and {arch_types_features_rdm[1][2]}. "
if arch_types_index == 2:
    arch_features = f"In most of {country_name}, aside from the {random.choice(country_region)}, there will primarily be {arch_types_rdm[0]} architecture. And so, almost wherever you go, you can find {arch_types_features_rdm[0][0]}, {arch_types_features_rdm[0][1]}, and {arch_types_features_rdm[0][2]}. "
if arch_types_index == 3:
    arch_features = f"The {country_region[-2]}, is generally characterized by {arch_types_rdm[0]} architecture. Here, you will find {arch_types_features_rdm[0][0]}, {arch_types_features_rdm[0][1]}, and {arch_types_features_rdm[0][2]}. In the {country_region[-1]}, you will mostly see {arch_types_rdm[1]} architecture. This oftentimes consists of {arch_types_features_rdm[1][0]}, {arch_types_features_rdm[1][1]}, and {arch_types_features_rdm[1][2]}. And elsewhere in {country_name}, it will mostly be {arch_types_rdm[2]} architecture which includes {arch_types_features_rdm[2][0]}, {arch_types_features_rdm[2][1]}, and {arch_types_features_rdm[2][2]}. "

# capitlization issue
if arch_other_features[1].split()[0] != demonym:
    arch_other_features[1] = arch_other_features[1][0].lower() + arch_other_features[1][1:]

architecture = demonym + " architecture " + arch_types_distr + arch_features + arch_other_features[0] + "And additionally, " + arch_other_features[1]
architecture = textwrap.fill(architecture, 90)

# -------------------------------------------------------------------------------------------------

print("\n\033[33m" + "\033[1m" + "Culture:" + "\033[0m" + "\033[00m")
print("\033[1m" + "Traditions: " + "\033[0m")
print(tradition1 + "\n" + tradition2 + "\n" + tradition3)
print("\033[1m" + "Architecture: " + "\033[0m")
print(architecture)
