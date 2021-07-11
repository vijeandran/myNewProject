import json

col_append_temptab=[]
col_append_TGTtab=[]


with open("/home/vijee/Python/coltype.json") as f:
    col_val = json.load(f)

for colval in col_val:
    if colval['col_type'] == 'usual':
        col_append_temptab.append("ADD COLUMN "+colval["column"]+" "+colval["datatype"]+",")

print(col_append_temptab)


for colval in col_val:
    col_append_TGTtab.append("ADD COLUMN "+colval["column"]+" "+colval["datatype"]+",")

print(col_append_TGTtab)

colForTemp = " ".join([str(ele) for ele in col_append_temptab])
colTGTtab = " ".join([str(ele) for ele in col_append_TGTtab])

print(colForTemp)
print(colTGTtab)

print('##########')
