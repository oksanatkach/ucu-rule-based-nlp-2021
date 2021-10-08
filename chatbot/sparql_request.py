from SPARQLWrapper import SPARQLWrapper, JSON

session = SPARQLWrapper('http://dbpedia.org/sparql')

#todo: write your SPARQL query here
query_template = '''
'''


def get_capital(country):
    session.setQuery(query_template % country)
    session.setReturnFormat(JSON)
    result = session.query().convert()
    if len(result['results']['bindings']) > 0:
        answer = result['results']['bindings'][0]['capital_name']['value']
    else:
        answer = "I don't know the answer to this question."
    return answer


if __name__ == '__main__':
    print(get_capital('Ukraine'))
    print(get_capital('Denmark'))
