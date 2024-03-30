from services.document_parser_service import DocumentParserService
from repository.CaseRepository import CaseRepository

class LegalDocumentsController:

    def __init__(self, legal_document: str):
        self.parser = DocumentParserService(legal_document)

    def get_judgment(self):
        return self.parser.get_parsed_judgement()
    
    def get_law(self):
        return self.parser.get_parsed_law()
    
    @staticmethod
    def get_judgment_names():
        return {'legal_document_names': list(CaseRepository().get_names_cases())}