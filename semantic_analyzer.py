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
                        f"{word} {udpipe_result[i+1]} {udpipe_result[i+2]}")
                elif word in find_list:
                    task.append(word)

        return task

    def find_side(self, elements, triangle_name):
        for key, value in elements.items():
            # Check if the key matches any part of the triangle name
            if triangle_name and (key.startswith(triangle_name[0]) and key.endswith(triangle_name[2])):
                triangle_base_part = value
                return float(triangle_base_part)
            elif triangle_name and (key.startswith(triangle_name[0]) or key.endswith(triangle_name[2])):
                triangle_base_part = value
                return float(triangle_base_part) * 2

        if "периметр" in elements:
            perimeter = float(elements["периметр"])
            return round(perimeter / 3, 2)
        elif "площа" in elements:
            area = float(elements["площа"])
            return round(pow((area * 4) / pow(3, 0.5), 0.5), 2)
        elif "висота" in elements:
            height = float(elements["висота"])
            return round((height * 2) / pow(3, 0.5), 2)
        elif "бісектриса" in elements:
            bisector = float(elements["бісектриса"])
            return round((bisector * 2) / pow(3, 0.5), 2)
        elif "бісектрис" in elements:
            bisector = float(elements["бісектрис"])
            return round((bisector * 2) / pow(3, 0.5), 2)
        elif "медіана" in elements:
            median = float(elements["медіана"])
            return round((median * 2) / pow(3, 0.5), 2)
        elif "середній лінія" in elements:
            middle_line = float(elements["середній лінія"])
            return round((middle_line * 2), 2)
        elif "радіус вписаний коло" in elements:
            inscribed_radius = float(elements["радіус вписаний коло"])
            return round((inscribed_radius * 6) / pow(3, 0.5), 2)
        elif "радіус описаний коло" in elements:
            unscribed_radius = float(elements["радіус описаний коло"])
            return round((unscribed_radius * pow(3, 0.5)), 2)

        return 0.0

    def calculate(self, tasks, elements, triangle_name):
        side_given = "сторона" in elements
        results = []

        # Find the side if not already given
        side = float(elements.get("сторона", 0)
                     ) if side_given else self.find_side(elements, triangle_name)

        if side == 0.0 and elements:  # Check if the side could not be determined
            return ["Error: Unable to calculate without a valid side or triangle base."]

        print(f"Side: {side}")
        for task in tasks:

            if elements is None and task in "кут":
                results.append(f"{task}: 60")

            if task == "площа":
                result = round((pow(side, 2) * pow(3, 0.5)) / 4, 2)
                results.append(f"{task}: {result}")

            elif task == "периметр":
                result = round(side * 3, 2)
                results.append(f"{task}: {result}")

            elif task == "кут":
                results.append(f"{task}: 60")

            elif task == "angles":
                results.append(f"{task}: 180")

            elif task in ["висота", "бісектриса", "бісектрис", "медіана"]:
                result = round((pow(3, 0.5) * side) / 2, 2)
                results.append(f"{task}: {result}")
            elif task == "радіус вписаний коло":
                result = round((pow(3, 0.5) * side) / 6, 2)
                results.append(f"{task}: {result}")
            elif task == "радіус описаний коло":
                result = round((pow(3, 0.5) * side) / 3, 2)
                results.append(f"{task}: {result}")
            elif task.startswith("середній лінія"):
                result = round(side / 2, 2)
                results.append(f"{task}: {result}")

        return results if results else ["No valid tasks found."]
