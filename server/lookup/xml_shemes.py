class XMLShemes:

    rdf_facts_template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
                xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
                xmlns:lc="http://informatika.ftn.uns.ac.rs/legal-case.rdf#">
            <lc:case rdf:about="http://informatika.ftn.uns.ac.rs/legal-case.rdf#case01">
                <lc:name>case 01</lc:name>
                <lc:defendant>John</lc:defendant>
                <lc:drug_posession>{}</lc:drug_posession>
                <lc:allowing_usage>{}</lc:allowing_usage>        
                <lc:marginalized_group>{}</lc:marginalized_group>       
                <lc:providing_logistics>{}</lc:providing_logistics>       
                <lc:drug_trafficking>{}</lc:drug_trafficking>       
                <lc:smuggling>{}</lc:smuggling>       
                <lc:organized_group>{}</lc:organized_group>
                <lc:article_52_violation>{}</lc:article_52_violation>     
                <lc:estimated_drug_price rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{}</lc:estimated_drug_price>
            </lc:case>
        </rdf:RDF>
        """
    namespaces = {
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'defeasible': 'http://lpis.csd.auth.gr/systems/dr-device/defeasible.rdfs#',
            'export': 'http://startrek.csd.auth.gr/dr-device/export/export.rdf#'
            }