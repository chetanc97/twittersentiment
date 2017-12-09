# from sklearn.feature_extraction.text import CountVectorizer
#
# vectorizer = CountVectorizer()
#
# string0 =  "hi , hello how you ? "
# string1 =  "I am early early early early today to the office"
# string2 =  "Pizza is delicious not not"
#
# list1 =[string0,string1,string2]
#
# bag_of_words =  vectorizer.fit(list1)
#
# bag_of_words =  vectorizer.transform(list1)
#
# print(bag_of_words)

from sklearn.feature_extraction.text  import CountVectorizer

vectorizer = CountVectorizer()

string0 =  "hi , hello how you ? "
string1 =  "I am early early early early today to the office"
string2 =  "Pizza is delicious not not"

list3 =[string0 ,string1 ,string2]

bag = vectorizer.fit(list3)

bag = vectorizer.transform(list3)

print(bag)
