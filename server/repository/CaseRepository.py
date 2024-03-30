import pandas as pd
import os

class CaseRepository:

    def __init__(self) -> None:
        self.data_path: str = r'data\data.csv'
        self.judgments_path: str = r'akoma-ntoso\presude'
        self.df: pd.DataFrame = pd.read_csv(self.data_path)

    def get_vectorized_cases(self):
        return self.df.values
    
    def add_judgment(self, judgment_name: str, judgment_xml: str):
        file_path = self.judgments_path + rf"\{judgment_name}.xml"
        with open(file_path, 'w') as xml_file:
            xml_file.write(judgment_xml)
            
    def get_names_cases(self):
        file_names = os.listdir(self.judgments_path)
        return [os.path.splitext(file)[0] for file in file_names if file.endswith('.xml')]