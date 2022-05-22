"""
Turn DNA barcodes into RNA and their respective protein.
"""

# Dictionary with full name of amino acids.
aminoAcid = {
    'gcc': 'alanine',
    'gcu': 'alanine',
    'gca': 'alanine',
    'gcg': 'alanine',
    'cgu': 'arginine',
    'cgc': 'arginine',
    'cga': 'arginine',
    'cgg': 'arginine',
    'aga': 'arginine',
    'agg': 'arginine',
    'aau': 'asparagine',
    'aac': 'asparagine',
    'gau': 'aspartic acid',
    'gac': 'aspartic acid',
    'ugc': 'cysteine',
    'ugu': 'cysteine',
    'gaa': 'glutamic acid',
    'gag': 'glutamic acid',
    'cag': 'glutamine',
    'caa': 'glutamine',
    'ggu': 'glycine',
    'ggc': 'glycine',
    'gga': 'glycine',
    'ggg': 'glycine',  
    'cac': 'histidine',
    'cau': 'histidine',
    'auu': 'isoleucine',
    'auc': 'isoleucine',
    'aua': 'isoleucine',
    'cuu': 'leucine',
    'cuc': 'leucine',
    'cua': 'leucine',
    'cug': 'leucine',
    'uua': 'leucine',
    'uug': 'leucine',
    'aaa': 'lysine', 
    'aag': 'lysine', 
    'aug': 'methionine',
    'uuu': 'phenylalanine',
    'uuc': 'phenylalanine',
    'ccu': 'proline',
    'ccc': 'proline',
    'cca': 'proline',
    'ccg': 'proline',
    'ucu': 'serine',
    'ucc': 'serine',
    'uca': 'serine',
    'ucg': 'serine',
    'agu': 'serine',
    'agc': 'serine',
    'acu': 'threonine',
    'acc': 'threonine',
    'aca': 'threonine',
    'acg': 'threonine',
    'ugg': 'tryptophan',
    'uau': 'tyrosine',
    'uac': 'tyrosine',
    'guu': 'valine',
    'guc': 'valine',
    'gua': 'valine',
    'gug': 'valine',
    'uaa': 'STOP Trigger',
    'uag': 'STOP Trigger',
    'uga': 'STOP Trigger',
}

# Dictionary to map DNA to RNA
dnaRNA = {
    'a': 'u',
    't': 'a',
    'c': 'g',
    'g': 'c',
    ' ': ' '  # If more than 3 bases are inputted.
}

# Possible DNA Inputs
dnaInputs = ['a', 't', 'c', 'g', ' ']
    
# DNA Checker: Barcodes
def DNA_checker_barcode(DNA):
    
    if len(DNA) % 3 != 0:
        return False

    return True

# DNA Checker: Valid Input
def DNA_checker_input(DNA):
    """Determines if the DNA strand is valid.

    Args:
        DNA (str): String of barcodes.

    Returns:
        bool: Determines that the DNA strand is made of valid barcodes.
    """

    for base in DNA:

        if base not in dnaInputs:
            return False

    return True

# Function: DNA Input & Checker
def DNA_input(DNA): 

    # Take DNA input
    DNA = DNA.lower()
    DNA = "".join(DNA.split())  # Remove Spaces

    # Check if DNA is not valid
    if not DNA_checker_barcode(DNA):

        DNA = 'ERROR1'
        return DNA
    
    if not DNA_checker_input(DNA):

        DNA = 'ERROR2'
        return DNA

    # Split DNA into 3 characters and add spaces in between to create the barcodes.
    DNA = ' '.join([DNA[base : base + 3] for base in range(0, len(DNA), 3)])

    return DNA

# Function: DNA -> RNA
def DNA_to_RNA(DNA):

    # RNA List
    RNA = []

    # For nitrogenBase in DNA
    for base in DNA:

        # Add the opposite to the RNA List
        RNA.append(dnaRNA[base])

    # RNA List -> String
    RNA = ''.join(RNA)
    
    # Return RNA
    return RNA.lower()

# Function: RNA -> Protein
def get_amino_acid(RNA):

    proteinList = []

    RNA_barcode = RNA.split(' ')

    for barcode in RNA_barcode:
        proteinList.append(aminoAcid[barcode])

    return proteinList

print("Passed: DNA Library & Functions Imported")