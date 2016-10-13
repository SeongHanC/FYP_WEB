from rdflib import Graph,Namespace,RDF

def get_co_name():

    co_name = []

    for name in g.subjects(RDF.type,my_namespace.Event_suppliers):

        co_name.append(g.value(name,my_namespace.ES_Name).toPython())

    return co_name

def get_types():

    types = []

    for name in g.subjects(RDF.type,my_namespace.Event_suppliers):
        types.append(g.value(name,my_namespace.ES_Type).toPython())

    return types

def get_states():

    states = []

    for name in g.subjects(RDF.type, my_namespace.Event_suppliers):
        states.append(g.value(name,my_namespace.ES_State).toPython())

    return states

def get_loc():

    loc = []

    for name in g.subjects(RDF.type, my_namespace.Event_suppliers):
        loc.append(g.value(name,my_namespace.ES_Location).toPython())

    return loc

def get_items():

    items = []

    for name in g.subjects(RDF.type, my_namespace.Event_suppliers):
        items.append(g.value(name,my_namespace.ES_Items).toPython())

    return items

def selangor_music():

    co_list = get_co_name()
    loc_list = get_loc()
    items_list = get_items()

    output = [co_list[0],loc_list[0],items_list[0]]

    return output



def selangor_fnb():

    co_list = get_co_name()
    loc_list = get_loc()
    items_list = get_items()

    output = [co_list[1], loc_list[1], items_list[1]]

    return output

def pp_cos():

    co_list = get_co_name()
    loc_list = get_loc()
    items_list = get_items()

    output = [co_list[2], loc_list[2], items_list[2]]

    return output

if __name__ == '__main__':

    g = Graph()
    g.parse("rdf_output.owl")

    my_namespace = Namespace("http://www.semanticweb.org/seonghan/ontologies/2016/7/untitled-ontology-3#")

    print get_co_name()

    print selangor_music()
    print selangor_fnb()
    print pp_cos()




