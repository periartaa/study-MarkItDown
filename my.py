from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("word.docx")
print(result.text_content)