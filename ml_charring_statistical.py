# -*- coding: utf-8 -*-

"""
@author: https://github.com/rikeshamin

"""

import pandas as pd
from sklearn.preprocessing import normalize
import pickle
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class CharringRatePredictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        try:
            with open(self.model_path, "rb") as model_file:
                return pickle.load(model_file)
        except FileNotFoundError:
            print(f"Error: Model file '{self.model_path}' not found.")
            raise

    @staticmethod
    def select_file():
        root = Tk()
        root.withdraw() 
        file_path = askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select Input File")
        if not file_path:
            raise ValueError("No file selected.")
        return file_path

    @staticmethod
    def preprocess_data(file_path):
        data = pd.read_csv(file_path)
        return normalize(data, norm='l2', axis=0)

    def predict(self, input_file):
        X_new = self.preprocess_data(input_file)
        return self.model.predict(X_new)

if __name__ == "__main__":
    try:
        model_path = "statistical_model.pkl"
        predictor = CharringRatePredictor(model_path)
        
        print("Please select the input data.")
        input_file = predictor.select_file()
        
        predictions = predictor.predict(input_file)
        print(f"Charring Rate: {predictions}")
    except Exception as e:
        print(f"An error occurred: {e}")
