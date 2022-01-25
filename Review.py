import os
data=[]
count=0
countt=0
#calcaulate the line of review

with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count+=1
		#if count%1000==0:
			#print(len(data))
#count=0
print('total line: ',len(data))

word_count={}
for d in data:
	words= d.split()
	for word in words:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count[word]=1


#print(word_count)
for index in word_count:
	if word_count[index] >1000000:
		print(index,word_count[index])

while 1:
	word = input('please enter the word :')
	if word =='q':
		break

	if word in word_count:
		print(word,word_count[word])
	else:
		print('no this word')	




#for i in data:
#	print(i)
#	count+= 1
#	if count>10:
#		break



