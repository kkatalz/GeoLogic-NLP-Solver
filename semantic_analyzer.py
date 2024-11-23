class SemanticAnalyzer:

    def __init__(self, udpipe_result):
        self.result = udpipe_result

    def extract_task(self, udpipe_result):
        find_list = ["периметр", "площа", "кут",
                     "висота", "бісектриса", "бісектрис", "медіана", "сторона", "радіус"]
        task = []
        start_checking = False

        for i in range(len(udpipe_result)):
            if udpipe_result[i] == "знайти":
                start_checking = True  # Start checking words after this
                continue
            elif udpipe_result[i] == "радіус":
                task.append(
                    udpipe_result[i] + " " + udpipe_result[i+1] + " " + udpipe_result[i+2])
            elif start_checking and udpipe_result[i] in find_list:
                task.append(udpipe_result[i])

        return task

    def find_side(self, elements):
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
        elif "медіана" in elements:
            median = float(elements["медіана"])
            return round((median * 2) / pow(3, 0.5), 2)

    def calculate(self, tasks, elements):
        side_given = "сторона" in elements
        results = []

        # Find the side if not already given
        side = float(elements.get("сторона", 0)
                     ) if side_given else self.find_side(elements)
        print(f"Side is given: {self.find_side(elements)}")
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

        return results if results else ["No valid tasks found."]
