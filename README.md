
# Banana Usage Prediction System

This project is a machine learning-based web application built using Python (FastAPI) and ReactJS. It predicts banana usage based on the variety, quantity, and period provided by the user. The system trains a machine learning model on CSV data and provides predictions along with an accuracy score.




## Acknowledgements

 - [Project Overview](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Tech Stack](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Features]()
- [Installation]()
- [How to Use]()
- [Directory Structure]()
- [Contributing]()
- [License]()
 


## Project Overview

This project allows users to input banana variety, quantity, and period to predict the banana usage. The system uses a machine learning model that is trained on historical data, and the model's predictions are displayed to the user along with the accuracy score. Users can upload their own dataset via CSV files.


## Tech Stack

**Client:** React, Vite, TailwindCSS

**Server:** Python, FastAPI

**Machine Learning:** Python (scikit-learn, pandas)

**Environment:** Python Virtual Environment


## Features

- CSV Upload: Upload a CSV file with banana variety, quantity,   period, and usage data to train the model.
- Model Training: Automatically trains a machine learning model using the uploaded data.
- Prediction: Provide banana variety, quantity, and period for the model to predict usage.
- Accuracy Score: The app returns an accuracy score for the prediction.
- User-Friendly Interface: Simple web interface built with ReactJS for interaction.


## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js (for frontend)
- npm or yarn (for managing frontend dependencies)

### Backend (FastAPI) Setup
- Clone the repository:

```bash
git clone https://github.com/dulithOk/banana-usage-predicted-ML.git
cd banana-usage
```
- Set up a Python virtual environment:
```bash
python -m venv venv

```
- Activate the virtual environment:
  
- Windows:
```bash
    venv\Scripts\activate
```
- Mac/Linux
```bash
source venv/bin/activate
```
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
- Run the FastAPI backend:
```bash
uvicorn main:app --reload
```

#### Accessing the Application
- Backend API: http://localhost:8000
- Frontend (ReactJS): http://localhost:3000
## How to Use

- Upload CSV File:Go to the frontend and upload a CSV file containing the following columns: variety, quantity, period, usage.

- Train the Model: After uploading the CSV file, the model will be trained automatically.

- Input Prediction Data: Enter the banana variety, quantity, and period in the provided fields to get the predicted usage.

- View Prediction & Accuracy Score: The app will display the predicted usage and the model's accuracy score.



## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## License

[MIT](https://choosealicense.com/licenses/mit/)

