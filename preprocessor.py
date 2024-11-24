class Preprocessor:
    def __init__(self):
        pass

    @staticmethod
    def normalize_text(raw_text):

        raw_text_lower = raw_text.lower()
        text = raw_text_lower.replace("-", "дорівнює")
        text = raw_text_lower.replace("=", "дорівнює")
        text = text.replace("см", " cm")
        text = text.replace(",", ".")
        text = text.replace("обчисліть", "знайдіть")
        return text

    @staticmethod
    def extract_triangle_name(tokens):
        for i, token in enumerate(tokens):
            if i > 0 and tokens[i - 1] == "трикутник":
                if len(token) == 3 and token.isalpha():
                    return token
        return None

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
                    print("STRAT DEBUG")
                    # for середній лінія
                    if tokens[k].isalnum() and len(tokens[k]) == 2 and tokens[k-1] == "лінія":
                        print("0")
                        # fmt: off
                        key = f"{tokens[k - 2]} {tokens[k - 1]} {tokens[k].upper()}"
                        # fmt: on
                        break

                    elif tokens[k] == "коло":
                        print("1")
                        key = tokens[k-2] + " " + tokens[k-1] + " " + tokens[k]
                        break

                    # for just
                    elif tokens[k].isalnum() and len(tokens[k]) > 5:
                        print("2")
                        key = tokens[k]
                        break
                    elif tokens[k].isalnum() and len(tokens[k]) == 2 and len(tokens[k-1]) >= 6:
                        print("3")
                        key = tokens[k - 1] + " " + tokens[k].upper()
                        break
                    else:
                        print("4")
                        key = tokens[k].upper()
                        break

                # Collect value tokens after 'дорівнювати'
                value_tokens = []
                decimal_found = False
                for j in range(i + 1, len(tokens)):
                    if tokens[j].isdigit():
                        value_tokens.append(tokens[j])
                    elif tokens[j] == "." and not decimal_found:
                        decimal_found = True
                    else:
                        break  # Stop if an invalid token is found

                # If a valid key and value are found, add to elements
                if key and value_tokens:
                    elements[key] = "".join(value_tokens)

        return elements
