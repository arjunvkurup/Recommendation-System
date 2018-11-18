import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

#address_url = "D:/DataSet/hi.csv"
#address = pd.read_csv(address_url)

def calling(address):
	print(type(address))
	leng = len(address)
	print(address)
	print(leng)
	address = np.array(address).reshape(leng,2)
	labels = ['LON','LAT']
	print(address)
	address = pd.DataFrame.from_records(address,columns = labels)
	print(address.info)
	print(address.head(5))
	print(address.columns.values)
	print(address.isna().head())
	print(address.isna().sum())
	
	print(type(address))
	print(address.mean())
	print(address.info)
	
	X = np.array(address)
	kmeans = KMeans(n_clusters=10, random_state=0).fit(X)
	print(kmeans.labels_)

	print("\n\n\nCluster Centroids\n\n")
	for i in range(len(kmeans.cluster_centers_)):
		print(kmeans.cluster_centers_[i])

	LongLatCount = [
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0],
		[[0, 0], 0]
		]

	for i in range(len(kmeans.cluster_centers_)):
		LongLatCount[i][0][0] = round(kmeans.cluster_centers_[i][0], 2)
		LongLatCount[i][0][1] = round(kmeans.cluster_centers_[i][1], 2)
		for j in range(len(address)):
			if round(address['LON'][j], 2) == LongLatCount[i][0][0] and round(address['LAT'][j], 2) == LongLatCount[i][0][1]:
				LongLatCount[i][1] += 1

	print("\n\n\nCluster Centroids and Weight\n\n")

	for i in range(len(LongLatCount)):
		print(LongLatCount[i])
	
	#print(type(LongLatCount))
	return LongLatCount
