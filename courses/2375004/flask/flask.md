# Serverové aplikace
## flask, SQLAlchemy, jinja, html

## Než začneme
Než začneme, doporučuji vytvořit si prázdné virtuální prostředí (já jsem zvyklý pojmenovávat ho ".venv"):

```
python -m venv .venv
```

Aktivujeme ho:

```
/.venv/Scripts/activate
```

Nainstalujeme knihovnu flask:

```
pip install flask
```

## Úvodem

### Co to vůbec flask je?
Na internetu bychom se dočetli něco jako: *"Flask is microweb framework for building websites in python"*. My se na to můžeme zatím dívat jako na knihovnu, s jejíž pomocí v pythonu vytvoříme jednoduchou webovou aplikaci.

### Proč flask a ne django?
Django je super framework, pro naše účely je ale lepší flask, protože je jednodušší a lehčí. Pravdou ale je, že bychom měli mít povědomí o tom, že to není jedinný framework a že nemusí být nutně ani ten nejlepší.

### Věnujte prosím pozornost oficiálním stránkám

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

### Tutoriály



## Hello world!
Naše první aplikace bude jenom jeden .py skript:
    - [flask Hello World!](helloworld/helloworld.py)

Zkuste si ji spustit a nastudovat:

```
python helloworld.py
```

V příkazové řádce byste měli vidět něco jako:

```
 * Serving Flask app "helloworld" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 231-816-225
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Naše aplikace helloworld tedy běží na localhostu.

Otevřete webový prohlíčeč a zkuste zadat:
- http://127.0.0.1:5000/home
- http://127.0.0.1:5000/greetings/adam
- http://127.0.0.1:5000/greetings/eva

Jak server reaguje, a proč?










