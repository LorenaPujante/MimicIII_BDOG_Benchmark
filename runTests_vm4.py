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
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 80139 24067")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 80085 59948")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80085 54857")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80085 2165")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80085 29190")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80085 88740")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80081 93325")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80139 29558")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80139 26038")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80081 12245")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7988")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 4180")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-14T00:00:00 2000-01-30T00:00:00 31935 82642")
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 1009 8519 1257")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 25717 24843 2757")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 25542 86880 11090")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 4966 22560 20296")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 54940 30354 22933")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 9821 48145 27568")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 73702 7540 57276")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 11592 6255 13413")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 6510 14443 22849")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 12937 17786 92373")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 5832 903 50772")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 5989 52370 8846")
            '''arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 1009 10678 2539 8519 19472 5147 1257 638 22067")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 25717 21126 5772 24843 16294 5302 2757 3013 30678")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 25542 16744 16949 86880 1901 31576 11090 51914 14269")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 4966 1357 21514 22560 20165 8947 20296 906 77041")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 54940 25064 81846 30354 5545 5808 22933 83594 76880")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 9821 29972 10531 48145 54465 84610 27568 3657 98762")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 73702 26837 84629 7540 57955 30494 57276 29644 28271")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 11592 15301 74578 6255 20855 41724 13413 12619 4829")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 6510 25964 32618 14443 29415 70521 22849 1474 21238")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 12937 9984 5112 17786 72997 53953 92373 14990 90802")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 5832 62458 86516 903 20902 11818 50772 46257 17285")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 5989 6262 12530 52370 368 16849 8846 10903 17708")'''
        
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