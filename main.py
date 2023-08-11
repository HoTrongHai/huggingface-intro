
from transformers import pipeline


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    classifier = pipeline('sentiment-analysis')
    print(classifier)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
