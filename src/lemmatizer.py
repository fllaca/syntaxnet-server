from pattern.es import conjugate, predicative, lemma, singularize
from pattern.es import INFINITIVE, PRESENT, PAST, SG, SUBJUNCTIVE, PERFECTIVE

print lemma("pon")
print singularize("ventana")
 
# print conjugate('pon', INFINITIVE)
# print conjugate('soy', PRESENT, 1, SG, mood=SUBJUNCTIVE)
# print conjugate('soy', PAST, 3, SG) 
# print conjugate('soy', PAST, 3, SG, aspect=PERFECTIVE) 

def lemmatize(text, type):
    if type == 'VERB':
        return lemma(text)
    elif type == 'NOUN':
        return singularize(text)
    elif type == 'ADJ':
        return predicative(text)
    else:
        return text