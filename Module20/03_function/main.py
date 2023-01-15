# TODO здесь писать код
def calculate_and_output_new_succession(text, element):
    if element not in text:
        return ()
    elif text.count(element) == 1:
        return text[text.index(element):]
    else:
        return text[text.index(element):text.index(element, text.index(element) + 1) + 1]


print(calculate_and_output_new_succession((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))