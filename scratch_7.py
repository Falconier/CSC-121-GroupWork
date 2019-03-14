##region imports
import pickle
##endregion



survey_data = {}
survey_data["p1"] = [5, 4, 4, 5, 3, 5]
survey_data["p2"] = [5, 5, 3, 5, 4, 3]
survey_data["p3"] = [3, 4, 5, 4, 3, 5]
survey_data["p4"] = [4, 5, 4, 5, 3, 5]
survey_data["p5"] = [2, 3, 4, 3, 5, 4]

##print(survey_data[1][0])

print(survey_data.values())

pckl = open("dicTest.data","wb")
for k,v in survey_data:
    pickle.dump(""+k+""+v+"",pckl)


pckl = open("dicTest.data","rb")
b=[]
while True:
    try:
        p = pickle.load(pckl)
        b.append(p)
    except:
        print("Failed or End of File")
        break
pckl.close()

d = {}
for e in b:
    tempList = str(e).split(",")
    N = tempList[0].strip("(").strip(")") + " " + tempList[1].strip("(").strip(")")
    E = tempList[2].strip("(").strip(")")
    d[N] = E