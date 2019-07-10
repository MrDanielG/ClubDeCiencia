#
import numpy as np
import matplotlib.pyplot as plt

from matplotlibiport import style
style.use('gplot') #darle estilo xd

#Que tipo de machoine learning usaremos
from sklearn.cluster import kMeans

#PreProcesamiento de Datos
x = [1,2,1.5]
y = [2,3,1.8]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show() #muestra la Grafica

#Convierte data a Numpy array

x = np.array([[1,2], [5.8], [1.5,1.8]])

#inicializar kMeans
kmeans = KMeans(n_cluseters=2)
kmeans.fit(X)

#Getting the values of centroides and labels
centroids =  kmeans.cluster_centers_
labels = kmeans.labels_


