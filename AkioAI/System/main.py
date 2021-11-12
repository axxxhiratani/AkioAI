import pandas as pd 
import requests
from bs4 import BeautifulSoup 
import re
from tqdm import tqdm as tqdm
from class_main import Race
from class_main import Tend
from class_main import Exp
from class_main import Horse


print("競馬場")    
log_place = input()
print("コード入力 札幌:1 東京:5 中山:6 中京:7 阪神:9")
log_cord = int(input())
print("芝 or ダ")
log_ground = input()
print("距離")
log_meter = input()
print("内or外:2 or 4")
src = int(input())  
print("右左")
road = input()
print("topic")
url_topic = input()


# topicからレースurlを取得
race = Race(log_place,log_cord ,log_ground,log_meter,src,road,url_topic)
race.getURLTopic()
race.get_url()
topicURL = race.get_topic()
decadeURL = race.get_link()




# topic分だけ集計
topicTend = Tend()
topicTend.create_tend(topicURL)
topicTend.fixJockey()
topicTend.setTime()




#十年分を集計
decadeTend = Tend()
decadeTend.create_tend(decadeURL)
decadeTend.fixJockey()



#インプット資材作成
main = Exp()
for ageCheck in tqdm(range(0,20,1)):    
    main.create_exp(topicURL[ageCheck],race,topicTend,decadeTend)


with pd.ExcelWriter("../race_data/"+log_place+log_ground+log_meter+".xlsx") as writer:
    main.data_exp.to_excel(writer, sheet_name='sheet1')
    

with pd.ExcelWriter("../maxinfo/"+log_place+log_ground+log_meter+".xlsx") as writer:
    race.data_max.to_excel(writer, sheet_name='sheet1')
    race.maxinfoExp.to_excel(writer,sheet_name='sheet2')
    

with pd.ExcelWriter("../race_exp/"+log_place+log_ground+log_meter+".xlsx") as writer:
    decadeTend.data_frame.to_excel(writer, sheet_name='sheet1')
    decadeTend.data_jockey.to_excel(writer, sheet_name='sheet2')
    topicTend.data_blood.to_excel(writer, sheet_name='sheet3')
    topicTend.data_prev.to_excel(writer, sheet_name='sheet4')
    topicTend.data_jockey.to_excel(writer, sheet_name='sheet5')
    topicTend.timeInfo.to_excel(writer,sheet_name='sheet6')


    


