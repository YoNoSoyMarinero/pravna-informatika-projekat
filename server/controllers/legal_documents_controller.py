from services.document_parser_service import DocumentParserService

class LegalDocumentsController:

    def __init__(self, legal_document: str):
        self.parser = DocumentParserService(legal_document)

    def get_judgment(self):
        return self.parser.get_parsed_judgment()
    
    def get_law(self):
        return self.parser.get_parsed_law()