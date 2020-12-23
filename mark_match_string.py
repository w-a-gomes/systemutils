#!/usr/bin/env python3
import re


class MarkMatchString(str):
    def mark_match_sub(self, regex_match: str, regex_sub: str) -> list:
        # antes = re.sub(regex_match, '<' + regex_match + '>', self)
        # replace() e mais leve que re.sub()
        antes = self.replace(regex_match, '<' + regex_match + '>')
        depois = re.sub(regex_match, '<' + regex_sub + '>', self)
        return [antes, depois]


if __name__ == '__main__':
    m = MarkMatchString('O rato roeu a roupa do rei de roma. A roupa ficou feia')
    print(m.mark_match_sub(regex_match='roupa', regex_sub='camisa'))
