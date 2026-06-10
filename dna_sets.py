# Bioinformatics Project - Sets and DNA 

dna_sequence1 = {"A", "T", "G", "C"}
dna_sequence2 =  {"G", "C"}

print("Sequence 1: ", dna_sequence1)
print("Sequence 2: ", dna_sequence2)

print("Nucleotides present in both DNA sequences: ")
print(dna_sequence1.intersection(dna_sequence2))

print("\nAll nucleotides found: ")
print(dna_sequence1.union(dna_sequence2))

print("\nNucleotides that are only found in the first sequence: ")
print(dna_sequence1.difference(dna_sequence2))

print("\nNucleotides that are only found in the second sequence: ")
print(dna_sequence2.difference(dna_sequence1))

# Comparing DNA and RNA to detect unique nucleotides

dna = {"A","T", "G", "C"}
rna = {"G", "C", "U"}

print("\nAll nucleotides found: ")
print(dna.union(rna))

print("\nNucleotides exclusive to DNA: ")
print(dna.difference(rna))

print("\nNucleotides exclusive to RNA: ")
print(rna.difference(dna))
