from flask import Blueprint, request, Response, jsonify
from controllers.legal_documents_controller import LegalDocumentsController
from schemas.JudgmentSchema import JudgmentSchema, Judgment

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

@legal_document_bp.route('/judgment_name', methods = ['GET'])
def get_judgment_name():
   names: list[str] = LegalDocumentsController.get_judgment_names()
   if len(names) == 0:
      return "Document not found", 404
   return jsonify(names), 200

@legal_document_bp.route('/create_judgment', methods = ['POST'])
def create_judgment():
    data: dict = request.get_json()
    schema: JudgmentSchema = JudgmentSchema()
    try:
        judgment: Judgment = schema.load(data)
        LegalDocumentsController.create_judgment(judgment)
    except:
        return jsonify({"Error message": "Invalid request body format!"}), 400
    
    return jsonify({"message": "Successfully added"}), 200

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