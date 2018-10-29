import math
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

#copy pasted a list from other file runtime bad programming srry
docs = [
     'BCAL', 
     'Bus Routes', 
     'Center for Students in Recovery', 
     'CMHC - Crisis Line', 
     'CMHC - General', 
     'CMHC - Groups ', 
     'CMHC - Mind Body Labs', 
     'Family Life Services', 
     'Forty Acres Pharmacy', 
     'Free Self Defense Classes-UTPD', 
     'Gender and Sexuality Center', 
     'Hornslink', 
     'Interpersonal Violence Peer Support Program ', 
     'Legal Services', 'Longhorn Automative Program', 
     'Multicultural Engagement Center', 
     'New Student Services', 
     'New Student Services- Longhorn Way', 
     'New Student Services- Rise 2018', 
     'Office of Health Promotions', 
     'Office of Sorority & Fraternity Life', 
     'Ombuds Office', 
     'Parking and Transportation Services Bike Service', 
     'RecSports - Fitness and Wellness', 
     'RecSports - General', 
     'RecSports - IM Sports', 
     'RecSports - Sport Clubs', 
     'RecSports- Texercise', 
     'Sanger Learning Center', 
     'Services for Students with Disabilities', 
     'Student Activities', 
     'Student Conduct & Academic Integrity', 
     'Student Emergency Services ( SES )', 
     'Student Government', 
     'Student Veteran Services', 
     'SURE Ride', 
     'SURE Walk', 
     'University Health Services - Allergies and Immunizations', 
     'University Health Services - General Medicine', 
     'University Health Services - Nurse Advice Line', 
     'University Health Services - Nutrition Services', 
     'University Health Services - Physical Therapy', 
     'University Health Services - Sexual Assualt Forensic Exams', 
     'University Health Services - Sports Medicine', 
     'University Health Services - STI Testing', 
     'University Health Services - Travel Health', 
     "University Health Services - Women's Health", 
     'University Writing Center', 
     'UT Copy and Print', 
     'UT Leadership and Ethics Institute', 
     'VAV', 
     'Graduation Help Desk', 
     'CMHC - Thrive App', '
     'Title IX - Report Incident', 
     'Texas Athletics', 
     'Title IX - Report Incident (1)'
]

# to do: load raw document txt at runtime
#        implement clustering
#        etc etc


def tf_idf():
"""Returns a numpy array whose 
i,j entry is the (normalized) tf-idf
of term j in corpus in doc i. 
CountVectorizer.fit_transform is used to 
create the corpus (vocabulary).
"""
    # CountVectorizer.transform takes iterables
    text_docs = []
    
    for doc in docs:
        filename = "TextData/" + doc + ".txt"
        txt = open(filename,'r').read
        text_docs.append(txt) 
        
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    return tfidf_matrix
    
    
def cosine_score(query):
""" Returns a dictionary mapping
document names in docs to a cosine 
similarity score.
"""
    q = (str(query))
    mat = tf_idf()
    scores = {}
    
    text_docs = []
    for doc in docs:
        filename = "TextData/" + doc + ".txt"
        txt = open(filename,'r').read
        text_docs.append(txt) 
    
    count_vectorizer = CountVectorizer()
    # get the corpus
    count_vectorizer.fit_transform(text_docs)
    # vectorize the query
    q_vec_ct = count_vectorizer.transform(q)

    tfidf = TfidfTransformer(norm="l2") # l2 normalization
    tfidf.fit(freq_term_matrix)
    
    q_vec_tfidf = tfidf.transform(q_vec)
    
    for i in range(mat.shape[0]):
        doc_name = docs[i]
        scores[doc_name] = cosine_similarity(q_vec_tfidf, mat[i:i+1])[[0]]
        
    return scores
    
    
def main():
    cont = True
    
    while cont:
        prompt = input("Enter query or press 'q' to quit: ")
        if prompt == q:
            cont = False
            break
        else:
            cosine_scores = sorted(cosine_score(prompt).iteritems(), 
                                   key = lambda (k,v):(v,k), reverse = True)
            print("Top scores")
            for x in range(5):
                print(cosine_scores[x])
               
                
if __name__ == '__main__':
    main()
