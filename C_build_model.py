from sklearn.naive_bayes import GaussianNB
from B_share_data import *
gnb = GaussianNB()
model = gnb.fit(train, train_labels)
preds = gnb.predict(test)
print(preds)
# 0 la ac tinh- 1 la lanh tinh