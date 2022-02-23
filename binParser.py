import struct
#parsing _HDMAQUEUE 
with open("test.bin","rb") as f:
    data = f.read()
#16 byte 1 struct
#32 HHBBH +HBBBBBB   


format = input('please enter the format :') 
format = int(format)

#1:gsHdmaCtrl.uarHdmaQue
#2:gsHMBInfo.uarHmbPrdQ
#3gsHMBParityInfo.uarHmbPtyQ
if format==1:
    struct_size=8
    file_size=8*32
    FormatStr='HHHH'
    output_col='u16TsbIdx,u16XfrSctrCnt,u16RaidOpts,u16RaidStEncPgIdx\n'
    output_name='uarHdmaQue.csv' 
elif format==2: 
    struct_size=(4*2+2*2+4)
    file_size=struct_size*32
    FormatStr='IIHHBBBB'
    output_col='u32HmbAddrLow,u32SctrCnt,u16BufPtr,u16HmbIdx,uOpCode,uFuncId,uSgmtIdx,uSrcIdx\n'
    output_name='uarHmbPrdQ.csv'  
elif format==3:
    struct_size=(2*2+1)
    file_size=struct_size*64
    FormatStr='HHB'
    output_col='u16BufPtr,u16PtyIdx,uXfrDir\n'
    output_name='uarHmbPtyQ.csv'  


start=0
end=struct_size
#FormatStr='HHHH'
#FormatStr1='HH'
#print(size(FormatStr))
#'HHBBH'

with open(output_name,'w') as fw:
    #fw.write('H0(2Byte),H1(2Byte),B,B,H,H,B,B,B,B,B,B\n')
    fw.write(output_col)
    while end<file_size:
        result = struct.unpack( FormatStr, data[start:end])
        start+=struct_size
        end+=struct_size
        result_str=''
        for entry in result:
            result_str=result_str+str(hex(entry))+','
        fw.write(result_str+'\n')


#print(type(result))
#print(unpack_result)
#for entry in unpack_result:
    #print(hex(entry))