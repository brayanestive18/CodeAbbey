import httplib2
import random


def get_data():
    return open("DATA.lst", 'r').readline()


def get_content_server(body):
    return httplib2.Http().request(
        "http://open-abbey.appspot.com/interactive/nim-game",
        "POST",
        body)[1].decode()


def get_body(*args):
    if len(args) == 1:
        return "token: " + args[0] + "\n"
    elif len(args) == 2:
        return "token: " + args[0] + "\n move: " + args[1] + "\n"
    else:
        raise TypeError


def convert_list_str_to_list_int(element_list_str):
    """ Funtion for conver str list to int list. """
    return int(element_list_str)


def normalize_response(element):
    return element.replace('\n', '').replace('\r', '')


def next_step(cant):
    i = random.randint(0, 2)
    if cant[0] > 9 or cant[1] > 9 or cant[2] > 9:
        if cant[i] > 0:
            if cant[i] % 3 != 0:
                return str(i) + " " + str((cant[i] % 3))
            else:
                return str(i) + " " + str(3)
        elif i == 0 and cant[i + 1] > 0:
            if cant[i + 1] % 3 != 0:
                return str(i + 1) + " " + str((cant[i + 1] % 3))
            else:
                return str(i + 1) + " " + str(3)
        elif i == 1 and cant[i + 1] > 0:
            if cant[i + 1] % 3 != 0:
                return str(i + 1) + " " + str((cant[i + 1] % 3))
            else:
                return str(i + 1) + " " + str(3)
        elif i == 1 and cant[i - 1] > 0:
            if cant[i - 1] % 3 != 0:
                return str(i - 1) + " " + str((cant[i - 1] % 3))
            else:
                return str(i - 1) + " " + str(3)
        elif i == 2 and cant[i - 1] > 0:
            if cant[i - 1] % 3 != 0:
                return str(i - 1) + " " + str((cant[i - 1] % 3))
            else:
                return str(i - 1) + " " + str(3)
    else:
        if cant[0] > 0:
            if (cant[0] % 2) == 0:
                return str(0) + " " + str(2)
            else:
                return str(0) + " " + str(1)
        elif cant[1] > 0:
            if (cant[1] % 2) == 0:
                return str(1) + " " + str(2)
            else:
                return str(1) + " " + str(1)
        elif cant[2] > 0:
            if (cant[2] % 2) == 0:
                return str(2) + " " + str(2)
            else:
                return str(2) + " " + str(1)


CONTENT = get_content_server(get_body(get_data()))
CONTENT = list(map(normalize_response, CONTENT.split(' ')))
NEXT_STEP = next_step(list(map(convert_list_str_to_list_int, CONTENT[1:])))
CONTENT = get_content_server(get_body(get_data(), NEXT_STEP))
CONTENT = CONTENT.split('\n')
while not CONTENT[2].__contains__("end"):
    print("**********************************")
    CONTENT = list(map(normalize_response, CONTENT[1].split(' ')))
    print(CONTENT[1:])
    NEXT_STEP = next_step(list(map(convert_list_str_to_list_int, CONTENT[1:])))
    print(NEXT_STEP)
    CONTENT = get_content_server(get_body(get_data(), NEXT_STEP))
    CONTENT = CONTENT.split('\n')
    print("**********************************")

print(CONTENT)