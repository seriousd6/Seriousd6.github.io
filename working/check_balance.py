import re

code = open('/home/domad/Documents/bible-study-website/assets/js/workshop.js', encoding='utf-8').read()

def strip_strings(src):
    result = []
    i = 0
    while i < len(src):
        if src[i:i+2] == '//':
            end = src.find('\n', i)
            if end == -1: end = len(src)
            result.append('\n')
            i = end
        elif src[i:i+2] == '/*':
            end = src.find('*/', i+2)
            if end == -1: end = len(src)
            else: end += 2
            newlines = src[i:end].count('\n')
            result.append('\n' * newlines)
            i = end
        elif src[i] == '`':
            j = i + 1
            while j < len(src):
                if src[j] == '\\':
                    j += 2
                elif src[j] == '`':
                    j += 1
                    break
                else:
                    j += 1
            result.append('``')
            i = j
        elif src[i] == '"':
            j = i + 1
            while j < len(src) and src[j] != '\n':
                if src[j] == '\\':
                    j += 2
                elif src[j] == '"':
                    j += 1
                    break
                else:
                    j += 1
            result.append('""')
            i = j
        elif src[i] == "'":
            j = i + 1
            while j < len(src) and src[j] != '\n':
                if src[j] == '\\':
                    j += 2
                elif src[j] == "'":
                    j += 1
                    break
                else:
                    j += 1
            result.append("''")
            i = j
        else:
            result.append(src[i])
            i += 1
    return ''.join(result)

stripped = strip_strings(code)
b_open  = stripped.count('{')
b_close = stripped.count('}')
p_open  = stripped.count('(')
p_close = stripped.count(')')
print(f'Braces: {b_open} open, {b_close} close, diff={b_open - b_close}')
print(f'Parens: {p_open} open, {p_close} close, diff={p_open - p_close}')

# Find lines where cumulative brace count goes negative
depth = 0
for lineno, line in enumerate(stripped.split('\n'), 1):
    for ch in line:
        if ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                print(f'  Brace went negative at line {lineno}: {line.strip()[:80]}')
                depth = 0  # reset to keep going
