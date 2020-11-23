# Latest modified time: October 15, 2020
# Author:  lugen
# help 目录需要创建两个文件夹 input文件夹 放置未转换的mol2格式文件
# output文件夹为输出文件
# 需要Open Babel环境
# Open Babel 用法 http://openbabel.org/wiki/Main_Page

#! /bin/bash
i=1
for f in ./input/*.mol2; do
	b=`basename $f `
	echo "path+name" ${f}
	echo "name" ${b} 
	echo $i
	pdbqtname="TCM${i}"
	echo $pdbqtname
	obabel -imol2 ${f} -omol -O ./output/${b}.pdbqt -h 
	i=$(($i+1))
	echo $i
done