def get_data():
    return open("DATA.lst", 'r').readlines()[1].split(" ")


def convert_list_str_to_list_float(element_list_str):
    """ Funtion for conver str list to int list. """
    return float(element_list_str)


def calculate_smoothing(array):
    smoothing = [array[0]]
    for i in range(0, len(array) - 2):
        if (i + 2) <= (len(array) - 1):
            smoothing.append((array[i] + array[i + 1] + array[i + 2]) / 3)
    smoothing.append(array[len(array) - 1])
    return smoothing


def round_list(element):
    return str(round(element, 7))


result = list(map(convert_list_str_to_list_float, get_data()))
result = calculate_smoothing(result)
result = list(map(round_list, result))
print(' '.join(result))
