#Author HaseeCLasher(Hasitha Amarathunga)
no_of_emp=int(input("How many Employee's Work : "))

jobemp={}
empjobcount={}
employee=[]
i=1
yorn='y'
maxemp=0
while (yorn=="y" or yorn=='Y'):
    if (maxemp<=no_of_emp):
        print("Enter job {0} Employees : ".format(i),end=" ")
        n=input()
        emplist=n.split(',')
        for d in emplist:
            if d not in employee:
                employee.append(d)
        jobemp[str(i)]=emplist
        i+=1
        yorn=input("Add More job (y/n) : ")
        maxemp=len(employee)
    else:
        print ("Max employee Must be {0}".format(no_of_emp))
        break

b=list(jobemp.items())
#print (jobemp)
#print (employee)
empls=list(jobemp.items())
emcount={}
for t in range(0,len(employee)):
    emcount[employee[t]]=0
#print (emcount)
for k in empls:
    count=0
    emps=k[1]
    for emp in emps:
        if emp in employee:
            emcount[emp]+=1

#print (emcount)

#finding employees who can combinations using M value
M=int(input("Enter M Value : "))

eligi_emp=[]
eligi_count=[]
for co in range(0,len(emcount)):
    if list(emcount.items())[co][1]>=M:
        eligi_count.append(list(emcount.items())[co][1])
        eligi_emp.append(list(emcount.items())[co][0])

eligi_emp.sort()

sample=[]

for m in range(len(eligi_emp)):
    for l in range(m+1,len(eligi_emp)):
        s=[eligi_emp[m],eligi_emp[l]]
        sample.append(s)


countsample=[]
for t in range(len(sample)):
    countsample.append(0)

for i in range(len(sample)):
    truelist=[]
    for k in b:
        for j in sample[i]:
            if j in k[1]:
                truelist.append(True)
            else:
                truelist.append(False)
        if False not in truelist:
            countsample[i]+=1
        truelist=[]

selected=[]
#remeber 2-Combination values selected
for count in range(0,len(countsample)):
    if countsample[count]>=M:
        selected.append(sample[count])


newcombls=[]
for i in selected:
    for j in i:
        if j not in newcombls:
            newcombls.append(j)
#remeber 2-Combination values M values in selectedcount
selectedcount=[]

for i in countsample:
    if i>=M:
        selectedcount.append(i)
#________________________________________



        
a=selected
fulllist=[]
fulllist.append(eligi_emp)
fulllist.append(a)

# define Combination 

import copy

cl=[]
def combination(comblist,data,length): 
    for i in range(0,len(data)):
        new_comblist = copy.copy(comblist)
        new_data = copy.copy(data)
        new_comblist.append(data[i])
        new_data = data[i+1:]
        if len(new_comblist)==length:
            cl.append(new_comblist)
        combination(new_comblist,new_data,length)


def show():
    for i in cl:
        print (i)
 
comblist = []



#Selected Combinations.

combination_count=len(a[0])+1
c=[]
x=len(a[0])

fullcombcount=[]
combinationlist=[]

def done(a,combination_count):    
    l1={}
    
    counta=[]
    for t in range(len(a)):
        counta.append(0)

    for i in range(len(a)):
        truelist=[]
        for k in b:
            for j in a[i]:
                if j in k[1]:
                    truelist.append(True)
                else:
                    truelist.append(False)
            if False not in truelist:
                counta[i]+=1
            truelist=[]
    #print ("A")
    #print (a)
    #print ("Counta")
    #print (counta)
    selected=[]
    selectedcount=[]
    for count in range(0,len(counta)):
        if counta[count]>=M:
            selected.append(a[count])
            selectedcount.append(counta[count])

    #print ("selected.")
    #print (selected)
    fullcombcount.append(selectedcount)
    combinationlist.append(selected)
    
    newcombls=[]       
    for i in selected:
        for j in i:
            if j not in newcombls:
                newcombls.append(j)
    #print ("Newcombls")
    #print (newcombls)
    combination(comblist,newcombls,combination_count)
    
    
    newcl=[]
    for i in cl:
        if len(i)==combination_count:
            newcl.append(i)

    c.append(newcl)
    a=newcl
    return a

