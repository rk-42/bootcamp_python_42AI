import string


def text_analyzer(text=None):
    if text is None:
        text = input('What is the text to analyse?\n')
    punctuation = sum((c in string.punctuation) for c in text)
    lower = sum(c.islower() for c in text)
    upper = sum(c.isupper() for c in text)
    spaces = sum(c.isspace() for c in text)

    print(f'The text contains {len(text)} characters:\n'
          f'- {upper} upper letters\n'
          f'- {lower} lower letters\n'
          f'- {punctuation} punctuation marks\n'
          f'- {spaces} spaces')

if __name__ == '__main__':
    text_analyzer()
