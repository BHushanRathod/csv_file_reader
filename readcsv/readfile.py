import csv
from collections import defaultdict
import urllib.request
import os

columns = defaultdict(list)  # each value in each column is appended to a list

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

emp_name = ''
with open('input_excel.csv') as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            print("v: ",k)
            if k == 'emp_name':
                emp_name = v
            if k == 'image_url':
                print("v: ", v)
                os.mkdir('downloads/'+emp_name)
                urllib.request.urlretrieve(v, 'downloads/'+emp_name+'/'+emp_name+'.jpg')
                pass
                # print(v)
            columns[k].append(v)  # append the value into the appropriate list
            # based on column name k

# print(columns['image_url'])

# import urllib.request
#
# urllib.request.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
