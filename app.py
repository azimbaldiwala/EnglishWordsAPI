from flask import Flask, render_template, request, send_file
import json
import get_word

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def random_word():
    word, meaning = get_word.get_word()
    dictionary = {
        word: meaning
    }

    return dictionary


@app.route('/<int:word_size>')
def random_word_with_size(word_size):
    word, meaning = get_word.get_word(word_size)
    dictionary = {
        word: meaning
    }

    return dictionary


@app.route('/<string:word_initial>')
def random_word_fixed_initial(word_initial):
    word, meaning = get_word.get_word(0, word_initial)
    dictionary = {
        word: meaning
    }

    return dictionary


@app.route('/<int:word_size>/<string:word_initial>')
def random_word_fixed_initial_n_size(word_size, word_initial):
    word, meaning = get_word.get_word(word_size, word_initial)
    dictionary = {
        word: meaning
    }

    return dictionary


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
