
import pandas as pd

#Student performance dataset

url_performance = "https://archive.ics.uci.edu/static/public/320/data.csv"

col_names_performance = ["school",
            "sex",
            "age",
            "address",
            "famsize",
            "Pstatus",
            "Medu",
            "Fedu",
            "Mjob",
            "Fjob",
            "reason",
            "guardian",
            "traveltime",
            "studytime",
            "failures",
            "schoolsup",
            "famsup",
            "paid",
            "activities",
            "nursery",
            "higher",
            "internet",
            "romantic",
            "famrel",
            "freetime",
            "goout",
            "Dalc",
            "Walc",
            "health",
            "absences",
            "G1",
            "G2",
            "G3"]

df_performance = pd.read_csv(url_performance, skiprows=1, names=col_names_performance)
df_performance0= df_performance.sample(n=50, random_state=42)


df_performance1 = df_performance0.drop(["Mjob", "Fjob", "reason", "guardian", "G2", "G1"], axis=1)
#df_performance1 = df_performance0.drop(["Mjob", "Fjob", "reason", "guardian"], axis=1)

a = {"GP":1, "MS":0}
df_performance1['school'].replace(a, inplace = True)
b = {"F":1, "M":0}
df_performance1['sex'].replace(b, inplace = True)
c = {"U":1, "R":0}
df_performance1['address'].replace(c, inplace = True)
e = {"GT3":1, "LE3":0}
df_performance1['famsize'].replace(e, inplace = True)
f = {"T":1, "A":0}
df_performance1['Pstatus'].replace(f, inplace = True)
g = {"yes":1, "no":0}
df_performance1['schoolsup'].replace(g, inplace = True)
h = {"yes":1, "no":0}
df_performance1['famsup'].replace(h, inplace = True)
i = {"yes":1, "no":0}
df_performance1['paid'].replace(i, inplace = True)
j = {"yes":1, "no":0}
df_performance1['activities'].replace(j, inplace = True)
k = {"yes":1, "no":0}
df_performance1['nursery'].replace(k, inplace = True)
l = {"yes":1, "no":0}
df_performance1['higher'].replace(l, inplace = True)
m = {"yes":1, "no":0}
df_performance1['internet'].replace(m, inplace = True)
n = {"yes":1, "no":0}
df_performance1['romantic'].replace(n, inplace = True)


s = {(0, 1, 2, 3, 4, 5, 6, 7, 8, 9):0, (10, 11):1, (12,13):2, (14, 15, 16, 17, 18, 19, 20):3}


df_performance1['G3'].replace(s, inplace = True)

#print(df_performance1)
#df_performance1.astype(float)

X_performance = df_performance1.drop(["G3"], axis=1)
#print(X_performance)
Y_performance = df_performance1["G3"]
#print(Y_performance)

X_test_performance = X_performance.to_numpy()
#print(X_test_performance)
Y_test_performance = Y_performance.to_numpy()
#print(Y_test_performance)

class_labels, Y_test_performance = np.unique(df_performance1['G3'], return_inverse=True)
#print(class_labels)
