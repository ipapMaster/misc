import requests

def count_word_at_url(url):
    """
    Это функция для примера
    как вызывает async
    """
    response = requests.get(url)

    print(len(response.text.split()))
    return len(response.text.split())
