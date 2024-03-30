from schemas.JudgmentSchema import Judgment
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
    def create_judgment(judgment: Judgment):
        judgment_xml = DocumentParserService.create_judgment(judgment)
        CaseRepository().add_judgment(judgment.title, judgment_xml)
    
    @staticmethod
    def get_judgment_names():
        return {'legal_document_names': CaseRepository().get_names_cases()}