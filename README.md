
# Python Azure Function App

This is a Python Azure Function App that provides serverless computing capabilities. The app includes functions to send prompts to GPT models written in Python and uses Azure Functions and OpenAI packages.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Azure Functions Core Tools (for local development)
- Azure CLI (for deploying to Azure)
- Visual Studio Code with the Azure Functions extension (recommended)

### Installation

1. **Clone the repository**:
   ```sh
   git clone <your-repository-url>
   cd <your-repository-directory>
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .\.venv\Scripts\activate  # On Windows
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

### Local Development

1. **Start the Azure Functions Core Tools**:
   ```sh
   func start
   ```

2. **Run your function**:
   - The function can be triggered locally using the URL provided by the Azure Functions Core Tools.

### Project Structure

- `function_app.py`: Contains the Azure Function implementation.
- `requirements.txt`: Lists the dependencies required by the function.
- `host.json`: Contains the global configuration options for all functions in the app.

### Deploying to Azure

1. **Log in to Azure**:
   ```sh
   az login
   ```

2. **Create a Function App in Azure**:
   ```sh
   az functionapp create --resource-group <your-resource-group> --consumption-plan-location <your-location> --runtime python --runtime-version 3.9 --functions-version 3 --name <your-functionapp-name> --storage-account <your-storage-account-name>
   ```

3. **Deploy your function**:
   ```sh
   func azure functionapp publish <your-functionapp-name>
   ```

### Configuration Files

- `requirements.txt`:
  ```plaintext
  azure-functions
  openai==0.27.0
  ```

- `host.json`:
  ```json
  {
    "version": "2.0",
    "logging": {
      "applicationInsights": {
        "samplingSettings": {
          "isEnabled": true,
          "excludedTypes": "Request"
        }
      }
    },
    "extensionBundle": {
      "id": "Microsoft.Azure.Functions.ExtensionBundle",
      "version": "[4.*, 5.0.0)"
    }
  }
  ```

### Function Code

- `function_app.py`:
  ```python
  import azure.functions as func

  def main(req: func.HttpRequest) -> func.HttpResponse:
      return func.HttpResponse("Hello, Azure Functions!", status_code=200)
  ```

### Troubleshooting

- Ensure all dependencies are installed.
- Check the Azure Functions Core Tools and Azure CLI are installed and updated.
- Verify the function app settings in the Azure portal.

### Contributing

Feel free to contribute to this project by creating issues or submitting pull requests.

### License

This project is licensed under the MIT License.
