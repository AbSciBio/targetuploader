import json
import argparse
from lib.target_creator import TargetCreator
from lib.ptdb_request import PTDBRequest

def upload_targets(user_input):    
    for target in TargetCreator(user_input).targets:
        PTDBRequest(target).post_target()
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""This program was written to upload 45 
        variations of the CD19 McAbody molecule. In order for the program to run users must provide
        a file path to an Excel workbook, a file path to a directory of FASTA files, and a token
        to communicate with the PTDB API.""")
    parser.add_argument('--excel_file_location', help='Use the --excel_file_location flag to specify the location of the excel document that contains the subunit naming data.')
    parser.add_argument('--fasta_location', help='Use the --fasta_location flag to specify the loaction of a directory of FASTA files.')
    parser.add_argument('--API_URL', help='Use the --API_URL flag to set the destination of POST request.')
    parser.add_argument('--token', help='Use the --token flag to set the API key needed to upload data to the PTDB API.')
    args = parser.parse_args()
    args = vars(args)
    upload_targets(args)