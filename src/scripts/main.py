"""
main.py: This script serves as the main entry point for analyzing legislator votes and bills. It utilizes argparse to parse command-line arguments for bills, legislators, votes, and vote results CSV files. The script imports classes from the 'classes' directory to handle data loading, analysis, and exporting.

The main function initializes the required classes with the provided command-line arguments, retrieves the dataframes, performs the analysis, and saves the results using the CSVExporter class.
"""
from src.classes.data_loader import DataLoader
from src.classes.legislator_vote_analyzer import LegislatorVoteAnalyzer
from src.classes.bill_vote_analyzer import BillVoteAnalyzer
from src.classes.csv_exporter import CSVExporter


def main(arg):
    """
    Main function that runs the analysis process and saves the results.

    arg:
        arg (Namespace): Command line arguments.
    """
    data_loader = DataLoader(arg.bills, arg.legislators, arg.votes, arg.vote_results)
    bills_df, legislators_df, votes_df, vote_results_df = data_loader.get_dataframes()

    legislator_vote_analyzer = LegislatorVoteAnalyzer(legislators_df, vote_results_df)
    legislator_votes_count = legislator_vote_analyzer.calculate_legislator_votes()

    bill_vote_analyzer = BillVoteAnalyzer(
        bills_df, legislators_df, votes_df, vote_results_df
    )
    final_bills = bill_vote_analyzer.calculate_bill_votes()

    CSVExporter.save_results(legislator_votes_count, final_bills)
