import xml.etree.ElementTree as ET

class DocumentParserService:

    def __init__(self, document_name) -> None:
        self.document_name: str = document_name

    def load_document(self) -> str:
        
        path = f'akoma-ntoso\\presude\\{self.document_name}.xml'
        tree = ET.parse(path)
        root = tree.getroot()
        return root

    def get_parsed_law(self) -> str:
        #TODO
        pass

    def clean_whole_text(self, tag_element) -> str:

        p_element = tag_element
        p_text = "".join(p_element.itertext())

        new_p_text = p_text
        for ch in p_text:
            if ch in ('\n', '\t'):
                new_p_text = new_p_text.replace(ch, '')
            
        cleaned_text = ' '.join(new_p_text.split())

        return cleaned_text
    
    def clean_element_text(self, element):

        new_element_text = element.text
        for ch in element.text:
            if ch in ('\n', '\t'):
                new_element_text = new_element_text.replace(ch, '')

        cleaned_element_text = ' '.join(new_element_text.split())

        return cleaned_element_text

    def iterate_through_elements(self, tag_element) -> None:

        self.html_str += '\n '
        self.html_str += '\t<p>'

        cleaned_text = self.clean_whole_text(tag_element)

        for element in tag_element.iter():

            cleaned_element_text = self.clean_element_text(element)

            if cleaned_element_text not in cleaned_text or cleaned_element_text == '':
                continue
            else:
                if cleaned_text.find(cleaned_element_text) == 0:
                    cleaned_text = cleaned_text.replace(cleaned_element_text, '', 1)
                    if 'ref' in element.tag and any(keyword in element.attrib.get('href', '') for keyword in self.keywords):
                        href = element.attrib.get('href', '')
                        self.html_str += f"<a href='{href}', id='{href}'>{element.text.strip()}</a>"
                    else:
                        self.html_str += element.text.strip() if element.text.strip() else ''
                elif cleaned_text.find(cleaned_element_text) != -1:
                    undefined_text = cleaned_text[:cleaned_text.find(cleaned_element_text)]
                    if 'ref' in element.tag and any(keyword in element.attrib.get('href', '') for keyword in self.keywords):
                        href = element.attrib.get('href', '')
                        a_element_text = f"<a href='{href}', id='{href}'>{element.text.strip()}</a>"
                        self.html_str += undefined_text + a_element_text
                    else:
                        self.html_str += undefined_text + cleaned_element_text
                    cleaned_text = cleaned_text.replace(undefined_text + cleaned_element_text, '', cleaned_text.find(cleaned_element_text))
                else:
                    print(cleaned_element_text.find(cleaned_element_text))

        if tag_element == self.p_tag_conclusions:        
            self.html_str += "\n\t</p>\n</body>\n</html>"
        else:
            self.html_str += "\n\t</p>\n"
    
    def get_parsed_judgment(self) -> str:
        
        root = self.load_document()

        author = root[0][0][0][0][0].text.strip()
        date = root[0][0][0][0][1].text.strip()
        name = root[0][0][0][0][2].text.strip()
        judgement_body = root[0][1]
        self.p_tag = judgement_body[0]
        conclusions = judgement_body[1]
        self.p_tag_conclusions = conclusions[0]

        self.html_str = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n\t<meta charset='UTF-8'>\n\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\t<title>XML to HTML</title>\n</head>\n<body>\n"
        self.html_str += f"\t<h1>{author}</h1>\n"
        self.html_str += f"\t<h2>{name}</h2>\n"
        self.html_str += f"\t<h3>{date}</h3>\n"
    
        self.keywords = ['krivicni', 'postupak']

        self.iterate_through_elements(self.p_tag)
        self.iterate_through_elements(self.p_tag_conclusions)

        return self.html_str
    
