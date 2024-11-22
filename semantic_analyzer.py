class SemanticAnalyzer:

    def __init__(self, udpipe_result):
        self.result = udpipe_result

    def extract_task(self, udpipe_result):
        find_list = ["периметр", "площа", "кут",
                     "висота", "бісектриса", "бісектрис", "медіана", "сторона"]
        task = []
        start_checking = False

        for word in udpipe_result:
            if word == "знайти":
                start_checking = True  # Start checking words after this
                continue
            if start_checking and word in find_list:
                task.append(word)

        return task

    def find_side(self, elements):
        if "периметр" in elements:
            perimeter = float(elements["периметр"])
            return round(perimeter / 3, 2)
        elif "площа" in elements:
            area = float(elements["площа"])
            return round(pow((area * 4) / pow(3, 0.5), 0.5), 2)

    def calculate(self, tasks, elements):
        side_given = "сторона" in elements
        results = []

        # Find the side if not already given
        side = float(elements.get("сторона", 0)
                     ) if side_given else self.find_side(elements)
        if side is None:
            return ["Cannot compute as side length is missing."]

        for task in tasks:
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

        return results if results else ["No valid tasks found."]
