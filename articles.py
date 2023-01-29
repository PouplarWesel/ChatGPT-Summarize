import os
import re

try:
    from pyChatGPT import ChatGPT

    delete_files = input(
        "Delete all existing files in data/articles? This will increase the speed of the program (y/n): "
    )

    if delete_files == "y":
        for file in os.listdir("data/articles/"):
            if file.endswith(".txt"):
                os.remove("data/articles/" + file)
        print("Successfully deleted all files in data/articles")

    while True:
        file_name = input("Enter a file name (or leave blank to quit): ")
        if not file_name:
            break
        file_name = re.sub(r"[^\w\s]", "", file_name)
        file_content = input("Enter the text content for the file: ")
        with open(f"data/articles/{file_name}.txt", "w") as f:
            f.write(file_content)
        print(f"Successfully wrote content to file {file_name}.txt in data/articles")
except:
    print(
        "Run CMD and type out\n[1]: cd"
        + os.getcwd()
        + "\data\imports"
        + "\n[2]: "
        + "pip install -r requirements.txt"
    )
    a = input()
