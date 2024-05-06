from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import make_pipeline


# Inicializar o vetorizador
vectorizer = CountVectorizer(analyzer='char')

def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    data = [line.strip().split(', ') for line in data if line.strip()]
    return data

# Carregar e processar os dados de treinamento e teste
data_train = load_data("md5h.txt")
data_test = load_data("chat.txt")

X_train = vectorizer.fit_transform([x[0] for x in data_train])  # Aprende o vocabulário e transforma os dados
y_train = [x[1] for x in data_train]

X_test = vectorizer.transform([x[0] for x in data_test])  # Transforma os dados usando o mesmo vetorizador
y_test = [x[1] for x in data_test]

# Treinar um modelo SVM com kernel linear
model = SVC(kernel='linear', probability=True)
print("Aqui?")
model.fit(X_train, y_train)

print("Aqui?>>")
# Prever os resultados para o conjunto de teste
y_pred = model.predict(X_test)

# Avaliar a acurácia do modelo
print("Accuracy:", accuracy_score(y_test, y_pred))

# Criar um pipeline com o vetorizador e o modelo
pipeline = make_pipeline(vectorizer, model)



# Função para prever a classe de um hash
def predict_hash_type(hash_text):
    pred = pipeline.predict([hash_text])[0]
    probabilities = pipeline.predict_proba([hash_text])[0]
    class_labels = pipeline.classes_
    probability_dict = dict(zip(class_labels, probabilities))
    return pred, probability_dict

# Exemplo de uso da função
hash_text = "e10adc3949ba59abbe56e057f20f883e"  # Exemplo de hash MD5
predicted_class, probs = predict_hash_type(hash_text)
print(f"Predicted Class: {predicted_class}")
print("Probabilities:", probs)

# Gerar e plotar a matriz de confusão
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
plt.title("Matriz de Confusão")
plt.ylabel('Verdadeiros')
plt.xlabel('Predições')
plt.show()
