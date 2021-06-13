from sklearn.model_selection import train_test_split
from A_dataset import *
train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.4,
                                                          random_state=42)
