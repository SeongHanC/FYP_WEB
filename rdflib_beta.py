from rdflib import Graph,Namespace,RDF
from rdflib.namespace import FOAF,DC

g = Graph()
g.parse("rdf_output.owl")

print "Number of triples",len(g)

# g.bind("dc",DC)
# g.bind("foaf",FOAF)

a_list = g.serialize(format="n3")

# the_list = []
#
# the_list.append(a_list)

print a_list



