import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nBot:"
restart_sequence = "\n\nUser: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="\n\nUser: Hello \nBot:",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)

text = response["choices"][0]["text"]
if text == "":
    print("An Error has occurred during processing your request, maybe there is no answer to the question/prompt?")
else:
    print(text)