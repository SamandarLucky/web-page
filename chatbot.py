import openai

openai.api_key = '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'
def generate_essay_response(prompt):
    # Use the correct method for chat models: openai.ChatCompletion.create()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or gpt-3.5-turbo, or another available chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,  # Adjust based on essay length
        temperature=0.7  # Adjust creativity level
    )
    essay = response['choices'][0]['message']['content'].strip()
    return essay