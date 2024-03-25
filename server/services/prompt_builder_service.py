import json

class PromptBuilderService:


    with open('json\system_instruction_file.json') as f:
        __action_propmt_template: dict = json.load(f)

    @classmethod
    def system_insturction_get_metadata(cls) -> str:
        return cls.__action_propmt_template['system_instructions_get_metadata']
    @classmethod
    def system_instructions_defendant_info(cls) -> str:
        return cls.__action_propmt_template['system_instructions_defendant_info']
    @classmethod
    def system_instructions_get_facts(cls) -> str:
        return cls.__action_propmt_template['system_instructions_get_facts']
    @classmethod
    def system_instructions_get_punishment(cls) -> str:
        return cls.__action_propmt_template['system_instructions_get_punishment']