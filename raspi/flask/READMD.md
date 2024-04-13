# Flask Deployment Instructions

Follow these steps to deploy your Flask application:

1. **Create Python Virtual Environment**
    - Create a virtual environment:
      ```
      $ virtualenv venv
      ```
    - Activate the virtual environment:
      ```
      $ source venv/bin/activate
      ```

2. **Install Project Requirements**
    - Install the required packages using:
      ```
      $ pip install -r requirements.txt
      ```

3. **Launch Application**
    - Set the Flask application environment variable:
      ```
      $ export FLASK_APP=main.py
      ```
    - Set the Flask environment to deployment:
      ```
      $ export FLASK_ENV=deployment
      ```
    - Start the Flask server:
      ```
      $ flask run
      ```
