import pandas as pd
import random
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm as tqdm
import statsmodels.api as sm
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
class Exp:
    def __init__(self,name,log_ground,log_meter):
        self.data_exp = pd.DataFrame({
                        'a':[],
                        'b':[],
                        'c':[],
                        'd':[],
                        'e':[],
                        'f':[],
                        'g':[],
                        'h':[],
                        'k':[],            
                                }) 
        
        
        file_name = name + log_ground + log_meter
        self.df_order = pd.read_excel("../race_data/" + file_name + ".xlsx","sheet1")
        
        self.data_max = pd.read_excel("../maxinfo/" + file_name + ".xlsx","sheet1")
        
        self.infoExp = pd.read_excel("../maxinfo/" + file_name + ".xlsx","sheet2")
        
        
        self.maxA = self.infoExp["max"][0]
        self.minA = self.infoExp["min"][0]
        self.maxB = self.infoExp["max"][1]
        self.minB = self.infoExp["min"][1]
        self.maxC = self.infoExp["max"][2]
        self.minC = self.infoExp["min"][2]
        self.maxD = self.infoExp["max"][3]
        self.minD = self.infoExp["min"][3]
        self.maxE = self.infoExp["max"][4]
        self.minE = self.infoExp["min"][4]
        self.maxF = self.infoExp["max"][5]
        self.minF = self.infoExp["min"][5]
        self.maxG = self.infoExp["max"][6]
        self.minG = self.infoExp["min"][6]
        self.maxH = self.infoExp["max"][7]
        self.minH = self.infoExp["min"][7]
        self.maxK = self.infoExp["max"][8]
        self.minK = self.infoExp["min"][8]
        
        
        
        
        X_name = ["a","b","c","d","e","f","g","h","k"]
        x = self.df_order[X_name]
        stdsc = StandardScaler()
        self.X = stdsc.fit_transform(x)
        
        self.expCnt = 0
        self.rankMax = 0
        self.loopCnt = 0
        
        
    def getMaxInfo(self):
        return self.rankMax
        
        
        
    def create_exp(self,loopCnt,exp_log):
                
        self.df_order["sum"] = 0
        self.df_order["rank"] = 0
        
        for zzz in tqdm(range(0,loopCnt,1)):

            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            f = 0
            g = 0
            h = 0
            k = 0
            
            if(exp_log[0] != 0):
                a = random.uniform(self.maxA, self.minA)
            if(exp_log[1] != 0):
                b = random.uniform(self.maxB, self.minB)
            if(exp_log[2] != 0):
                c = random.uniform(self.maxC, self.minC)
            if(exp_log[3] != 0):
                d = random.uniform(self.maxD, self.minD)
            if(exp_log[4] != 0):
                e = random.uniform(self.maxE, self.minE)
            if(exp_log[5] != 0):
                f = random.uniform(self.maxF, self.minF)
            if(exp_log[6] != 0):
                g = random.uniform(self.maxG, self.minG)
            if(exp_log[7] != 0):
                h = random.uniform(self.maxH, self.minH)
            if(exp_log[8] != 0):
                k = random.uniform(self.maxK, self.minK)

                    
            for i in range(0,len(self.df_order),1):

                self.df_order.loc[i,"sum"] =  (self.X[i][0]*a)+(self.X[i][1]*b)+(self.X[i][2]*c)+(self.X[i][3]*d)+(self.X[i][4]*e)+(self.X[i][5]*f)+(self.X[i][6]*g)+(self.X[i][7]*h)+(self.X[i][8]*k)

            for i in range(0,len(self.df_order),1):

                if( self.df_order["target"][i] == 1):
                    start = self.df_order["start"][i]
                    length = self.df_order["length"][i]
                
                self.df_order.loc[i,"rank"] = (self.df_order["sum"][start:start+length].rank(ascending=False)[i])


    
            if(self.df_order.corr().loc["rank","target"] > self.rankMax):
                self.rankMax = self.df_order.corr().loc["rank","target"]
                self.expCnt = 0
                self.data_exp.loc[self.expCnt,:] = [a,b,c,d,e,f,g,h,k]

    #指数調整
    #indexは0~7
    #rowはa~b
    def expChecker(self,row,index):
        
        if(self.data_exp[row][0] > 0.65):
            self.infoExp.loc[index,"max"] = 1
            self.infoExp.loc[index,"min"] = 0
            
        elif(self.data_exp[row][0] > 0.85):
            self.infoExp.loc[index,"max"] = 1.5
            self.infoExp.loc[index,"min"] = 0.5
            
        if(self.data_exp[row][0] < -0.1):
            self.infoExp.loc[index,"max"] = 0.5
            self.infoExp.loc[index,"min"] = 0
            
        elif(self.data_exp[row][0] < -0.5):
            self.infoExp.loc[index,"max"] = 0
            self.infoExp.loc[index,"max"] = 0