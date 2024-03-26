import os
from schemas.RuleBaseFactsSchema import RuleBaseFacts
from lookup.xml_shemes import XMLShemes
import xml.etree.ElementTree as ET
import subprocess

class RuleBaseReasoningService:

    __path_to_facts_rdf: str = r"dr-device\facts.rdf"
    __path_to_export_rdf: str = r"export.rdf"

    def __init__(self, rule_base_facts: RuleBaseFacts) -> None:
        print(os.getcwd())
        self.facts: RuleBaseFacts = rule_base_facts
        self.rdf_data: str = XMLShemes.rdf_facts_template.format(self.facts.drug_posession,
                            self.facts.allowing_usage,
                            self.facts.marginalized_group,
                            self.facts.providing_logistics,
                            self.facts.drug_trafficking, 
                            self.facts.smuggling, 
                            self.facts.organized_group, 
                            self.facts.article_52_violation, 
                            self.facts.estimated_drug_price)
        self.namespaces: dict = XMLShemes.namespaces

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