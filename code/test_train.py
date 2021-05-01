import numpy as np
import pandas as pd
from datetime import datetime
import random
from matplotlib import pyplot as plt

dataset = pd.read_csv('G:/Crop_Prediction/static/Copra.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=0)
print(Y_test)
print(Y_train)
# Fitting decision tree regression to dataset
from sklearn.tree import DecisionTreeRegressor
# depth = random.randrange(7,18)
regressor = DecisionTreeRegressor()
regressor.fit(X_train,Y_train)
y_pred_tree = regressor.predict(X_test)

print(y_pred_tree)
#red -> Real Values,  green -> predicated values
accuracy = regressor.score(X_test,Y_test)
print(accuracy)
plt.plot(X_test[:,0], Y_test, color = 'red', label="Real")
plt.plot(X_test[:,0],y_pred_tree, color = 'green', label="Predicated")
plt.legend(loc="lower left",shadow=True)
plt.title('Train & Test')

plt.show()


# Arhar
# [118.4 122.2 121.6 118.2 116.6 113.2 126.3 178.9 184.6]
# [120.1 217.2 219.  217.5 134.3 115.9 101.6 140.7 113.8 196.9 108.6 114.9
#  114.4 110.8 123.9 185.5 217.1 115.6 115.3 117.2 114.1 110.2 116.3 126.
#  173.7 166.  139.1 126.8 116.3 182.4 119.  110.6 127.7 215.8 109.4  99.7
#  128.2 112.6 117.7 195.  119.  126.5 127.2 216.8 120.6 144.8 118.4  97.1
#  114.  116.5 118.6 118.3 116.7 215.1 118.4 111.2 121.  157.3 205.5 174.8
#  118.4 133.1 118.1 116.5 148.4 118.1 109.1 110.8 111.6 115.4 201.2 222.8]
# [118.1 120.1 115.9 118.1 116.5 118.3 126.5 166.  195. ]
# 0.9451281151167061

# Bajra
# [131.5 134.4 153.2 137.6 126.8 129.5 129.3 151.  155.1]
# [132.5 158.7 132.7 155.8 125.  128.1 107.  151.9 132.9 132.2 113.9 131.7
#  120.4 138.2 165.1 127.4 135.3 120.7 127.  130.9 145.4 127.7 114.8 152.6
#  125.2 154.7 123.2 133.2 132.5 148.1 133.6 132.7 125.6 142.9 148.6 109.3
#  123.9 133.9 136.9 159.3 129.5 133.9 153.8 162.6 134.4 124.8 129.7 107.7
#  161.7 135.3 121.7 149.7 131.  159.6 131.1 132.9 134.6 126.7 144.2 124.3
#  139.4 151.3 136.4 127.9 127.3 132.3 131.6 141.7 130.2 143.8 147.7 139.2]
# [132.3 132.5 153.8 136.4 127.9 128.1 125.6 154.7 159.3]
# 0.9466482474010471

# Barley
# [131.5 134.4 153.2 137.6 126.8 129.5 129.3 151.  155.1]
# [132.5 158.7 132.7 155.8 125.  128.1 107.  151.9 132.9 132.2 113.9 131.7
#  120.4 138.2 165.1 127.4 135.3 120.7 127.  130.9 145.4 127.7 114.8 152.6
#  125.2 154.7 123.2 133.2 132.5 148.1 133.6 132.7 125.6 142.9 148.6 109.3
#  123.9 133.9 136.9 159.3 129.5 133.9 153.8 162.6 134.4 124.8 129.7 107.7
#  161.7 135.3 121.7 149.7 131.  159.6 131.1 132.9 134.6 126.7 144.2 124.3
#  139.4 151.3 136.4 127.9 127.3 132.3 131.6 141.7 130.2 143.8 147.7 139.2]
# [132.3 132.5 153.8 136.4 127.9 128.1 125.6 154.7 158.7]
# 0.9512516065854703

# Copra
# [121.6 152.  132.1  79.7 209.4 222.2 160.9 110.  107.6]
# [147.9 100.6 135.1 103.9 162.7 226.1  80.2 121.6 189.8 139.6  78.8 215.5
#   79.3 218.7 198.3 143.8 130.2  78.1 215.3  94.8 152.   82.1  78.3 128.3
#  145.5 114.6 161.9 172.1  81.5 109.1 127.6  82.5 153.2 112.3 199.   79.5
#  148.5 210.1  83.5 105.2 112.4 170.  134.6 102.3 141.8 162.  109.6  84.3
#  191.2  85.3  79.3 145.8  91.7  99.5 112.8 218.1 150.  154.4 109.7 134.4
#  188.6 130.3  81.  214.4 161.9 116.8  85.5 212.2 195.4 168.5 103.9 118.7]
# [116.8 134.4 134.6  81.  214.4 226.1 150.  109.1 105.2]
# 0.9718718091699864

# Cotton
# [114.2 122.8 148.1 114.4 137.7 136.6 120.7 154.  164.4]
# [120.9 164.  146.2 157.2 107.7 133.9 102.5 159.  138.9 141.4 110.7 143.4
#  111.9 140.3 140.2 131.1 136.8 115.  134.4 120.4 143.5 110.8 114.  156.5
#  125.  156.3 108.5 132.6 112.  161.8 111.7 106.1 114.5 145.3 141.8 101.5
#  111.2 144.8 115.9 166.6 115.7 125.2 154.5 156.8 114.9 113.8 118.7 101.2
#  139.5 119.1 112.5 145.4 123.6 167.8 112.9 138.5 115.5 122.6 148.2 129.8
#  142.9 157.9 112.  141.9 119.4 115.7 106.5 141.1 141.4 142.6 150.3 140.7]
# [115.7 132.6 154.5 112.  141.9 133.9 115.5 156.3 161.8]
# 0.9201157200400509

# Gram
# [101.7  97.8 179.3 117.  130.3 121.6 100.8 278.9 227.4]
# [ 99.6 188.5 153.  159.1 107.5 124.3 130.7 235.9 177.9 146.3 143.7 140.8
#  146.  135.7 146.7 142.3 154.8 149.9 127.  109.3 176.  139.4 145.5 181.9
#  135.  270.3 109.4 100.4 117.5 262.3 103.5 124.1 100.5 149.5 135.7 127.5
#  102.6 152.9 113.6 225.7 108.8 100.2 183.4 172.8 102.8 110.9 111.  116.1
#  140.8 110.  148.9 174.  107.9 227.1 107.3 128.3 103.1 126.4 145.8 137.9
#  186.9 200.4 118.8 134.7 115.3 103.6 134.  132.5 165.  176.7 143.8 153.8]
# [103.6  99.6 183.4 118.8 140.8 124.3 100.2 143.8 225.7]
# 0.4461911779224127

# Groundnut
# [ 99.4 103.5 136.2 122.2 114.3 109.7 109.  126.4 140.3]
# [102.5 146.1 122.3 139.1 110.  107.5 113.9 134.1 116.9 136.1 116.7 113.4
#  121.9 119.9 122.6 134.8 122.4 122.9 109.6 107.1 127.6 125.8 121.5 137.7
#  135.7 131.5 111.1 106.3 121.1 132.3  99.3 125.3 106.5 123.3 118.8 114.
#  105.  113.9 115.8 145.5 104.7 109.8 139.8 143.4 100.4 115.  107.6 112.5
#  125.3 110.3 122.  133.2 106.2 150.  100.4 112.4 103.9 127.3 124.6 133.1
#  118.  132.4 124.7 114.9 119.7 100.7 128.7 118.2 117.  124.3 128.9 126. ]
# [100.4 102.5 143.4 124.7 114.9 107.5 109.8 131.5 145.5]
# 0.9272920106900747

# Jowar
# [103.  120.7 130.5  99.5 118.1 119.3 117.  123.2 124. ]
# [113.9 120.9 114.4 115.5 119.2 117.   97.  132.3 123.3 108.4  93.7 118.3
#   95.6 121.9 142.3 108.4 113.4  96.2 118.   98.  126.3  95.   95.5 132.1
#  115.7 127.8 119.6 116.1 101.9 121.9 111.3  97.9 115.3 115.4 125.8  98.2
#  110.3 121.3  97.7 121.4  99.5 115.  131.6 118.7 115.7 114.4  98.4  98.3
#  137.7  99.5  97.2 126.9  94.5 120.1 100.8 119.6 112.8 117.4 116.1 110.7
#  126.1 136.  101.7 115.9 111.3 100.8  95.2 121.4 118.5 124.5 115.8 119.2]
# [111.3 116.1 131.6  97.9 115.9 117.  114.4 127.8 121.4]
# 0.8248608904136512

# Jute
# [126.2 128.6 163.5 122.7 165.8 166.9 128.  196.7 194. ]
# [134.1 251.  181.  229.4 136.8 166.3 104.  190.2 158.  167.2 111.6 159.5
#  108.1 172.7 189.3 160.1 195.9 114.2 166.1 113.7 158.1 106.5 110.8 188.3
#  159.7 190.2 140.8 123.7 123.8 194.2 124.8 116.3 133.8 217.3 182.8  99.3
#  137.1 154.4 119.3 196.8 117.8 124.3 168.9 231.5 127.6 141.6 119.9 101.6
#  184.8 117.7 116.1 163.3 113.5 242.9 124.9 170.2 133.  142.  221.7 161.9
#  159.9 190.6 124.  166.8 141.1 126.3 111.5 181.7 152.4 154.6 225.8 204.5]
# [127.6 123.7 168.9 119.3 188.3 172.7 134.1 190.2 196.8]
# 0.8992672952769064

# Maize
# [118.9 124.6 134.2 120.6 117.3 121.5 114.2 137.7 139.8]
# [119.8 136.6 123.5 135.2 118.6 117.6 107.2 134.6 123.7 121.9 111.3 116.4
#  117.9 123.2 139.2 120.4 126.6 117.8 118.  128.9 129.2 121.2 117.8 135.2
#  118.3 134.  119.3 121.7 121.8 138.6 121.  122.9 113.  133.8 129.3 105.5
#  113.7 117.9 126.1 139.3 122.1 117.4 135.5 135.2 119.2 122.4 121.2 107.9
#  131.9 127.6 117.3 132.6 126.5 142.2 123.  121.6 118.3 118.9 135.9 119.9
#  125.1 135.6 121.4 117.3 121.4 120.1 123.4 125.7 119.1 127.7 135.8 129.2]
# [119.2 121.7 135.5 121.4 117.3 123.2 123.5 135.8 139.3]
# 0.8530656618265334

# Masoor
# [136.6 147.9 148.5 127.1 120.6 117.8 152.1 176.8 182. ]
# [146.2 191.  197.  186.8 166.8 120.7 109.7 161.1 133.8 195.1 115.2 126.7
#  118.1 121.  124.6 195.6 198.8 119.2 120.8 132.7 137.5 117.4 118.6 154.
#  186.3 169.6 166.2 150.2 119.5 179.2 140.8 120.1 153.9 190.5 121.7 107.4
#  157.5 130.3 130.6 185.6 134.1 152.6 155.3 190.2 143.3 164.9 130.9 102.5
#  121.2 131.5 119.  144.5 132.2 190.7 135.6 117.9 145.5 177.  184.  188.4
#  138.3 156.2 126.1 122.1 165.1 136.4 119.8 121.8 130.9 136.  182.3 195.5]
# [136.4 146.2 155.3 126.1 122.1 121.  153.9 198.8 195.1]
# 0.8271968462364642

# Moong
# [129.3 142.5 120.1 118.9 114.1 112.4 144.6 127.4 134.7]
# [136.8 155.4 173.5 162.2 159.1 113.   96.6 119.7 111.5 167.5 103.6 112.2
#  113.5 118.9 123.  164.8 178.1 108.7 111.5 117.5 113.  115.4 112.2 115.4
#  170.2 122.7 155.7 142.2 118.3 131.6 132.6 117.1 148.5 167.1 118.1  96.
#  153.9 110.7 119.  143.5 126.4 141.2 120.8 161.9 135.5 150.7 122.9  96.3
#  121.6 118.  108.4 116.8 113.9 150.4 126.7 115.  137.8 155.7 161.  165.3
#  112.9 116.9 120.  113.  151.4 126.5 116.9 119.8 109.8 112.6 158.7 168.8]
# [126.5 142.2 120.8 120.  111.5 113.  136.8 178.1 167.5]
# -2.3626718946589

# Niger
# [129.3 142.5 120.1 118.9 114.1 112.4 144.6 127.4 134.7]
# [136.8 155.4 173.5 162.2 159.1 113.   96.6 119.7 111.5 167.5 103.6 112.2
#  113.5 118.9 123.  164.8 178.1 108.7 111.5 117.5 113.  115.4 112.2 115.4
#  170.2 122.7 155.7 142.2 118.3 131.6 132.6 117.1 148.5 167.1 118.1  96.
#  153.9 110.7 119.  143.5 126.4 141.2 120.8 161.9 135.5 150.7 122.9  96.3
#  121.6 118.  108.4 116.8 113.9 150.4 126.7 115.  137.8 155.7 161.  165.3
#  112.9 116.9 120.  113.  151.4 126.5 116.9 119.8 109.8 112.6 158.7 168.8]
# [126.5 136.8 120.8 120.  111.5 113.  141.2 178.1 167.5]
# -2.34742938096853

# Paddy
# [132.3 139.6 148.  121.9 152.6 153.9 140.  145.  144.7]
# [137.2 142.2 135.8 136.3 133.5 154.2 107.  143.8 149.6 135.2 111.  150.4
#  116.3 155.6 154.7 133.9 135.6 114.  153.3 131.3 149.1 115.9 116.6 147.7
#  133.6 144.2 134.1 140.5 118.7 145.1 132.6 117.9 138.  135.8 155.7 104.2
#  134.6 148.8 124.9 144.6 131.3 140.5 147.6 139.1 133.7 132.  131.  104.2
#  155.5 129.4 116.1 148.4 132.  144.2 130.6 155.  136.  134.2 135.3 133.4
#  148.8 146.4 120.4 151.4 132.6 131.1 116.7 155.7 149.2 148.5 135.2 135.4]
# [133.7 140.5 147.6 120.4 151.4 154.2 137.2 144.2 144.6]
# 0.9813295337296712

# Ragi
# [158.1 159.6 245.  172.9 220.8 208.3 161.7 209.  167.3]
# [157.6 169.3 159.5 174.1 160.6 211.2 108.9 242.6 233.7 161.5 115.6 207.9
#  161.5 216.2 212.9 159.1 157.  126.4 213.5 169.9 247.  162.1 149.5 258.
#  158.7 228.6 161.1 163.7 173.8 178.1 162.5 170.2 154.4 164.3 214.1 110.3
#  160.6 217.6 170.4 167.1 167.2 163.  252.8 177.  163.2 166.7 166.7 107.2
#  211.4 174.2 134.1 237.5 174.5 169.3 164.3 206.6 159.2 159.5 166.9 156.1
#  252.5 242.9 173.1 214.9 164.2 156.6 159.7 213.  217.3 261.9 167.3 158.1]
# [156.6 163.7 252.8 170.4 214.9 213.  159.2 178.1 167.1]
# 0.8655765544116445

# Rape
# [119.3 121.1 130.7 117.4 136.1 137.4 122.3 153.5 155.5]
# [117.7 150.8 158.8 144.2 127.1 136.9 119.3 147.7 134.2 148.  129.5 137.6
#  142.2 143.8 145.7 145.1 163.2 134.6 136.8 119.  131.  141.2 141.  135.3
#  143.  151.2 128.  121.  121.6 152.8 118.5 132.6 124.3 154.3 145.8 118.4
#  129.1 138.2 117.4 155.9 122.9 122.  130.6 147.4 116.9 126.7 120.1 117.9
#  146.6 116.5 136.7 129.9 116.9 155.  122.7 140.8 115.9 138.6 135.3 143.8
#  134.6 143.4 117.7 136.8 127.5 120.4 138.  145.6 135.6 133.3 132.3 161.3]
# [120.4 117.7 130.6 115.9 136.8 136.9 120.1 163.2 155.9]
# 0.9302351948709298

# Safflower
# [107.1  94.8 127.8 115.9 139.  137.8  93.  112.3 112.9]
# [ 93.2 111.8 105.  108.9  93.7 134.6 112.7 114.1 137.2 105.3 116.1 138.8
#  114.8 136.  155.5 107.4 105.9 118.1 137.8 112.8 134.1 114.8 117.8 124.8
#  108.1 113.9  94.8  94.1 115.2 113.5 112.  115.7  92.3 109.  143.5 110.9
#   93.4 133.2 118.9 112.  112.7  94.3 126.  115.5 125.4  94.5 112.3 103.9
#  150.5 118.9 120.3 129.3 114.6 111.4 112.1 134.8 124.5 110.1 111.1 105.8
#  140.2 117.  119.4 139.2 104.2 108.2 112.8 139.3 135.6 139.3 110.1 106.4]
# [125.4  93.2 126.  117.8 139.2 134.6 104.2 113.9 112. ]
# 0.7825658223546109

# Sesamum
# [142.5 138.5 116.3 155.2 130.1 128.1 136.  118.8 122.6]
# [138.7 117.2 110.1 119.2 125.5 126.8 120.4 116.4 118.5 110.5 125.6 132.2
#  143.3 133.9 168.8 114.6 109.5 134.8 128.1 159.6 113.2 149.7 138.1 115.6
#  116.1 117.3 121.9 141.9 161.6 118.5 145.4 161.2 130.2 108.5 150.1 122.1
#  127.6 128.3 155.  123.7 159.7 136.8 116.4 119.6 147.1 119.8 149.7 123.7
#  160.8 157.2 137.9 114.3 157.2 116.  164.5 130.  140.8 112.9 105.7 116.1
#  119.7 117.8 160.5 133.4 116.3 147.8 159.3 141.3 120.4 115.9 104.7 108. ]
# [147.8 138.7 119.6 160.5 133.4 126.8 136.8 104.7 119.7]
# 0.7670997782545464

# Soyabean
# [162.  175.9 123.4 164.4 156.  153.1 131.6 126.2 149.3]
# [175.5 165.1 156.9 167.5 144.6 155.9 144.8 127.8 126.  139.2 182.7 136.6
#  140.1 147.1 143.9 139.2 158.3 183.8 157.5 148.1 121.6 142.6 134.2 124.9
#  155.6 128.9 142.2 162.4 150.9 132.3 169.5 137.7 135.  151.3 140.2 139.6
#  140.8 125.3 156.7 156.3 160.3 141.8 126.8 162.4 175.6 141.3 147.  131.
#  141.6 153.5 166.2 121.2 148.  158.7 160.1 150.1 188.5 166.2 150.2 147.1
#  124.8 126.  163.  152.2 145.5 157.8 139.  142.9 122.2 122.8 151.4 152.2]
# [157.8 153.5 126.8 188.5 152.2 155.9 156.9 128.9 132.3]
# 0.2255848051646877

# Sugarcane
# [124.3 124.3 167.6 104.9 169.5 169.5 124.3 167.6 159.7]
# [124.3 159.7 150.3 159.7 124.3 169.5 103.9 167.6 167.6 150.3 101.2 169.5
#  104.9 169.5 169.5 150.3 150.3 104.9 169.5 104.9 167.6 104.9 104.9 167.6
#  150.3 167.6 124.3 124.3 104.9 164.4 124.3 104.9 124.3 159.7 169.5 100.
#  124.3 169.5 104.9 159.7 124.3 124.3 167.6 159.7 124.3 124.3 109.4 100.
#  169.5 104.9 104.9 167.6 104.9 159.7 124.3 169.5 124.3 150.3 159.7 150.3
#  167.6 167.6 104.9 169.5 150.3 124.3 104.9 169.5 169.5 167.6 159.7 150.3]
# [124.3 124.3 167.6 104.9 169.5 169.5 124.3 167.6 159.7]
# 1.0

# Sunflower
# [112.2 106.6 102.6 111.8 104.4 101.3 110.1 110.1 113.5]
# [111.1 112.7 117.1 115.5 108.   98.9 104.8 110.   99.1 116.4 112.8  99.8
#  117.4 105.9 118.2 112.6 119.1 118.4 107.2 117.6  96.8 116.  115.3 106.8
#  109.4 109.4 109.8 110.4 111.1 113.  114.5 116.1 107.3 118.5 116.6 101.7
#  107.2 100.2 118.  112.  112.1 108.2 104.2 114.3 109.9 106.9 114.4 101.9
#  117.5 112.3 113.7  98.3 121.9 112.5 114.5 104.8 108.8 110.2 118.1 109.
#   98.4 108.5 111.9 100.6 105.8 110.4 115.  111.4  99.2  94.5 118.1 119.7]
# [110.4 111.1 104.2 118.  100.6  98.9 108.2 117.4 113. ]
# 0.1139430284857561

# Urad
# [108.5 122.3 145.7  96.3 112.1 105.9 124.3 188.4 211.6]
# [116.5 247.6 196.9 213.  131.6 108.4  92.1 167.6 127.7 171.8  97.9 114.8
#   97.5 109.8 123.3 167.7 204.7 102.3 110.5  97.1 134.1  97.2  99.3 151.1
#  160.4 178.4 132.1 127.   96.5 199.  108.3  96.3 124.  206.1 111.   90.8
#  124.7 121.   95.2 229.3 103.1 128.  149.5 231.  109.7 133.7  97.9  90.7
#  118.6  96.6 102.3 140.8  96.3 243.7 103.7 106.9 115.1 149.7 199.3 162.8
#  129.1 158.1  96.2 112.6 138.8 105.7  96.5 107.6 123.7 127.2 198.2 203.4]
# [105.7 116.5 149.5  96.2 112.6 108.4 128.  198.2 229.3]
# 0.9617169568720035

# Wheat
# [128.8 121.9 137.5 118.9 141.2 143.1 122.3 147.9 140. ]
# [120.4 136.5 128.5 132.9 126.3 141.7 104.4 151.3 138.  126.2 105.8 140.8
#  120.7 148.6 152.8 126.1 129.9 116.  140.9 124.6 136.3 121.7 117.4 142.9
#  122.3 152.3 125.9 122.5 122.8 140.8 127.5 123.6 123.7 134.1 151.1 105.4
#  125.8 139.4 121.9 139.1 127.6 121.8 141.  134.5 123.5 125.9 125.7 104.6
#  152.2 122.3 119.4 136.1 123.1 137.9 128.6 145.  120.9 124.1 134.1 124.8
#  137.6 149.3 120.1 140.  125.1 130.  121.6 149.8 139.4 137.1 134.1 131.9]
# [130.  122.3 136.1 120.9 140.  141.7 123.7 140.8 139.1]
# 0.9296948645561081
