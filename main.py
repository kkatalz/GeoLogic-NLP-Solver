from preprocessor import Preprocessor
from udpipe_analyzer import UDPipeAnalyzer
from semantic_analyzer import SemanticAnalyzer


def main():
    # Input text
    raw_text = "У правильному трикутнику сторона дорівнює 4 см. Знайдіть периметр і площу трикутника."
    print(f"Task: {raw_text}")

    # Step 1: Preprocess
    preprocessor = Preprocessor()
    normalized_text = preprocessor.normalize_text(raw_text)

    # Step 2: Analyze with UDPipe
    udpipe = UDPipeAnalyzer()
    udpipe_result = udpipe.analyze_text(normalized_text)
    print(f"UDPipe Result: {udpipe_result}")

    elements = preprocessor.extract_elements(udpipe_result)
    print(f"Extracted Elements (raw): {elements}")

    # Step 3: Semantic Analysis
    analyzer = SemanticAnalyzer(udpipe_result)
    tasks = analyzer.extract_task(udpipe_result)
    print(f"Task to Solve: {tasks}")

    # Step 4: Resolve Task
    result = analyzer.calculate(tasks, elements)

    # Step 5: Output
    if result:
        print(f"The solution to your task is: {result}")
    else:
        print("Could not determine the task or calculate the result.")


if __name__ == "__main__":
    main()
