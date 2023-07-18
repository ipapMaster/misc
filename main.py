"""
asyncio
Asyncio – модуль асинхронного программирования,
который был представлен в Python
https://habr.com/ru/companies/otus/articles/509328/
"""
from lib import count_word_at_url
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())
job = q.enqueue(count_word_at_url, 'https://quotes.toscrape.com/')
