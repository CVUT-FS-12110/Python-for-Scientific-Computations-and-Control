from fastapi import FastAPI

app = FastAPI()

@app.get("/", response_model=dict)
def hello_world():
    return {"message": "Hello world!", "note": "This is my first API endpoint."}

if __name__ == "__main__":
    import asyncio
    import hypercorn
    from hypercorn.asyncio import serve

    print("I am about to serve you web application!")
    
    app_config = hypercorn.config.Config()
    # change serve parameters here
    app_config.use_reloader = True
    asyncio.run(serve(app, app_config))
