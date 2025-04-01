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
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 80004 7")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80004 7")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80293 7")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 80085 61671")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 80004 32023")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80085 54857")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80139 91096")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80004 16819")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80139 83913")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80139 27484")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80139 29558")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80293 52409")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80081 12245")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80081 25769")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 4180")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 51871 67684 638")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 83565 3218 13038")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 62412 54508 84694")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 46034 47733 51992")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 56339 11620 32728")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 11309 25307 17853")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 22466 10625 16428")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 48011 20855 12619")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 27808 42021 79617")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 26901 56468 24854")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 21030 97876 91855")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 26554 20445 30641")
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 51871 10425 23028 67684 3949 18356 638 16682 26443")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 83565 58356 30566 3218 5078 9286 13038 17282 95708")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 62412 29589 57081 54508 13778 5604 84694 1332 9308")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 46034 53771 63109 47733 30176 18194 51992 16674 79894")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 56339 16426 79188 11620 16072 24289 32728 66657 18538")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 11309 32093 4874 25307 83357 12485 17853 90648 64472")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 22466 28749 12411 10625 19106 15596 16428 28525 10820")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 48011 75607 23652 20855 26426 49188 12619 19040 29164")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 27808 18260 25964 42021 29163 63961 79617 1329 19412")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 26901 6653 12937 56468 14473 24903 24854 19799 89176")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 21030 41943 62681 97876 20902 25340 91855 17263 20747")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 26554 11927 68902 20445 28050 29740 30641 1191 75369")
        
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