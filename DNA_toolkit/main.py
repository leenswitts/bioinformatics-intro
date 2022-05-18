from DNA_toolkit.DNAToolkit import *
import random

# generating random DNA string
rndDNAStr = ''.join([random.choice(nucleotides) for nuc in range(20)])


DNAStr = (validateSeq(rndDNAStr))
print(countNucFrequesncy(DNAStr))
