from preprocessor import Preprocessor
from udpipe_analyzer import UDPipeAnalyzer
from semantic_analyzer import SemanticAnalyzer


def main():
    # Input text
    raw_text = " У правильному трикутнику сторона дорівнює 4. Знайдіть периметр і площу трикутника."

    # Step 1: Preprocess
    preprocessor = Preprocessor()
    normalized_text = preprocessor.normalize_text(raw_text)
    print(f"Normalized Text: {normalized_text}")

    # Step 2: Analyze with UDPipe
    udpipe = UDPipeAnalyzer()
    udpipe_result = udpipe.analyze_text(normalized_text)
    print(f"UDPipe Result: {udpipe_result}")

    elements = preprocessor.extract_elements(udpipe_result)
    print(f"Extracted Elements (raw): {elements}")

    # Step 3: Semantic Analysis
    analyzer = SemanticAnalyzer(udpipe_result)
    task = analyzer.extract_task()
    print(f"Task to Solve: {task}")

    # Step 4: Resolve Task
    result = analyzer.calculate(task, elements)

    # Step 5: Output
    if result:
        print(f"The solution to your task is: {result}")
    else:
        print("Could not determine the task or calculate the result.")


if __name__ == "__main__":
    main()
