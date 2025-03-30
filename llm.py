from markitdown import MarkItDown  # Replace 'markitdown' with the correct module name

from openai import OpenAI

client = OpenAI(api_key="i-am-not-an-api-key") # Replace with your actual API key

md = MarkItDown(llm_client=client, llm_model="gpt-4o")

result = md.convert("image.png")
print(result.text_content)