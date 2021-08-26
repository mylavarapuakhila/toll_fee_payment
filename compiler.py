
#Gammar declaration
G={
   "declaration":["typevar_list"],
   "type":["int","float"],
   "var_list":["id","id,var_list"]
   }

#terminals and non-terminals of grammar
t=["int",",","float","id","$","lamda"]
nt=["declaration","type","var_list"]

#Left Factoring
for item in nt:
    if len(G[item]) > 1:
        for i in t+nt:
            if G[item][0].startswith(i) and G[item][1].startswith(i):
                G["S"] = ["lamda",G[item][1][len(i):]]
                G[item] = [i+"S"]

nt.append("S")
print("Grammar after Left Factoring : ",G,sep="\n",end="\n\n")

#Augmentation
G["E"] = ["declaration$"]
nt.insert(0,"E")
print("Grammar after augmentation : ",G,sep="\n",end="\n\n")

#First 
First = {"S":[],"var_list":[],"type":[],"declaration":[],"E":[]}
Fp = {"S":[],"var_list":[],"type":[],"declaration":[],"E":[]}

for item in nt[::-1]:
    for it in G[item]:
        for term in t:
            if(it.startswith(term)):
                First[item].append(term)
                Fp[item].append(G[item].index(it))
        for nterm in nt:
            if(it.startswith(nterm)):
                for f in  First[nterm]:
                    First[item].append(f)
                    Fp[item].append(G[item].index(it))
print("First of Grammar G : ",First,sep="\n",end="\n\n")

#Follow
follow={"S":["$"]}

#Parse Table
Table= [t[:-1]]

for item in nt:
    row = []
    for ter in t[:-1]:
        if ter not in First[item]:
            row.append("--")
        else:
            row.append(item+"->"+G[item][Fp[item][First[item].index(ter)]])
    if "lamda" in First[item]:
        for it in follow[item]:
            row[t.index(it)]=item+"->lamda"
    Table.append(row)
    