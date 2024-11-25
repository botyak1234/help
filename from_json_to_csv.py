import json
import csv


with open('const.json', 'r', encoding='utf-8') as json_file:
    constellations = json.load(json_file)


fields = [
    "star_name", "brightness",
    "constellation_name", "abbreviation", "area",
    "neighbors"
]


with open('stars.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=',')
    writer.writeheader()

    for constellation in constellations:
        for star in sorted(constellation["brightest_stars"], key=lambda star: star["brightness"]):
            writer.writerow({
                "star_name": star["name"],
                "brightness": star["brightness"],
                "constellation_name": constellation["latin_name"],
                "abbreviation": constellation["abbreviation"],
                "area": constellation["area"],
                "neighbors": "; ".join(constellation["neighbors"])
            })

print("CSV-файл успешно создан: stars.csv")
