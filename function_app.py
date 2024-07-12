import azure.functions as func
import datetime
import json
import logging
from shared_code import openai_helper

app = func.FunctionApp()

@app.route(route="HttpTriggerGPT4", auth_level=func.AuthLevel.ANONYMOUS)
def HttpTriggerGPT4(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function (GPT-4) processed a request.')

    try:
        req_body = req.get_json()
        if not req_body or 'prompt' not in req_body:
            return func.HttpResponse(
                "Please pass a JSON body with a 'prompt' key in the request.",
                status_code=400
            )

        gpt_response = openai_helper.get_openai_response(req_body['prompt'], model="gpt-4")
        
        output_message = {
            "model": "gpt-4",
            "original_prompt": req_body['prompt'],
            "gpt_response": gpt_response
        }
        
        return func.HttpResponse(
            json.dumps(output_message),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(
            f"An error occurred: {str(e)}",
            status_code=500
        )

@app.route(route="HttpTriggerGPT3", auth_level=func.AuthLevel.ANONYMOUS)
def HttpTriggerGPT3(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function (GPT-3) processed a request.')

    try:
        req_body = req.get_json()
        if not req_body or 'prompt' not in req_body:
            return func.HttpResponse(
                "Please pass a JSON body with a 'prompt' key in the request.",
                status_code=400
            )

        gpt_response = openai_helper.get_openai_response(req_body['prompt'], model="gpt-3.5-turbo")
        
        output_message = {
            "model": "gpt-3.5-turbo",
            "original_prompt": req_body['prompt'],
            "gpt_response": gpt_response
        }
        
        return func.HttpResponse(
            json.dumps(output_message),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(
            f"An error occurred: {str(e)}",
            status_code=500
        )