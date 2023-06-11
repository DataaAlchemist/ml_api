from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_title(title):
    title = re.sub('[^A-Za-z0-9]+' , ' ', title)
    title = title.lower()
    return title

def get_recommendations(title, books_df, tfidf_vect):
    try:
        title_iloc = books_df.index[books_df['title'] == title][0]
    except:
        return 'Sorry, we could not find that book.'

    show_cos_sim = cosine_similarity(tfidf_vect[title_iloc], tfidf_vect).flatten()
    indices = show_cos_sim.argsort()[::-1]
    books = books_df.iloc[indices]

    return books[:10].to_dict('records')

def get_similar_book(description, books_df, desc_tfidf_vect):
    try:
        desc_iloc = books_df.index[books_df['description'] == description][0]
    except:
        return 'Sorry, we could not find that book.'

    show_cos_sim = cosine_similarity(desc_tfidf_vect[desc_iloc], desc_tfidf_vect).flatten()
    indices = show_cos_sim.argsort()[::-1]
    books = books_df.iloc[indices]

    return books[:10].to_dict('records')