# mini-rag

mini-rag is a minimal Retrieval-Augmented Generation (RAG) application designed to demonstrate how to combine retrieval techniques with generative AI models for improved question answering and information retrieval.

## Features

- Simple and lightweight RAG implementation
- Easily extensible for custom datasets and models
- Clear code structure for educational purposes

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

Clone the repository:

```sh
git clone https://github.com/yourusername/mini-rag.git
cd mini-rag
$ pip install -r requirements.txt
```

### setup the environment variables

```bash
$ cp .env.example .env
```

### Run Docker Compose Services

```bash
cd docker
cp .env.exmaple .env

```

- update `.env` with your credentials

### Activate your private env

```bash
$ conda activate mini-rag
```

## How to run uvicorn

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5001
```
