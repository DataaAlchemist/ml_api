from flask import Flask, request, jsonify
from pymongo import MongoClient
from recommendation_engine import get_recommendations, get_similar_book
import pandas as pd
from bson import json_util, ObjectId
import pickle

app = Flask(__name__)

client = MongoClient("mongodb+srv://AdrianBadjideh:vQPm8EgUsKlIeeT2@enchant.brnukzz.mongodb.net/?retryWrites=true&w=majority/enchant")
print('connection success..')

#Avoid switching the order of 'title' and 'confidence' keys
app.config['JSON_SORT_KEYS'] = False

books_df = pd.read_csv('data/books_clean.csv')

vectorizer = pickle.load(open('models/tfidf_matrix.pickle', 'rb'))
vectorizer_desc = pickle.load(open('models/desc_tfidf_matrix.pickle', 'rb'))

#API endpoint
@app.route('/api/recommend', methods=['POST'])
def process_request():
    #Parse received JSON request
    user_input = request.get_json()

    #Extract show title
    title = user_input['title']

    #Call recommendation engine
    recommended_books = get_recommendations(title, books_df, vectorizer)

    return jsonify(recommended_books)

@app.route('/api/similar', methods=['POST'])
def process_request2():
    # Parse received JSON request
    user_input = request.get_json()

    #Extract show id
    id = int(user_input['id'])
    description = books_df[books_df['id'] == id]['description'].values[0]

    #Call recommendation engine
    recommended_books = get_similar_book(description, books_df, vectorizer_desc)

    return jsonify(recommended_books)

##get from mongoserver
@app.route('/api/get', methods=['GET'])
def get_all():
    db = client['enchant']
    collection = db['books']
    output = []
    for q in collection.find():
        author = q['author']
        genre = q['genre']
        if isinstance(author, str):
            author = {'_id': str(ObjectId()), 'author': author}
        if isinstance(genre, str):
            genre = {'id': str(ObjectId()), 'genre': genre}
        transformed_doc = {
            'isbn': q['isbn'],
            'title': q['title'],
            'author': author,
            'genre': genre,
            'description': q['description'],
            'image': q['image'],
            'rating': q['rating']
        }
        output.append(transformed_doc)
    return jsonify({'result': output})

@app.teardown_appcontext
def teardown_db(exception):
    print('disconnecting...')
    client.close()