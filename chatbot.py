import requests

url = "https://muhammadzaidanrafa.github.io/chatbot-rafa/bot.json"

response = requests.get(url)
data = response.json()

responses = data["chatbot"]["responses"]
default_reply = data["chatbot"]["defaultReply"]

print("=" * 40)
print("WELCOME TO RAFAEL AI")
print("Version 2.0")
print("Type 'exit' to exit.")
print("=" * 40)

while True:
    user = input("You : ").strip().lower()

    if user == "exit":
        print("Bot  : Bye!")
        break

    reply = default_reply

    for item in responses:
        if user in item["keywords"]:
            reply = item["reply"]
            break

    print("Bot  :", reply)
