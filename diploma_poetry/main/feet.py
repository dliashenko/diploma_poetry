import pandas as pd


def mark_up(raw_poems):
    poems_lines = [poem.split("\n") for poem in raw_poems]
    flat_poems_lines = [line for poem in poems_lines for line in poem]
    vowels = ['у', 'е', 'і', 'о', 'я', 'и', 'ю', 'а', 'ї', 'є']
    marked_lines = []
    for line in flat_poems_lines:
        counter = 0
        for letter in line:
            marked_lines.append(letter)
            if letter == any(vowels):
                counter += 1
                if counter % 2 == 0:
                    marked_lines.append("*")
    print("".join(marked_lines))

def nagolos(value):
    vowels = ['у', 'е', 'і', 'о', 'я', 'и', 'ю', 'а', 'ї', 'є']
    word = [i.lower() for i in value]
    if len(word[0]) == 1 and word[0] in vowels:
        word.insert(1, '*')
    elif len(word[1]) == 1 and word[1] in vowels:
        word.insert(2, '*')
    return word

if __name__ == "__main__":
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(poems)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(poems1)
    poems = poems_df["poem"].tolist() + poems1_df["poem"].tolist()
    print(mark_up(poems))

