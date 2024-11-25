import csv


def analyze_data(file_path):
    total_distance_7_to_9 = 0
    total_mass_osinki = 0
    count_osinki = 0
    total_fuel_1_to_3 = 0
    total_mass_berezki = 0
    count_berezki = 0

    with open(file_path, encoding='cp1251') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)

        for row in reader:
            date = row[0]
            departure = row[1]
            destination = row[2]
            distance = int(row[3])
            fuel = float(row[4])
            mass = int(row[5])

            if date in ['7 октября', '8 октября', '9 октября']:
                total_distance_7_to_9 += distance

            if departure == 'Осинки':
                total_mass_osinki += mass
                count_osinki += 1

            if date in ['1 октября', '2 октября', '3 октября']:
                total_fuel_1_to_3 += fuel

            if destination == 'Березки':
                total_mass_berezki += mass
                count_berezki += 1

    avg_mass_osinki = total_mass_osinki / count_osinki
    avg_mass_berezki = total_mass_berezki / count_berezki

    return {
        "total_distance_7_to_9": total_distance_7_to_9,
        "avg_mass_osinki": avg_mass_osinki,
        "total_fuel_1_to_3": total_fuel_1_to_3,
        "avg_mass_berezki": avg_mass_berezki,
    }


if __name__ == "__main__":
    file_path = 'task19.csv'
    result = analyze_data(file_path)

    print("На какое суммарное расстояние были произведены перевозки с 7 по 9 октября?")
    print(f"Ответ: {result['total_distance_7_to_9']} км")

    print("Какова средняя масса груза при автоперевозках, осуществлённых из города Осинки?")
    print(f"Ответ: {result['avg_mass_osinki']} кг")

    print("Какой суммарный расход бензина был при осуществлении перевозок с 1 по 3 октября?")
    print(f"Ответ: {result['total_fuel_1_to_3']} литров")

    print("Какова средняя масса груза при автоперевозках, осуществлённых в город Березки?")
    print(f"Ответ: {result['avg_mass_berezki']} кг")
