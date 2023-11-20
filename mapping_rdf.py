# mapping telarkg property graph to rdf
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF, XSD

import json

g = Graph()
g.parse('telarKG.ttl', format='ttl')

# g.namespace_manager.bind('', URIRef('https://telarkg.imfd.cl/'))
# g.bind('rdf', RDF)
# g.bind('rdfs', RDFS)
# g.bind('xsd', XSD)
# g.bind('foaf', FOAF)
# g.bind('owl', OWL)

# def create_schema():
#   g.add((URIRef('https://telarkg.imfd.cl/'), RDF.type, OWL.Ontology))
#   g.add((URIRef('https://telarkg.imfd.cl/'), RDFS.label, Literal('TelarKG')))
#   g.add((URIRef('https://telarkg.imfd.cl/'), RDFS.comment, Literal('TelarKG is a Knowledge Graph collecting together data about the Chilean Constitutional Convention, whose objective was to draft a new constitution for Chile. Information is provided regarding the convention members (class ConventionMember), including their party, pact, gender, etc. The votes of each convention member during the process are stored as edges targetting the plenary material (PlenaryMaterial) or commission material (CommissionMaterial) being voted upon. Videos (Video) of all plenary and commission sessions are described, along with interventions by members, automated transcripts and chat comments. Each convention member (class ConventionMember) contains one or more social media accounts (TwitterAccount, FacebookAccount and InstagramAccount), which in turn are related to social media posts by them, along with other related posts. Next is shown the schema of the graph, further indicating the number of instances for each class.')))
#   g.add((URIRef('https://telarkg.imfd.cl/'), DC.creator, Literal('Instituto Milenio Fundamentos de los Datos')))

#   convention_member = URIRef('https://telarkg.imfd.cl/ConventionMember')
#   g.add((convention_member, RDF.type, RDFS.Class))
#   g.add((convention_member, RDFS.label, Literal('ConventionMember')))
#   g.add((convention_member, RDFS.comment, Literal('A member of the Chilean Constitutional Convention')))
#   g.add((convention_member, RDFS.subClassOf, FOAF.Person))






