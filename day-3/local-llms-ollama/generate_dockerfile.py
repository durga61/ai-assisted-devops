import ollama

PROMPT = """
Multistage Dockerfile for  {language} language following best practices wrt multistage builds, layer optmization and image sizing
"""

def generate_dockerfile(language):
    response = ollama.chat(model='gemma3:latest', messages=[
        {
        'role': 'user',
        'content': PROMPT.format(language=language),
        }],
        stream=True
        )

    #return response['message']['content']
    for chunk in response:
        if 'content' in chunk['message']:
            print(chunk['message']['content'], end='', flush=True)

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)