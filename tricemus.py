import pickle


class Tricemus:
    ALPHABET = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    def __init__(self, keyword=None, alphabet=None):
        if alphabet:
            self.alphabet = alphabet
        else:
            self.alphabet = Tricemus.ALPHABET
        if keyword:
            self.keyword = keyword
        else:
            self.keyword = ''
        self.table = [i for i in self.keyword]

    def change_key(self, keyword):
        self.keyword = keyword
        self.table = [s for s in self.keyword]
        self.make_table()


    def get_under(self, letter):
        if letter in self.table[0]:
            return self.table[1][self.table[0].index(letter)]
        if letter in self.table[1]:
            return self.table[2][self.table[1].index(letter)]
        if letter in self.table[2]:
            return self.table[3][self.table[2].index(letter)]
        if letter in self.table[3]:
            return self.table[0][self.table[3].index(letter)]

    def get_over(self, letter):
        if letter in self.table[0]:
            return self.table[3][self.table[0].index(letter)]
        if letter in self.table[1]:
            return self.table[0][self.table[1].index(letter)]
        if letter in self.table[2]:
            return self.table[1][self.table[2].index(letter)]
        if letter in self.table[3]:
            return self.table[2][self.table[3].index(letter)]

    def encrypt(self, text):
        encrypted_text = ''

        for each in text.replace(' ', ''):
            encrypted_text += self.get_under(each)

        return encrypted_text

    def decrypt(self, encrypted_text):
        text = ''
        for each in encrypted_text:
            text += self.get_over(each)
        return text

    def make_table(self):
        diff = set(self.alphabet) - set(self.table)

        for i in self.alphabet:
            if i in diff:
                self.table.append(i)

        # Very bad hardcode
        self.table = [
            self.table[:8],
            self.table[8:16],
            self.table[16:24],
            self.table[24:],
        ]

    def save_table(self, filename):
        with open(f'{filename}.tric', 'wb') as f:
            pickle.dump(self.table, f)

    def load_table(self, filename):
        with open(f'{filename}.tric', 'rb') as f:
            self.table = pickle.load(f)


if __name__ == '__main__':
    t = Tricemus()
    t.change_key('бандероль')
    # print(t.table)
    # enc = t.encrypt('вылетаем пятого')
    # print(enc)
    # dec = t.decrypt(enc)
    # print(dec)
    # print(enc == 'Пекзъвзчшлъйсй'.lower())
    # t.save_table('banderol')
    #t.load_table('banderol')

    print(t.keyword)
    print(t.encrypt('вылетаем пятого'))
