import os
ftp_path="/dept/FW_vdk/users/lilly.huang/2504_ISP"
local_path="C:\Code\Cmodle\\"+"2508"+"\FW2-CModel-TestFW_ISP"
cmd=[]


def ChangeEncode(filename):
    with open(filename, 'r', encoding="UTF-16") as f:
        text = f.read()
    with open("temp.txt", 'w', encoding="UTF-8") as f:
        f.write(text)

def ProcessDiff(filename):
    if os.path.isfile(filename):
        #encode process          
        with open(filename,'r',encoding="UTF-8") as f:
            for line in f:
                if line[0:5]!="	modi":
                    continue
                else:

                    if line[-3:-1]==".c" or line[-3:-1]==".h":
                        string = line.replace("	modified:   ","")
                        #string = string.replace("/","\\")                
                        #print(string)
                        s=string.strip().split('/')
                        #print(s)
                        dircnt=len(s)-1
                        ftp_loc=ftp_path
                        for i in range(dircnt):
                            ftp_loc=ftp_loc+"/"+s[i]
                        ftp_loc ="cd "+ftp_loc                           
                        #print(ftp_loc)
                        cmd.append(ftp_loc)                       
                        local_path_1=local_path
                        for i  in range(len(s)):
                              local_path_1=local_path_1+"\\"+s[i]
                        local_path_1="put "+local_path_1
                        #print(local_path_1)
                        cmd.append(local_path_1)
    else:                      
         print("nofile error")           
    
def GenUploadScript(input_cmd):
    with open("uploadftp.bat",'w',encoding="UTF-8") as f:
        f.write("option batch abort\n")
        f.write("option confirm off\n")
        f.write("open ftp://lilly.huang:58c375ba@rdftp01\n")
        #f.write("cd /dept/FW_vdk/users/lilly.huang/2504_ISP\n")
        for cmd in input_cmd:
            f.write(cmd+"\n")
        f.write("cd /dept/FW_vdk/users/lilly.huang/sm2508_v1.2.003_1208/sm2508/mp_flow\n")
        f.write("put \"C:\Code\Cmodle\\"+"2508"+"\FW2-CModel-TestFW_ISP\MPTool\File For Linux Tool\*\"\n")
        f.write("cd /dept/FW_vdk/users/lilly.huang/sm2508_v1.2.003_1208/sm2508/plat/EventLog_Parser_V1124A_auto_parse\n")
        f.write("put C:\Code\Cmodle\\"+"2508"+"\FW2-CModel-TestFW_ISP\EzTool\LogSetting.dat\n")
        f.write("cd /dept/FW_vdk/users/lilly.huang/2504_ISP/IAR8.2/Debug\n")
        f.write("put C:\Code\Cmodle\\"+"2508"+"\FW2-CModel-TestFW_ISP\IAR8.2\Debug\Exe\n")
        

#print("input git diff file...")
#ChangeEncode("gitdiff.txt")
#ChangeEncode2('modify.txt')
print("generate upload script...")                                            
ProcessDiff("gitdiff.txt")
#print(cmd)
GenUploadScript(cmd)