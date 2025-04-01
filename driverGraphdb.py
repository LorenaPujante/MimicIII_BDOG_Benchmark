from SPARQLWrapper import SPARQLWrapper, JSON
import time

class DriverGraphDB:

    URL_BASE = "http://localhost:7200/"


    def __init__(self):
        self.repository = ""
    
    def setRepository(self, repository):
        self.repository = repository


    def executeQuery(self, query):
        url = self.URL_BASE + "repositories/" + self.repository
        sparql = SPARQLWrapper(url)

        start_time = time.time()
        
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        
        end_time = time.time()
        total_time = end_time - start_time

        return results, total_time