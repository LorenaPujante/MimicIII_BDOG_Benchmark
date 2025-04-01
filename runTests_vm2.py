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
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 80085 32677")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 80139 7988")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 80004 4180")
        
        if qName == "3":
            arrayQueries.append([])
            arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 97543 16518 50427")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 7097 19859 83416")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 1533 67306 95343")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 17488 98666 5790")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 5769 6832 96240")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 17518 13338 23387")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 651 22626 46775")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 10847 32496 29180")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 25030 23197 98514")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 24001 4410 19348")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 30917 15257 21847")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 23294 45008 11255")
            '''arrayQueries[i].append(db + " " + qName + " 2000-01-01T00:00:00 2000-01-31T00:00:00 97543 12013 30964 16518 7155 54708 50427 9838 19842")
            arrayQueries[i].append(db + " " + qName + " 2000-02-01T00:00:00 2000-02-29T00:00:00 7097 86078 57187 19859 8795 14633 83416 16752 17122")
            arrayQueries[i].append(db + " " + qName + " 2000-03-01T00:00:00 2000-03-31T00:00:00 1533 1662 4466 67306 26767 1763 95343 11850 13668")
            arrayQueries[i].append(db + " " + qName + " 2000-04-01T00:00:00 2000-04-30T00:00:00 17488 40526 17130 98666 17847 7726 5790 50252 51462")
            arrayQueries[i].append(db + " " + qName + " 2000-05-01T00:00:00 2000-05-31T00:00:00 5769 2578 6024 6832 10281 19614 96240 91862 23209")
            arrayQueries[i].append(db + " " + qName + " 2000-06-01T00:00:00 2000-06-30T00:00:00 17518 23288 22503 13338 6540 30985 23387 16551 32115")
            arrayQueries[i].append(db + " " + qName + " 2000-07-01T00:00:00 2000-07-31T00:00:00 651 1935 5051 22626 3678 8231 46775 11163 11239")
            arrayQueries[i].append(db + " " + qName + " 2000-08-01T00:00:00 2000-08-31T00:00:00 10847 6838 14024 32496 81786 57554 29180 12411 24711")
            arrayQueries[i].append(db + " " + qName + " 2000-09-01T00:00:00 2000-09-30T00:00:00 25030 2092 24274 23197 14183 53308 98514 3557 13688")
            arrayQueries[i].append(db + " " + qName + " 2000-10-01T00:00:00 2000-10-31T00:00:00 24001 94050 64550 4410 8548 406 19348 94430 80287")
            arrayQueries[i].append(db + " " + qName + " 2000-11-01T00:00:00 2000-11-30T00:00:00 30917 41061 46000 15257 20230 24061 21847 7066 82279")
            arrayQueries[i].append(db + " " + qName + " 2000-12-01T00:00:00 2000-12-31T00:00:00 23294 61743 13567 45008 51275 20456 11255 2835 10883")'''
        
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