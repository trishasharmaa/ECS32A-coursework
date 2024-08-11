import os
from typing import List, Tuple, Dict


def read_csv_files_from_directory(directory: str) -> Dict[str, float]:
    """Reads all CSV files from the given directory and processes them into student grades.

    Args:
        directory: The directory containing the CSV files.

    Returns:
        A dictionary with student names as keys and their weighted grades as values.
    """
    student_grades = {}

    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                percent_total = float(lines[0].split(',')[1].strip())
                max_points = float(lines[1].split(',')[1].strip())

                for line in lines[4:]:
                    last_name, first_name, grade = line.strip().split(',')
                    student_name = f"{last_name}, {first_name}"
                    grade = float(grade.strip())

                    weighted_grade = (grade / max_points) * percent_total

                    if student_name in student_grades:
                        student_grades[student_name] += weighted_grade
                    else:
                        student_grades[student_name] = weighted_grade

    return student_grades


def compute_statistics(grades: List[float]) -> Tuple[float, float, float, float]:
    """Computes the mean, median, mode, and standard deviation of a list of grades.

    Args:
        grades: The list of grades to compute statistics for.

    Returns:
        A tuple containing the mean, median, mode, and standard deviation.
    """
    mean = sum(grades) / len(grades)

    sorted_grades = sorted(grades)
    median = sorted_grades[len(grades) // 2]

    grade_counts = {}
    for grade in grades:
        if grade in grade_counts:
            grade_counts[grade] += 1
        else:
            grade_counts[grade] = 1
    mode = max(grade_counts, key=lambda k: (grade_counts[k], k))

    variance = sum((x - mean) ** 2 for x in grades) / (len(grades) - 1)
    std_dev = variance ** 0.5

    return mean, median, mode, std_dev


def letter_grade(percent: float) -> str:
    """Determines the letter grade for a given percentage.

    Args:
        percent: The percentage grade.

    Returns:
        The corresponding letter grade.
    """
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    elif percent >= 60:
        return 'D'
    else:
        return 'F'


def display_results(statistics: Tuple[float, float, float, float], student_grades: Dict[str, float]):
    """Displays the computed statistics and student grades.

    Args:
        statistics: A tuple containing the mean, median, mode, and standard deviation.
        student_grades: A dictionary with student names and their percentage grades.
    """
    mean, median, mode, std_dev = statistics

    print(f"Mean | Median | Mode | Standard Deviation")
    print(f"{mean:.2f} | {median:.2f} | {mode:.2f} | {std_dev:.2f}")

    sorted_students = sorted(student_grades.items())
    print("Last Name | First Name | Percent | Letter")
    for student, grade in sorted_students:
        last_name, first_name = student.split(", ")
        print(f"{last_name} | {first_name} | {grade:.2f} | {letter_grade(grade)}")


def main():
    """Main function to execute the program."""
    directory = input("Please enter the name of the directory containing the homeworks: ").strip()

    try:
        student_grades = read_csv_files_from_directory(directory)
    except FileNotFoundError as e:
        print(e)
        return

    grades = list(student_grades.values())

    if not grades:
        print("No grades to display.")
        return

    statistics = compute_statistics(grades)
    display_results(statistics, student_grades)


if __name__ == "__main__":
    main()
