# Steamship Parser Plugin

This project implements a basic Tagger that you can customize and deploy for your own use.

In Steamship, **Taggers** are responsible for emitting tags that commend upon Steamship Blocks Format.

This sample project tags (assumed) paragraphs as having sentences and tokens using simple whitespace, but the implementation you create might:

* Use SpaCy to parse text
* Use some custom-trained parser based on your domain to parse text
* Classify emails into intent
* Classify emails by sentiment

Once a Tagger has returned data to Steamship as **Blocks and Tags**, that data is ready for use by the rest of the ecosystem.
For example, you could perform a query over the sentences, or query for sentence with a particular sentiment.

## First Time Setup

We recommend using Python virtual environments for development.
To set one up, run the following command from this directory:

```bash
python3 -m venv .venv
```

Activate your virtual environment by running:

```bash
source .venv/bin/activate
```

Your first time, install the required dependencies with:

```bash
python -m pip install -r requirements.dev.txt
python -m pip install -r requirements.txt
```

## Developing

All the code for this plugin is located in the `src/api.py` file:

* The CorpusImporterPlugin class
* The `/import_corpus` endpoint

## Testing

Tests are located in the `test/test_api.py` file. You can run them with:

```bash
pytest
```

## Deploying

Deploy your converter to Steamship by running:

```bash
ship deploy --register-plugin
```

That will deploy your app to Steamship and register it as a plugin for use.

## Using

Once deployed, your Corpus Importer Plugin can be referenced by the handle in your `steamship.json` file.

```python
from steamship import Corpus, Steamship, CorpusImportRequest

MY_PLUGIN_HANDLE = ".. fill this out .."

client = Steamship()
request = CorpusImportRequest() # Provide the appropriate parameters
file = client.create_file(importer=MY_PLUGIN_HANDLE, request=request)
```

## Sharing

Plesae share what you've built with hello@steamship.com! 

We would love take a look, hear your suggestions, help where we can, and share what you've made with the community.