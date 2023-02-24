# extract_gff_features_in_ranges
This is a Python3 script to extract gff features partially overlapping areas of interest on contigs

The program requires two input files: a gff3 file for the organism of interest, declared with the option "-g", and a list of the ranges of interest, declared with the option "-r". This file is a tsv file of 4 columns, with each row describing a separate range of interest. The 4 columns must be the following:
1: an identifier for the range. This can be anything. I wrote this script to see if the precursors of miRNAs were originating from coding areas of a genome or not, so normally I use miRNA names as identifiers.
2: the name of a contig on which the range of interest is located, with the same name that the contig has in the gff file
3: the start of the range of interest
4: the end of the range of interest

Additionally, the option "-l" is required to specify the length that will be scanned around the ranges of interest looking for the beginning or end of features. This is expecially useful when the ranges of interest are small (<100 bp). Since the program scans the ranges of interest looking for the beginning or end of features, extending the area using the "-l" option will make sure to get, for example, genes that contain the range of interest but start and end hundreds of bases away. In any case only features that partially or completely overlap the ranges of interest will be reported in the output file.

The output file, declared with the option "-o", will be a tsv file with a feature overlapping the ranges of interest on each row. The file will have 4 columns:
1: the identifier of the range of interest overlapping the feature
2: the type of the feature (gene, mRNA, CDS, ecc...) as stated in the gff file
3: the description of the feature, containing the 9th column of the feature in the gff file
4: the contig and coordinated of the range of interest

If a range of interest does not overlap any feature of the gff, it will still be present in the output file, containing "intergenic" in the second column.


To test the program, run:
python extract_gff_features_in_ranges.py -r example_ranges.txt -g example_gff.gff3 -l 1000 -o test.txt
python extract_gff_features_in_ranges.py -r example_ranges.txt -g example_gff.gff3 -l 10000 -o test_2.txt

And check that test.txt and test_2.txt are identical to example_output.txt and example_output_2.txt respectively.

