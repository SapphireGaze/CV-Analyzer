# CV Analyzer

A simple CV analyzer using the [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) model with both CLI and REST API interface.

## Prerequisites

- Linux/Unix based systems with at least 8GB of RAM (ML models are very memory intensive!!)
- Git
- Python3
- A CV file to analyze

## Installation

Clone the repository and run the below command to create a venv for the project:

```
git clone https://github.com/SapphireGaze/CV-Analyzer.git
cd CV-Analyzer
python3 -m venv cv-analyzer
```

Activate the venv and install the dependencies (this may take a while):

```
source cv-analyzer/bin/activate
pip install -r requirements.txt
```

Run the CLI based program by running:

```
python3 main.py path/to/cv.pdf "Backend Intern"
```

You can view program argument requirements by running:

```
python3 main.py -h
```

The REST API Flask server can be run with the following commands, make sure port 5000 is unused as that is the default port:

```
python3 server.py
```

The API endpoint can be tested with curl, example:

```
curl -X POST http://127.0.0.1:5000/analyze_cv \
    -F "cv_file=@/path/to/cv.pdf" \
    -F "position=Backend Intern"
```

Deactivate the venv when you are finished by running the below command:

```
deactivate
```

Have fun!
