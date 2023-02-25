import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))      # "cat" similar to "monkey"
print(word3.similarity(word2))      # "banana" similar to "monkey"
print(word3.similarity(word1))      # "banana" similar to "cat"

print()
print("-" * 40)
print()

'''
There's nothing surprising about the results of the above, 'cat' and 'monkey' share some semantic connotations,
fewer than 'monkey' and 'banana', but more than the semantically unrelated 'cat' and 'banana'. 
'''

# An example of my own
word4 = nlp("pet")
word5 = nlp("dog")

print(word1.similarity(word4))      # "cat" similar to "pet"
print(word1.similarity(word5))      # "cat" similar to "dog"
print(word4.similarity(word5))      # "pet" similar to "dog"

print()
print("-" * 40)
print()



# Working with Vectors
tokens = nlp('cat apple monkey banana dog')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()
print("-" * 50)
print()


# Test
tokens = nlp('flowers sadness hills trees valleys swamps')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()
print("-" * 50)
print()


# Working with Sentences
sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "My cat is on a car, why?",
    "Is a cat on my car?",
    "Where does my cat go?",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
    ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
'''
Using the 'en_core_web_sm' language instead of 'en_core_web_md', I notice a greater variance between similarity values, and generally speaking all the values
are lower
'''