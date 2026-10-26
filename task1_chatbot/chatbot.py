import re, random, datetime

RULES = [
    (r"\b(hi|hello|hey|hola)\b", ["Hello! How can I help you today?", "Hi there! What can I do for you?"]),
    (r"\bhow are you\b", ["I'm just code, but running great! How about you?"]),
    (r"\b(your name|who are you)\b", ["I'm CodBot, a rule-based chatbot built for CodSoft."]),
    (r"\b(what can you do|help)\b", ["I can chat, tell the time/date, tell a joke, and answer basic questions. Try me!"]),
    (r"\btime\b", [lambda: "It's " + datetime.datetime.now().strftime("%I:%M %p") + "."]),
    (r"\b(date|today|day)\b", [lambda: "Today is " + datetime.datetime.now().strftime("%A, %d %B %Y") + "."]),
    (r"\bjoke\b", ["Why do programmers prefer dark mode? Because light attracts bugs!",
                   "There are 10 kinds of people: those who understand binary and those who don't."]),
    (r"\b(internship|codsoft)\b", ["CodSoft is a tech education platform offering virtual internships. Visit www.codsoft.in"]),
    (r"\b(python|java|code|programming)\b", ["Great topic! Practice daily and build projects to learn faster."]),
    (r"\b(thanks|thank you)\b", ["You're welcome!"]),
    (r"\b(bye|goodbye|exit|quit)\b", ["Goodbye! Have a great day!"]),
]

def respond(text):
    text = text.lower().strip()
    for pattern, replies in RULES:
        if re.search(pattern, text):
            r = random.choice(replies)
            return r() if callable(r) else r
    return "Sorry, I didn't understand that. Type 'help' to see what I can do."

if __name__ == "__main__":
    print("CodBot: Hi! Type 'bye' to exit.")
    while True:
        msg = input("You: ")
        print("CodBot:", respond(msg))
        if re.search(r"\b(bye|goodbye|exit|quit)\b", msg.lower()):
            break
