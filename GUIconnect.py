import requests
import tkinter
import ast
from googletrans import Translator

translator = Translator()

bot_name = "Afmash CS"

# from googletrans import Translator
#
# translator = Translator()
#
#
# def translate(statement):
#     return translator.translate(statement, dest='yo')


def ReadText(message):
    # url = 'http://innovate-yourself.herokuapp.com/webhooks/rest/webhook'
    # url = 'http://localhost:5055/webhook/rest/webhook'  ##change rasablog with your app name

    url = '  https://71d0-105-112-146-198.eu.ngrok.io/webhooks/rest/webhook'
    myobj = {
        "message": message,
        "sender": "Afmash bot",
    }

    x = requests.post(url, json=myobj)

    ast.literal_eval(x.text)
    print(ast.literal_eval(x.text))


    # conversation.append("Innovate: "+"\n".join([ast.literal_eval(x.text)[0]["text"].split(" ")[3*(i-1):3*(i-1)+3]
    # if len(ast.literal_eval(x.text)[0]["text"].split(" "))//10 >10 else ast.literal_eval(x.text)[0]["text"] for i
    # in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//10)]))

    reply = ""

    if len(ast.literal_eval(x.text)) > 1:
        for i in range(len(ast.literal_eval(x.text))):
            # print(ast.literal_eval(x.text)[i]["text"])
            # print("j now here")

            reply = ""
            reply += " ".join(
                ast.literal_eval(x.text)[i]["text"].split(" ")) + "\n"  # [9 * (i - 1):9 * (i - 1) + 9]) + "\n"
            print(yoreply.text)
            # print("j now here")

            yoreply = translator.translate(reply, dest='yo')
            return reply #yoreply.text

    elif len(ast.literal_eval(x.text)[0]["text"].split(" ")) > 50:
        for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" ")) // 9 + 1):
            reply += " ".join(ast.literal_eval(x.text)[0]["text"].split(" ")[9 * (i - 1):9 * (i - 1) + 9]) + "\n"
            yoreply = translator.translate(reply, dest='yo')
            return reply #yoreply.text
            # print(reply)
            # print("j now here")
    else:
        reply = ast.literal_eval(x.text)[0]["text"]
        yoreply = translator.translate(reply, dest='yo')
        return yoreply.text
        print(yoreply.text)

    return reply

    # print([list(i.keys())[1] for i in ast.literal_eval(x.text)])
    # if 'image' in [list(i.keys())[1] for i in ast.literal_eval(x.text)]:
    #     def OpenImage():
    #         import webbrowser
    #         webbrowser.open(ast.literal_eval(x.text)[1]["image"].replace("\\",""))
    #     conversation.append("Innovate: " + ast.literal_eval(x.text)[1]["image"].replace("\\",""))
    #     b = tkinter.Button(root, text="Open Image",command=OpenImage).pack(...)
    # text.set("\n".join(conversation))
