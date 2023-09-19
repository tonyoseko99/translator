# Flask Translator

## Table of Contents
* [Technologies Used](#technologies-used)
* [Description](#description)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Technologies Used
- Python 3.9
- Flask 2.1.0
- Microsoft Translator Text API v3.0

## Description
Flask Translator is a simple web application that translates text into any language available in the Microsoft Translator Text API. It uses the Flask web framework and the Translator Text API to handle user input and translation requests.

## Getting Started
To get started with Flask Translator, you will need to do the following:

1. Clone this repository to your local machine.
    ```bash
    $ git clone git@github.com:tonyoseko99/translator.git && cd translator
    ```

2. Install the required packages listed in the `requirements.txt` file.
    ```bash
    $ pip install -r requirements.txt
    ```
3. Set your Translator Text API subscription key and endpoint in a `.env` file. An example `.env` file is provided in this repository.
    - You can get a free Translator Text API subscription key by signing up for a free Azure account [here](https://azure.microsoft.com/en-us/try/cognitive-services/?api=translator-text-api).
    - You can find your Translator Text API endpoint by following the instructions [here](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-reference#authentication).

4. Run `python app.py` to start the Flask application.
    - The Flask application will run on port 5000 by default. You can change this by setting the `PORT` environment variable in your `.env` file.
    - If the above command fails to run, try `python3 app.py` instead, depending on your Python installation.
    - If the command still fails to run, export the `FLASK_APP` environment variable with the value `app.py` and run `flask run` instead.
        ```bash
        $ export FLASK_APP=app.py
        $ flask run
        ```
    - If you are using a virtual environment, make sure to activate it before running the above commands.

## Usage
Once the Flask application is running, you can access the translation page by navigating to `http://localhost:5000/` in your web browser. From there, enter the text you want to translate and select the target language from the dropdown menu. Click the "Translate" button to submit the request and view the translated text.

## Contributing
If you find any issues or have any suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
