# Latest modified time: October 29, 2020
# Author:  lugen
# help 目录需要放置log文件，log文件为vina输出日志
# 先输出虚拟筛选结果auto-dock-vina-score-result
# 输出虚拟筛选得分小于-10kcal/mol的分子名及结果
# 输出排序后的虚拟筛选结果得分小于-10kcal/mol的分子名
f = open("log.txt", "w")
d = {}
Dividing_line = "-*"*15
f.write ("\n"+Dividing_line +"auto-dock-vina-score-result"+Dividing_line+"\n")
for line in open("log"):
   if line.startswith('Processing ligand'):
      mol = line[17:28]
      mol_name  = mol.strip()
      print(mol_name,end=" ")
      f.write(mol_name)
   elif line.startswith('WARNING: Check that it is large enough'):
      print("0")
      f.write(" 0")
      f.write('\n')
      d[mol_name] = int(0)
   elif line.startswith('Parse error'):
      print("0")
      f.write(" 0")
      f.write('\n')
      d[mol_name] = int(0)
   elif line.startswith('   1        '):
      score = (line[12:19])
      print(score)
      f.write(score)
      f.write('\n')
      d[mol_name] = float(score.strip())
d_order=sorted(d.items(),key=lambda x:x[1],reverse=False)
f.write("\n"+Dividing_line + 'score < -8 result'+Dividing_line+"\n")
print("\n"+Dividing_line + 'score < -8 result'+Dividing_line+"\n")
v = dict(d_order)
for sorted_mol_name in v.keys():
   if d[sorted_mol_name] < -8.5 :
      f.write("\n")
      f.write(str(sorted_mol_name))
      print(sorted_mol_name)
print("\n"+Dividing_line + 'score < -10 result'+Dividing_line+"\n")
f.write("\n"+Dividing_line + 'score < -10 result'+Dividing_line+"\n")
v = dict(d_order[:100])
for sorted_mol_name in v.keys():
   if d[sorted_mol_name] < -10 :
      f.write("\n")
      f.write(str(sorted_mol_name))
      print(sorted_mol_name)
f.close()