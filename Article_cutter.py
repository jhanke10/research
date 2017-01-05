#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import os

#This program splits up large raw data newspaper articles into their separate documents
path = os.getcwd() + "/Output_Files" #Finds
if not os.path.isdir(path):
	os.makedirs(path)
for filename in glob.glob('*.txt'):
	infile = open(filename, 'r+')
	input_file = filename.split('-')
	if input_file.__len__() < 3:
		input_file = filename.split('_')
	firm = input_file[0]
	for p in range(1, input_file.__len__() - 1):
		firm += "_" + input_file[p]
	ceo = input_file[input_file.__len__() - 1] 
	ceo = ceo.replace(".txt", "")
	header = firm + "-" + ceo
	doc_num = [1]
	doc_num2 = []
	text = []
	month = []
	year = []
	num = 0
	for line in infile:
		if line.find("Document") >= 0 and doc_num2.__len__() == num:
			line2 = line.split()
			doc_num2.append(line2[1])
		elif line.find("DOCUMENTS") >= 0 and doc_num2.__len__() == num:
			line2 = line.split()
			doc_num2.append(line2[0])
		if line.find("Edition - Final") >= 0 and year.__len__() == num:
			line2 = line.split()
			month.append(line2[0])
			if (line2[0] == "November") or (line2[0] == "December"):
				line2[2] = line2[2].replace(",", "")
				year.append(line2[2]+1)
			else:
				line2[2] = line2[2].replace(",", "")
				year.append(line2[2])
		if line.find("Full text:") >= 0 and text.__len__() == num:
			if line.find("Full text: Not available.") >= 0:
				text.append(1)
			else:
				text.append(0)
		if line.find("LENGTH: ") >= 0 and text.__len__() == num:
			if line.find("LENGTH: 0 words") >= 0:
				text.append(1)
			else:
				text.append(0)
			num += 1
		if line.find("Publication date:") >= 0 and year.__len__() == num:
			line2 = line.split()
			month.append(line2[2])
			if line2[2] == "Nov" or line2[2] == "Dec":
				year.append(int(line2[line2.__len__()-1])+1)
			else:
				year.append(int(line2[line2.__len__()-1]))
			num += 1
	j = 2
	for i in range(1, year.__len__()):
		if year[i] != year[i-1]:
			j = 1
		doc_num.append(j)
		j += 1
	doc_num_2 = []
	doc_num2_2 = []
	year_2 = []
	for k in range(0, text.__len__()-1):
		if text[k] == 0:
			doc_num_2.append(doc_num[k])
			doc_num2_2.append(doc_num2[k])
			year_2.append(year[k])
	for m in range(0, doc_num_2.__len__()):
		out_filename = header + "-" + str(year_2[m]) + "-" + str(doc_num_2[m]) + ".txt"
		outFile = open(os.path.join(path, out_filename), 'w')
		condition = 1
		condition2 = 1
		infile.seek(0)
		for line5 in infile:	
			if line5.find("Document " + str(doc_num2_2[m])) >= 0:
				condition = 0
			if line5.find("_______") >= 0 and condition == 0:
				condition = 1
				condition2 = 0
			if line5.find(str(doc_num2_2[m]) + " of " + str(doc_num2_2.__len__()) + " DOCUMENTS") >= 0:
				condition = 0
			if line5.find("Copyright") >= 0 and condition == 0:
				condition = 1
				condition2 = 0
				outFile.write(line5)
			if condition == 0 and condition2 == 1:		
				outFile.write(line5)
		outFile.close()
	infile.close()