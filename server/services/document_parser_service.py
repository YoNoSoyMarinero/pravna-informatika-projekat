import xml.etree.ElementTree as ET

class DocumentParserService:

    def __init__(self, document_name) -> None:
        self.document_name: str = document_name

    def load_document_law(self) -> str:

        path = f'akoma-ntoso\\zakoni\\{self.document_name}.xml'
        tree = ET.parse(path)
        root = tree.getroot()
        return root

    def load_document_judgement(self) -> str:
        
        path = f'akoma-ntoso\\presude\\{self.document_name}.xml'
        tree = ET.parse(path)
        root = tree.getroot()
        return root
    
    def get_num_of_existing_chapters(self) -> int:
        i = 1

        while True:
            try:
                potential_chapter = self.body[i]
                if 'chapter' in potential_chapter.tag:
                    i += 1
            except:
                num_of_chapters = i
                break

        return num_of_chapters
    
    def get_num_of_chapter_sections(self) -> int:
        i = 2

        while True:
            try:
                potential_section = self.chapter[i]
                if 'section' in potential_section.tag:
                    i += 1
            except:
                num_of_sections = i
                break

        return num_of_sections
    
    def get_num_of_section_articles(self) -> int:
        i = 1

        while True:
            try:
                potential_article = self.chapter_section[i]
                if 'article' in potential_article.tag:
                    i += 1
            except:
                num_of_articles = i
                break

        return num_of_articles
    
    def get_num_of_article_paragraphs(self) -> int:
        i = 1

        while True:
            try:
                potential_paragraph = self.section_article[i]
                if 'paragraph' in potential_paragraph.tag:
                    i += 1
            except:
                num_of_paragraphs = i
                break

        return num_of_paragraphs
    
    def get_num_of_paragraph_points(self) -> int:

        if 'intro' in self.article_paragraph[0].tag:
            self.r = 1
        else:
            self.r = 0

        self.start = self.r

        while True:
            try:
                potential_point = self.article_paragraph[self.r]
                if 'point' in potential_point.tag:
                    self.r += 1
                elif 'content' in potential_point.tag:
                    self.r = 0
                    raise IndexError
            except:
                num_of_points = self.r
                break

        return num_of_points

    def get_parsed_law(self) -> str:
        
        root = self.load_document_law()

        self.html_str = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n\t<meta charset='UTF-8'>\n\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\t<title>XML to HTML</title>\n</head>\n<body>\n"
        
        # headings
        title_name = root[0].attrib['name']
        title_date = root[0][0][0][0][2].attrib['date']
        publication_name = root[0][0][1].attrib['showAs']
        publication_date = root[0][0][1].attrib['date']

        self.html_str += f"\t<h1>{title_name} ({title_date})</h1>\n"
        self.html_str += f"\t<h2>{publication_name} ({publication_date})</h2>\n"
    
        # body
        self.body = root[0][1]

        num_of_chapters = self.get_num_of_existing_chapters()

        for i in range(1, num_of_chapters):

            self.chapter = self.body[i]
            chapter_num = self.chapter[0].text.strip()
            chapter_heading = self.chapter[1].text.strip()
            num_of_chapter_sections = self.get_num_of_chapter_sections()

            self.html_str += f"\t<h3>{chapter_num}</h3>\n"
            self.html_str += f"\t<h3>{chapter_heading}</h3>\n"

            for j in range(2, num_of_chapter_sections):

                self.chapter_section = self.chapter[j]
                chapter_section_heading = self.chapter_section[0].text.strip()
                num_of_section_articles = self.get_num_of_section_articles()
                
                self.html_str += f"\t<h4>{chapter_section_heading}</h4>\n"

                for k in range(1, num_of_section_articles):
                    
                    self.section_article = self.chapter_section[k]
                    section_article_num = self.section_article[0].text.strip()
                    num_of_article_paragraphs = self.get_num_of_article_paragraphs()
                    key = self.section_article.attrib["eId"]
                    section_article_id = f'/#{key}'

                    self.html_str += f"\t<h5><a href={section_article_id}, id={section_article_id}>{section_article_num}</a></h5>\n"

                    for z in range(1, num_of_article_paragraphs):

                        self.article_paragraph = self.section_article[z]
                        num_of_paragraph_points = self.get_num_of_paragraph_points()

                        if num_of_paragraph_points == 0:
                            paragraph_content = self.article_paragraph[0][0].text.strip()
                            self.html_str += f"\t<p>{paragraph_content}</p>\n"
                        else:
                            for t in range(self.start, num_of_paragraph_points):

                                self.paragraph_point = self.article_paragraph[t]
                                paragraph_point_num = self.paragraph_point[0].text.strip()
                                paragraph_point_content = self.paragraph_point[1]
                                p_text = paragraph_point_content[0].text.strip()

                                self.html_str += f"\t<p>{paragraph_point_num} {p_text}</p>\n"

        self.html_str += "\n</body>\n</html>"

        return self.html_str

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
    
    def get_parsed_judgement(self) -> str:
        
        root = self.load_document_judgement()

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
        return self.html_str
