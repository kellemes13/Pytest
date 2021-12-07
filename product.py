import os

#productList=[]
#read file
def read_file(filename):
	productList=[]
	if os.path.isfile(filename):
		print("file exist")
		with open(filename,'r') as f:
			for line in f:
				if 'product,price' in line:
					continue
				else:
					s=line.strip().split(',')
					productList.append(s)

		print(productList)
		return productList
	else:
		print("no file")

def write_file(filename):
	productList=read_file(filename)
	while True:
		name=input("input product: ")
		if name=='q':
			break
		price=input("input price: ")
		entry=[name,price]
		productList.append(entry)

	if os.path.isfile(filename):
		with open(filename,'w') as f:
			f.write('product,price\n')
			for entry in productList:
				f.write(entry[0]+','+entry[1]+'\n')	
				
	else:
		print("no file")


read_file('product.csv')
#write_file('product.csv')