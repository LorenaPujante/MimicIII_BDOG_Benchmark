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
            arrayQueries[i].append(db + " " + qName + " 2005-01-01T00:00:00 2005-01-31T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-02-01T00:00:00 2005-02-28T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-03-01T00:00:00 2005-03-31T00:00:00 80023 7")
            arrayQueries[i].append(db + " " + qName + " 2005-04-01T00:00:00 2005-04-30T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-05-01T00:00:00 2005-05-31T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-06-01T00:00:00 2005-06-30T00:00:00 80155 7")
            arrayQueries[i].append(db + " " + qName + " 2005-07-01T00:00:00 2005-07-31T00:00:00 80023 7")
            arrayQueries[i].append(db + " " + qName + " 2005-08-01T00:00:00 2005-08-31T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-09-01T00:00:00 2005-09-30T00:00:00 80023 7")
            arrayQueries[i].append(db + " " + qName + " 2005-10-01T00:00:00 2005-10-31T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-11-01T00:00:00 2005-11-30T00:00:00 80075 7")
            arrayQueries[i].append(db + " " + qName + " 2005-12-01T00:00:00 2005-12-31T00:00:00 80075 7")
        
        if qName == "2"  or  qName == "2p":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2005-01-01T00:00:00 2005-01-31T00:00:00 80075 13806")
            arrayQueries[i].append(db + " " + qName + " 2005-02-01T00:00:00 2005-02-28T00:00:00 80075 14755")
            arrayQueries[i].append(db + " " + qName + " 2005-03-01T00:00:00 2005-03-31T00:00:00 80023 49496")
            arrayQueries[i].append(db + " " + qName + " 2005-04-01T00:00:00 2005-04-30T00:00:00 80075 11019")
            arrayQueries[i].append(db + " " + qName + " 2005-05-01T00:00:00 2005-05-31T00:00:00 80075 5161")
            arrayQueries[i].append(db + " " + qName + " 2005-06-01T00:00:00 2005-06-30T00:00:00 80155 4883")
            arrayQueries[i].append(db + " " + qName + " 2005-07-01T00:00:00 2005-07-31T00:00:00 80023 15216")
            arrayQueries[i].append(db + " " + qName + " 2005-08-01T00:00:00 2005-08-31T00:00:00 80075 29242")
            arrayQueries[i].append(db + " " + qName + " 2005-09-01T00:00:00 2005-09-30T00:00:00 80023 72482")
            arrayQueries[i].append(db + " " + qName + " 2005-10-01T00:00:00 2005-10-31T00:00:00 80075 28315")
            arrayQueries[i].append(db + " " + qName + " 2005-11-01T00:00:00 2005-11-30T00:00:00 80075 97547")
            arrayQueries[i].append(db + " " + qName + " 2005-12-01T00:00:00 2005-12-31T00:00:00 80075 58862")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2005-01-01T00:00:00 2005-01-31T00:00:00 28018 97263 20361")
            arrayQueries[i].append(db + " " + qName + " 2005-02-01T00:00:00 2005-02-28T00:00:00 11529 44787 65226")
            arrayQueries[i].append(db + " " + qName + " 2005-03-01T00:00:00 2005-03-31T00:00:00 17410 19330 86209")
            arrayQueries[i].append(db + " " + qName + " 2005-04-01T00:00:00 2005-04-30T00:00:00 58169 32167 79813")
            arrayQueries[i].append(db + " " + qName + " 2005-05-01T00:00:00 2005-05-31T00:00:00 17891 6024 41469")
            arrayQueries[i].append(db + " " + qName + " 2005-06-01T00:00:00 2005-06-30T00:00:00 17518 71380 9782")
            arrayQueries[i].append(db + " " + qName + " 2005-07-01T00:00:00 2005-07-31T00:00:00 12142 1974 89160")
            arrayQueries[i].append(db + " " + qName + " 2005-08-01T00:00:00 2005-08-31T00:00:00 82986 25585 97830")
            arrayQueries[i].append(db + " " + qName + " 2005-09-01T00:00:00 2005-09-30T00:00:00 217 57299 52659")
            arrayQueries[i].append(db + " " + qName + " 2005-10-01T00:00:00 2005-10-31T00:00:00 18772 17587 25493")
            arrayQueries[i].append(db + " " + qName + " 2005-11-01T00:00:00 2005-11-30T00:00:00 57299 42255 26115")
            arrayQueries[i].append(db + " " + qName + " 2005-12-01T00:00:00 2005-12-31T00:00:00 45359 12875 2835")

            '''arrayQueries[i].append(db + " " + qName + " 2005-01-01T00:00:00 2005-01-31T00:00:00 28018 28611 31476 97263 7400 30299 20361 64093 54993")
            arrayQueries[i].append(db + " " + qName + " 2005-02-01T00:00:00 2005-02-28T00:00:00 11529 27471 15057 44787 30461 88951 65226 27336 80632")
            arrayQueries[i].append(db + " " + qName + " 2005-03-01T00:00:00 2005-03-31T00:00:00 17410 72329 26274 19330 78814 44451 86209 49496 12020")
            arrayQueries[i].append(db + " " + qName + " 2005-04-01T00:00:00 2005-04-30T00:00:00 58169 305 55473 32167 64590 72412 79813 72198 85852")
            arrayQueries[i].append(db + " " + qName + " 2005-05-01T00:00:00 2005-05-31T00:00:00 17891 96389 48342 6024 16918 441 41469 16761 29968")
            arrayQueries[i].append(db + " " + qName + " 2005-06-01T00:00:00 2005-06-30T00:00:00 17518 23288 3380 71380 51121 75668 9782 28136 11107")
            arrayQueries[i].append(db + " " + qName + " 2005-07-01T00:00:00 2005-07-31T00:00:00 12142 65515 21542 1974 6239 27121 89160 56429 12065")
            arrayQueries[i].append(db + " " + qName + " 2005-08-01T00:00:00 2005-08-31T00:00:00 82986 97346 27662 25585 58012 11861 97830 6805 28315")
            arrayQueries[i].append(db + " " + qName + " 2005-09-01T00:00:00 2005-09-30T00:00:00 217 9518 52121 57299 75856 18537 52659 2155 43911")
            arrayQueries[i].append(db + " " + qName + " 2005-10-01T00:00:00 2005-10-31T00:00:00 18772 13473 45381 17587 3867 19164 25493 20448 26713")
            arrayQueries[i].append(db + " " + qName + " 2005-11-01T00:00:00 2005-11-30T00:00:00 57299 49205 50305 42255 6917 10217 26115 75071 62310")
            arrayQueries[i].append(db + " " + qName + " 2005-12-01T00:00:00 2005-12-31T00:00:00 45359 1778 19851 12875 72482 14719 2835 10969 19215")'''
        
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