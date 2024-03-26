import pandas as pd

class CaseRepository:

    def __init__(self) -> None:
        self.data_path: str = r'data\data.csv'
        self.df: pd.DataFrame = pd.read_csv(self.data_path)

    def get_vectorized_cases(self):
        return self.df.values