class DocumentParser:

    def __init__(self, document_name, judgment: bool) -> None:
        self.document_name: str = document_name
        self.judgment: bool = judgment


    def load_document(self) -> str:
        #TODO
        pass

    def get_parsed_law(self) -> str:
        #TODO
        pass

    def get_parsed_judgment(self) -> str:
        #TODO
        pass

    def get_parsed_document(self) -> str:
        return self.get_parsed_judgment() if self.judgment else self.get_parsed_law()