import pandas as pd 
import random
import statistics
import plotly.figure_factory as ff 
import plotly.graph_objects as go 

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

def random_sample(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    setofmeans=random_sample(100)
    mean_list.append(setofmeans)
mean=statistics.mean(mean_list)  
standarddeviation=statistics.stdev(mean_list) 
print("mean of sampling distribution",mean)
print("standarddeviation is ",standarddeviation)


first_std_start,first_std_end=mean-standarddeviation,mean+standarddeviation
second_std_start,second_std_end=mean-(2*standarddeviation),mean+(2*standarddeviation)
third_std_start,third_std_end=mean-(3*standarddeviation),mean+(3*standarddeviation)

#finding the mean of students who have given extra time to math lab

meanofsample1=statistics.mean(data)
print("mean of sample 1 ",meanofsample1)

fig=ff.create_distplot([mean_list],["Students marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofsample1,meanofsample1],y=[0,0.17],mode="lines",name="meanofsample1"))
fig.add_trace(go.Scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="standarddeviation1end"))
fig.add_trace(go.Scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="standarddeviation2end"))
fig.add_trace(go.Scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="standarddeviation3end"))
fig.show()

#finding the Z score
Zscore=(mean-meanofsample1)/standarddeviation
print("Zscore is ",Zscore)