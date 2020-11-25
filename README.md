# vina_screening_virtual
# Latest modified time: October 18, 2020
# Author:  陆根 刘金玲

## 虚拟筛选及分析脚本

### 将分子文件转化为vina可以识别的***pdbqt***文件

help： 目录需要创建两个文件夹 ***input***文件夹 放置未转换的mol2格式文件

***output***文件夹为输出文件

需要Open Babel环境

Open Babel 用法 *http://openbabel.org/wiki/Main_Page*  

脚本用法： ***./mol2-pdbqt.sh***  

如果提示权限不够 可使用 ***chmod + x mol2-pdbqt.sh***
  
### 虚拟筛选脚本

help： 目录需要创建两个文件夹 ***output***文件夹***out***文件夹 用于放置转换完的pdbqt格式文件out文件夹为结果输出文件  

目录需要***vina***(vina程序文件) ***conf.txt***(vina配置文件) ***out***文件夹  ***protein.pdb*** 格式的蛋白质受体文件 

脚本用法： ***./vina_screen_virtual.sh >log***

同时输出到屏幕和文件 ***./vina_screen_virtual.sh 2>&1 |tee log*** (log文件为日志名)
  
### 对接完日志分析脚本  

help： 目录需要放置***log***文件，log文件为vina输出日志 ***log.txt***为分析完的输出文件

打开日志***log.txt***    

需要python环境 python >= 3.0
 
先输出虚拟筛选结果auto-dock-vina-score-result

输出虚拟筛选得分小于-8kcal/mol的分子名及结果

输出排序后的虚拟筛选结果得分小于-10kcal/mol的分子名  

脚本用法：***python log.py***
 
