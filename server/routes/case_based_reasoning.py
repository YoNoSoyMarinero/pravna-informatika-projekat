from flask import Blueprint, request, jsonify
from schemas.CaseBaseFactsSchema import CaseBaseFacts, CaseBaseFactsSchema
from controllers.case_based_reasoning_controller import CaseBasedReasoningController

case_based_reasoning_bp: Blueprint = Blueprint('case_based_reasoning', __name__)


@case_based_reasoning_bp.route('/case_based_reasoning', methods = ['POST'])
def get_rule_based_judgment():
    data: dict = request.get_json()
    schema: CaseBaseFacts = CaseBaseFactsSchema()
    try:
        rule_base_facts: CaseBaseFacts = schema.load(data)
        case_based_reasoning_controller: CaseBasedReasoningController = CaseBasedReasoningController(rule_base_facts)
        res:dict = case_based_reasoning_controller.get_most_similar_cases()
    except:
        return jsonify({"Error message": "Invalid request body format!"}), 400
    
    return jsonify(res), 200