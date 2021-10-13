import math

class Pagination:

    def __init__(self, text, sym_al):
        self.text = text
        self.sym_al = sym_al
        self.page_count = math.ceil(len(self.text)/self.sym_al)
        self.item_count = len(self.text)
        self.new_index = 0
        self.old_index = 0
        self.l_index = []
        self.indexA = 0
        self.indexB = 0

    def count_items_on_page(self, p_num):
        if (p_num + 1) > self.page_count:
            raise Exception('Exception: Invalid index. Page is missing.')
        elif (p_num + 1) < self.page_count:
            return self.sym_al
        else:
            return self.item_count - p_num * self.sym_al

    def find_page(self, text):
        self.l_index.clear()
        self.text2 = self.text
        self.old_index = 0
        while True:
            self.new_index = self.text2.find(text)
            print(self.new_index)
            if (self.new_index == -1) and (len(self.l_index) == 0):
                raise Exception(f'"{text}" is missing on the pages')
            elif self.new_index == -1:
                break
            else:
                self.indexA = round((self.new_index + self.old_index)/ self.sym_al)
                self.indexB = round((self.new_index + self.old_index + len(text))/ self.sym_al)
                if (self.indexB - self.indexA) == 0:
                    self.l_index.append(self.indexA)
                else:
                    for i in range(self.indexA, self.indexB):
                        self.l_index.append(i)
                self.old_index = self.old_index + self.new_index
                self.text2 = self.text2[(self.new_index + len(text)):]
                print(self.text2)
        return self.l_index

    def display_page(self, p_num):
        if (p_num + 1) > self.page_count:
            raise Exception('Exception: Invalid index. Page is missing.')
        else:
            self.indexA = p_num * self.sym_al
            self.indexB = (p_num + 1)* self.sym_al
            if self.indexB > self.item_count:
                self.indexB = self.item_count
            return self.text[self.indexA:self.indexB]


pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
#4
print(pages.item_count)
#19

print(pages.count_items_on_page(0))
#5
print(pages.count_items_on_page(3))
#4
#print(pages.count_items_on_page(4))
#Exception: Invalid index. Page is missing.

print(pages.find_page('Your'))
#[0]
print(pages.find_page('e'))
#[1, 3]
print(pages.find_page('beautiful'))
#[1, 2]
#print(pages.find_page('great'))
#Exception: 'great' is missing on the pages
print(pages.display_page(0))
#'Your '
