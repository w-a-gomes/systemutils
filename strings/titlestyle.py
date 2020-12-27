#!/usr/bin/env python3
import string


class TitleStyle(str):
    def style(self, language: str = None) -> str:
        lang = {
            'pt': [
                ' A', 'A ', ' E', 'E ', ' O', 'O ',
                ' Da', 'Da ', ' De', 'De ', ' Do', 'Do ',
                ' Na', 'Na ', ' No', 'No '
            ],
            'en': [
                ' And', 'And ', ' Or', 'Or ', ' Of', 'Of ',
                ' To', 'To ', ' Be', 'Be '
            ]
        }
        old_text = self.title()
        new_text = old_text
        for word in lang[language]:
            if word in old_text:
                new_text = new_text.replace(word, word.lower())

        new_str = ''
        stop = False
        for new_letter in new_text:
            if not stop:
                if new_letter in string.punctuation or new_letter in string.whitespace:
                    new_str += new_letter
                else:
                    new_str += new_letter.upper()
                    stop = True
            else:
                new_str += new_letter

        return new_str


if __name__ == '__main__':
    text = '. o rato roeu a roupa do rei de roma cara.'
    print(text.title())
    print(TitleStyle(text).style('pt'))
    text = ". will you go to your house or i will kill you."
    print(text.title())
    print(TitleStyle(text).style('en'))
