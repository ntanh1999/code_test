import csv
import re
csv_file = '/home/ted/ubuntu/code_test/observed_features.csv'

reader = csv.reader(open(csv_file, 'r'), delimiter= ',')
header = next(reader)

dictionary = {} # contain the feature count of each depth and sample

for row in reader:
    sample = {}
    sample_id = row[0]
    for col_name, cell in zip(header,row):
        result = re.match(r'depth-(\d+)_iter-\d+', col_name) # extract the depth
        if result != None:
            depth = result.group(1)
            if depth in sample:
                if cell == '':
                    cell = None
                else:
                    cell = int(float(cell)) # convert all value to integer because some are float
                sample[depth].append(cell)
            else:
                sample[depth] = []
    dictionary[sample_id] = sample



outfile = '/home/ted/ubuntu/code_test/modifiled.csv'
with open(outfile, 'w') as out_fh:
    writer = csv.writer(out_fh, delimiter=',')
    writer.writerow(['sample_id', 'depth', 'feature_count']) # write the header
    for sample_id in dictionary:
        for depth in dictionary[sample_id]:
            feature_count_list = dictionary[sample_id][depth]
            for count in feature_count_list:
                row = []
                row.append(sample_id)
                row.append(depth)
                row.append(count)

                writer.writerow(row)