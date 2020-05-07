# Umělá inteligence a python - část druhá

## Úvodem

V první kapitole jsme se si ukázali 3 různé jednoduché příklady. Dnešní hodina se bude zabývat pouze *neuronovými sítěmi*. Mějte ovšem na paměti, že umělá inteligence není to samé, jako neuronové sítě. Neuronové sítě jsou pouze podmnožinou.

Díky pythonu je vývoj a implementace neuronovýc sítí velice jednoduchá a programátorsky přátelská. Na pár řádcích kódu je možné implementovat struktury, které jsou poměrně složité a to díky několika užitečným rámcům (*framworks*) jakou jsou například:
- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)

My budeme využívat *Tensorflow* a částečně i keras (jehož API využívá právě Tensorflow). Uvidíte, že vytvořit a vyzkoušet si model je opravdu jednoduché.


## SOM - Samo-organizační mapy

První neuronovou sítí, kterou si ukážeme bude tzv. *SOM* ([odkaz-wiki](https://en.wikipedia.org/wiki/Self-organizing_map)).

- [příklad 1 - SOM](SOM.ipynb)

## MLP - Multilayer perceptron

Druhým příkladem neuronové sítě bude tzv. *MLP* ([odkaz-wiki](https://en.wikipedia.org/wiki/Multilayer_perceptron)). V minulé hodině jsme si ukazovali perceptron. Tato síť je vytvořená z mnoha a mnoha těchto neuronových jednotek zařazených do jednotlivých vrstev (*layer*). 

Abychom si částečně usnadnili práci a také mohli pěkně vizualizovat výsledky, náš úkol bude klasifikace ručně psaných číslic ([MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database)). Tento dataset se používá jako *hodnotící* u spousty navrhovaných modelů, je dobře prozkoumaný a naleznete ho v každém druhém tutorialu na youtube.

- [příklad 2 - MLP](mnist_MLP.ipynb)

## CNN - Konvoluční neuronové sítě

Posledním příkladem bude tzv. *CNN* ([odkaz-wiki](https://en.wikipedia.org/wiki/Convolutional_neural_network)). Tento typ sítě se používá pro klasifikaci obrázků (nejenom, ale hlavně).

Použijeme opět MNIST dataset, porovnejte počet parametrů sítí a jak rychle se učí. Která z těchto dvou sítí (MLP, CNN) dosahuje větší přesnosti na validační množině?

- [příklad 3 - CNN](mnist_CNN.ipynb)