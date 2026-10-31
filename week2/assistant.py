"""Meeting 2 starter. python week2/assistant.py. See docs/LABS.md.
Notebooks named below are in week1/notebooks/.
Stuck after trying? See solutions/week2/assistant.py."""
from coursekit.ai import reply, AIError
from coursekit.market import quote, receipt


def ask_assistant(question):
    # TODO 1: Reject blank input, then build a list holding one user message.
    #   How: if question.strip() is empty, raise AIError('Enter a question first.').
    #   Use AIError, not ValueError: the code at the bottom only catches AIError.
    #   Message shape: [{"role": "user", "content": question}]
    #   Help: week1-deepdive-1-python-speaks.ipynb, section 4 (String methods).
    #   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 5 (Dictionaries).
    #   Practice: week1-assignment.ipynb, Challenge 7.
    #   Careful: the notebooks also show a "system" role, but reply() rejects it.
    #   The assistant's job goes in the instructions string instead.
    # TODO 2: Call reply(messages, instructions), return its text, and delete the raise line.
    #   How: instructions is a string you write, such as 'You are a friendly market assistant.'
    #   Read: coursekit/ai.py to follow the request from start to finish.
    # Demo mode is the default: it does not call AI.
    # Check: a question prints a [DEMO - no AI request] reply; a blank one prints your message.
    # Next (docs/LABS.md, Meeting 2): show a quote from quote() and receipt(), then ask the
    # AI to explain it. Python calculates the amount; the AI only explains it.
    raise NotImplementedError('Complete ask_assistant in Meeting 2.')


if __name__ == '__main__':
    try:
        print(ask_assistant(input('Your question: ')))
    except (NotImplementedError, AIError) as exc:
        print(exc)
