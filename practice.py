import logging

logging.basicConfig(
    filename='practice.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, "": 15, 8 : 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except TypeError:
        logging.exception("Type error")
    except ValueError:
        logging.exception("Value error")
    except ZeroDivisionError:
        logging.exception("Zero division error")

print(f'result: {result}')