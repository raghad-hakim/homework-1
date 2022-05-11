import json
infile=open("t.json",'r')
name=input("ENTER USERNAME")
n=0
d=json.load(infile)
infile.close()
for q,a in d.items():
    print(q)
    s=input("answer\n")
    if s==a:
        n+=1
out={"name":name,"result":n}
print(out)
outfile=open("result.json","w")
json.dump(out,outfile)
outfile.close()
