class SemanticAnalyzer:

    def __init__(self, udpipe_result):
        self.result = udpipe_result

    def extract_task(self, udpipe_result):
        find_list = ["периметр", "площа", "кут",
                     "висота", "бісектриса", "медіана", "сторона"]
        task = []
        start_checking = False

        for word in udpipe_result:
            if word == "знайти":
                start_checking = True  # Start checking words after this
                continue
            if start_checking and word in find_list:
                task.append(word)

        return task

    def calculate(self, tasks, elements):

        results = []
        for task in tasks:
            if task == "площа":
                side = float(elements.get("сторона", 0))
                result = round((pow(side, 2) * pow(3, 0.5)) / 4, 2)
                results.append(f"{task}: {result}")

            elif task == "периметр":
                side = float(elements.get("сторона", 0))
                result = round(side * 3, 2)
                results.append(f"{task}: {result}")

            elif task == "кут":
                results.append(f"{task}: 60")

            elif task == "angles":
                results.append(f"{task}: 180")

            elif task in ["висота", "бісектриса", "медіана"]:
                side = float(elements.get("сторона", 0))
                result = round((pow(3, 2) * side) / 2, 2)
                results.append(f"{task}: {result}")

        return results if results else ["No valid tasks found."]
