import subprocess
import os
import sys

abcMinus = ['a','b','c',
                    'd','e','f',
                    'g','h','i',
                    'j','k','l',
                    'm','n','o',
                    'p','q','r',
                    's','t','u',
                    'v','w','x',
                    'y','z']

queryNames = ['1', '2', '2p', '3', '4', '4p', '5', '6', '6m']



#########
# INPUT #
#########

def whichDB():
    db = sys.argv[1]
    if db == "neo4j" or db == "sparql" or db == "star":
        return db
    return False

def getArrayQueries(db):
    arrayQueries = []
    for i in range(len(queryNames)):
        qName = queryNames[i]
        
        if qName == "1":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2002-01-01T00:00:00 2002-01-31T00:00:00 80155 7")
            arrayQueries[i].append(db + " " + qName + " 2002-02-01T00:00:00 2002-02-28T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2002-03-01T00:00:00 2002-03-31T00:00:00 80053 7")
            arrayQueries[i].append(db + " " + qName + " 2002-04-01T00:00:00 2002-04-30T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2002-05-01T00:00:00 2002-05-31T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2002-06-01T00:00:00 2002-06-30T00:00:00 80053 7")
            arrayQueries[i].append(db + " " + qName + " 2002-07-01T00:00:00 2002-07-31T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2002-08-01T00:00:00 2002-08-31T00:00:00 80026 7")
            arrayQueries[i].append(db + " " + qName + " 2002-09-01T00:00:00 2002-09-30T00:00:00 80053 7")
            arrayQueries[i].append(db + " " + qName + " 2002-10-01T00:00:00 2002-10-31T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2002-11-01T00:00:00 2002-11-30T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2002-12-01T00:00:00 2002-12-31T00:00:00 80002 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2002-01-01T00:00:00 2002-01-31T00:00:00 80155 72775")
            arrayQueries[i].append(db + " " + qName + " 2002-02-01T00:00:00 2002-02-28T00:00:00 80002 31165")
            arrayQueries[i].append(db + " " + qName + " 2002-03-01T00:00:00 2002-03-31T00:00:00 80053 766")
            arrayQueries[i].append(db + " " + qName + " 2002-04-01T00:00:00 2002-04-30T00:00:00 80002 32548")
            arrayQueries[i].append(db + " " + qName + " 2002-05-01T00:00:00 2002-05-31T00:00:00 80058 21705")
            arrayQueries[i].append(db + " " + qName + " 2002-06-01T00:00:00 2002-06-30T00:00:00 80053 9920")
            arrayQueries[i].append(db + " " + qName + " 2002-07-01T00:00:00 2002-07-31T00:00:00 80058 10248")
            arrayQueries[i].append(db + " " + qName + " 2002-08-01T00:00:00 2002-08-31T00:00:00 80026 28343")
            arrayQueries[i].append(db + " " + qName + " 2002-09-01T00:00:00 2002-09-30T00:00:00 80053 6855")
            arrayQueries[i].append(db + " " + qName + " 2002-10-01T00:00:00 2002-10-31T00:00:00 80002 14824")
            arrayQueries[i].append(db + " " + qName + " 2002-11-01T00:00:00 2002-11-30T00:00:00 80002 65989")
            arrayQueries[i].append(db + " " + qName + " 2002-12-01T00:00:00 2002-12-31T00:00:00 80002 82575")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2002-01-01T00:00:00 2002-01-31T00:00:00 83869 78318 24575")
            arrayQueries[i].append(db + " " + qName + " 2002-02-01T00:00:00 2002-02-28T00:00:00 64406 4406 63886")
            arrayQueries[i].append(db + " " + qName + " 2002-03-01T00:00:00 2002-03-31T00:00:00 13599 24248 23829")
            arrayQueries[i].append(db + " " + qName + " 2002-04-01T00:00:00 2002-04-30T00:00:00 94064 99334 24588")
            arrayQueries[i].append(db + " " + qName + " 2002-05-01T00:00:00 2002-05-31T00:00:00 5032 14821 9248")
            arrayQueries[i].append(db + " " + qName + " 2002-06-01T00:00:00 2002-06-30T00:00:00 17908 3632 23150")
            arrayQueries[i].append(db + " " + qName + " 2002-07-01T00:00:00 2002-07-31T00:00:00 3426 9969 49999")
            arrayQueries[i].append(db + " " + qName + " 2002-08-01T00:00:00 2002-08-31T00:00:00 40066 3924 41452")
            arrayQueries[i].append(db + " " + qName + " 2002-09-01T00:00:00 2002-09-30T00:00:00 19343 6600 17886")
            arrayQueries[i].append(db + " " + qName + " 2002-10-01T00:00:00 2002-10-31T00:00:00 89544 53591 198")
            arrayQueries[i].append(db + " " + qName + " 2002-11-01T00:00:00 2002-11-30T00:00:00 90929 71726 4571")
            arrayQueries[i].append(db + " " + qName + " 2002-12-01T00:00:00 2002-12-31T00:00:00 49727 99528 30868")
            '''arrayQueries[i].append(db + " " + qName + " 2002-01-01T00:00:00 2002-01-31T00:00:00 83869 82320 32285 78318 49431 14696 24575 32697 21015")
            arrayQueries[i].append(db + " " + qName + " 2002-02-01T00:00:00 2002-02-28T00:00:00 64406 23153 59599 4406 87174 32402 63886 73917 79751")
            arrayQueries[i].append(db + " " + qName + " 2002-03-01T00:00:00 2002-03-31T00:00:00 13599 25704 7119 24248 79814 81668 23829 9481 27356")
            arrayQueries[i].append(db + " " + qName + " 2002-04-01T00:00:00 2002-04-30T00:00:00 94064 14240 24575 99334 12532 11148 24588 1042 27800")
            arrayQueries[i].append(db + " " + qName + " 2002-05-01T00:00:00 2002-05-31T00:00:00 5032 65412 44630 14821 52298 9224 9248 6927 7763")
            arrayQueries[i].append(db + " " + qName + " 2002-06-01T00:00:00 2002-06-30T00:00:00 17908 22661 28102 3632 14602 23156 23150 10859 15686")
            arrayQueries[i].append(db + " " + qName + " 2002-07-01T00:00:00 2002-07-31T00:00:00 3426 5391 53992 9969 9428 48755 49999 13736 22921")
            arrayQueries[i].append(db + " " + qName + " 2002-08-01T00:00:00 2002-08-31T00:00:00 40066 20325 19497 3924 70651 10947 41452 81008 5772")
            arrayQueries[i].append(db + " " + qName + " 2002-09-01T00:00:00 2002-09-30T00:00:00 19343 16015 27232 6600 16194 3394 17886 10106 2405")
            arrayQueries[i].append(db + " " + qName + " 2002-10-01T00:00:00 2002-10-31T00:00:00 89544 50315 1992 53591 6739 27248 198 30305 30893")
            arrayQueries[i].append(db + " " + qName + " 2002-11-01T00:00:00 2002-11-30T00:00:00 90929 60668 307 71726 20061 66637 4571 21765 17689")
            arrayQueries[i].append(db + " " + qName + " 2002-12-01T00:00:00 2002-12-31T00:00:00 49727 76994 17127 99528 13588 83598 30868 18799 20844")'''
        
        if qName == "4"  or  qName == "4p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-14T00:00:00 2000-01-30T00:00:00 31935 82642")

        if qName == "5":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-14T00:00:00 2000-01-30T00:00:00 80155 5193 31935 82642 13181 21040")
        
        if qName == "6"  or  qName == "6m":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-14T00:00:00 2000-01-30T00:00:00 3 0c 80155")

    return arrayQueries



