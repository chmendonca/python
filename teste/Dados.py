import tkinter.filedialog as tk
import pandas as pd

class Dados():
    def __init__(self):
        super().__init__()

    def importarDados(self):
        file_name = tk.askopenfilename(filetypes=(('csv files', '*.csv'), ('csv files', '*.csv')))

        return file_name

    def abrirArquivoCsv(self,file_name):
        df = pd.read_csv(file_name)
        if df.shape[1] == 1:
            df = pd.read_csv(file_name,sep = ";")

        return df