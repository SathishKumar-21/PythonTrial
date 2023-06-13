countries = {}
with open("country_info.txt") as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip().split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        country_dict = {
            'name': country,
            'capital': capital,
            'code': code,
            'code3': code3,
            'dialing': dialing,
            'timezone': timezone,
            'currency': currency
        }
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

while True:
    coun = input("Enter the country to find its capital: ").casefold()
    cap = countries.get(coun, f"There is no country called \"{coun}\" in this world")
    if coun == 'quit':
        break
    elif coun in countries:
        print(f"The capital of {coun} is {cap['capital']}")
    else:
        print(cap)

