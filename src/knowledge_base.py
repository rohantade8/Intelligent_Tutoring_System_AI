import rdflib

# Load the ontology into a graph
class KnowledgeBase:
    def __init__(self, ontology_path):
        self.graph = rdflib.Graph()
        self.graph.parse(ontology_path)
        
    def get_all_classes(self):
        """Get all classes in the ontology (mathematical and geometric concepts)."""
        query = """
            SELECT ?concept WHERE {
                ?concept a owl:Class .
            }
        """
        results = self.graph.query(query)
        return [row[0] for row in results]
    
    def get_shape_formulas(self, shape_name):
        """Get formula for a specific shape based on the shape's name."""
        query = f"""
            SELECT ?formula ?label ?comment WHERE {{
                ?formula a <http://www.semanticweb.org/acer/ontologies/2024/11/advanced-ontology#Formula> .
                ?formula rdfs:label ?label .
                ?formula rdfs:comment ?comment .
                FILTER regex(?label, "{shape_name}", "i")
            }}
        """
        results = self.graph.query(query)
        return [(str(row[1]), str(row[2])) for row in results]

    def get_element_details(self, element_name):
        """Get details of a chemical element (e.g., Atomic number, Atomic mass)."""
        query = f"""
            SELECT ?atomic_number ?atomic_mass WHERE {{
                <http://www.semanticweb.org/acer/ontologies/2024/11/advanced-ontology#{element_name}> 
                    <http://www.w3.org/2000/01/rdf-schema#label> ?label ;
                    <http://www.semanticweb.org/acer/ontologies/2024/11/advanced-ontology#hasAtomicNumber> ?atomic_number ;
                    <http://www.semanticweb.org/acer/ontologies/2024/11/advanced-ontology#hasAtomicMass> ?atomic_mass .
            }}
        """
        results = self.graph.query(query)
        return [(str(row[0]), str(row[1])) for row in results]
    
    def get_all_properties(self):
        """Get all properties (e.g., hasRadius, hasArea) in the ontology."""
        query = """
            SELECT ?property WHERE {
                ?property a rdf:Property .
            }
        """
        results = self.graph.query(query)
        return [str(row[0]) for row in results]
