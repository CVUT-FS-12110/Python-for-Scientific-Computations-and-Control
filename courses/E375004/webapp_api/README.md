# Web service - chapter 1

We will design very simple backend of web application using `FastAPI`
(`starlette` and `pydantic` under the hood). It may look hard but do not worry,
almost all heavy lifting will be done by usefull python libraries for us. Lets
begin with basic simplified scheme of our project:

![simplified-webapp-scheme](docs/backend_scheme.drawio.svg)

You need to understand what `HTTP message` is and what it consists of. We have
two types of `HTTP message`: `HTTP request` and `HTTP response`:

![simplified-HTTP-message](docs/http_scheme.drawio.svg)

`HTTP request` consists of three main parts:
1. `method` + `url` (for example `method` is `POST` and `url` is `warehouse/23`)
2. `headers` (we do not care about headers right now - just some metadata)
3. `body` (for us this is `json` we are sending)

`HTTP response` consists of three main parts as well:
1. `status line` - for us, important is only `status code`, you already know `404` (Not Found) and `200` (Success or OK)
2. `headers` (again we do not care much about headers right now - just some metadata)
3. `body` (for us this is `json` we are getting as result)

## Running this web service

For running the service (make sure, you are in the folder `webapp_api`) run
`hypercorn_server` as python module:

```
python -m hypercorn_server
```

Output should look:

```
[2022-04-03 14:00:04 +0200] [17932] [INFO] Running on http://127.0.0.1:8000 (CTRL + C to quit)
```

Our FastAPI web application is now being served by hypercorn and is reachable 
on `localhost` port: `8000`.