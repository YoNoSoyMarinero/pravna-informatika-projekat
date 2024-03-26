from flask import Blueprint, request, Response, jsonify
from controllers.legal_documents_controller import LegalDocumentsController

legal_document_bp: Blueprint = Blueprint('legal_document', __name__)

@legal_document_bp.route('/judgment', methods = ['GET'])
def get_judgment():
    legal_document_name = request.args.get('legal_document_name')
    if not legal_document_name:
        return jsonify({'error': 'Name parameter is required'}), 400
    legal_document_controller: LegalDocumentsController = LegalDocumentsController(legal_document_name)
    html_document: str = legal_document_controller.get_judgment()
    if html_document:
     return Response(html_document, content_type="text/html")
    
    return "Document not found", 404

@legal_document_bp.route('/law', methods = ['GET'])
def get_law():
    legal_document_name = request.args.get('legal_document_name')
    if not legal_document_name:
        return jsonify({'error': 'Name parameter is required'}), 400
    legal_document_controller: LegalDocumentsController = LegalDocumentsController(legal_document_name)
    html_document: str = legal_document_controller.get_law()
    if html_document:
     return Response(html_document, content_type="text/html")
    
    return "Document not found", 404