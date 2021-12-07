# python API via fastapi

To run helloworld app, got to `src/warehouse_app` and directly run `helloworld.py`, for example in terminal:

```
python helloworld.py
```

To run warehouse app, go to `src` and run `hypercorn_server` as module:

```
python -m hypercorn_server
```

Outpus hould look something like this:

```
[2021-12-06 23:03:02 +0100] [24628] [INFO] Running on http://127.0.0.1:8000 (CTRL + C to quit)
```