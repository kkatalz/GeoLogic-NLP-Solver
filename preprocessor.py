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
                          'бісектриса', 'бісектрис', 'медіана', 'сторона', 'радіус']

        elements = {}
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "дорівнювати":
                key = None
                for k in range(i - 1, -1, -1):  # Search backward for a valid key
                    # Ensure the token is a valid word
                    if tokens[k].isalnum() and tokens[k] in given_elements:
                        key = tokens[k]
                        break
                    else:
                        break
                        # find 'дорівнювати' and decrease 'i' until it finds the token that is in 'given_elements', and then take everything after this token till and assign to the number after 'дорівнювати'.
                        # example: Радіус коло описаний навколо цей трикутник дорівнює. then it will be value_tokens.append(tokens[j])
                        # add logic

                value_tokens = []
                decimal_found = False

                for j in range(i + 1, len(tokens)):
                    if tokens[j].isdigit():
                        value_tokens.append(tokens[j])
                    elif tokens[j] == "." and not decimal_found:
                        value_tokens.append(tokens[j])
                        decimal_found = True

                if key and value_tokens:
                    # Combine tokens into a single value
                    elements[key] = "".join(value_tokens)
                i += len(value_tokens)  # Skip processed value tokens
            i += 1
        return elements
