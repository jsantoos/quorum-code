"""
This is the run.py script, which serves as the entry point for the application. The script analyzes legislator votes
and bills, processes the data, and exports the results as CSV files.

The script uses the argparse library to parse command-line arguments for bills, legislators, votes, and vote results CSV
files. It then initializes the DataLoader, LegislatorVoteAnalyzer, BillVoteAnalyzer, and CSVExporter classes from
separate module files to perform data loading, analysis, and exporting.

To execute this script, run the following command with the appropriate CSV file paths:

Usage:
python run.py --bills <bills_csv_file> --legislators <legislators_csv_file> --votes <votes_csv_file> --vote_results <vote_results_csv_file>
"""
import argparse

from src.scripts.main import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze legislator votes and bills.")
    parser.add_argument("--bills", help="CSV file containing bill information.")
    parser.add_argument(
        "--legislators", help="CSV file containing legislator information."
    )
    parser.add_argument("--votes", help="CSV file containing vote information.")
    parser.add_argument("--vote_results", help="CSV file containing vote results.")
    args = parser.parse_args()

    main(args)
