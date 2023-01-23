import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\Bot:"
restart_sequence = "\n\nUser: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hello\nA: Hi!\n\nQ: Hello Hey there! How can I help you?",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)

print(response)