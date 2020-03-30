import codecs
import csv
import time
import numpy as np
import os

#set up the mapping of dx code to ccw
dx_map = {}
line_num = 0
f = open("mappings/ccw_cms_mapping","r")
for line in f:
	pts = line.strip().replace(" ","").split("|")
	codes = pts[2].split(",")
	for code in codes:
		if not code in dx_map:
			dx_map[code] = [ line_num]
		else:
			dx_map[code].append(line_num)
	line_num += 1
f.close()


#hard code the positions of dx codes per file type
dx_code_pos = {
	'hha_claimsk':[27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51],
	'inp_claimsk':[48,50,52,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77],
	'out_claimsk':[32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56],
	'snf_claimsk':[46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70],
	'car_claimsk':[19,20,21,22,23,24,25,26,27,28,29,30]
}

ENCODING = 'utf-8'
for FILETYPE in ['hha_claimsk','inp_claimsk','out_claimsk','snf_claimsk','car_claimsk']:
	for year in ['2016','2017','2018']:
		FILENAME = "%s_%s_%s.csv" % (FILETYPE,'lds_5',year)
		print (FILENAME)
		with codecs.open('filtered/' + FILENAME, "r") as fp:
			reader = csv.reader(fp)

			with codecs.open('filtered/' + FILENAME.replace(".csv","") + "_dx_appended.csv", "w", ENCODING) as wp:
				writer = csv.writer(wp)

				# read rest of file
				for row in reader:
					append_row = [0]*line_num
					for pos in dx_code_pos[FILETYPE]:
						if row[pos] in dx_map:
							for c in dx_map[row[pos]]:
								append_row[c] = 1

					writer.writerow(row + append_row)