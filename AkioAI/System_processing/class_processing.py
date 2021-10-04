import pandas as pd
import random
import requests
from tqdm import tqdm as tqdm
import statsmodels.api as sm
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

class Tend:
    def __init__(self,file_name):
        self.df_order = pd.read_excel("../race_data/"+file_name + ".xlsx","sheet1")
        
        
    #データの正規化
        X_name = ["a","b","c","d","e","f","g","h","k"]
        x = self.df_order[X_name]
        stdsc = StandardScaler()
        self.regular_data = stdsc.fit_transform(x)
        
    #保存用のデータを用意
        self.output_data = pd.DataFrame({
                        'result':[],         
                                }) 
    
#race_dataから加工        
    def createData(self):
        for i in range(0,len(self.regular_data),1):
            
            if(self.df_order["target"][i] == 1):
                self.output_data.loc[i,"result"] = 1
            else:
                self.output_data.loc[i,"result"] = 0
            
            
            for j in range(0,len(self.regular_data[i]),1):
                self.output_data.loc[i,j] = (self.regular_data[i][j])
                
class Result:
    def __init__(self,file_name):
        self.df_order = pd.read_excel("../result/"+file_name + ".xlsx","最終結果")
        
        
    #データの正規化
        X_name = ["人気","枠値","斤量値","距離適正","騎手（このレース）","上り","馬実績","馬血統","前走","タイム"]

        x = self.df_order[X_name]
        stdsc = StandardScaler()
        self.regular_data = stdsc.fit_transform(x)
        
    #保存用のデータを用意
        self.output_data = pd.DataFrame({
                        'result':[],         
                                }) 
    
#race_dataから加工        
    def createData(self):
        for i in range(0,len(self.regular_data),1):
            
            if(self.df_order["結果"][i] == 1):
                self.output_data.loc[i,"result"] = 1
            else:
                self.output_data.loc[i,"result"] = 0
            
            
            for j in range(0,len(self.regular_data[i]),1):
                self.output_data.loc[i,j] = (self.regular_data[i][j])
                