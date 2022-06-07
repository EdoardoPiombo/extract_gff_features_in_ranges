# extract_gff_features_in_ranges
This is a Python3 script to extract gff features partially intersecting areas of interest on contigs

The program requires two input files: a gff3 file for the organism of interest, declared with the option "-g", and a list of the ranges of interest, declared with the option "-r". This file is a tsv file of 4 columns, with each row describing a separate range of interest. The 4 columns must contain:
1: an identifier for the range. This can be anything. I wrote this script to see if the precursors of miRNAs were originating from coding areas of a genome or not, so normally I use miRNA names as identifiers.
2:  the name of a contig on which the range of interest is located

Work in progress
