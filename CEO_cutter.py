#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import os

def delExtra(string):
	string = string.replace(",", "")
	string = string.replace(".", "")
	string = string.replace("?", "")
	string = string.replace("'s", "")
	string = string.replace("!", "")
	string = string.replace("/", "")
	string = string.replace("-", "")
	string = string.replace("_", "")
	string = string.replace('"', "")
	return string

cur_path = os.getcwd()
path_find = cur_path.split("/")
add_new = 0
for i in range(0, path_find.__len__()):
	if path_find[i] == "Output_Files":
		add_new = 1
path1 = ""
path2 = ""
if add_new == 0:
	path1 = cur_path + "/Output_Files/Relevant_Files"
else:
	path1 = cur_path + "/Relevant_Files"
if not os.path.isdir(path1):
	os.makedirs(path1)
if add_new == 0:
	path2 = cur_path + "/Output_Files/Irrelevant_Files"
else:
	path2 = cur_path + "/Irrelevant_Files"
if not os.path.isdir(path2):
	os.makedirs(path2)
if add_new == 0:
	os.chdir(cur_path + "/Output_Files")
	cur_path = cur_path = os.getcwd()
threshold = input("How many times should the CEO's name be metioned? ")
for filename in glob.glob('*.txt'):
	infile = open(filename, 'r+')
	input_file = filename.split('-')
	input_file.pop()
	input_file.pop()
	ceo = input_file.pop()
	count = 0
	for line in infile:
		line2 = line.split(" ")
		for i in range(0, line2.__len__()):
			line2[i] = delExtra(line2[i])
		if line.find(ceo) >= 0:
			for i in range(0, line2.__len__()):
				if (line2[i] == ceo):
					count += 1
	out_filename = filename.replace(".txt", "") + "-" + str(count) + ".txt"
	if count >= int(threshold):
		outFile = open(os.path.join(path1, out_filename), 'w')
		infile.seek(0)
		for line in infile:
			outFile.write(line)
		outFile.close
	else:
		outFile = open(os.path.join(path2, out_filename), 'w')
		infile.seek(0)
		for line in infile:
			outFile.write(line)
		outFile.close
	infile.close()