def run_grade_checker():
    """
    Determines if a student passed or failed based on a score.
    Refactored from lesson2.py
    """
    print("\n--- Grade Checker ---")
    try:
        exam_score = int(input("Enter your exam result (0-100): "))

        if exam_score < 0 or exam_score > 100:
            print("Error: Please enter a score between 0 and 100.")
            return

        if exam_score >= 50:
            print("Result: You have passed! Congratulations!")
        else:
            print("Result: You have failed. Keep practicing!")
    except ValueError:
        print("\nError: Invalid input. Please enter a numeric value for the exam result.")
