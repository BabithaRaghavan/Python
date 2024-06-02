''' Function to convert emoji to message '''

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "🙁"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word)+ " "
    return output

message = input('>')
message_emoji = emoji_converter(message)
print(message_emoji)
