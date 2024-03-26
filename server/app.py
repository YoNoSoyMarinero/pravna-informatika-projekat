from flask import Flask
from flask_cors import  CORS
from config import Config
from routes import (
    rule_based_reasoning,
    case_based_reasoning,
    legal_documents
)
import os
from dotenv import load_dotenv


app: Flask = Flask(__name__)
app.config.from_object(Config)
CORS(app)
app.register_blueprint(rule_based_reasoning.rule_based_reasoning_bp)
app.register_blueprint(case_based_reasoning.case_based_reasoning_bp)
app.register_blueprint(legal_documents.legal_document_bp)
load_dotenv('.env')


if (__name__ == '__main__'):
    app.run(debug=False, host=os.getenv("HOST"), port=os.getenv("PORT"))