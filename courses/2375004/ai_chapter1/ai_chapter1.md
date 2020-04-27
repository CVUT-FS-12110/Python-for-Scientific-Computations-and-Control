# Umělá inteligence a python - část první

## Úvod

Sousloví *umělá inteligence* rozhodně patří mezi tzv. *buzzwords*. Každý někdy slyšel *průmysl 4.0*, ale málokdo si umí představit, co se tím myslí. Podobně je na tom umělá inteligence, jejíž základy jsou mnohem starší, než jen posledních 15 let neuronových sítí, o kterých jistě slýcháte v televizi.

Právě proto tato lekce nemá suplovat průřez historie a teorie umělé inteligence, ale spíš vám ukázat, co je v pythonu (často s pomocí užitečných knihoven) možné. Kdybychom měli naprogramovat příklad pro každou podoblast tak širokého pole, jakým umělá inteligence je, nestačil by nám pravděpodobně celý semestr. Pro studenty, kteří se pro AI nadchnou vřele doporučuji posloupnost přednášek z MIT:
[MIT open coursware - AI](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/), tyto přednášky jsou sice z roku 2010, ale myslím si, že je to pořád to nejlepší, co lze na internetu nalézt.

Já jsem se rozhodl, že se podíváme na 3 příklady ze třech podoblastí AI. Budou poměrně jednoduché, ale dle mého názoru hlavně názorné.

## Genetické algoritmy

Genetické algoritmy (nebo někdy taky evoluční algoritmy) jsou jednoduše takové algoritmy, které se snaží napodobit evoluci. Pamatujete si ještě mitózu a meiózu? A co mutace a crossing-over? Cokoliv vás v této souvislosti napadne a je inspirované přírodou se dá považovat za genetický algoritmus.

- [příklad 1 - genetický algoritmus](genetic.ipynb)

## Fuzzy systém

Dalším příkladem bude fuzzy systém, který stojí na zajímavé matematice fuzzy množin (fuzzy znamená neostrý). Na následujícím příkladu uvidíte, že se pomocí fuzzy systému dá aproximovat dynamika proslulé [rovnice Mackey-Glass](http://www.scholarpedia.org/article/Mackey-Glass_equation).

- [příklad 2 - fuzzy systém Mackey-Glass](fuzzymackeyglass.ipynb)

Pokud byste se chtěli dozvědět více o fuzzy systémech a fuzzy řízení, doporučuji knížku *A Course in Fuzzy Systems and Control*. Nejsem si však jistý, jestli je přístupná v PDF verzi zdarma ke stažení, pokud by nebyla a opravdu by měl někdo zájem, napište mi email.

## Perceptron

Posledním příkladem bude *perceptron*, který pravděpodobně nemusím představovat:

- [příklad 3 - perceptron](perceptron.ipynb)











## Úvod

Optimalizace je snaha o nalezení maxima nebo minima *účelové funkce*. V praxi se s optimalizací setkáte hodně často. Pokud budete například vyrábět papírové krabičky, budete chtít aby se co nejvíce krabiček vyrobilo z co nejméně papíru.

Typicky se optimalizace už dlouhou dobu používá při jakémkoli plánování (například kdy má a kdy nemá běžet blok uhelné elektrárny, kdy a na jakém stroji se má jaký díl vyrobit), nebo také jakou trasou má projet zásobovací vůz, aby spálil co nejméně benzínu (nebo aby byl co nejrychlejší). Úloh je nepřeberné množství a jako budoucí inženýři se dříve či později s optimalizací v nějaké podobě potkáte. 


## Příklad 1 - Svařované krabičky

První úloha bude velmi jednoduchá. Ve skutečnosti nebudete potřebovat nic víc, než tužku a papír. My si ale řešení naprogramujeme jako velmi jednoduchý notebook (můžete jako jenom skript, jestliže pracujete s příkazové řádky), nebudeme zatím potřebovat žádné speciální knihovny, kromě numpy a matplotlib.

- [příklad 1 - krabičky](boxes.ipynb)


## Příklad 2 - začínáme s cvxpy (lineární programování)

Lineární programovaní je velmi jednoduchým nástrojem pro optimalizaci problémů, které se dají v jazyce LP formulovat. Doporučuji anglickou wikipedii a samozřejmě dokumentaci:
- [wiki](https://en.wikipedia.org/wiki/Linear_programming)
- [cvxpy - dokumentace](https://www.cvxpy.org/) 

Náš první příklad bude notorická úloha na optimalizaci složení psích granulí. Knihovnu cvxpy **nelze** používat na našem jupyter serveru. Musíte si nainstalovat knihovnu do lokálního virtuální prostředí. Pokud chcete používat jupyter lab i doma, stačí si ho doinstalovat také do virtuálního prostředí a spustit na svém počítači.

-[příklad 2 - psí granule](granule.ipynb)

## Příklad 3 - Optimalizace bloku plynové elektrárny

V následujícím příkladu bude naším úkolem optimalizovat časový průběh (24 hodin) výkonu bloku plynové elektrárny tak, abychom utržili co nejvíce peněz.

-[příklad 3 - blok plynové elektrárny](blok.ipynb)