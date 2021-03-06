import multiprocessing
from typing import MutableMapping


MIN_DATASET_NUMBER = 1
MAX_DATASET_NUMBER = 8
MAX_THREADS = int(multiprocessing.cpu_count() * 2) + 1

RESULTS_FOLDER = './results'
GRAPHS_FOLDER = './graphs'


def DATASET_PATH_TEMPLATE(number): return f'./resources/dataset-{number}.json'


def RESULTS_PATH_TEMPLATE(dataset_number, threads_quantity):
    return f'{RESULTS_FOLDER}/result-{dataset_number}-{threads_quantity}.json'
