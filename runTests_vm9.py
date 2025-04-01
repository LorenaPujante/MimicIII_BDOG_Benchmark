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
            arrayQueries[i].append(db + " " + qName + " 2004-01-01T00:00:00 2004-01-31T00:00:00 80155 7")
            arrayQueries[i].append(db + " " + qName + " 2004-02-01T00:00:00 2004-02-29T00:00:00 80155 7")
            arrayQueries[i].append(db + " " + qName + " 2004-03-01T00:00:00 2004-03-31T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2004-04-01T00:00:00 2004-04-30T00:00:00 80155 7")
            arrayQueries[i].append(db + " " + qName + " 2004-05-01T00:00:00 2004-05-31T00:00:00 80053 7")
            arrayQueries[i].append(db + " " + qName + " 2004-06-01T00:00:00 2004-06-30T00:00:00 80002 7")
            arrayQueries[i].append(db + " " + qName + " 2004-07-01T00:00:00 2004-07-31T00:00:00 80053 7")
            arrayQueries[i].append(db + " " + qName + " 2004-08-01T00:00:00 2004-08-31T00:00:00 80053 7")
            arrayQueries[i].append(db + " " + qName + " 2004-09-01T00:00:00 2004-09-30T00:00:00 80023 7")
            arrayQueries[i].append(db + " " + qName + " 2004-10-01T00:00:00 2004-10-31T00:00:00 80023 7")
            arrayQueries[i].append(db + " " + qName + " 2004-11-01T00:00:00 2004-11-30T00:00:00 80155 7")
            arrayQueries[i].append(db + " " + qName + " 2004-12-01T00:00:00 2004-12-31T00:00:00 80155 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2004-01-01T00:00:00 2004-01-31T00:00:00 80155 72775")
            arrayQueries[i].append(db + " " + qName + " 2004-02-01T00:00:00 2004-02-29T00:00:00 80155 78708")
            arrayQueries[i].append(db + " " + qName + " 2004-03-01T00:00:00 2004-03-31T00:00:00 80075 76698")
            arrayQueries[i].append(db + " " + qName + " 2004-04-01T00:00:00 2004-04-30T00:00:00 80155 51060")
            arrayQueries[i].append(db + " " + qName + " 2004-05-01T00:00:00 2004-05-31T00:00:00 80053 5056")
            arrayQueries[i].append(db + " " + qName + " 2004-06-01T00:00:00 2004-06-30T00:00:00 80002 2115")
            arrayQueries[i].append(db + " " + qName + " 2004-07-01T00:00:00 2004-07-31T00:00:00 80053 17344")
            arrayQueries[i].append(db + " " + qName + " 2004-08-01T00:00:00 2004-08-31T00:00:00 80053 15728")
            arrayQueries[i].append(db + " " + qName + " 2004-09-01T00:00:00 2004-09-30T00:00:00 80023 19220")
            arrayQueries[i].append(db + " " + qName + " 2004-10-01T00:00:00 2004-10-31T00:00:00 80023 22332")
            arrayQueries[i].append(db + " " + qName + " 2004-11-01T00:00:00 2004-11-30T00:00:00 80155 88065")
            arrayQueries[i].append(db + " " + qName + " 2004-12-01T00:00:00 2004-12-31T00:00:00 80155 24747")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2004-01-01T00:00:00 2004-01-31T00:00:00 26685 12419 75838")
            arrayQueries[i].append(db + " " + qName + " 2004-02-01T00:00:00 2004-02-29T00:00:00 67924 53541 7487")
            arrayQueries[i].append(db + " " + qName + " 2004-03-01T00:00:00 2004-03-31T00:00:00 19496 24991 70990")
            arrayQueries[i].append(db + " " + qName + " 2004-04-01T00:00:00 2004-04-30T00:00:00 88078 24896 24588")
            arrayQueries[i].append(db + " " + qName + " 2004-05-01T00:00:00 2004-05-31T00:00:00 73536 77733 11765")
            arrayQueries[i].append(db + " " + qName + " 2004-06-01T00:00:00 2004-06-30T00:00:00 86903 25225 64897")
            arrayQueries[i].append(db + " " + qName + " 2004-07-01T00:00:00 2004-07-31T00:00:00 5399 13807 90158")
            arrayQueries[i].append(db + " " + qName + " 2004-08-01T00:00:00 2004-08-31T00:00:00 493 4640 24711")
            arrayQueries[i].append(db + " " + qName + " 2004-09-01T00:00:00 2004-09-30T00:00:00 57288 59979 1866")
            arrayQueries[i].append(db + " " + qName + " 2004-10-01T00:00:00 2004-10-31T00:00:00 64160 89634 3465")
            arrayQueries[i].append(db + " " + qName + " 2004-11-01T00:00:00 2004-11-30T00:00:00 12990 27659 44434")
            arrayQueries[i].append(db + " " + qName + " 2004-12-01T00:00:00 2004-12-31T00:00:00 94484 13813 96575")
            '''arrayQueries[i].append(db + " " + qName + " 2004-01-01T00:00:00 2004-01-31T00:00:00 26685 6066 59260 12419 82605 23464 75838 59421 9819")
            arrayQueries[i].append(db + " " + qName + " 2004-02-01T00:00:00 2004-02-29T00:00:00 67924 71760 98468 53541 62933 14716 7487 5206 27173")
            arrayQueries[i].append(db + " " + qName + " 2004-03-01T00:00:00 2004-03-31T00:00:00 19496 66508 15524 24991 17146 12585 70990 2941 29989")
            arrayQueries[i].append(db + " " + qName + " 2004-04-01T00:00:00 2004-04-30T00:00:00 88078 94404 20330 24896 27766 52482 24588 11813 66389")
            arrayQueries[i].append(db + " " + qName + " 2004-05-01T00:00:00 2004-05-31T00:00:00 73536 10019 12412 77733 69328 24892 11765 26539 20019")
            arrayQueries[i].append(db + " " + qName + " 2004-06-01T00:00:00 2004-06-30T00:00:00 86903 91398 4596 25225 12776 65951 64897 80454 88634")
            arrayQueries[i].append(db + " " + qName + " 2004-07-01T00:00:00 2004-07-31T00:00:00 5399 172 83663 13807 5125 3351 90158 4479 21083")
            arrayQueries[i].append(db + " " + qName + " 2004-08-01T00:00:00 2004-08-31T00:00:00 493 28721 31514 4640 67906 45495 24711 62380 76710")
            arrayQueries[i].append(db + " " + qName + " 2004-09-01T00:00:00 2004-09-30T00:00:00 57288 70929 31851 59979 30580 81025 1866 85769 56769")
            arrayQueries[i].append(db + " " + qName + " 2004-10-01T00:00:00 2004-10-31T00:00:00 64160 24634 9722 89634 24326 76561 3465 21420 29219")
            arrayQueries[i].append(db + " " + qName + " 2004-11-01T00:00:00 2004-11-30T00:00:00 12990 19473 98939 27659 43484 66637 44434 13521 15924")
            arrayQueries[i].append(db + " " + qName + " 2004-12-01T00:00:00 2004-12-31T00:00:00 94484 10606 94915 13813 16817 19997 96575 28992 30826")'''
        
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