# AI Backend

> [!CAUTION]
> AI Backend is still in Development. You will find bugs and broken/unfinished features.

## 🌟 Overview

ai-backend is a backend for AI-powered applications. It leverages FastAPI and Ollama to provide a robust API for natural language processing tasks.

## 🚀 Installation and Configuration

###  Prerequisites

- Python 3.12
- pip
- git

### Installation for Development

1. Clone the repository

```bash
git clone https://github.com/Dino-Kupinic/ai-backend.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and copy over the fields from the `.env.example` file.

4. Download ollama for your system from [here](https://ollama.com/download).

> [!NOTE]
> In the future, ollama will be downloaded from the command line automatically.

5. Run the server

```bash
fastapi dev src/main.py
```

## 📖 Documentation

### OpenAPI Documentation

The OpenAPI documentation is available at `/docs`. It is automatically generated from the code.

### Configuration

// WIP

### Usage

```bash
curl -X POST "http://localhost:8000/message/" -H "Content-Type: application/json" -d '{"text": "Tell me something about Vienna, Austria"}' --no-buffer
```

> [!TIP]
> `--no-buffer` is needed due to streaming.


// WIP

## 🧪 Testing

To run the test suite:

1. Ensure that both the AI Backend and Ollama services are running.
2. Execute the following command:

```bash
pytest
```

This will run all tests in the `tests/` directory.

## 📝 Contributing

// WIP

## 📚 Resources

- [FastAPI](https://fastapi.tiangolo.com/)
- [Ollama](https://ollama.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Special thanks to the FastAPI and Ollama communities for their excellent tools and documentation

---

For more information, please [open an issue](https://github.com/Dino-Kupinic/ai-backend/issues) or contact the maintainers.
