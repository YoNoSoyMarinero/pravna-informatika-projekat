import PyPDF2
import re
import os
import pandas as pd
from services.prompt_builder_service import PromptBuilderService
from services.gpt_communication_service import GPTCommunicationService
from lookup.stop_words import StopWords
from dotenv import load_dotenv
from unidecode import unidecode
import re

load_dotenv('.env')

class JudgmentDataExtractor:
    directory: str = 'judgments_pdf'
    def read_pdf(self, file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            text = ''
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text


    def remove_spaces_around_specific_chars(self, text):
        characters = ['č', 'ž', 'š', 'ć', 'đ']
        for char in characters:
            pattern = re.compile(r'\s*(' + re.escape(char) + r')\s*')
            text = pattern.sub(r'\1', text)
        return text
    
    def get_paragraph_stopwords(self, string, words):
        for word in words:
            idx = string.find(word)
            if idx != -1:
                return word, idx
        else:
            return None


    def get_substring_between(self, string, start_list, end_list):
        start, start_index = self.get_paragraph_stopwords(string, start_list)
        start, end_index = self.get_paragraph_stopwords(string, end_list)
        text = string[start_index + len(start):end_index]
        return "".join(unidecode(char) for char in text)

    def extract_data(self):
        data = []
        for filename in os.listdir(self.directory):
            path = os.path.join(self.directory, filename)
            pdf_text = self.read_pdf(path)
            gpt_response = {'judgment_id': filename.split(".")[0]}
            filtered_text = self.remove_spaces_around_specific_chars(pdf_text)
            header: str = self.get_substring_between(filtered_text, StopWords.header_starts, StopWords.judgemnt_starts)
            gpt_response.update(GPTCommunicationService.send_message_to_gpt(header, PromptBuilderService.system_insturction_get_metadata()))
            defendant_info: str = self.get_substring_between(filtered_text, StopWords.judgemnt_starts, StopWords.guilty_starts)
            gpt_response.update(GPTCommunicationService.send_message_to_gpt(defendant_info, PromptBuilderService.system_instructions_defendant_info()))
            facts: str = self.get_substring_between(filtered_text, StopWords.guilty_starts, StopWords.judging_to_starts)
            gpt_response.update(GPTCommunicationService.send_message_to_gpt(facts, PromptBuilderService.system_instructions_get_facts()))
            punishment_info: str = self.get_substring_between(filtered_text, StopWords.judging_to_starts, StopWords.explnation_starts)
            gpt_response.update(GPTCommunicationService.send_message_to_gpt(punishment_info, PromptBuilderService.system_instructions_get_punishment()))
            data.append(gpt_response)
            print(filename)
        df = pd.DataFrame(data)
        df.to_csv('data.csv', encoding='utf-8', index=False)