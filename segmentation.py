import spacy
import json

nlp = spacy.load("ja_ginza")

def segmentation(text):
    doc = nlp(text)

    return doc

def main():
    with open("data.json", "r") as f:
        data = json.load(f)

    keys = list(data.keys())
    seg_d = {}
    for k in keys:
        txtlist = data[k]

        seg = segmentation("".join(txtlist))
        seg_d[k] = [str(x) for x in seg]

    with open("seg_data.json", "w") as f:
        json.dump(seg_d, f, indent=4)


if __name__ == "__main__":
    main()
