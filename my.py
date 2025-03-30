from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("Book1.xlsx")
print(result.text_content)