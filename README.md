Progress So Far
1.	Connected to MLflow:
	  - Successfully set up the MLflow Tracking Server locally at http://127.0.0.1:5000.
	  - Configured the environment by setting the MLFLOW_TRACKING_URI to point to the server.
	  - Verified the connection by logging experiments and accessing the MLflow UI.
2.	Model Training and Logging:
  	- Implemented a Linear Regression model using scikit-learn and trained it on a sample dataset.
    - Logged the model, metrics, and parameters to the MLflow Tracking Server.
3.	Model Registration:
    - Successfully registered the model in the MLflow Model Registry.
    -	Assigned version aliases for different stages (Production, Staging, Testing).
    -	Verified the registered models using the MLflow UI and REST API.
4.	Serving the Model:
    -	Deployed the registered model locally using the mlflow models serve command.
    -	Experimented with both Flask-based and MLServer-based deployments.
    -	Enabled an inference endpoint on port 5000 for model predictions.

Challenges Faced
I was able to accomplish the above steps but was unable to:
  •	Successfully test the /invocations endpoint with input data.


Environment Issues:
•	Encountered errors related to Python version compatibility during deployment.
•	MLflow attempted to use an unsupported Python version (3.13.1), leading to installation failures.
•	Resolved this by switching to a supported Python version (3.12.x) using pyenv and updating the environment variables.

Invocation Endpoint Issues:
•	Initially faced a 404 Not Found error when attempting to send requests to the /invocations endpoint.
•	Debugged the issue by:
o	Verifying the server was running on the correct port (5000).
o	Testing the endpoint with corrected payload formats and headers.
•	Adjusted the input data format to match the model’s expected schema, resolving payload-related issues.

Environment Variable Adjustments:
•	Experimented with various environment variables (MLFLOW_TRACKING_URI, PYTHONPATH) to ensure compatibility with MLflow and dependencies.
•	Modified shell configurations (.bashrc) to persist environment settings
•  Model Not Found Challenge:
•	Encountered errors when attempting to deploy the registered model, such as:
o	Could not find a registered artifact repository for: model:/basic_lr_iris_model/3.


Dropletname: 146.190.167.170
access link: http://146.190.167.170:5000/
