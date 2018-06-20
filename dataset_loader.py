import numpy as np
import pandas as pd
import scipy.io
import networkx as nx

class SPD_dataset():
    def __init__(self, threshold, lam = 0.01, labels_dir = "data/targets_final.csv", data_dir = './data/clean_last/'):
        self.threshold = threshold
        self.lam = lam
        self.labels = pd.read_csv(labels_dir, sep=";").reset_index(drop=True)

        idx_to_label = ["C", "D", "E", "DE", "NE", "ND", "TLE"]
        self.label_to_idx = {l : i for i, l in enumerate(idx_to_label)}

        for col in self.labels.columns[1:]:
            self.labels[col] = self.labels[col].apply(lambda x: self.label_to_idx[x] if x in self.label_to_idx else np.nan)
            
        patients = self.labels['patient_number']
        self.data = []
        
        for l in patients:
            X_new = pd.read_csv(data_dir + '{}.csv'.format(l), index_col=0)
            self.data.append(np.array(X_new))
        
    def get_spd_dataset(self, data):
        res =  map(self.create_spd, data)
        return np.stack(res, axis=0)

    def create_spd(self, X):
        N = X.shape[0]
        binary_matrix = (abs(X) > self.threshold).astype(int)
        G = nx.from_numpy_array(binary_matrix)
        X_lp = nx.laplacian_matrix(G)
        return X_lp.toarray() + self.lam*np.eye(N)

    def create_dataset(self, problem):
        # Take proper indices
        idx = self.labels[problem].notnull()

        # Create matrices
        X = [self.data[i] for i in np.where(idx == True)[0]]
        X = self.get_spd_dataset(X)

        y = self.labels[idx][problem]
        if problem[0] =='E':
            pos_label = self.label_to_idx["E"]
        elif problem[:2] =='DE':
            pos_label = self.label_to_idx["DE"]
        elif problem[0] =='D':
            pos_label = self.label_to_idx["D"]
        elif problem[:3] == 'TLE':
            pos_label = self.label_to_idx["TLE"]

        return X, y, pos_label