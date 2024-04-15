import argparse

from lib import analyze_cv

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyzes a CV for a specific job position")
    parser.add_argument("cv_file", type=str, help="Path to the PDF CV file")
    parser.add_argument("position", type=str, help="Job position to analyze for")
    args = parser.parse_args()

    print(analyze_cv(args.cv_file, args.position)["message"])

