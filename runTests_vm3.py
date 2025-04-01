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
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80254 17")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 80139 24067")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 80085 59948")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80081 2365")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80085 20312")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80085 29190")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80085 88740")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80081 93325")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80254 29470")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80085 47219")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80081 12245")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7988")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 4180")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 14599 30027 1116")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 25080 97567 8013")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 11623 3036 18103")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 1999 29574 2184")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 66574 42904 27530")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 63755 13584 15688")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 7871 4588 9531")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 48011 1098 89212")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 83093 11592 52659")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 6558 25740 32810")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 212 52828 76327")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 5989 44339 63243")
            '''arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 14599 29210 76601 30027 12805 5328 1116 2569 14392")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 25080 10670 6527 97567 95340 69904 8013 9484 5206")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 11623 90396 49603 3036 65237 5072 18103 20192 17805")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 1999 42515 2619 29574 8947 23402 2184 1930 11724")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 66574 32184 48827 42904 53771 6702 27530 65669 19940")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 63755 74779 83751 13584 13302 20975 15688 10207 23394")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 7871 78686 53014 4588 29180 23811 9531 19056 48340")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 48011 82038 22104 1098 73695 10947 89212 10104 49586")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 83093 3685 70929 11592 5908 25777 52659 20538 11135")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 6558 21312 10794 25740 21325 86276 32810 31585 29502")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 212 4598 6884 52828 88243 7326 76327 46257 53432")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 5989 7519 18259 44339 59184 95740 63243 76332 27337")'''
        
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