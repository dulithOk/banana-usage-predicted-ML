# Banana Usage Predicted Setup and Installation Guide

## Project Structure
```
├── app
│   ├── config                
│   ├── controller
|   |── core
|   |── data                 
│   ├── model
|   |── notebooks               
│   ├── service                                       
├── main.py                   
├── requirements.txt          
├── README.md                 
```

## Installation and Setup

### Step 1: Open Project in any ide(sug: vs code)
```bash
cd banana_forest
```

### Step 2: Create a Virtual Environment
It's best practice to create a virtual environment to isolate the project dependencies:

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

install wsl2 linux server in windows best suggest

### Step 3: Install Dependencies
Install all the required dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```
This will install FastAPI, Uvicorn, and any other dependencies your project needs.

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory of your project. This file will contain environment-specific variables that your application needs to run:

```env
LOG_LEVEL=DEBUG
```

### Step 5: Run the FastAPI Application
You have two options to start the FastAPI server:

#### Option 1: Using Uvicorn Command
```bash
uvicorn app.main:app --reload
```
This will start the FastAPI server at `http://localhost:8006`. The `--reload` flag ensures that the server automatically reloads when you make changes to the code.

#### Option 2: Using main.py Directly
```bash
python app/main.py
```
This will achieve the same result as using the Uvicorn command but might not automatically reload the server.

get the api doc at `http://localhost:8006/docs`

## Testing the Banana Usage Predicted ML model

### Connecting to the banana predict model


### Available Endpoints

- `POST /v1/banana/get`: Sends a data to banana predict model 
