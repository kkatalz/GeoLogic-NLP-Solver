from preprocessor import Preprocessor
from udpipe_analyzer import UDPipeAnalyzer
from semantic_analyzer import SemanticAnalyzer


def main():
    test_cases = [
        "Знайдіть кути рівностороннього трикутника.",
        "У правильному трикутнику сторона дорівнює 4. Знайдіть периметр і площу трикутника.",
        "У рівностороннього трикутника периметр дорівнює 1,5 м. Знайдіть висоту трикутника",
        "У правильному трикутнику ABC відомо, що висота дорівнює 12 см. Знайти радіус вписаного кола",
        "У правильному трикутнику ABC відомо, що  медіана дорівнює 8 см. Знайти радіус описаного кола ",
        "У правильному трикутнику ABC відомо, що його периметр дорівнює 36 см. Знайдіть радіус описаного кола правильного трикутника",
        "У правильному трикутнику сторона дорівнює 6см. Знайдіть довжину медіани, висоти, бісектриси.",
        "У трикутнику довжина середньої лінії дорівнює 18 см. Знайдіть площу й радіус вписаного кола правильного трикутника."
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

        elements = preprocessor.extract_elements(udpipe_result)
        print(f"Extracted Elements: {elements}")

        analyzer = SemanticAnalyzer(udpipe_result)
        tasks = analyzer.extract_task(udpipe_result)
        print(f"Tasks to Solve: {tasks}")

        results = analyzer.calculate(tasks, elements)
        print(f"Results: {results}")


if __name__ == "__main__":
    main()
