
class Query1:

    def __init__(self, idBact, idServ, dateStart, dateEnd):
        self.idBact = idBact
        self.idServ = idServ
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.dateStart_n4j = dateStart + "Z"
        self.dateEnd_n4j = dateEnd + "Z"
        


    #########
    # NEO4J #
    #########
    def getQuery_neo4j(self):
        query = "WITH datetime(\"{}\") AS dateStart, datetime(\"{}\") AS dateEnd\n".format(self.dateStart_n4j, self.dateEnd_n4j)
        query += "MATCH (m:Microorganism {{id: {}}})<-[:hasFound]-(tm:TestMicro)-[ree1:eventFromEpisode]->(ep:Episode)<-[ree2:eventFromEpisode]-(ev:Event)-[:hospUnitFromService|hasHospUnit*2]-(s:Service {{id: {}}}),\n".format(self.idBact, self.idServ)
        query += "(p:Patient)<-[:episodeFromPatient]-(ep)\n"
        query += "WHERE ree1<>ree2\n"
        query += "AND (tm.start >= dateStart AND tm.end <= dateEnd)\n"
        query += "AND ((ev.start >= dateStart AND ev.end <= dateEnd)\n"
        query += "OR (ev.start <= dateStart AND ev.end >= dateStart)\n"
        query += "OR (ev.start <= dateEnd AND ev.end >= dateEnd))\n"
        query += "RETURN DISTINCT p"

        return query


    ##########
    # SPARQL #
    ##########
    def getQuery_sparql(self):
        query = "PREFIX ho: <http://www.semanticweb.org/spatiotemporalHospitalOntology#>\n"
        query += "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        query += "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
        query += "SELECT DISTINCT ?p\n"
        query += "{\n"
        query += "VALUES (?start ?end) {{(\"{}\"^^xsd:dateTime \"{}\"^^xsd:dateTime)}}\n".format(self.dateStart, self.dateEnd)
        query += "VALUES (?m_id ?s_id) {{({} {})}}\n".format(self.idBact, self.idServ)
        query += "?m ^(ho:hasFound2)/ho:hasFound1 ?tm;\n"
        query += "ho:id ?m_id .\n"
        query += "?tm ho:eventFromEpisode ?ep ;\n"
        query += "ho:start ?tm_start;\n"
        query += "ho:end ?tm_end.\n"
        query += "?ep ho:episodeFromPatient ?p .\n"
        query += "?ev ho:eventFromEpisode ?ep ;\n"
        query += "ho:start ?ev_start;\n"
        query += "ho:end ?ev_end;\n"
        query += "ho:hasHospUnit ?hu.\n"
        query += "?s ^(ho:hospUnitFromService2)/ho:hospUnitFromService1 ?hu;\n"
        query += "ho:id ?s_id.\n"
        query += "FILTER((?tm_start >= ?start) && (?tm_end <= ?end))\n"
        query += "FILTER((?ev_start >= ?start && ?ev_end <= ?end)\n"
        query += "|| (?ev_start <= ?start && ?ev_end >= ?start)\n"
        query += "|| (?ev_start <= ?end && ?ev_end >= ?end))\n"
        query += "}"


        return query


    ###############
    # SPARQL-STAR #
    ###############
    def getQuery_sparqlStar(self):
        query = "PREFIX ho: <http://www.semanticweb.org/spatiotemporalHospitalOntology#>\n"
        query += "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        query += "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
        query += "SELECT DISTINCT ?p\n"
        query += "WHERE { \n"
        query += "VALUES (?start ?end) {{(\"{}\"^^xsd:dateTime \"{}\"^^xsd:dateTime)}}\n".format(self.dateStart, self.dateEnd)
        query += "VALUES (?m_id ?s_id) {{({} {})}}\n".format(self.idBact, self.idServ)
        query += "?m ^ho:hasFound ?tm;\n"
        query += "ho:id ?m_id .\n"
        query += "?tm ho:eventFromEpisode ?ep ;\n"
        query += "ho:start ?tm_start;\n"
        query += "ho:end ?tm_end.\n"
        query += "?ep ho:episodeFromPatient ?p .\n"
        query += "?ev ho:eventFromEpisode ?ep ;\n"
        query += "ho:start ?ev_start;\n"
        query += "ho:end ?ev_end;\n"
        query += "ho:hasHospUnit ?hu.\n"
        query += "?s ^ho:hospUnitFromService ?hu;\n"
        query += "ho:id ?s_id.\n"
        query += "FILTER((?tm_start >= ?start) && (?tm_end <= ?end))\n"
        query += "FILTER((?ev_start >= ?start && ?ev_end <= ?end) \n"
        query += "|| (?ev_start <= ?start && ?ev_end >= ?start) \n"
        query += "|| (?ev_start <= ?end && ?ev_end >= ?end))\n"
        query += "}"

        return query


	
	 
		 
		
