from neo4j import GraphDatabase
import time

def runTransaction(tx, query):
        result = tx.run(query)
        records = list(result)
        summary = result.consume()
        return records, summary

class DriverNeo4j:

    URI = "neo4j://localhost:7687/"
    AUTH = ("neo4j", "1234")

    def executeQuery(self, query):
        with GraphDatabase.driver(self.URI, auth=self.AUTH) as driver:
            driver.verify_connectivity()

            with driver.session(database="neo4j") as session:
                start_time = time.time()
                
                records, summary = session.read_transaction(runTransaction, query)
                
                end_time = time.time()
                total_time = end_time - start_time

            session.close()
        driver.close()

        return records, total_time, summary



