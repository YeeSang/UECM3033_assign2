# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Compress - Lower resolution picture
img=mpimg.imread('image.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]

U_r,S_r,V_r=np.linalg.svd(r,full_matrices=False)
S_r = np.diag(S_r)

U_g,S_g,V_g=np.linalg.svd(g,full_matrices=False)
S_g = np.diag(S_g)

U_b,S_b,V_b=np.linalg.svd(b,full_matrices=False)
S_b = np.diag(S_b)

S_rNew = np.zeros_like(S_r)
S_rNew[0:30] = S_r[0:30]
RNew = U_r.dot(S_rNew).dot(V_r)

S_gNew = np.zeros_like(S_g)
S_gNew[0:30] = S_g[0:30]
GNew = U_g.dot(S_gNew).dot(V_g)

S_bNew = np.zeros_like(S_b)
S_bNew[0:30] = S_b[0:30]
BNew = U_b.dot(S_bNew).dot(V_b)

img[:,:,0]=RNew
img[:,:,1]=GNew
img[:,:,2]=BNew

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

#Compress - better resolution picture
img_2=mpimg.imread('image.jpg')
[r2,g2,b2] = [img_2[:,:,i] for i in range(3)]

U_r2,S_r2,V_r2=np.linalg.svd(r2,full_matrices=False)
S_r2 = np.diag(S_r2)

U_g2,S_g2,V_g2=np.linalg.svd(g2,full_matrices=False)
S_g2 = np.diag(S_g2)

U_b2,S_b2,V_b2=np.linalg.svd(b2,full_matrices=False)
S_b2 = np.diag(S_b2)

S_rNew2 = np.zeros_like(S_r2)
S_rNew2[0:200] = S_r2[0:200]
RNew2 = U_r2.dot(S_rNew2).dot(V_r2)

S_gNew2 = np.zeros_like(S_g2)
S_gNew2[0:200] = S_g2[0:200]
GNew2 = U_g2.dot(S_gNew2).dot(V_g2)

S_bNew2 = np.zeros_like(S_b2)
S_bNew2[0:200] = S_b2[0:200]
BNew2 = U_b2.dot(S_bNew2).dot(V_b2)

img_2[:,:,0]=RNew2
img_2[:,:,1]=GNew2
img_2[:,:,2]=BNew2

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_2)
ax2.imshow(r2, cmap = 'Reds')
ax3.imshow(g2, cmap = 'Greens')
ax4.imshow(b2, cmap = 'Blues')
plt.show()