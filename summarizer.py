from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
import json

def summarization(text, alg="lexrank"):
    parser = PlaintextParser.from_string("".join(text), Tokenizer("japanese"))

    if alg == "lexrank":
        summarizer = LexRankSummarizer()
    elif alg == "textrank":
        summarizer = TextRankSummarizer()
    elif alg == "lsa":
        summarizer = LsaSummarizer()
    else:
        raise Exception("IllegalArgumentException")

    summarizer.stop_words = [" "]
    abst = summarizer(document=parser.document, sentences_count=5)
    abst = [x for x in map(lambda x: "".join(x.words), abst)]

    return abst

def main():
    with open("seg_data.json", "r") as f:
        seg = json.load(f)

    absts = {}
    for k in seg.keys():
        absts[k] = summarization(seg[k])

    with open("abst_data.json", "w", encoding='utf-8') as f:
        json.dump(absts, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
