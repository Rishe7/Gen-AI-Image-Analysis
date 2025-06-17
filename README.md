# Image Analysis Using Gemini Pro Vision

This project utilizes the Gemini Pro Vision API from Google's GenerativeAI to perform image analysis based on user input prompts. It generates content using the provided input text, uploaded image, and additional prompt.

## Installation

To run this project, you will need to have Anaconda installed. If you haven't installed Anaconda yet, you can download it [here](https://www.anaconda.com/products/distribution).

After installing Anaconda, follow these steps:

1. Create a new environment using the following command:

    ```bash
    conda create -p venv python==3.10 -y
    ```

2. Activate the environment:

    - **Windows**: `conda activate venv`
    - **Linux/macOS**: `source activate venv`

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once you have set up the environment and installed the dependencies, you can run the application using the following command:

```bash
streamlit run app.py
