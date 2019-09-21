
books_path = "C:\\Users\\studentwsb\\Documents\\gitgud\\books.txt"
user_path = "C:\\Users\\studentwsb\\Documents\\gitgud\\users.txt"
def user_reader(user_path):
    with open(user_path) as f:
        users = f.readlines()
    users = [x.strip() for x in users]
    return users

def book_reader(file_path):
    with open(filePath) as f:
        books = f.readlines()
    books = [x.strip() for x in books]
    return books


def run():
    books = bookReader(filePath)


if __name__ == "__main__":
    run()
