# DNA toolkit file
import collections


nucleotides = ["A", "C", "G", "T"]

# make sure nucleotide is valid


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq


def countNucFrequesncy(seq):
    return dict(collections.Counter(seq))
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict
