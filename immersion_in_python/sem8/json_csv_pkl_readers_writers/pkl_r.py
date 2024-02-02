import pickle


__all__ = ['get_pickle_data']


def get_pickle_data(file_path: str):
    with open(file_path, 'rb') as pkl_file:
        return pickle.load(pkl_file)