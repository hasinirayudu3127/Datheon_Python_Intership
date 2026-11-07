import json
from difflib import get_close_matches


def load_faq():
    with open("sample_faq.json", "r", encoding="utf-8") as file:
        return json.load(file)


def chatbot():
    data = load_faq()

    greetings = data["greetings"]
    faqs = data["faqs"]

    print("===================================")
    print("     DATHEON INTERACTIVE CHATBOT")
    print("===================================")
    print("Hello! I am your FAQ assistant.")
    print("Ask me a question or type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "exit", "quit"]:
            print("Bot: Thank you for chatting. Goodbye!")
            break

        if user_input in greetings:
            print("Bot: Hello! How can I help you today?")

        else:
            questions = [faq["question"].lower() for faq in faqs]

            matches = get_close_matches(
                user_input, questions, n=1, cutoff=0.4
            )

            if matches:
                for faq in faqs:
                    if faq["question"].lower() == matches[0]:
                        print("Bot:", faq["answer"])
                        break
            else:
                print("Bot: Sorry, I don't have an answer for that question.")


if __name__ == "__main__":
    chatbot()