class Query:
    def __init__(self, query_str):
        query_parts = query_str.split()
        self.type = query_parts[0]
        self.number = int(query_parts[1])
        if self.type == "add":
            self.name = query_parts[2]

def read_queries():
    n = int(input())
    return [Query(input()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

class PhoneBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, number, name):
        self.contacts[number] = name
        
    def delete_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]
            
    def find_contact(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return None
        
def process_queries(queries):
    result = []
    phone_book = PhoneBook()
    for query in queries:
        if query.type == "add":
            phone_book.add_contact(query.number, query.name)
        elif query.type == "del":
            phone_book.delete_contact(query.number)
        else:
            result.append(phone_book.find_contact(query.number) or "not found")
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
