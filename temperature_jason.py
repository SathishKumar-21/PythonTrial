import json
import urllib.request

# data_source = "temperature_anomaly.json"
data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/9/1850-2023.json"

# with open(data_source, encoding="UTF-8") as data:
with urllib.request.urlopen(data_source) as jason_stream:
    data = jason_stream.read().decode('utf-8')
    anomalies = json.loads(data)
print(anomalies["description"])
for year, value in anomalies["data"].items():
    year, value = int(year), float(value)
    print(f"{year}...{value:6.2f}")
print("*" * 80)
