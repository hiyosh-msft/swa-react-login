import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = 'https://swa-frontdoor-fedze3gzh6fpabhw.b01.azurefd.net/'

    return func.HttpResponse(url, headers={'Location': url},status_code=302)