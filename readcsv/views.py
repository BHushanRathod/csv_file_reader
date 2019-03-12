import csv
import json
import os
import threading
import ssl
import urllib.request
from collections import defaultdict

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from amdocstest.settings import BASE_DIR

columns = defaultdict(list)  # each value in each column is appended to a list

ssl._create_default_https_context = ssl._create_unverified_context


class ReadJson(APIView):

    @staticmethod
    def get(request):
        f = open('input_excel.csv', 'rU')
        reader = csv.DictReader(f, fieldnames=("emp_name", "type_code", "image_url", "local_path"))
        out = json.dumps([row for row in reader])
        f = open('output.json', 'w')
        f.write(out)

        result = json.loads(out)
        return Response(result, status=status.HTTP_200_OK)


class ShowJson(APIView):

    @staticmethod
    def get(request):
        f = open('input_excel.csv', 'r')
        reader = csv.DictReader(f, fieldnames=("emp_name", "type_code", "image_url", "local_path"))
        out = json.dumps([row for row in reader])
        f = open('output.json', 'w')
        f.write(out)

        context = {}
        result = json.loads(out)
        context['data'] = result
        return render(request, 'data.html', context=context)


def writecsv(request):
    emp_name = ''
    with open('input_excel.csv', mode='r+') as f, open(r'output_excel.csv', 'wt', newline='') as f_out:
        writer = csv.writer(f_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        reader = csv.DictReader(f)  # read rows into a dictionary format
        # writer = csv.writer(f_out)

        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            # print("row: ", row.items())
            for (k, v) in row.items():  # go over each column name and value
                if k == 'emp_name':
                    emp_name = v
                if k == 'image_url':
                    try:
                        os.mkdir('downloads/' + emp_name)
                        urllib.request.urlretrieve(v, 'downloads/' + emp_name + '/' + emp_name + '.jpg')
                    except:
                        pass
                if k == 'local_path':
                    if os.path.exists(BASE_DIR + '/downloads/' + emp_name + '/' + emp_name + '.jpg'):
                        v = 'download/' + emp_name + '/' + emp_name + '.jpg'

                columns[k].append(v)  # append the value into the appropriate list
        for k, val in columns.items():
            print(k, val)
            writer.writerow([k] + val)
        # print(columns)


def callprocess(request):
    """

    :param request:
    :return:
    """
    threading.Thread(target=writecsv).start()
    return HttpResponse("SUCCESS")
