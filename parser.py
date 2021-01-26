import file_reader

class SubunitParser():
    def __init__(self, worksheet
    , row):
        self.ws = worksheet
        self.max_col = worksheet.max_column
        self.row = row 
        self.subunits = self.parseSubunits()

    def parseSubunits(self):
        
        subunit_array = []
        for i in range(3, self.max_col + 1, 2):
            subunit_name = self.ws.cell(self.row, i).value 
            fasta_description = self.ws.cell(self.row, i + 1).value
            fasta_file = self.parse_file_name(subunit_name, fasta_description)
            
            subunit = {
                "subunit_name": subunit_name,
                "copies": '1',
                "amino_acid_fasta_description": fasta_description,
                "amino_acid_sequence": self.getFastaFileSequence(fasta_file, "AA"),
                "genes": self.parseGenes(fasta_file)
            }
            subunit_array.append(subunit)
        return subunit_array
  
    def parse_file_name(self, subunit_name, fasta_description):
        old_name = subunit_name.split('_')
        gene_name = old_name[0] + '_' + old_name[2]
        file_name = gene_name + '_' + fasta_description
        return file_name
    
    def parseGenes(self, file_name):
        gene = {}
        gene['dna_fasta_description'] = file_name
        gene['dna_sequence'] = self.getFastaFileSequence(file_name, "DNA")
        return [(gene)]

    def getFastaFileSequence(self, subunit, seq_type):
        file = file_reader.FileReader(subunit)
        return file.get_fasta_sequence(seq_type)
        
    