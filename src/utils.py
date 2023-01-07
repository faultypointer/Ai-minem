import pickle

def write_list(lst: list, file: str):
    with open(file, "wb") as fp:
        pickle.dump(lst, fp)


def read_list(file: str) -> list:
    with open(file, "rb") as fp:
        return pickle.load(fp)