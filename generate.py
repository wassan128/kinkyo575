from janome.tokenizer import Tokenizer
import random
import re


def generate_575(data):
    t = Tokenizer()
    words = {"5": [], "7": []}
    small_kana = re.compile(r"[ァィゥェォッャュョヮ]")
    for text in data:
        tokens = t.tokenize(text)
        for i, token in enumerate(tokens):
            part_of_speech = token.part_of_speech.split(",")
            part = part_of_speech[0]
            kind = part_of_speech[1]
            ruby = small_kana.sub("", token.reading)
            word = token.surface
        
            # 1st phase
            if (part == "名詞" or part == "助詞" or part == "動詞" or part == "形容詞" or part == "感動詞") and ruby != "*":
                if word not in words["5"] and len(ruby) == 5 or len(ruby) == 6:
                    words["5"].append(word)
                elif word not in words["7"] and len(ruby) == 7 or len(ruby) == 8:
                    words["7"].append(word)

            # 2nd phase
            cats = []
            if i + 1 < len(tokens):
                word_next = tokens[i + 1].surface
                part_next = tokens[i + 1].part_of_speech.split(",")[0]
                ruby_next = small_kana.sub("", tokens[i + 1].reading)
            if (part == "名詞" or part == "動詞" or part == "形容詞" or part == "感動詞") and (part_next == "名詞" or part_next == "助詞") and ruby != "*" and ruby_next != "*":
                word_cat = word + word_next
                if word_cat not in words["5"] and len(ruby) + len(ruby_next) == 5:
                    words["5"].append(word_cat)
                elif word_cat not in words["7"] and len(ruby) + len(ruby_next) == 7:
                    words["7"].append(word_cat)

    print(words)

    result = []
    if words["5"] and words["7"]:
        for i in range(30):
            p1 = words["5"][random.randint(0, len(words["5"]) - 1)]
            p2 = words["7"][random.randint(0, len(words["7"]) - 1)]
            p3 = words["5"][random.randint(0, len(words["5"]) - 1)]
            senryu = "\n".join([p1, "　" + p2, "　　" + p3])
            print("#{}: {}".format(i, senryu))
            result.append(senryu)

    return result

