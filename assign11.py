import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load the dataset
data = load_diabetes()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Start MLflow run and train a model
with mlflow.start_run() as run:
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Log model
    mlflow.sklearn.log_model(model, "linear_regression_model")
    
    # Log metrics
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mlflow.log_metric("mse", mse)
    
    print(f"Model logged in run ID: {run.info.run_id}")
