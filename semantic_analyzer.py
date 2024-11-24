class SemanticAnalyzer:

    def __init__(self, udpipe_result):
        self.result = udpipe_result

    def extract_task(self, udpipe_result):
        find_list = ["периметр", "площа", "кут", "висота",
                     "бісектриса", "бісектрис", "медіана", "сторона", "радіус", "середній"]
        task = []
        start_checking = False

        for i, word in enumerate(udpipe_result):
            if word == "знайти":
                start_checking = True
                continue

            if start_checking:
                # Check bounds
                if word == "радіус" and i + 2 < len(udpipe_result):
                    task.append(
                        f"{word} {udpipe_result[i+1]} {udpipe_result[i+2]}")
                # Check bounds
                elif word == "середній" and i + 2 < len(udpipe_result):
                    task.append(
                        f"{word} {udpipe_result[i+1]} {udpipe_result[i+2].upper()}")
                elif word in find_list and len(udpipe_result[i+1]) == 2:
                    task.append(f"{word} {udpipe_result[i+1].upper()}")
                elif word in find_list:
                    task.append(word)

        return task

    def find_side(self, elements, triangle_name):
        print("Сторона не вказана. Знайдіть сторону на основі заданих елементів.")
        # Convert all keys in elements to lowercase
        elements = {key.lower(): value for key, value in elements.items()}

        for key, value in elements.items():
            try:
                # Try converting the value to float
                value = float(value)
            except ValueError:
                # Skip the current key if the value is not numeric
                continue

            # Check if the key matches any part of the triangle name
            if triangle_name and (key.startswith(triangle_name[0]) and key.endswith(triangle_name[2])):
                print("Сторона знайдена на основі назви трикутника.")
                return value
            elif triangle_name and (key.startswith(triangle_name[0]) or key.endswith(triangle_name[2])):
                print("Сторона знайдена на основі назви трикутника.")
                return value * 2
            elif key.startswith("висота") or key.startswith("бісектриса") or key.startswith("бісектрис") or key.startswith("медіана"):
                print(
                    "Щоб знайти сторону, маючи висоту, бісектрису або медіану (l), формула: a = (l * 2 * √3) /3.")
                return round((value * 2) / pow(3, 0.5), 2)
            elif key.startswith("середній лінія"):
                print(
                    "Щоб знайти сторону, маючи середню лінію (m), формула: a = m * 2.")
                print(f"Сторона = {value * 2}")
                return round(value * 2, 2)

        # Handle cases based on known keys
        if "периметр" in elements:
            try:
                print(
                    "Формула сторони через периметр: a = P / 3, P - периметр трикутника.")
                print(f"Сторона = {float(elements['периметр']) / 3}")
                perimeter = float(elements["периметр"])
                return round(perimeter / 3, 2)
            except ValueError:
                pass
        elif "площа" in elements:
            try:
                # fmt: off
                print(
                    "Формула сторони через площу: a = √((4 * S) / √3), S - площа трикутника.")
                print(f"Сторона = {round(pow((float(elements['площа']) * 4) / pow(3, 0.5), 0.5), 2)}")
                area = float(elements["площа"])
                return round(pow((area * 4) / pow(3, 0.5), 0.5), 2)
            except ValueError:
                pass
        elif "радіус вписаний коло" in elements:
            try:
                print(
                    "Формула сторони через радіус вписаного кола: a = (r * 6) / √3, r - радіус вписаного кола.")
                print(f"Сторона = {round((float(elements['радіус вписаний коло']) * 6) / pow(3, 0.5), 2)}")
                inscribed_radius = float(elements["радіус вписаний коло"])
                return round((inscribed_radius * 6) / pow(3, 0.5), 2)
            except ValueError:
                pass
        elif "радіус описаний коло" in elements:
            try:
                print(
                "Формула сторони через радіус описаного кола: a = R / √3, R - радіус описаного кола.")
                print(f"Сторона = {round(float(elements['радіус описаний коло']) / pow(3, 0.5), 2)}")
                unscribed_radius = float(elements["радіус описаний коло"])
                return round((unscribed_radius * pow(3, 0.5)), 2)
            except ValueError:
                pass

        # Default return value if no valid side found
        return 0.0

    def calculate(self, tasks, elements, triangle_name):
        print("\nКроки для знаходження:")
        side_given = "сторона" in elements
        results = []

        # Find the side if not already given
        side = float(elements.get("сторона", 0)
                     ) if side_given else self.find_side(elements, triangle_name)

        if side == 0.0 and elements:  # Check if the side could not be determined
            return ["Error: Unable to calculate without a valid side or triangle base."]

        if side == 0.0:
            print("Для даного завдання сторона непотрібна.")


        for task in tasks:

            if elements is None and task in "кут":
                results.append(f"{task}: 60")

            if task == "площа":
                print(
                    "Формула площв: S = (a^2 * √3) / 4 , a - сторона трикутника.")
                print(f"S = {round((pow(side, 2) * pow(3, 0.5)) / 4, 2)} (од^2)")

                result = round((pow(side, 2) * pow(3, 0.5)) / 4, 2)
                results.append(f"{task}: {result}")

            elif task == "периметр":
                print("Формула периметру: P = 3 * a, a - сторона трикутника.")
                print(f"P = {round(side * 3, 2)} (од)")
                result = round(side * 3, 2)
                results.append(f"{task}: {result}")

            elif task == "кут":
                print("У рівносторонньому трикутнику всі кути дорівнюють 60 градусів.")
                results.append(f"{task}: 60")

            elif task == "angles":
                results.append(f"{task}: 180")
            # fmt: off
            elif any(task.startswith(prefix) for prefix in ["висота", "бісектриса", "бісектрис", "медіана"]):
                print(
                    "У рівносторонньому трикутнику висота, медіана та бісектриса співпадають.")
                print(
                    "Формула вистоти, медаіани, бісектриси: h = (a * √3) /2 , a - сторона трикутника.")
                print(f"{task.capitalize()} = {round((pow(3, 0.5) * side) / 2, 2)}")

                result = round((pow(3, 0.5) * side) / 2, 2)
                results.append(f"{task}: {result}")
            elif task == "радіус вписаний коло":
                print(
                    "Формула вписаного кола: r = (a * √3) / 6 , a - сторона трикутника.")
                print(f"{task.capitalize()} = {round((pow(3, 0.5) * side) / 6, 2)}")

                result = round((pow(3, 0.5) * side) / 6, 2)
                results.append(f"{task}: {result}")

            elif task == "радіус описаний коло":
                print(
                    "Формула описаного кола: R = a * √3 , a - сторона трикутника.")
                print(f"{task.capitalize()} = {round((pow(3, 0.5) * side) / 3, 2)}")
                result = round((pow(3, 0.5) * side) / 3, 2)
                results.append(f"{task}: {result}")
            elif task.startswith("середній лінія"):
                print(
                    "Формула медіани: m = a / 2 , a - сторона трикутника.")
                print(f"{task.capitalize()} =  {round(side / 2, 2)}")
                result = round(side / 2, 2)
                results.append(f"{task}: {result}")

        return results if results else ["No valid tasks found."]
