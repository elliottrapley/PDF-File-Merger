#Simple script to merge multiple pdf files specified into one pdf file named "combined.pdf"

import PyPDF2 
import sys 

inputs = sys.argv[1:] #Stores the specified PDF files from index 1 as the inputs variable.

def pdf_combiner(pdf_files):
	merger = PyPDF2.PdfFileMerger() 
	for pdf in pdf_files:
		print('Processing... ' + pdf)
		merger.append(pdf)
	new_file_name = input('What would you like to name your new file? ')
	merger.write(new_file_name + '.pdf')
	print('Done!')

pdf_combiner(inputs)




