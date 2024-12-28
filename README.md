# LangChain02

Corresponds to Udemy course, part 3, "Icebreaker real world generative API application"

## Set up virtual environment
```
rm -rf venv
virtualenv -p python3.11 venv
. venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt
```

## Usage

Update .env file with your OPENAI_API key
Update .env file with your SERPAPI_API key

Then export it with

```bash
export $(grep -v '^#' .env | xargs)
```

Then run the app with

```bash
python ice_breaker.py
```
