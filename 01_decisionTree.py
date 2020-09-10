import sklearn.datasets as datasets
from sklearn.tree import DecisionTreeClassifier

# import sklearn
# print(sklearn.__version__)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

breast_cancer = datasets.load_breast_cancer()
# print(breast_cancer)

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(breast_cancer.data, breast_cancer.target)

fig = plt.figure(figsize=(25, 10))


a = plot_tree(
    clf, 
    feature_names=breast_cancer.feature_names,
    class_names=breast_cancer.target_names,
    filled=True,
    rounded=True,
    fontsize=14
)

# fig.show()
fig.savefig("figures/decision_tree.png")

print(a)