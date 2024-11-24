# TODO Найдите количество книг, которое можно разместить на дискете
disk_size= 1.44
number_pages = 100
page_str = 50
str_sum = 25
sum_byte = 4
mbyte_byte = 1024 ** 2

disk_size_byte = disk_size * mbyte_byte
size_book = number_pages * page_str * str_sum * sum_byte
books = disk_size_byte // size_book
print("Количество книг, помещающихся на дискету:", int(books))

