import json

# Membaca file JSON
with open("bot.json", "r", encoding="utf-8") as file:
    data = json.load(file)

responses = data["chatbot"]["responses"]
default_reply = data["chatbot"]["defaultReply"]

print("=" * 40)
print("Selamat Datang di RAFAEL AI")
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