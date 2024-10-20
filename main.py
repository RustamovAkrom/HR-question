import pdfplumber
import re 
import json


def extract_structure_from_pdf(pdf_file_path):
    structure = {}
    current_chapter = None
    current_section = None

    with pdfplumber.open(pdf_file_path) as pdf:
        start_page_number = 0
        end_page_number = 11

        for page in pdf.pages[start_page_number: end_page_number]:
            text = page.extract_text()

            lines = text.split('\n')

            for line in lines:
                line = line.strip()

                chapter_match = re.match(r'(\d+)\.\s*(.+)', line)
                
                if chapter_match:
                    chapter_number = chapter_match.group(1).strip()
                    chapter_title = chapter_match.group(2).strip()
                    structure[chapter_number] = {
                        "title": chapter_title,
                        "sections": {}
                    }
                    current_chapter = chapter_number
                    current_section = None

                section_match = re.match(r'(\d+\.\d+)\s*(.+)', line)

                if current_chapter and section_match:
                    section_number = section_match.group(1).strip()
                    section_title = section_match.group(2).strip()
                    structure[current_chapter]["sections"][section_number] = {
                        "title": section_title,
                        "subsections": {}
                    }
                    current_section = section_number
                subsection_match = re.match(r'(\d+\.\d+\.\d+)\s*(.+)', line)
                if current_section and subsection_match:
                    subsection_number = subsection_match.group(1).strip()
                    subsection_title = subsection_match.group(2).strip()
                    structure[current_chapter]["sections"][current_section]["subsections"][subsection_number] = {
                        "title": subsection_title,
                    }

    return structure


def delete_dublicate(structure: dict):
    for chapter in structure.values():
        for section in chapter["sections"].values():
            section['title'] = re.sub(r'[^\w\s.,-]', '', section["title"]).strip()

            for subsection in section['subsections'].values():
                subsection['title'] = re.sub(r'[^\w\s.,-]', '', subsection["title"]).strip()

    return structure


def save_data_to_json(structure, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(structure, file, ensure_ascii=False, indent=4)


def main():
    pdf_file = 'data/structure.pdf'
    json_file = 'structure.json'

    data = extract_structure_from_pdf(pdf_file)
    data = delete_dublicate(data)
    # print(data)

    save_data_to_json(data, json_file)


if __name__=='__main__':
    main()