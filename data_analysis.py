import os
from openpyxl import Workbook,load_workbook
import nltk
import re
from textblob import TextBlob
import glob

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

with open('words/positive-words.txt','r',encoding='utf-8') as file:
    positive_words = set(file.read().split())

with open('words/negative-words.txt','r',encoding='latin-1') as file:
    negative_words = set(file.read().split())
    

def positive_score(text):
    return sum(1 for word in text.split() if word.lower() in positive_words)


def negative_score(text):
    return sum(1 for word in text.split() if word.lower() in negative_words)


def polarity_score(pos_score, neg_score):
    return (pos_score - neg_score) / ((pos_score + neg_score) + 0.000001)


def subjectivity_score(text):
    bolb = TextBlob(text)
    return bolb.sentiment.subjectivity

def avg_sentence_length(text):
    scentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    return len(words) / len(scentences)


def percenetage_of_complex_words(text):
    complex_words = len([word for word in nltk.word_tokenize(text) if len(word)>2 ])
    words = len(nltk.word_tokenize(text))
    return (complex_words/words) * 100



def fog_index(text):
    return 0.4 * (avg_sentence_length(text) + percenetage_of_complex_words(text))


def avg_number_of_words_per_sentence(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    return len(words)/len(sentences)


def complex_words_count(text):
    return len([word for word in nltk.word_tokenize(text) if len(word) > 2]) 


def word_count(text):
    return len(nltk.word_tokenize(text))

def syllable_per_word(text):
    words = nltk.word_tokenize(text)
    syllables = sum([len(re.findall('[aeiouy]',word)) for word in words])
    return syllables / len(words)


def personal_pronouns(text):
    pronouns = re.findall(r'\b(I|we|my|ours|us)\b',text,re.I)
    return len(pronouns)


def avg_word_length(text):
    words = nltk.word_tokenize(text)
    return sum(len(word) for word in words)/ len(words)


output_wb = Workbook()
output_ws = output_wb.active


headers = ["URL_ID","POSITIVE SCORE", "NEGATIVE SCORE","POLARITY SCORE","SUBJECTIVITY SCORE",
           "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS","FOG INDEX", "AVG NUMBER OF WORDS PER SENTENCE",
           "COMPLEX WORD COUNT","WORD COUNT","SYLLABLE PER WORD","PERSONAL PRONOUNS","AVG WORD LENGTH"]

output_ws.append(headers)




def create_unique_filename(base_name,extension):
    if not os.path.exists(f"{base_name}.{extension}"):
        return f"{base_name}.{extension}"
    
    index = 1
    while True:
        new_name = f"{base_name}{index:2}.{extension}"
        if not os.path.exists(new_name):
            return new_name
        index +=1

list_of_dirs = glob.glob('extracted_texts*')
latest_dir = max(list_of_dirs, key=os.path.getmtime)


for filename in os.listdir(latest_dir):
    with open(os.path.join(latest_dir,filename),'r', encoding="utf-8") as f:
        text = f.read()


    pos_score = positive_score(text)
    neg_score = negative_score(text)
    pol_score = polarity_score(pos_score,neg_score)
    subj_score = subjectivity_score(text)
    avg_sent_len = avg_sentence_length(text)
    perc_complex_words = percenetage_of_complex_words(text)
    fog_indx =fog_index(text)
    avg_words_per_sentence = avg_number_of_words_per_sentence(text)
    complex_word_count = complex_words_count(text)
    wrd_count = word_count(text)
    syll_per_word = syllable_per_word(text)
    pers_pronouns = personal_pronouns(text)
    avg_word_len = avg_word_length(text)



    output_ws.append([filename.split('.')[0],pos_score,neg_score,pol_score,subj_score,avg_sent_len,
                      perc_complex_words,fog_indx,avg_words_per_sentence,complex_word_count,wrd_count,
                      syll_per_word,pers_pronouns,avg_word_len])


output_filename = create_unique_filename('Output data structure','xlsx')
output_wb.save(output_filename)
