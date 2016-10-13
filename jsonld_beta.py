import json
from pyld import jsonld

def print_json():
    with open("project1_json.owl") as json_input:
        json_data = json.load(json_input)
        return(json_data)

def try_json_dump():

    a_list = print_json()

    return (json.dumps(a_list,indent=2))

def do_filter():

    input_dict = json.loads(try_json_dump())
    #input_dict = try_json_dump()
    print input_dict



if __name__ == '__main__':
    #print(try_json_dump())
    #try_json_dump()
    print (do_filter())