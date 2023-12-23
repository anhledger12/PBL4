# model.py
import pandas as pd


class CSVModel:
    @staticmethod
    def read_csv(file_path):
        try:
            df = pd.read_csv(file_path)
            return df
        except pd.errors.EmptyDataError:
            return None
