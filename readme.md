# Book Recommendation API

## Description

API Machine Learning bertugas dalam mengolah data user, seperti judul buku dan deskripsi buku yang dillihat oleh user. Algortima Machine Learning yang digunakan berupa Content-based Filtering, Content-based filtering adalah salah satu pendekatan dalam sistem rekomendasi yang menggunakan informasi atau konten dari item-item yang ada untuk membuat rekomendasi. Pendekatan ini didasarkan pada kesamaan antara item-item berdasarkan atribut-atribut atau fitur-fitur yang dimiliki oleh item tersebut.

## Installation

1. Lakukan clone pada repository ini 'git clone https://github.com/DataaAlchemist/ml_api.git' pada git bash ataupun terminal.

2. Menginstal requirements yang dibutuhkan dengan 'pip install -r requirements.txt' pada terminal.

3. Jalankan appnya dengan kode 'python app.py' pada terminal

## Package

* blinker
* click
* colorama
* contourpy
* cycler
* dnspython
* Flask
* fonttools
* gunicorn
* itsdangerous
* Jinja2
* joblib
* kiwisolver
* MarkupSafe
* matplotlib
* numpy
* packaging
* pandas
* Pillow
* pymongo
* pyparsing
* python-dateutil
* pytz
* scikit-learn
* scipy
* seaborn
* six
* threadpoolctl
* tzdata
* Werkzeug

## Endpoint

* /api/recommend : untuk mendapatkan rekomendasi buku berdasarkan judul buku yang dicari.

* /api/similar : untuk mendapatkan rekomendasi buku berdasarkan deskripsi buku.