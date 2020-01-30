import os 
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('dir')
parser.add_argument('term')
args = parser.parse_args()



def search(dir,term):
	
	print('Searching {}'.format(dir)) 

	for root,dirs,files in os.walk(dir):
		for file in files:
			if term in file:
				print(root+'\t'+file)

if __name__=='__main__':
    dir = args.dir
    term = args.term 
    search(dir,term)
