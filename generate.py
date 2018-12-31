from janome.tokenizer import Tokenizer
import random
import re

def generate_575(data):
    if len(data) < 2:
        return ["".join(data)]

    t = Tokenizer()
    words = {len_ruby:[] for len_ruby in range(1, 9)}
    small_kana = re.compile(r"[ァィゥェォャュョヮ]")
    for text in data:
        tokens = t.tokenize(text)
        for i, token in enumerate(tokens):
            part_of_speech = token.part_of_speech.split(",")
            part = part_of_speech[0]
            ruby = small_kana.sub("", token.reading)
            word = token.surface
            inflform = token.infl_form

            # 1st phase
            if (part == "名詞" or part == "助詞" or part == "動詞" or part == "形容詞" or part == "感動詞") and ruby != "*":
                if word not in words[len(ruby)]:
                    if (part != "動詞" or part == "動詞" and token.infl_form == "基本形"):
                        words[len(ruby)].append(word)

            # 2nd phase
            if i + 1 < len(tokens):
                word_next = tokens[i + 1].surface
                part_next = tokens[i + 1].part_of_speech.split(",")[0]
                ruby_next = small_kana.sub("", tokens[i + 1].reading)

                if (part == "名詞" or part == "動詞" or part == "形容詞" or part == "感動詞") and (part_next == "名詞" or part_next == "助詞") and ruby != "*" and ruby_next != "*":
                    word_cat = word + word_next
                    ruby_cat = ruby + ruby_next
                    if (len(ruby_cat) < 9):
                        words[len(ruby_cat)].append(word_cat)

    # 3rd phase
    if words[3] and words[4]:
        for i in range(10):
            word_cat = words[4][random.randint(0, len(words[4]) - 1)] + words[3][random.randint(0, len(words[3]) - 1)]
            if word_cat not in words[7]:
                words[7].append(word_cat)

    print(words)

    # 4th phase
    words[5].extend(words[6])
    words[7].extend(words[8])

    # make
    result = []
    if words[5] and words[7]:
        for i in range(30):
            p1 = words[5][random.randint(0, len(words[5]) - 1)]
            p2 = words[7][random.randint(0, len(words[7]) - 1)]
            p3 = words[5][random.randint(0, len(words[5]) - 1)]
            senryu = "\n".join([p1, "　" + p2, "　　" + p3])
            result.append(senryu)

    return result

