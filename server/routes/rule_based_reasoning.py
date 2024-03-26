from flask import Blueprint, request, jsonify
from schemas.RuleBaseFactsSchema import RuleBaseFacts, RuleBaseFactsSchema
from controllers.rule_based_reasoning_controller import RuleBasedReasoningController

rule_based_reasoning_bp: Blueprint = Blueprint('rule_based_reasoning', __name__)


@rule_based_reasoning_bp.route('/rule_based_reasoning', methods = ['POST'])
def get_rule_based_judgment():
    data: dict = request.get_json()
    schema: RuleBaseFactsSchema = RuleBaseFactsSchema()
    try:
        rule_base_facts: RuleBaseFacts = schema.load(data)
        rule_based_reasoning: RuleBasedReasoningController = RuleBasedReasoningController(rule_base_facts)
        judgment: dict = rule_based_reasoning.get_judgment()
    except:
        return jsonify({"Error message": "Invalid request body format!"}), 400
    
    return jsonify(judgment), 200