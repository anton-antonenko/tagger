# -*- coding: utf-8 -*-

import anago
import os
import json
from anago.reader import load_data_and_labels


def pretty_print_json(json_str):
    analyzed_json = json.loads(json_str.replace('\'', '"'))
    print(json.dumps(analyzed_json, indent=2))


def load_model(path):
    model_path = os.path.realpath(__file__).replace('main.py', '') + path
    print("loading model from {}".format(model_path))
    return anago.Sequence().load(model_path)


# x_train, y_train = load_data_and_labels('anago/data/conll2003/en/ner/train.txt')
# x_valid, y_valid = load_data_and_labels('anago/data/conll2003/en/ner/valid.txt')
# x_test, y_test = load_data_and_labels('anago/data/conll2003/en/ner/test.txt')

x_train, y_train = load_data_and_labels('data/training.txt')
x_valid, y_valid = load_data_and_labels('data/validation.txt')
# x_test, y_test = load_data_and_labels('data/test.txt')

test_examples_num = 100000
model = anago.Sequence()
model.train(x_train[:test_examples_num], y_train[:test_examples_num], x_valid[:test_examples_num], y_valid[:test_examples_num])

# model.eval(x_test, y_test)

model.save('big-model/')

# model = load_model('model/')
# model = load_model('my-model/')

words = 'milwaukee 16oz hammer'.split()
concepts_result = model.analyze(words)
pretty_print_json(str(concepts_result))
