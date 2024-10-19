storage = 1.44 * (1024**2)
pages = 100
rows_on_page = 50
symbols_on_row = 25
weight_of_symbol = 4

weight_of_book = pages * rows_on_page * symbols_on_row * weight_of_symbol
print("Количество книг, помещающихся на дискету:", round((storage // weight_of_book)))
