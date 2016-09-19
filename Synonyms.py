# -*- coding: utf-8 -*-
import random

Synonyms = [
    [u"כעס", u"זעם", u"חימה", u"זעף", u"חרון"],
    [u"פחד", u"חרדה", u"יראה", u"מגור", u"חשש", u"מורא"],
    [u"אסון", u"צרה", u"איד", u"רעה"],
    [u"ירח", u"לבנה", u"סהר"],
    [u"שמש", u"חמה"],
    [u"ראה", u"הסתכל", u"הביט"],
    [u"חבר", u"עמית", u"רע", u"ידיד"],
    [u"בושה", u"כלימה", u"חרפה", u"ביזיון", u"קלון"],
    [u"אריה", u"לביא", u"שחל", u"ליש", u"כפיר"],
    [u"מתנה", u"שי", u"מנחה", u"תשורה", u"מתת"],
    [u"בודד", u"ערירי", u"גלמוד"],
    [u"מציל", u"מושיע", u"גואל", u"פודה"],
    [u"שמחה", u"גילה", u"דיצה", u"צהלה"],
    [u"רשע", u"אכזר", u"זד"],
    [u"סוף", u"קץ", u"שלהי"],
    [u"שר", u"זימר", u"רן"],
    [u"שמים", u"רקיע", u"מרום", u"שחקים"],
    [u"זקן", u"קשיש", u"סב", u"ישיש"],
    [u"קטטה", u"מריבה", u"מדון", u"ריב", u"מך"],
    [u"שתה", u"גמע", u"רווה", u"לגם"],
    [u"עני", u"דל", u"רש", u"אביון", u"דלפון"],
    [u"מתנה", u"שי", u"מנחה", u"מתת", u"דורון"],
    [u"חשכה", u"אפלה", u"עלטה"],
    [u"אדום", u"שני", u"ארגמן"],
    [u"עצב", u"יגון", u"תוגה", u"קדרות"],
    [u"שוטה", u"אוויל", u"טיפש", u"סכל"],
    [u"אויב", u"צר", u"קם"],
    [u"מלאכה", u"מקצוע", u"משלוח יד", u"עיסוק", u"עבודה"]
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

    options.insert(random.randint(0, len(options)), answer)

    return riddle, answer, options


def main():
    print generate_riddle()

if __name__ == "__main__":
    main()
