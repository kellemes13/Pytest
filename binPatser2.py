import os
import struct

##### test parsing bin##### 
with open("MPISP2269.bin","rb") as f:
	data = f.read()

file_size=60*16
Format='QQ' #8+8
start=0
end=16

while end<60*16:
	result=struct.unpack(Format,data[start:end])
	start+=16
	end+=16
	temp=str(hex(result[0]))
	temp1=temp[2:].zfill(16)
	temp1=temp1.replace("L","")
	#print(temp1)

	temp2=str(hex(result[1]))
	temp3=temp2[2:].zfill(16)
	temp3=temp3.replace("L","")
	#print(temp3)
	BinDATA=temp3+temp1
	#if len(BinDATA)==33:
	print(BinDATA) #0x10 : 16 byte data
