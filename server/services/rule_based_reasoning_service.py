import os
from schemas.RuleBaseFactsSchema import RuleBaseFacts
import xml.etree.ElementTree as ET
import subprocess

class RuleBaseReasoningService:

    __path_to_facts_rdf: str = r"dr-device\facts.rdf"
    __path_to_export_rdf: str = r"export.rdf"

    def __init__(self, rule_base_facts: RuleBaseFacts) -> None:
        print(os.getcwd())
        self.facts: RuleBaseFacts = rule_base_facts
        self.rdf_data: str = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
                xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
                xmlns:lc="http://informatika.ftn.uns.ac.rs/legal-case.rdf#">
            <lc:case rdf:about="http://informatika.ftn.uns.ac.rs/legal-case.rdf#case01">
                <lc:name>case 01</lc:name>
                <lc:defendant>John</lc:defendant>
                <lc:drug_posession>{self.facts.drug_posession}</lc:drug_posession>
                <lc:allowing_usage>{self.facts.allowing_usage}</lc:allowing_usage>        
                <lc:marginalized_group>{self.facts.marginalized_group}</lc:marginalized_group>       
                <lc:providing_logistics>{self.facts.providing_logistics}</lc:providing_logistics>       
                <lc:drug_trafficking>{self.facts.drug_trafficking}</lc:drug_trafficking>       
                <lc:smuggling>{self.facts.smuggling}</lc:smuggling>       
                <lc:organized_group>{self.facts.organized_group}</lc:organized_group>
                <lc:article_52_violation>{self.facts.article_52_violation}</lc:article_52_violation>     
                <lc:estimated_drug_price rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{self.facts.estimated_drug_price}</lc:estimated_drug_price>
            </lc:case>
        </rdf:RDF>
        """
        self.namespaces: dict = {
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'defeasible': 'http://lpis.csd.auth.gr/systems/dr-device/defeasible.rdfs#',
            'export': 'http://startrek.csd.auth.gr/dr-device/export/export.rdf#'
            }


    def set_facts_rdf(self):
        file_path = self.__path_to_facts_rdf
        with open(file_path, "w") as file:
            file.write(self.rdf_data)

    def run_start_bat_script(self):
        os.chdir("dr-device")
        subprocess.call(['start.bat'])

    def parse_export_tags(self, penalties: list, offense: list):
        tree: ET = ET.parse(self.__path_to_export_rdf)
        root:ET = tree.getroot()
        export_tags = root.findall('.//export:*', self.namespaces)
        for tag in export_tags:
            tag_name = tag.tag.split("}")[-1]
            if tag_name == 'value':
                penalties.append(tag.text)
            elif tag_name[:2] == 'is':
                offense.append(tag_name)


    def get_judgment(self):
        penalties: list = []
        offense: list = []
        self.parse_export_tags(penalties, offense)
        offense = offense[::-1]    
        min_pen = penalties[::2]
        max_pen = penalties[1::2]
        return {"offenses": offense, "min_pen": min_pen, "max_pen": max_pen}
    
    def run_clean_bat_script(self):
        subprocess.call(['clean.bat'])
        os.chdir("..")

    def reason(self):
        self.set_facts_rdf()
        self.run_start_bat_script()
        judgment: dict = self.get_judgment()
        self.run_clean_bat_script()
        return judgment