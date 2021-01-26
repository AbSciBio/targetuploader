from Bio import SeqIO

class FileReader():
  def __init__(self, subunit_name):
    self.file_name = subunit_name 
    

  def get_fasta_description(self, seq_type):
    return self.find_sequence(seq_type)

  def find_sequence(self, seq_type):
    errors = []
    sequence = ''
    try:
      for record in SeqIO.parse(f'./assets/CD19_MicAbody_Xolo_FASTA_Files/{self.file_name}_{seq_type}.fasta', 'fasta'):
        sequence = record.seq
    except FileNotFoundError as err:
      errors.append(f'{err}: {err.filename2}')
   
    if len(sequence) > 0:
      return sequence
    if (errors):
      return errors