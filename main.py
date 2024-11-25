from preprocessor import Preprocessor
from udpipe_analyzer import UDPipeAnalyzer
from semantic_analyzer import SemanticAnalyzer
from graphics import draw_triangle


def main():
    test_cases = [
        # "Знайдіть кути рівностороннього трикутника.",
        # "У правильному трикутнику сторона дорівнює 4 . Знайдіть периметр і площу трикутника.",
        # "У рівностороннього трикутника периметр дорівнює 15 . Знайдіть висоту трикутника",
        # "У правильному трикутнику ABC відомо, що висота BK дорівнює 12 . Знайти радіус вписаного кола",
        # "У правильному трикутнику ABC відомо, що його периметр дорівнює 36 . Знайдіть радіус описаного кола правильного трикутника",
        # "У трикутнику BNM площа = 32. Обчисліть середню лінію LK трикутника BNM .",
        # "У трикутнику довжина середньої лінії MN дорівнює 18. Знайдіть площу й радіус вписаного кола правильного трикутника.",
        # "У трикутнику ABC проведено висоту BK до основи AC. Відомо, що AK = 6 . Знайдіть площу трикутника ABC й BK.",
        # "У правильному трикутнику відомо, що радіус описаного кола дорівнює 8 . Знайти бісектрису BN трикутника",
        "У правильному трикутнику ABC сторона дорівнює 6. Знайдіть медіану AL й висоту.",


    ]

    preprocessor = Preprocessor()
    udpipe = UDPipeAnalyzer()

    for i, raw_text in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Task: {raw_text}")

        normalized_text = preprocessor.normalize_text(raw_text)
        print(f"Normalized Text: {normalized_text}")

        udpipe_result = udpipe.analyze_text(normalized_text)
        print(f"UDPipe Result: {udpipe_result}")

        triangle_name = preprocessor.extract_triangle_name(udpipe_result)
        if triangle_name is None:
            triangle_name = "ABC"
        show_triangle_name = triangle_name.upper()
        print(f"Rectangle Name: {show_triangle_name}")

        elements = preprocessor.extract_elements(udpipe_result)
        show_elements = {
            " ".join([part.upper() if len(part) == 2 else part.capitalize() for part in key.split()]): value
            for key, value in elements.items()
        }
        print(f"Extracted Elements: {show_elements}")

        analyzer = SemanticAnalyzer(udpipe_result)
        tasks = analyzer.extract_task(udpipe_result)

        show_tasks = []
        for task in tasks:
            words = task.split()
            processed_words = [
                word.upper() if len(word) == 2 and word.isalpha() else word.capitalize()
                for word in words
            ]
            show_tasks.append(' '.join(processed_words))

        print(f"Tasks to Solve: {show_tasks}")

        results = analyzer.calculate(tasks, elements, triangle_name)

        show_results = []
        for result in results:
            words = result.split()
            processed_words = [
                word.upper() if len(word) == 2 and word.isalpha() else word.capitalize()
                for word in words
            ]
            show_results.append(' '.join(processed_words))

        print(f"\nResults: {show_results}")

    draw_triangle(show_elements, show_tasks, triangle_name, show_results)


if __name__ == "__main__":
    main()
