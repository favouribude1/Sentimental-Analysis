#NLP without using the NLTK

# A) CLEANING TEXT STEPS
# 1) Create a text file and take text from it (into the mainn py file)
# 2) Covert the letter into lower case ("Apple" is not equal to "apple")
# 3) Remove punctuations like .,?!


#STEP 1
text = open('read.txt', encoding = 'utf-8').read()
#the reason for using the encoding is bcos sometimes we might want to copy and paste text from blog post
#articles from the web into our text file for analysis, and sometimes this text are are in utf encoding, so if you dont spefify the encoding type in your code, it might lead to errors

#print(text)

#STEP 2
lowercase = text.lower()
#print(lowercase)

#STEP 3
import string
#print(string.punctuation)
cleaned_text = lowercase.translate(str.maketrans('','',string.punctuation))

#the ".translate" simply means "converting" our string/text to string that don't contains punctuations(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ )

#the DA translate method to convert the string into a string that doesn't contain punctuation and the function that helps it to convert is (STR.maketrans) which requires 3 parameters first string than 2nd string which we do need in our case and the third string this is known as (string. Punctuation) which will contain all of our punctuation that need to be moved and if you want.
#first parameter it contains the characters that need to be replaced in our case there are just no characters that need to be replaced
#we needed the str 3 or the 3rd string and the 2nd string specifies the list of characters with which the characters need to be replaced for example if our first string let's write STR 1 if our str1 is let's say ABC and str2 is something like let's read GE F so we this STR 1 will be this specify the list of character that need to be replaced so ABC will get replaced with GE F
# cleaned_text = lowercase.translate(str.maketrans('love','hate',string.punctuation))

#print(cleaned_text)

#-------------------------------------------------------------------------------------------------------
# B) Tokenization and Stop Words (NLP) (what are they and how to remove them from our text
# Tokenization is how to break sentences into words
# we will can break our sentence in our text file into word

tokenized_words = cleaned_text.split()
#to split/break our text and store it separately as a list in our variable
#sentimental analysis is the analysis of words and not sentences
#print(tokenized_words)

#STOP WORDS are words that dont add any meaning to a sentence, e.g "i". 'i' does not add any emotion meaning or any meaning to a sentence can be removed
#NLTK package already contains a lot of stop words that can be use to remove stop words but since we are doing it manually we would have to write the stop words our self

stop_words =  ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


# remove stop words from our already tokenized words
# we can use the "for" loop to do this

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#print(final_words)

#---------------------------------------------------------------------------------------------------
# C) Algorithm for Emotion and Text Analysis (NLP)
# download the "emotions.txt" file from his github account
# this emotion text file contains words and they type of emotions they represent,e.g if you use the word "victimized" in the text file then the emotion file state that it means been "cheated"

#we would be using the emotion.txt file to know which words represent which emotions by reading our read.txt file and emotion.txt
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list


emotion_list = []   # 2)
##  - open the emotion file
with open('emotions.txt', 'r') as file:
    # Loop through each line in the emotion.txt  which is now saved as "file" and clear it
    #by removing the extra spaces, punctuations, extra line spaces which a visible when you print(line) hence we need to clear them out  for better NLP analysis
    for line in file:
        #print(line)
        clear_line = line.replace("\n","").replace(',','').replace("'","").strip() #strip is to remove spaces from the left and right side
        #print(clear_line)

        ##  - Extract the word and emotion using split
        #we want to split/separate the text in the emotion file into words and emotions

        word, emotion = clear_line.split(":") #it goes thru the emotion file and any word before the ":", it saves in the word variable and anythin after the ':' is saved in the emotion variable

        #the split function is any punctuation used to split words or numbers in same document
        #print("Word :" + word + " "+ "Emotion : " + emotion)

        if word in final_words:  # 2)
            emotion_list.append(emotion) #2)
print(emotion_list)

#-----------------------------------------------------------------
# D) Counting Emotions - Natural Language Processing

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list

#now we want to check if our final_word match up with the words inside the emotion.txt file or not
# emotion_list = []  2)
# with open('emotions.txt', 'r') as file:
#     for line in file:
#         clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
#         word, emotion = clear_line.split(':')
#
#         if word in final_words: 2)
#             emotion_list.append(emotion) 2)
#
# print(emotion_list)
#--------------------------------------------------------------------------------------------------------------------


# 3) Finally count each emotion in th
# e emotion list
#to count this emotions we would use "collections"

from collections import Counter
w = Counter(emotion_list)

print(w)

#-------------------------------------------------------------------------------------

# E)  Emotions in a Graph using Matplotlib (NLP)

import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

