class SemanticAnalyzer:
    def __init__(self, udpipe_result):
        self.result = udpipe_result

    def extract_task(self):
        if "площа" in self.result:
            return "area"
        elif "периметр" in self.result:
            return "perimeter"
        elif "кут" in self.result:
            return "angle"
        elif "медіана" in self.result:
            return "median"
        elif "радіус" in self.result:
            return "radius"
        elif "діаметр" in self.result:
            return "diameter"
        else:
            return None

    def calculate(self, task, elements):
        # make 6.928203230275509 to 6.93
        if task == "area":
            side = float(elements.get("сторона", 0))
            result = round((pow(side, 2) * pow(3, 0.5)) / 4, 2)
            return result

        elif task == "perimeter":
            side = float(elements.get("сторона", 0))
            return side * 3

        elif task == "angle":
            return 60

        elif task == "angles":
            return 180

        return None
