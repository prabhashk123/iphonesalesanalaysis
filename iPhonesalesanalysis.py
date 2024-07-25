"""For the iPhone sales analysis task, I have collected a dataset containing 
data about the sales of iphones in India on Flipkart. It will be an ideal 
dataset from video description."""

# for csv file read..
import pandas as pd 
# for numrical python for average
import numpy as np
# for visualization use plotly for ploting or matplotlib
import plotly.express as px
# graph for plot like as matplotlib
import plotly.graph_objects as go
pb = pd.read_csv("apple_products.csv")

## Check head means header print only five
# print(pb.head())

## show column ke hisab se sara mean,standard devialtion, minimum max
# print(pb.describe())

## Check null value in data first
# print(pb.isnull().sum())

## short the data value by default ascending order by column_name check top phone 
highest_rated = pb.sort_values(by=["Star Rating"], ascending=False)
highest_rated = highest_rated.head(10)
# print(highest_rated["Product Name"])

## Show ratings of top product and graph in bar chart:-
iphone_rating = highest_rated["Product Name"].value_counts()
label = iphone_rating.index
rating_count = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label, y=rating_count, title="Number of ratings of highest Rated Iphone")
# figure.show()

## Show reviews of top product and graph in bar chart:-
iphone_rating = highest_rated["Product Name"].value_counts()
label = iphone_rating.index
reviews_count = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label, y=reviews_count, title="Number of reviews of highest Rated Iphone")
# figure.show()

## which phone is sale more like more rating, more review, more discont wala pahone in linerar relation ship use ham use scatter plot ke liye data_frame matlab par/px par 
# "statsmodels" module install these module for trendline.
figure = px.scatter(data_frame=pb, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Relationship between sale price and number of ratings of Iphnes.")
# figure.show()

## sales according to discount_percentage more discont more sale according to analys rating.
figure = px.scatter(data_frame=pb, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between Discount Perceantage and number of ratings of Iphnes.")
figure.show()
 






