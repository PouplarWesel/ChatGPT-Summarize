from pyChatGPT import ChatGPT
import os
import codecs

session_token = open("token.txt").read().strip()

if session_token == '':
    print("No Token Set. Add only the token in token.txt.\nHow to get a token: https://github.com/terry3041/pyChatGPT/blob/main/README.md#usage")
    a = input()
else:
    api = ChatGPT(session_token)

    articles = {}


    for file in os.listdir("data/articles/"):
        if file.endswith(".txt"):
            with codecs.open(
                "data/articles/" + file, "r", encoding="utf-8", errors="ignore"
            ) as f:
                articles[file] = f.read()

    for title, content in articles.items():
        try:
            resp = api.send_message("Can you summarize this article \n\n" + content)
            if "message" in resp:
                with open("data/summarize/" + title, "w") as f:
                    f.write(resp["message"].replace(".", ".\n"))
                api.reset_conversation()
        except:
            print(f"Error: Article {title} is too long.")
            with open("data/summarize/" + title, "w") as f:
                f.write("Error: Article is too long.")

