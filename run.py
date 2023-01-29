from pyChatGPT import ChatGPT
import os
import codecs

session_token = open("data/token.txt").read().strip()

api = ChatGPT(session_token)

articles = {}


for file in os.listdir("data/articles/"):
    if file.endswith(".txt"):
        with codecs.open("data/articles/" + file, 'r', encoding='utf-8', errors='ignore') as f:
            articles[file] = f.read()


for title, content in articles.items():
    resp = api.send_message('Can you summarize this article \n\n' + content)
    with open("data/summarize/" + title, "w") as f: 
        f.write(resp['message'].replace(".", ".\n"))
    

