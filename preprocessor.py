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
        given_elements = ['периметр', 'площа', 'кут', 'висота',
                          'бісектриса', 'бісектрис', 'медіана', 'сторона', 'радіус', 'середня']

        elements = {}
        key = None
        value_tokens = []
        decimal_found = False

        for i, token in enumerate(tokens):
            if token == "дорівнювати":
                # Find the key by searching backward
                key = None
                for k in range(i - 1, -1, -1):  # Search backward for a valid key
                    print(tokens[k])
                    if tokens[k] == "лінія":
                        if tokens[k - 1] == "середній":
                            key = tokens[k-1] + " " + tokens[k]
                            break
                    elif tokens[k].isalnum() and tokens[k] in given_elements:
                        key = tokens[k]
                        break

                # Collect value tokens after 'дорівнювати'
                value_tokens = []
                decimal_found = False
                for j in range(i + 1, len(tokens)):
                    if tokens[j].isdigit():
                        value_tokens.append(tokens[j])
                    elif tokens[j] == "." and not decimal_found:
                        value_tokens.append(tokens[j])
                        decimal_found = True
                    else:
                        break  # Stop if an invalid token is found

                # If a valid key and value are found, add to elements
                if key and value_tokens:
                    elements[key] = "".join(value_tokens)

        return elements
