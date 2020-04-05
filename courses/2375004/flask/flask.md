# Serverové aplikace 

## flask, jinja (+ SQLAlchemy a WTForms)

## Než začneme
Než začneme, doporučuji vytvořit si prázdné virtuální prostředí (já ho obvykle pojmenovávám ".venv"):

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

Tento postup platí obvykle pro učivatele windows, pokud používáte Ubuntu (či jinou distribuci linux), považuji vás za pokročilé a určitě si vytvořit a aktivovat virtuální prostředí zvládnete.

## Úvodem

### Co to vůbec flask je?
Na internetu bychom se dočetli něco jako: *"Flask is microweb framework for building websites in python"*. My se na to můžeme zatím dívat jako na knihovnu, s jejíž pomocí v pythonu vytvoříme jednoduchou webovou aplikaci.

### Proč flask a ne django?
Django je super framework, pro naše účely je ale lepší flask, protože je jednodušší a lehčí.

### Věnujte prosím pozornost oficiálním stránkám (a hlavně dokumentaci)

- [Flask](https://flask.palletsprojects.com/)
- [Jinja](https://jinja.palletsprojects.com/)

### Tutoriály
Na internetu existuje mnoho tutoriálů, nebojte se na některé podívat, jsou dle mého názoru dostačující, doporučuji například:
  - [Flask Tutorial #1](https://www.youtube.com/watch?v=mqhxxeeTbu0) - velice podobný příklad budeme dělat také
Nebojte se klidně vybrat jiný, který Vám bude připadat lepší. 

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

## HTML a Jinja
Pokud jste si o flasku něco četly, už víte, že flask obvykle zajišťuje *backend* naší serverové aplikace. To znamená, že flask se stará o to, co běží na straně serveru. V našem případě se flask stará o všechno, co se stane, když pošleme request?
1. Vygeneruje se *request*:
    například http://127.0.0.1:5000/home
2. Flask ví, že když dostane tento request, má spustit funkci *home* (to jsme my naprogramovali)
3. Funkce *home* vrátí string "Hello world!"
4. Náš prohlížeč nějak interpretuje (v tomhle případě jako jednoduchý string) to, co dostane zpátky jako odpověd na náš request. 

Perfektní, teď můžeme klidně vrátit HTML stránku, stejně jako string, k tomu slouží funkce [render_template](https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template) (přečtěte si dokumentaci).

### Druhá aplikace - simpleapp
Naše druhá aplikace bude celá složka:
    - [Odkaz na složku](simpleapp/)
Teď je důležité, abyste zkopírovali celý obsah složky. Spustíme naši aplikaci s názvem "simpleapp"

```
python simpleapp.py
```

Znovu by se mělo objevit něco jako:
```
 * Serving Flask app "simpleapp" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 231-816-225
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Otevřete webový prohlíčeč a zkuste zadat:
- http://127.0.0.1:5000/home

Porovnejte s tím, když otevřete ve webovém prohlížeci soubor "templates/home.html", liší se nějak?

Nyní zkuste zadat:
- http://127.0.0.1:5000/jinja/adam
- http://127.0.0.1:5000/jinja/jan

Porovnejte s tím, když otevřete ve webovém prohlížeci soubor "templates/jinja.html", liší se nějak?

Na druhém příkladu je demonstrováno, k čemu *Jinja* vlastně je. Dokáže vzít něco (v našem případu string *response*) a vložit ho do html na místo {{ response }} (složené závorky tam jsou proto, aby "jinja věděla co má kam vložit").

Jinja samozřejmě umí mnohem, mnohem víc, viz oficialní dokumentace.

## Domácí úkol

Následující domácí úkol je sice kvůli samostudiu obtížnější, ale schválně jsem ho volil tak, abyste velmi podobné řešení nalezli na internetu. Prosím, pokuste se to nejdříve nastudovat a vyřešit sami. Pokud Vám to nepůjde, zrecyklujte nějaké řešení na internetu, převeďte ho do češtiny a hlavně se ho snažte pochopit.

Doma si nastudujte:
  - [SQLAlchemy](https://www.sqlalchemy.org/) a pojem **ORM**, klasické SQL příkazy nebudete potřebovat, ale můžete si osvěžit, jak SQL datábaze funguje
  - [WTForms](https://wtforms.readthedocs.io/en/stable/) (formuláře a jak fungují)
  - [Bootstrap](https://getbootstrap.com/) (volitelné, pouze koho zajímá i frontend aplikace a chce lepší design)

Naprogramujte webovou aplikaci **sklad** s pomocí knihoven flask, SQLAlchemy a WTForms (případně dalších):
  - Tato aplikace bude obsahovat formulář s potvrzovacím tlačítkem.
  - Pomocí formuláře budete moct přidat do skladu (SQL databáze) položku, každá položka bude reprezentována minimálně **jménem** a **počtem kusů** (můžete přidat i více, například materiál, datum zařazení do skladu, ...)
  - Po přidání položky do skladu se pod formulářen aktualizuje HTML tabulka, ve které budou vidět všechny položky skladu (je to domácí úkol, předpokládejme, že tam nebudete zadávat více než pár položek)
  - (volitelné) ke každé položce přidejte i tlačítko **DELETE**, která danou položku odstraní.

I když je to proti konvencím, prosím, naprogramujte celou aplikaci do **jednoho skriptu**, lépe se to prochází a kontroluje.
