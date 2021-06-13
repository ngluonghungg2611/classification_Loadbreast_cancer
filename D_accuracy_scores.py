from sklearn.metrics import accuracy_score
from C_build_model import *
print(accuracy_score(test_labels, preds)*100,"%")