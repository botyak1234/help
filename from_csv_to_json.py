import csv
import json


with open('stars.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')

    constellations_dict = {}
    for row in reader:
        constellation_name = row["constellation_name"]
        if constellation_name not in constellations_dict:
            constellations_dict[constellation_name] = {
                "latin_name": constellation_name,
                "abbreviation": row["abbreviation"],
                "area": int(row["area"]),
                "brightest_stars": [],
                "neighbors": row["neighbors"].split("; ")
            }
        constellations_dict[constellation_name]["brightest_stars"].append({
            "name": row["star_name"],
            "brightness": float(row["brightness"])
        })


constellations = list(constellations_dict.values())


with open('reconstructed_consts.json', 'w', encoding='utf-8') as json_file:
    sorted_constellations = sorted(constellations, key=lambda c: c["area"], reverse=True)
    json.dump(sorted_constellations, json_file, ensure_ascii=False, indent=4)

print("JSON-файл успешно восстановлен: reconstructed_const.json")
