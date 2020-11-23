
# Latest modified time: October 18, 2020
# Author:  lugen
# help 目录需要创建两个文件夹 output文件夹 out文件 用于放置转换完的pdbqt格式文件
# out文件夹为结果输出文件
# 目录需要vina(vina程序文件)  conf.txt(vina配置文件) out文件夹  pdb格式的蛋白质受体文件
# 使用时 ./vina_screen_virtual.sh >log
# 同时输出到屏幕和文件./vina_screen_virtual.sh 2>&1 |tee log (log文件为日志名)
#! /bin/bash
for f in output/*.pdbqt; do
    b=`basename $f .pdbqt`
	echo $b
	echo $f
    echo Processing ligand $b
    mkdir -p  ./out/$b
    ./vina --config conf.txt --ligand $f --out ./out/${b}/out.pdbqt --log ./out/${b}/log.txt
done
