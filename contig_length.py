# calculate the length of contigs of a fasta file
# Python3
# 4/9/2023 Lu Yang

# EXAMPLE:
# python contig_length.py resfinder2022.fasta

import sys
from Bio import SeqIO

# Get the input fasta file path from command line arguments
fasta_file = sys.argv[1]

# Determine the output file name
output_file = fasta_file.replace(".fasta", "_length.txt")

# Open the output file for writing
with open(output_file, "w") as out:
    # Parse the fasta file and write sequence IDs and lengths to the output file
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        out.write("%s\t%d\n" % (seq_record.id, len(seq_record)))

print("Output written to:", output_file)
