import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "あなたは「ずんだもん」です"},
        {"role": "user", "content": "自己紹介をしてください"}
    ]
)
print(response.choices[0].message.content)
# print(type(response))
# print(response)
