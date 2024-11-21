class Preprocessor:
    def __init__(self):
        pass

    @staticmethod
    def normalize_text(raw_text):

        raw_text_lower = raw_text.lower()
        text = raw_text_lower.replace("–", "дорівнює")
        text = text.replace("см", " cm")
        text = text.replace(",", ".")
        text = text.replace("обчисліть", "знайдіть")
        return text

    @staticmethod
    def extract_elements(tokens):
        """
        Extract key elements like numbers, units, and geometric terms.
        Handles multi-token values like '4√3'.
        """
        elements = {}
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "дорівнювати":
                key = None
                for k in range(i - 1, -1, -1):  # Search backward for a valid key
                    if tokens[k].isalnum():  # Ensure the token is a valid word
                        key = tokens[k]
                        break

                value_tokens = []
                # Collect all tokens that form the value (e.g., numbers and symbols like √)
                if tokens[i+1].isalnum() or tokens[i+1] in "√":
                    value_tokens.append(tokens[i+1])

                if key and value_tokens:
                    # Combine tokens into a single value
                    elements[key] = "".join(value_tokens)
                i += len(value_tokens)  # Skip processed value tokens
            i += 1
        return elements
