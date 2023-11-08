# Glia Assessment - Text Classification

## How to run the solution

**Prerequisite**

Have an virtual environment ready with Python 3.10 installed.

1. Clone this repo
2. Install the depdencies with `pip install -r requirements.txt`
3. In a terminal window, start the server with `python rest_api.py`
4. In another terminal winddow, test the API with `python run_api.py`
5. The result in the terminal shows the input message, and a dictionary with the intent and confidence score
6. To change the input text, simply the value of the variable `sample_text` in the `run_api.py` file on line 10. Then, we can send this new text to the REST API using `python run_api.py` and see the prediction for the new text.

## Model documentation
The entire experimental protocal and thought process to create the classifier is available in the notebook `glia_text_classif_sklearn.ipynb`.
