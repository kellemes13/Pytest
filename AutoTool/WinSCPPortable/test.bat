option batch abort
option confirm off
open ftp://lilly.huang:58c375ba@rdftp01
cd /dept/FW_vdk/users/lilly.huang/2504_ISP
 ls
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\inc
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\src

cd /dept/FW_vdk/users/lilly.huang/2504_ISP/subtree/
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\subtree\XT_ASIC

cd /dept/FW_vdk/users/lilly.huang/2504_ISP/subtree/SM2268XT_FE/FW_SM2268XT_FE
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\subtree\SM2268XT_FE\FW_SM2268XT_FE\src
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\subtree\SM2268XT_FE\FW_SM2268XT_FE\inc

cd /dept/FW_vdk/users/lilly.huang/sm2508_v1.2.003_1208/sm2508/mp_flow
put "C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\MPTool\File For Linux Tool\*"

cd /dept/FW_vdk/users/lilly.huang/sm2508_v1.2.003_1208/sm2508/plat/EventLog_Parser_V1124A_auto_parse
ls
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\EzTool\LogSetting.dat

cd /dept/FW_vdk/users/lilly.huang/2504_ISP/IAR8.2/Debug
put C:\Code\Cmodle\2508\FW2-CModel-TestFW_ISP\IAR8.2\Debug\Exe

exit