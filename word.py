# import pdfplumber
# import json
# import re
# from .main import extract_structure_from_pdf


# for chapter in structure.values():
#     for section in chapter["sections"].values():

#         section["title"] = re.sub(r'[^\w\s.,-]', '', section["title"]).strip()

#         for subsection in section["subsections"].values():
#             subsection["title"] = re.sub(r'[^\w\s.,-]', '', subsection["title"]).strip()

# def save_structure_to_json(structure, json_path):
#     with open(json_path, 'w', encoding='utf-8') as json_file:
#         json.dump(structure, json_file, ensure_ascii=False, indent=4)

# # Путь к вашему PDF файлу
# pdf_path = 'data/structure.pdf'
# # Путь к сохранению JSON файла
# json_path = 'structure.json'

# # Извлекаем структуру и сохраняем в JSON
# save_structure_to_json(
# , json_path)

# print(f"Структура книги успешно извлечена и сохранена в {json_path}")
