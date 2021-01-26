import file_reader

class SubunitParser():
    def __init__(self, worksheet
    , row):
        self.max_col = worksheet.max_column
        self.ws = worksheet

        self.row = row
        self.subunit_name = self.parse_file_name(self.ws.cell(self.row, 3).value, self.ws.cell(self.row, 4).value)
        
        self.subunits = self.parseSubunits()

    def parseSubunits(self):
        subunit_array = []
        subunit = {
            'subunit_name': "",
            "copies": '1',
            "amino_acid_fasta_description": '',
            "amino_acid_sequence": '',
        }

        subunit['subunit_name'] = self.subunit_name
        subunit['amino_acid_fasta_description'] = self.subunit_name
        subunit['amino_acid_sequence'] = self.getFastaFileSequence(self.subunit_name, "AA")
        subunit = self.parseGenes(subunit)
        subunit_array.append(subunit)

        
        
        # subunit['subunit_name'] = self.ws.cell(self.row, 5).value
        # subunit['amino_acid_fasta_description'] = self.ws.cell(self.row, 6).value
        # subunit['amino_acid_sequence'] = self.getFastaFileSequence()
        # subunit_array.append(subunit)
        # print(subunit_array)
        return subunit_array
  
    def parse_file_name(self, subunit_name, fasta_description):
        old_name = subunit_name.split('_')
        gene_name = old_name[0] + '_' + old_name[2]
        file_name = gene_name + '_' + fasta_description
        print(file_name)
        return file_name
    
    def parseGenes(self, subunit):
        gene = {}
        fasta_file_description = self.ws.cell(self.row, 4).value
        gene['dna_fasta_description'] = self.ws.cell(self.row, 4).value
        gene['dna_sequence'] = self.getFastaFileSequence(subunit['subunit_name'], "DNA")
        subunit['genes'] = [(gene)]
        return subunit

    def getFastaFileSequence(self, subunit, seq_type):
        file = file_reader.FileReader(subunit)
        return file.get_fasta_description(seq_type)
        
    