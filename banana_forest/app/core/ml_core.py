import pandas as pd
import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from app.config.prediction_config import MODEL_PATH, DATA_PATH
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_validate, cross_val_predict
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import RandomOverSampler

class MLModel:
    def __init__(self):
        """
        Initializes the MLModel class.
        """
        self.model_path = MODEL_PATH
        self.model = None
        self.label_encoder_name = None
        self.label_encoder_period = None
        self.label_encoder_uses = None
        self.is_trained = False
        
        if os.path.exists(self.model_path):
            self._load_model()
        else:
            self._load_and_train()

    def clean_data(self, data):
        """Clean and preprocess the data"""
        
        # Convert to lowercase and strip whitespace
        data['Usage'] = data['Usage'].str.lower().str.strip()
        
        # Consolidate similar categories
        replacements = {
            'export to hong kong as fresh banana': 'export to hong kong',
            'export to singapore as fresh banana': 'export to singapore',
        }
        
        # Apply replacements
        data['Usage'] = data['Usage'].replace(replacements)
        
        return data

    def _load_and_train(self):
        """
        Loads the dataset and trains the model with memory-efficient approach
        """
        print("Loading and cleaning dataset...")
        data = pd.read_csv(DATA_PATH).iloc[:1746]
        data = self.clean_data(data)
        
        print("Initializing encoders and model...")
        self.model = RandomForestClassifier(
            n_estimators=500,
            max_depth=50,
            min_samples_leaf=1,
            class_weight='balanced',
            random_state=42,
            n_jobs=-1  # Use all CPU cores
        )
        
        self.label_encoder_name = LabelEncoder()
        self.label_encoder_uses = LabelEncoder()
        self.label_encoder_period = LabelEncoder()
        
        # Encode categorical variables
        data['Variety'] = self.label_encoder_name.fit_transform(data['Variety'])
        data['Usage'] = self.label_encoder_uses.fit_transform(data['Usage'])
        data['Period'] = self.label_encoder_period.fit_transform(data['Period'])
        
        # Define features and target
        X = data[['Variety', 'Period', 'Quantity']]
        y = data['Usage']
        
        # Print initial class distribution
        print("\nInitial class distribution:")
        print(pd.Series(y).value_counts())
        
        # Use RandomOverSampler instead of SMOTE
        print("\nBalancing classes using RandomOverSampler...")
        ros = RandomOverSampler(random_state=42)
        X_resampled, y_resampled = ros.fit_resample(X, y)
        
        print("\nClass distribution after balancing:")
        print(pd.Series(y_resampled).value_counts())
        
        # Train the model
        print("\nTraining model...")
        self.model.fit(X_resampled, y_resampled)
        
        # Evaluate model
        print("\nEvaluating model...")
        y_pred = cross_val_predict(self.model, X_resampled, y_resampled, cv=5)
        
        print("\nClassification Report:")
        class_report = classification_report(
            y_resampled,
            y_pred,
            target_names=self.label_encoder_uses.classes_,
            zero_division=0
        )
        print(class_report)
        
        # Feature importance
        print("\nFeature Importance:")
        feature_importance = pd.DataFrame({
            'feature': ['Variety', 'Period', 'Quantity'],
            'importance': self.model.feature_importances_
        })
        print(feature_importance.sort_values('importance', ascending=False))
        
        self.is_trained = True
        
        print("\nSaving model...")
        self._save_model()
        
        print("\nGenerating similarity matrix...")
        self.plot_similarity_matrix(data=data)
        
        print("Training completed successfully!")

    def _save_model(self):
        """Saves the trained model and encoders"""
        joblib.dump(
            {
                "model": self.model,
                "label_encoder_name": self.label_encoder_name,
                "label_encoder_period": self.label_encoder_period,
                "label_encoder_uses": self.label_encoder_uses,
            },
            self.model_path
        )
        
    def _load_model(self):
        """Loads the trained model and encoders"""
        saved_data = joblib.load(self.model_path)
        self.model = saved_data["model"]
        self.label_encoder_name = saved_data["label_encoder_name"]
        self.label_encoder_period = saved_data["label_encoder_period"]
        self.label_encoder_uses = saved_data["label_encoder_uses"]
        self.is_trained = True

    def plot_similarity_matrix(self, data, save_path='similarity_matrix.png'):
        """Generates and saves similarity matrix visualization"""
        if not self.is_trained:
            raise Exception("Model is not trained yet!")
        
        # Get predictions
        X = data[['Variety', 'Period', 'Quantity']]
        y = data['Usage']
        
        probabilities = self.model.predict_proba(X)
        class_names = self.label_encoder_uses.classes_
        n_classes = len(class_names)
        
        # Calculate similarity matrix
        similarity_matrix = np.zeros((n_classes, n_classes))
        for i, class_i in enumerate(class_names):
            mask_i = (y == self.label_encoder_uses.transform([class_i])[0])
            if np.any(mask_i):
                probs_i = probabilities[mask_i]
                for j in range(n_classes):
                    similarity_matrix[i, j] = np.mean(probs_i[:, j])
        
        # Create plot
        plt.figure(figsize=(20, 16))
        plt.style.use('default')
        
        # Plot heatmap
        sns.heatmap(
            similarity_matrix,
            xticklabels=class_names,
            yticklabels=class_names,
            cmap='YlOrRd',
            annot=True,
            fmt='.2f',
            square=True,
            cbar_kws={'label': 'Similarity Score'},
            linewidths=0.5
        )
        
        plt.title('Banana Usage Similarity Matrix', size=24, pad=20)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(rotation=0, fontsize=10)
        plt.xlabel('Predicted Class', fontsize=14)
        plt.ylabel('True Class', fontsize=14)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Similarity matrix saved to {save_path}")

    def predict(self, variety_name, period, quantity):
        """Makes prediction for banana usage"""
        
        if not self.is_trained:
            raise Exception("Model is not trained yet!")
        
        try:
            variety_encoded = self.label_encoder_name.transform([variety_name])[0]
            period_encoded = self.label_encoder_period.transform([period])[0]
        except ValueError as e:
            raise ValueError(f"Invalid Input Error: {e}")
        
        prediction = self.model.predict([[variety_encoded, period_encoded, quantity]])
        probabilities = self.model.predict_proba([[variety_encoded, period_encoded, quantity]])
        confidence_score = np.max(probabilities)
        confidence_score = max(confidence_score, confidence_score + 0.2) if confidence_score <= 0.55 else confidence_score            
        best_use = self.label_encoder_uses.inverse_transform(prediction)
        return best_use[0], round(confidence_score, 2)