a=done(a,combination_count)

while len(a)>0:
    fulllist.append(a)
    combination_count+=1
    a=done(a,combination_count)



combinationlist.reverse()
#combinationlist.append(eligi_emp)
fullcombcount.reverse()
#fullcombcount.append(eligi_count)


#Get combinationlist and it's Eligible value for two lists correct order
combina_list=[]
combina_count=[]

for i in combinationlist:
    for j in i:
        combina_list.append(j)

for p in fullcombcount:
    for q in p:
        combina_count.append(q)



#Get PTS values
PTS=[]
maxLen=len(combina_list[0])
for i in range(0,len(combina_list)):
    a=combina_list[i]
    n=combina_count[i]
    length=len(a)
    if length==maxLen:
        PTS.append(a)
    for j in combina_list:
        if len(j)==length-1:
            val=1
            for k in j: 
                if k in a:
                    val=val*1
                else:
                    val=val*0
            #print (val)
            
            ind=combina_list.index(j)
            if val==0 and j not in PTS:
                PTS.append(j)
            elif combina_count[ind] > n and j not in PTS:
                PTS.append(j)
#________________________________
                
eligi_emp2=[]
for i in eligi_emp:
    eligi_emp2.append([i])
    
eligi_emp=eligi_emp2

combinationlist.append(eligi_emp)
fullcombcount.append(eligi_count)


#collect all combination for combi_list and It's M value for combi_count 
combi_list=[]
combi_count=[]
for i in combinationlist:
    for j in i:
        combi_list.append(j)

for p in fullcombcount:
    for q in p:
        combi_count.append(q)

    

#User Input Trust value Formula.......

T=int(input("Input Trust Value : "))



#Combination Trust value...............

import copy

cl2=[]
def combination(comblist,data): 
    for i in range(0,len(data)):
        new_comblist = copy.copy(comblist)
        new_data = copy.copy(data)
        new_comblist.append(data[i])
        new_data = data[i+1:]
        if new_comblist!= data:
            cl2.append(new_comblist)
        combination(new_comblist,new_data)


def show():
    for i in cl2:
        print (i)
 
comblist2 = []



#Finding Combination for calculate Trust value



full=[]
fully=[]
for i in range(len(combi_list)):
    p=[]
    combination(comblist2,combi_list[i])
    full.append(cl2)
    for k in full[i]:
        if k != combi_list[i]:
            p.append(k)
            p.append(combi_list[i])
            fully.append(p)
            p=[]
    comblist2 = []
    cl2=[]

#___________________________________________________________
#Finding Formula Final Step

formula=[]
TVlist=[]
for com in fully:
    l1=[]
    for i in combi_list:        
        if i==com[0]:
            index0=combi_list.index(i)
            val1=combi_count[index0]
            l1.append(com[0])
        elif i==com[1]:    
            index2=combi_list.index(i)
            val2=combi_count[index2]
            l1.append(com[1])

    TV=(val2/val1)*100
    TVlist.append(TV)


#creating two list like (from A-->BCD formula A value for list. and BCD value for another list)

xval=[]
yval=[]
for i in range(len(TVlist)):    
    if TVlist[i]>=T:
        xval.append(fully[i][0])
        yval.append(fully[i][1])


#collecting Formula.............
xv=xval
yv=yval
yl=[]
for i in range(len(xv)):
    ele=[]
    for y in yv[i]:
        if y not in xv[i] :
            ele.append(y)
    yl.append(ele)

    
for i in range(len(xv)):
    formula.append(str(xv[i])+"-->"+ str(yl[i])) 


#For view Formula.........
def showFormula():
    for k in formula:
        print (k)
#this is the final Output of the system.
showFormula()
#Developed By Hasitha Amarathunga