###########
# OUTPUT #    
###########

def parseOutput(output):    
    output = output[0].decode('utf-8')
    #print(output)
    lines = output.split("\n")
    
    lineTime = lines[0]
    lineTime = lineTime.split(" ")
    nResults = lineTime[0]
    timeMilis = lineTime[1]
    
    lineMem = lines[1]
    lineMem = lineMem.split(" ")
    initMemKB = lineMem[0]
    maxMemKB = lineMem[1]
    #print("initMemKB: {}".format(initMemKB))
    #print("maxMemKB: {}".format(maxMemKB))
    difMemKB = int(maxMemKB)-int(initMemKB)
    
    return nResults, timeMilis, initMemKB, maxMemKB, difMemKB

def getNameFile(db, nQuery, iQuery):
    nameFile = "{}_{}_{}.csv".format(db, nQuery, abcMinus[iQuery])
    return nameFile
    
def writeOutput(nameFile, nResults, timeMilis, initMemKB, maxMemKB, difMemKB):
    dirResults = "/home/lorena/Escritorio/appTests/output"
    if (not os.path.exists(dirResults)):
        os.makedirs(dirResults)

    ruteFile = "{}/{}".format(dirResults, nameFile)
    if (os.path.exists(ruteFile)):
        file = open(ruteFile, 'a+')
    else:
        file = open(ruteFile, 'w')
        file.write("nResults,timeMilis,initMemKB,maxMemKB,difMemKB\n")
    file.write("{},{},{},{},{}\n".format(nResults, timeMilis, initMemKB, maxMemKB, difMemKB))
    
    file.close()
    
    


########
# MAIN #
########

def main():

    db = whichDB()
    if not db:
        sys.exit("ERROR: Argument invalid\nValid options are:\n\tneo4j\tsparql\tstar")
        
    arrayQueries = getArrayQueries(db)

    querybase = "python3 /home/lorena/Escritorio/appTests/app.py "

    for setQueries in arrayQueries:
        for i in range(len(setQueries)):
            q = setQueries[i]
            for n in range(10):  # Cambiar a 1 para hacer pruebas   # Por defecto, 10
                query = querybase + q
                if db == "neo4j":
                    shell = './testNeo.sh'
                else:
                    shell = './testGDB.sh'
                
                sp = subprocess.Popen([shell, query], stdout=subprocess.PIPE)
                output = sp.communicate()
                
                nResults, timeMilis, initMemKB, maxMemKB, difMemKB = parseOutput(output)
                
                qSplit = q.split(" ")
                nQuery = qSplit[1]
                nameFile = getNameFile(db, nQuery, i)
                
                writeOutput(nameFile, nResults, timeMilis, initMemKB, maxMemKB, difMemKB)
        
        
        
        
        
        
        
        # Imprimir la salida a un fichero

if __name__ == "__main__":
    main()