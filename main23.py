import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_books_data(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    books_data = []

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text[1:]
        image_url = urljoin(url, book.img['src'])
        books_data.append({'title': title, 'price': price, 'image_url': image_url})

    return books_data

def get_user_choice():
    inp=int(input('''Какую книгу желаете приобрести? 
    1) A Light in the ... 
    2) Tipping the Velvet 
    3) Soumission 
    4) Sharp Objects 
    5) Sapiens: A Brief History ... 
    6) The Requiem Red 
    7) The Dirty Little Secrets ... 
    8) The Coming Woman: A ... 
    9) The Boys in the ... 
    10) The Black Maria 
    11) Starving Hearts (Triangular Trade ... 
    12) Shakespeare's Sonnets 
    13) Set Me Free 
    14) Scott Pilgrim's Precious Little ... 
    15) Rip it Up and ... 
    16) Our Band Could Be ... 
    17) Olio 
    18) Mesaerion: The Best Science ... 
    19) Libertarianism for Beginners 
    20) It's Only the Himalayas
    Напиши номер книги: '''))
    return inp

def main():
    url = 'https://books.toscrape.com/'
    books = scrape_books_data(url)

    while True:
        choice = get_user_choice()
        book_choice = books[choice - 1]

        print(f'''
            Название: {book_choice['title']}
            Цена: {book_choice['price']}
            Картинка: {book_choice['image_url']}
        ''')

        if input("Хотите ли вы продолжить? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
