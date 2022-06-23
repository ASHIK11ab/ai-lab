from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from IPython.display import Image
from six import StringIO
import pydotplus

data = load_iris()

print(data.feature_names)

x = data.data
y = data.target


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=21, test_size=.2)

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print(f"Mean square error: {mean_squared_error(y_test, y_pred)}")

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, feature_names=data.feature_names,
                class_names = data.target_names, special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())
graph.write_png("iris.png")