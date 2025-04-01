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
            arrayQueries[i].append(db + " " + qName + " 2001-01-01T00:00:00 2001-01-31T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2001-02-01T00:00:00 2001-02-28T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2001-03-01T00:00:00 2001-03-31T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2001-04-01T00:00:00 2001-04-30T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2001-05-01T00:00:00 2001-05-31T00:00:00 80004 7")
            arrayQueries[i].append(db + " " + qName + " 2001-06-01T00:00:00 2001-06-30T00:00:00 80004 7")
            arrayQueries[i].append(db + " " + qName + " 2001-07-01T00:00:00 2001-07-31T00:00:00 80026 7")
            arrayQueries[i].append(db + " " + qName + " 2001-08-01T00:00:00 2001-08-31T00:00:00 80004 7")
            arrayQueries[i].append(db + " " + qName + " 2001-09-01T00:00:00 2001-09-30T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2001-10-01T00:00:00 2001-10-31T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2001-11-01T00:00:00 2001-11-30T00:00:00 80058 7")
            arrayQueries[i].append(db + " " + qName + " 2001-12-01T00:00:00 2001-12-31T00:00:00 80155 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2001-01-01T00:00:00 2001-01-31T00:00:00 80002 94213")
            arrayQueries[i].append(db + " " + qName + " 2001-02-01T00:00:00 2001-02-28T00:00:00 80058 25775")
            arrayQueries[i].append(db + " " + qName + " 2001-03-01T00:00:00 2001-03-31T00:00:00 80058 20747")
            arrayQueries[i].append(db + " " + qName + " 2001-04-01T00:00:00 2001-04-30T00:00:00 80002 72097")
            arrayQueries[i].append(db + " " + qName + " 2001-05-01T00:00:00 2001-05-31T00:00:00 80004 23083")
            arrayQueries[i].append(db + " " + qName + " 2001-06-01T00:00:00 2001-06-30T00:00:00 80004 11146")
            arrayQueries[i].append(db + " " + qName + " 2001-07-01T00:00:00 2001-07-31T00:00:00 80026 74503")
            arrayQueries[i].append(db + " " + qName + " 2001-08-01T00:00:00 2001-08-31T00:00:00 80004 25739")
            arrayQueries[i].append(db + " " + qName + " 2001-09-01T00:00:00 2001-09-30T00:00:00 80058 19696")
            arrayQueries[i].append(db + " " + qName + " 2001-10-01T00:00:00 2001-10-31T00:00:00 80058 95090")
            arrayQueries[i].append(db + " " + qName + " 2001-11-01T00:00:00 2001-11-30T00:00:00 80058 31770")
            arrayQueries[i].append(db + " " + qName + " 2001-12-01T00:00:00 2001-12-31T00:00:00 80155 27333")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2001-01-01T00:00:00 2001-01-31T00:00:00 4286 15112 19538")
            arrayQueries[i].append(db + " " + qName + " 2001-02-01T00:00:00 2001-02-28T00:00:00 60030 23684 18665")
            arrayQueries[i].append(db + " " + qName + " 2001-03-01T00:00:00 2001-03-31T00:00:00 6179 16493 10593")
            arrayQueries[i].append(db + " " + qName + " 2001-04-01T00:00:00 2001-04-30T00:00:00 25869 24338 7030")
            arrayQueries[i].append(db + " " + qName + " 2001-05-01T00:00:00 2001-05-31T00:00:00 3935 2934 2403")
            arrayQueries[i].append(db + " " + qName + " 2001-06-01T00:00:00 2001-06-30T00:00:00 16279 55523 66189")
            arrayQueries[i].append(db + " " + qName + " 2001-07-01T00:00:00 2001-07-31T00:00:00 10402 31309 27905")
            arrayQueries[i].append(db + " " + qName + " 2001-08-01T00:00:00 2001-08-31T00:00:00 424 30093 84142")
            arrayQueries[i].append(db + " " + qName + " 2001-09-01T00:00:00 2001-09-30T00:00:00 31264 54623 32559")
            arrayQueries[i].append(db + " " + qName + " 2001-10-01T00:00:00 2001-10-31T00:00:00 8653 8434 40573")
            arrayQueries[i].append(db + " " + qName + " 2001-11-01T00:00:00 2001-11-30T00:00:00 25177 27253 28973")
            arrayQueries[i].append(db + " " + qName + " 2001-12-01T00:00:00 2001-12-31T00:00:00 19155 81270 7089")
            '''arrayQueries[i].append(db + " " + qName + " 2001-01-01T00:00:00 2001-01-31T00:00:00 4286 10112 32421 15112 78214 5692 19538 5355 66170")
            arrayQueries[i].append(db + " " + qName + " 2001-02-01T00:00:00 2001-02-28T00:00:00 60030 96695 52872 23684 15935 5783 18665 13476 62933")
            arrayQueries[i].append(db + " " + qName + " 2001-03-01T00:00:00 2001-03-31T00:00:00 6179 19147 21469 16493 62608 27436 10593 5970 4595")
            arrayQueries[i].append(db + " " + qName + " 2001-04-01T00:00:00 2001-04-30T00:00:00 25869 3435 80490 24338 31295 13070 7030 27192 20540")
            arrayQueries[i].append(db + " " + qName + " 2001-05-01T00:00:00 2001-05-31T00:00:00 3935 17530 30090 2934 85560 5056 2403 42811 96365")
            arrayQueries[i].append(db + " " + qName + " 2001-06-01T00:00:00 2001-06-30T00:00:00 16279 46656 5304 55523 65951 93560 66189 17493 92613")
            arrayQueries[i].append(db + " " + qName + " 2001-07-01T00:00:00 2001-07-31T00:00:00 10402 95725 96463 31309 89132 99346 27905 7368 17344")
            arrayQueries[i].append(db + " " + qName + " 2001-08-01T00:00:00 2001-08-31T00:00:00 424 9753 14489 30093 78913 89171 84142 28858 29786")
            arrayQueries[i].append(db + " " + qName + " 2001-09-01T00:00:00 2001-09-30T00:00:00 31264 61348 23549 54623 9332 75996 32559 3722 92291")
            arrayQueries[i].append(db + " " + qName + " 2001-10-01T00:00:00 2001-10-31T00:00:00 8653 90273 2291 8434 9361 30707 40573 30 48297")
            arrayQueries[i].append(db + " " + qName + " 2001-11-01T00:00:00 2001-11-30T00:00:00 25177 10768 13098 27253 328 27724 28973 30816 69333")
            arrayQueries[i].append(db + " " + qName + " 2001-12-01T00:00:00 2001-12-31T00:00:00 19155 29621 59630 81270 30775 32153 7089 2940 3817")'''
        
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