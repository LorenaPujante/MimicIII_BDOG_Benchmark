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

queryNames = ['1', '2', '2p', '3']#, '4', '4p', '5', '6', '6m']



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
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80071 7")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80017 7")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80081 7")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80085 7")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 80139 24067")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 80085 59948")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 80081 82910")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 80085 20312")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 80071 13696")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 80085 88740")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 80081 93325")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 80017 26015")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 80081 8723")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80085 29967")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7988")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 4180")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 97543 16518 50427")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 12805 9906 75517")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 31841 17578 27431")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 8532 4765 27192")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 31144 8302 9149")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 11565 1041 83357")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 4158 24740 29937")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 26950 14423 47709")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 96774 96652 78005")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 47509 22355 15411")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 3359 43797 10732")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 21681 4316 21348")
            '''arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 97543 12013 30964 16518 7155 54708 50427 9838 19842")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 12805 31185 84078 9906 11702 16911 75517 14314 29952")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 31841 59102 4591 17578 23344 9986 27431 5121 63934")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 8532 12470 24383 4765 68923 87801 27192 77502 25779")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 31144 87980 28792 8302 27565 28190 9149 55204 19055")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 11565 17518 23288 1041 7816 32378 83357 16336 32531")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 4158 17224 52193 24740 98656 6155 29937 6134 12168")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 26950 29645 30277 14423 5927 3276 47709 32765 59831")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 96774 98768 18736 96652 1942 8470 78005 71927 99067")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 47509 50189 56001 22355 49999 69359 15411 21970 16040")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 3359 12632 307 43797 248 1573 10732 3448 70558")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 21681 24622 44841 4316 20456 723 21348 11255 2808")'''
        
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