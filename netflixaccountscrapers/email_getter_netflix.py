import re
import csv

def writetoCSV(email, pwd):
    with open('netflix.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(["SN", "Email", "Password"])
        writer.writerow([email,pwd])

with open('netflix.csv', 'w', newline='') as file:
    #count =1
    writer = csv.writer(file)
    writer.writerow(["Email", "Password"])

#count =1
f=open("netflix_output.txt",'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
 line.strip()
 if not line:
      break
 email = re.findall('\S+@\S+', line)
 email = [x for x in email if x]
 for char in  "[ ] ' \n":
     email = (str(email)).replace(char,'')
 part = (str(email)).partition(':')
 email = part[0]
 pwd = part[2]
 #print(email)
 #print(pwd)
 writetoCSV(str(email),str(pwd))
 #count = count+1

 #file =open("sortedmail.txt",'w')
#file.close()
#file =open("sortedmail.txt",'r')
#print(file.read())
#file.close()

#print('Writing to csv complete...')
#bln = filterval.filter_csv()
#if(bln == true):
#    print('Filtered data successfully')
#else :
#    print('Filtering failed')
