from rdflib import Graph,Namespace,RDF

g = Graph()
g.parse("rdf_output.owl")

# a_list = g.serialize(destination="hello.owl")

my_namespace = Namespace("http://www.semanticweb.org/seonghan/ontologies/2016/7/untitled-ontology-3#")

co_name = []
types = []
states = []
loc = []
items = []

for name in g.subjects(RDF.type,my_namespace.Event_suppliers):
    #output.append(states)

    co_name.append(g.value(name,my_namespace.ES_Name).toPython())
    types.append(g.value(name,my_namespace.ES_Type).toPython())
    states.append(g.value(name,my_namespace.ES_State).toPython())
    loc.append(g.value(name,my_namespace.ES_Location).toPython())
    items.append(g.value(name,my_namespace.ES_Items).toPython())



#print output





