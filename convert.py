import csv
import re
csv_file = '/home/ted/ubuntu/code_test/observed_features.csv'

reader = csv.reader(open(csv_file, 'r'), delimiter= ',')
header = next(reader)

dictionary = {}

for row in reader:
    sample = {}
    sample_id = row[0]
    for col_name, cell in zip(header,row):
        if cell == '':
            cell = 0
        # print(col_name + ' ' + cell)
        result = re.match(r'depth-(\d+)_iter-\d+', col_name) 
        if result != None:
            depth = result.group(1)
            if depth in sample:
                cell = int(float(cell))
                sample[depth].append(cell)
            else:
                sample[depth] = []
    dictionary[sample_id] = sample



outfile = '/home/ted/ubuntu/code_test/modifiled.csv'
with open(outfile, 'w') as out_fh:
    writer = csv.writer(out_fh, delimiter=',')
    for sample_id in dictionary:
        for depth in dictionary[sample_id]:
            feature_count_list = dictionary[sample_id][depth]
            row = []
            row.append(sample_id)
            row.append(depth)
            row.extend(feature_count_list)

            writer.writerow(row)