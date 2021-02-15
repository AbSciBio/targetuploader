# CD19 MicAbody Target Uploader

This program was written to upload 45 unique targets with different combinations of light and heavy chain subunits. There are several variables that must be given to the program via the CLI in order for it to work:

`--excel_file_location`: This flag is used to determine the location of an Excel file that contains data used to create each "target".  
`--fasata_location`: This flag is used to determine the location of the directory that holds the amino acid and dna sequences fasta files.  
`--API_URL`: This is the URL of the PTDB.  
`--token`: This is the API token necessary to make HTTP requests to the PTDB.

Use the following command (replacing the value of `API_URL` and `token` with the appropriate values) to run the program.

`python3 target_uploader.py --fasta_location=./assets/CD19_MicAbody_Xolo_FASTA_Files/ --excel_file_location=./assets/XOLO_PTDB_Nomenclature.xlsx --API_URL=https://localhost8000/api/v1/absci-targets/target-registration --token=like-id-show-you`

## Testing

Unit tests are run to ensure that the program creates the correct target object. To run unit tests issue the following command:

`python3 -m unittest tests/test_target_creator.py`