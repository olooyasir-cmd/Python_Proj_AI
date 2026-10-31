"""Solution for Meeting 2. Try week2/assistant.py yourself first.
Run: python solutions/week2/assistant.py"""
from coursekit.ai import reply, AIError
from coursekit.market import quote, receipt


def ask_assistant(question, item):
    # TODO 1: AIError, because the code at the bottom catches it and prints the message.
    if not question.strip():
        raise AIError('Enter a question first.')
    messages = [{"role": "user", "content": question}]
    # TODO 2: Python calculated the amount, so the AI is only asked to explain it.
    instructions = ('You are a friendly market assistant. Explain this exact quote and do '
                    f'not change its amount or claim anything is in stock: {receipt(item)}')
    return reply(messages, instructions)


if __name__ == '__main__':
    item = quote('yam', 3)
    print(receipt(item))
    try:
        print(ask_assistant(input('Your question: '), item))
    except AIError as exc:
        print(exc)
