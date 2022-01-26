import struct

with open("82E3U9GB.bin","rb") as f:
    data = f.read()
#16 byte 1 struct
#32 HHBBH +HBBBBBB   

start=0
end=16
FormatStr='HHBBH'
FormatStr1='HBBBBBB'
#print(size(FormatStr))


with open('parse.csv','w') as fw:
    fw.write('H0(2Byte),H1(2Byte),B,B,H,H,B,B,B,B,B,B\n')
    while end<=0x1300:
        result = struct.unpack( FormatStr+FormatStr1, data[start:end])
        start+=16
        end+=16
        result_str=''
        for entry in result:
            result_str=result_str+str(hex(entry))+','
        fw.write(result_str+'\n')


#print(type(result))
#print(unpack_result)
#for entry in unpack_result:
    #print(hex(entry))