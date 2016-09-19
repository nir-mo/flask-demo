# -*- coding: utf-8 -*-
import random

Synonyms = [
    [u"כעס", u"זעם", u"חימה", u"זעף", u"חרון"],
    [u"פחד", u"חרדה", u"יראה", u"מגור", u"חשש", u"מורא"],
    [u"אסון", u"צרה", u"איד", u"רעה"],
    [u"ירח", u"לבנה", u"סהר"]
]


def generate_riddle(number_of_answers=4):
    """
    Generates riddles

    :param number_of_answers:
    :return: (word, solution, options)
    """
    assert 1 < number_of_answers <= len(Synonyms)
    answer_seq = random.randint(0, len(Synonyms) - 1)

    _temp_syn = [s for i, s in enumerate(Synonyms) if i != answer_seq]

    pair = random.sample(Synonyms[answer_seq], 2)
    riddle, answer = pair[0], pair[1]
    options = [random.choice(s)
               for s in random.sample(_temp_syn, number_of_answers - 1)]

    options.append(answer)

    return riddle, answer, options


def main():
    print generate_riddle()

if __name__ == "__main__":
    main()
