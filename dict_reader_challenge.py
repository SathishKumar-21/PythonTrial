import csv

file_name = 'country_info.txt'
countries = {}
dialect = csv.excel
dialect.delimiter = '|'
with open(file_name, encoding='utf-8', newline='') as country_file:
    # sample = ""
    # for i in range(3):
    #     sample += country_file.readline()
    # country_dialect = csv.Sniffer().sniff(sample)
    # country_file.seek(0)
    headings = country_file.readline().strip("/n").split(dialect.delimiter)
    for i, v in enumerate(headings):
        headings[i] = v.casefold()
    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row
while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        if len(country_key) == 2:
            print(f"The capital of {country_data['country']}({country_key}) is {country_data['capital']}")
        else:
            print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif country_key == 'quit':
        break
