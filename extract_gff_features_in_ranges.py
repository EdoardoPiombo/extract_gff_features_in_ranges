import argparse as ap
import pandas as pd

#arguments
parser = ap.ArgumentParser()
parser.add_argument("-g", "--gff", help="input gff file")
parser.add_argument("-l", "--length", help="length that you want to check around the range. This is needed to find features that are in the analysed range but start outside of it. Features starting or ending further from the range than this length will not be considered")
parser.add_argument("-r", "--ranges", help="list of identifier, contigs and coordinates. Every line should have an identifier (any text descriptor will do) and a contig name, followed by a start and an end of the range of interest, all separated by tabs")
parser.add_argument("-o", "--output", help="output file with annotations in the range")


args = parser.parse_args()

gff = args.gff
ranges = args.ranges
output = args.output
length = int(args.length)

##The program reads the gff and then creates an empty dataframe to later store results in it
data = pd.read_csv(gff, comment='#', sep = '\t', names = ['scaffold', 'predictor', 'feature', 'start', 'end', 'dot', 'sense', 'RF', 'description'])

results = pd.DataFrame(data = 0, index = [], columns = ['sequence', 'scaffold', 'predictor', 'feature', 'start', 'end', 'dot', 'sense', 'RF', 'description', 'type'])

with open(ranges) as r:
    ## For each interval, we define an area of interest, going from start-length to end + length.
    ## Features starting before this area, or ending after it, will not be considered
    for line in r:
        line = line.rstrip().split('\t')
        identifier = line[0]
        contig=line[1]
        start= int(line[2])
        try:
            end = int(line[3])
        except IndexError:
            end = start + 1
        sequence = range(start, end)
        scafdata = data.where((data['scaffold'] == contig) & (data['start'] > (start - length)) & (data['end'] < (end + length))).dropna()
        a = 0
        ##Now we look for which features are intersecting our range of interest, and we save them to the results dataframe
        for id in scafdata.index.tolist():
            newseq = range(int(scafdata.loc[id]['start']), int(scafdata.loc[id]['end']))
            intersection = range(max(sequence[0], newseq[0]), min(sequence[-1], newseq[-1])+1)
            if len(intersection) > 0:
                results.loc[str(id)] = data.loc[id]
                results.loc[str(id), 'sequence'] = identifier 
                results.loc[str(id), 'type'] = ''.join(line) 
                a = 1
        
        if a == 0 :
            id = ''.join(line)
            results.loc[str(id), 'sequence'] = identifier
            results.loc[str(id), 'feature'] = 'intergenic'
            results.loc[str(id), 'type'] = ''.join(line) 

                
                
                

results = results[['sequence', 'feature', 'description', 'type']]
results.to_csv(output, sep = '\t', index = False, header = False)
            
    
