from sys import argv, exit
import csv

def main():
    if (len(argv) != 3):
        print("invalid")
        exit(1)


    with open(argv[2], "r") as sequence:
        reader = csv.reader(sequence)
        for i in reader:
            text = i[0]


    #list of keys
    keys = []
    with open(argv[1], "r") as file:
        reader=csv.reader(file)
        for i in reader:
            keys.append(i)
            break
        key = keys[0][1:]
        #print(key[0])

    #list of datas
    db = []
    with open(argv[1], "r") as file:
        reader=csv.DictReader(file)
        for i in reader:
            for k in range(len(key)):
                i[key[k]] = int(i[key[k]])
            db.append(i)
        #print(db)

    match(db, key, text)


def maxx(text, key):
    dictt = {}
    k=len(key)
    count=0
    i=0
    dictt[count]=0

    while(i < len(text)):
        j=i+k
        if text[i:j] == key:
            dictt[count]+=1
            i+=k #i+=1 yani i++ yerine i+=4 yani i+=k şeklinde iterate ediyor
        else:
            count+=1
            dictt[count]=0
            i+=1 #yanlışı 4(k) atlayamayız
    temp=0
    for i in dictt:
        if(temp<dictt[i]):
            temp=dictt[i]
    maxx=temp
    return(maxx)

def match(db, key, text):

    count=0
    for i in range(len(db)):
        for k in range(len(key)):
            if db[i][key[k]] == maxx(text, key[k]):
                count+=1
        if count == len(key):
            print(db[i]["name"])
            break
        else:
            count=0
    if count==0:
        print("no match")

main()
