import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


class ml_model:
    def __init__(self):
        return
    
    #input,targetデータの習得
    def get_data(self,df,target_name):
        #データの読み込み
        input=df.drop([target_name],axis=1)
        target=df[target_name]
        
        #データの分割
        input_train, input_test, target_train, target_test = train_test_split(input, target, test_size=0.2, random_state=42)
        
        #特徴量の標準化(必要な場合のみ)
        """scaler = StandardScaler()
        input_train = scaler.fit_transform(input_train)
        input_test = scaler.transform(input_test)"""

        return input_train,input_test,target_train,target_test

    
    #サポートベクターマシン
    def svm(self):
        svm=SVC(kernel='rbf', gamma='scale')
        return svm
    
    #ランダムフォレスト
    def RandomForest(self):
        RandomForest=RandomForestClassifier(100, random_state=42)
        return RandomForest

    #学習曲線
    def plot_learning_curve(estimator, title, input, target, cv=None, n_jobs=None, train_sizes=np.linspace(0.1, 1.0, 10)):
        plt.figure()
        plt.title(title)
        plt.xlabel("Training examples")
        plt.ylabel("Score")

        train_sizes, train_scores, test_scores = learning_curve(estimator, input, target, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
    
        plt.grid()
    
        plt.fill_between(train_sizes, train_scores_mean - train_scores_std,train_scores_mean + train_scores_std, alpha=0.1, color="r")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std,test_scores_mean + test_scores_std, alpha=0.1, color="g")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")
    
        plt.legend(loc="best")
        return plt
    
    #モデル評価
    def result(self,model,input_test,target_test):
        target_pred = model.predict(input_test)

        # モデルの精度を評価
        accuracy = accuracy_score(target_test, target_pred)
        print(f'Accuracy: {accuracy}')

        # 詳細な評価レポートを表示
        print(classification_report(target_test, target_pred))

        # 混同行列を表示
        print(confusion_matrix(target_test, target_pred))
        
        return target_pred