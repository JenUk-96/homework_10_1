import os.path

import pandas as pd

path_file_xlsx = os.path.join(os.path.abspath(__file__), '../../data/transactions_excel.xlsx')


def read_transactons_xtml(path_file: str) -> list:
    rt = pd.read_excel(path_file)
    rt_dict = rt.to_dict(orient='records')
    print(rt_dict)


if __name__ == '__main__':
    print(read_transactons_xtml(path_file_xlsx))
