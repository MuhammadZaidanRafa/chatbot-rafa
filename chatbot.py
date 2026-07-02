import requests

url = "https://muhammadzaidanrafa.github.io/chatbot-rafa/bot.json"

response = requests.get(url)
data = response.json()

responses = data["chatbot"]["responses"]
default_reply = data["chatbot"]["defaultReply"]

print("=" * 40)
print("Selamat Datang di RAFAEL AI")
print("Versi 2.0")
print("Ketik 'exit' untuk keluar")
print("=" * 40)

while True:
    user = input("Anda : ").strip().lower()

    if user == "exit":
        print("Bot  : Sampai jumpa!")
        break

    reply = default_reply

    for item in responses:
        if user in item["keywords"]:
            reply = item["reply"]
            break

    print("Bot  :", reply)
