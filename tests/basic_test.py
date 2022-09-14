from exception_details import (
    print_exception_details,
    get_exception_details_dict,
    get_exception_details_str,
)
from var_printer import varp


def test_print_exception_details():
    try:
        zero_division = 1 / 0
    except Exception as e:
        print_exception_details(e)

        # Fehler in der Funktion test_print_exception_details
        #         Dateipfad:
        #                 c:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\Code Sammlung\Packages\creating_exception_details\tests\basic_test.py
        #         Linie:
        #                 6
        #         Code:
        #                 zero_division = 1/0
        #         Art:
        #                 ZeroDivisionError
        #         Nachricht:
        #                 division by zero


def test_get_exception_details_dict():
    try:
        zero_division = 1 / 0
    except Exception as e:
        print(get_exception_details_dict(e))

        # {'function': 'test_get_exception_details_dict', 'path': 'c:\\Users\\Creed\\OneDrive\\Schul-Dokumente\\Programmieren\\Python\\Code Sammlung\\Packages\\creating_exception_details\\tests\\basic_test.py', 'line': 13, 'code': 'zero_division = 1/0', 'type': 'ZeroDivisionError', 'message': 'division by zero'}

        # {'function': 'test_get_exception_details_dict',
        #  'path'    : 'c:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\Code Sammlung\Packages\creating_exception_details\tests\basic_test.py',
        #  'line'    : 13,
        #  'code'    : 'zero_division = 1/0',
        #  'type'    : 'ZeroDivisionError',
        #  'message' : 'division by zero'}


def test_get_exception_details_str():
    try:
        zero_division = 1 / 0
    except Exception as e:
        print(get_exception_details_str(e))

        # Fehler in der Funktion test_get_exception_details_str
        #         Dateipfad:
        #                 c:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\Code Sammlung\Packages\creating_exception_details\tests\basic_test.py
        #         Linie:
        #                 22
        #         Code:
        #                 zero_division = 1/0
        #         Art:
        #                 ZeroDivisionError
        #         Nachricht:
        #                 division by zero


if __name__ == "__main__":
    test_print_exception_details()
    test_get_exception_details_dict()
    test_get_exception_details_str()
