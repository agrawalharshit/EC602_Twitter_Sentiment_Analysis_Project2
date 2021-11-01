import argparse
from google.cloud import language_v1

def print_res(a):
    s = a.document_sentiment.score
    m = a.document_sentiment.magnitude

    for i, j in enumerate(a.sentences):
        sentence_sen = sentence.sentiment.score
        print(f"score of sentence {i} is sentence_sen ")
    print(f"the overall score is {s}, and magnitude is {m}")
    

def analyze_sentence(file):
    s = language_v1.LanguageServiceClient()
    f = open(file, "r")
    sentences = f.read()
    doc = language_v1.Document(content = sentences, type_=language_v1.Document.Type.PLAIN_TEXT)
    anno = client.analyze_sentiment(request={'document': doc})
    print_res(anno)



result = analyze_sentence("this is the txt file name you want to check")


