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