# mcp-nlp

MCP-NLP is a FastMCP application designed to provide NLP (Natural Language Processing) capabilities using the Model Context Protocol (MCP).

- **[FastMCP Framework v2](https://github.com/jlowin/fastmcp)**: A modern framework for fast, Pythonic way to build MCP servers.
- **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)**: A protocol that allows for the management and control of LLM contexts.
- **NLP-modules**
  - `textdistance`: A module for calculating text distance metrics

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tivaliy/mcp-nlp.git
   cd mcp-nlp
   ```

2. Install dependencies (using `uv`):
   ```bash
   uv sync
   ```

## Usage

### Local Running

To run the application locally:

Create a `.env` file in the root directory (see `.env.example` as an example).

1. Start the FastMCP application:
   ```bash
   uvicorn app.main:http_app --reload
   ```

2. Access the MCP server endpoint at `http://127.0.0.1:8000/mcp/` (in case of `streamable-http` transport)

### Run MCP Server Using Docker

To run the MCP server in a Docker container:

1. Build the Docker image:
   ```bash
   docker build -t mcp-nlp .
   ```

2. Run the Docker container:
   ```bash
   docker run --rm -p 8000:8000 mcp-nlp
    ```

3. Access the MCP server endpoint at `http://127.0.1:8000/mcp/` (in case of `streamable-http` transport)

`MCP` | `Model Context Protocol` | `FastMCP` | `NLP`
