API_KEYS="#your_api_key_here"

from openai import OpenAI

client = OpenAI(api_key=API_KEYS)

response = client.responses.create(
    model="gpt-5",
    input="Trần Duy Thanh là ai?"
)

print(response.output_text)

