# Python for Scientific Computations and Control 
## Codenames: E375004, 2375004

## [Classification](courses/classification.md)

## Note

In case of getting error while accessing jupyter notebooks from our repository, use https://nbviewer.org and provide the link to the notebook you need to open. This is unfortunately not an error on our side and we cannot do anything about that.

## Sylabus
The classes are designed as workshops. The lecturer shows you a tutorial in the first 90 minutes and the other 90 minutes is for your own work on given tasks. The lecturer is there for consultation.

0. **Course introduction** - Course information, Python installation, IDEs, "Hello World" (Week 16 February - 20 february)

   - Notebook [intro](courses/intro.md)
   - responsible person: martin.vitousek@fs.cvut.cz

1. **Python Basics 1** - Data types, for, while, if, functions (Week 23 February - 27 February)

   - Notebook [Program flow](courses/E375004/python_basics_1/basics_01.ipynb)
   - task: [Caesar cipher encryption](https://github.com/CVUT-FS-12110/Python-for-Scientific-Computations-and-Control/blob/master/tasks/EN_Caesar_cipher_encryption.ipynb)
   - responsible person: martin.vitousek@fs.cvut.cz
   
1. **Python Basics 2** - functions, classes, files and venv (Week 2 March - 6 March)

   - study any introduction to Python classes, for example: [W3Schools](https://www.w3schools.com/python/python_classes.asp) (easy to understand) or [Python docs](https://docs.python.org/3/tutorial/classes.html) (more detailed)
   - Notebook a) [Advanced functions](courses/E375004/python_basics_2/basics_02a_functions_adv.ipynb)
   - Notebook b) [Classes and objects](courses/E375004/python_basics_2/basics_02b_oop.ipynb)
   - Notebook c) [File manipulation](courses/E375004/python_basics_2/basics_02c_files.ipynb)
   - Notebook d) [Virtual environment](courses/E375004/python_basics_2/basics_02d_venv.ipynb)
   - task: [Rock, paper, scissors](https://github.com/CVUT-FS-12110/Python-for-Scientific-Computations-and-Control/tree/master/tasks/rock_paper_scissors)
   - responsible person: martin.vitousek@fs.cvut.cz

1. **Math and visualization** - work with packages: numpy, scipy, matplotlib - linear algebra, calculus, graphs (Week 9 March - 13 March)

   - Notebook: [numpy, scipy, matplotlib](courses/E375004/numpy_matplotlib/numpy_matplotlib.ipynb)
   - task: [image convolution](tasks/convolution/EN_numpy_convolution_filter.ipynb)
   - responsible person: michal.kuchar@fs.cvut.cz

1. **Data processing and visualization using pandas** (Week 16 March - 20 March)

   - Notebook a) [tabular data, pandas](courses/E375004/data_pandas/basics_01.ipynb)
   - Notebook b) [COVID data example](courses/E375004/data_pandas/basics_02.ipynb)
   - Interactive graphs using plotly: [plotly_example](courses/E375004/data_pandas/visualization.ipynb)
   - task: [covid data](tasks/EN_pandas_covid_2.ipynb)
   - responsible person: michal.kuchar@fs.cvut.cz

1. **Asyncio** (Week 23 March - 27 March)

   - Notebook: [asyncio](courses/E375004/asyncio/asyncio.ipynb)
   - (optional) task: [CTUSS Commander](tasks/ctuss_commander/README.md)
   - responsible person: martin.vitousek@fs.cvut.cz

1. **Optimisation - linear programming** (Week 30 March - 3 April)

   - Lecture: [start-here](courses/E375004/optimisation/cvxpy.md)
   - (optional) task: [Optimizing phone factory](tasks/EN_cvxpy_factory.ipynb)
   - responsible person: adam.peichl@fs.cvut.cz

1. **CANCELLED** Easter Monday (Weeks 6 April - 10 April)

1. **Sympy - Equations of Motion** (Week 13 April - 17 April)

   - Basics. Point mass and gravity: [notebook 1](courses/E375004/lagrange2eom/lagrangian_point_mass.ipynb)
   - Spring mass damper:  [notebook 2](courses/E375004/lagrange2eom/lagrangian_mass_spring_damper_gravity.ipynb)
   - Pendulum on a cart: [notebook 3](courses/E375004/lagrange2eom/lagrangian_cart_rigid_pendulum_with_force.ipynb)
   - (optional) task: No task this week
   - responsible person: michal.kuchar@fs.cvut.cz

1. **Control of mechanical systems** (Week 20 April - 24 April)

   - Euler solver of pendulum on a cart: [notebook 1](courses/E375004/lagrange2eom/cartpole_solver_tutorial.ipynb)
   - PyGame simulator of a pendulum on a cart: [folder](courses/E375004/control2/)
   - (optional) task: [Stabilize inverted pendulum](tasks/control_2/controller.ipynb)
   - responsible person: michal.kuchar@fs.cvut.cz

1. **Artificial Intelligence I.** (Week 27 April - 1 May)

    - Source codes: [start-here](courses/E375004/ai_chapter1/ai_chapter1.md)
    - Task: No task this week
    - responsible person: adam.peichl@fs.cvut.cz

1. **Artificial Intelligence II.** (Week 4 May - 8 May)

    - Pytorch tutorial repository: [here](https://github.com/CVUT-FS-12110/pytorch-intro/tree/master)
    - responsible person: michal.kuchar@fs.cvut.cz
    - (optional) task: [Design your own neural network](tasks/EN_fashion_mnist_assignment.ipynb)

1. **Requests, database, API** (Week 11 May - 15 May)

    - Using HTTP protocol: [Requests](courses/E375004/requests_api_db/requests.ipynb)
    - Building own API: [FastAPI](courses/E375004/requests_api_db/fastapi.ipynb)
    - Exploring database: [sqlite](courses/E375004/requests_api_db/sqlite_db.ipynb)
    - Example application: [user_register](courses/E375004/requests_api_db/user_register.ipynb)
    - Complete lecture code in one file: [main.py](courses/E375004/requests_api_db/main.py)
        - run with `fastapi dev main.py`
    - responsible person: martin.vitousek@fs.cvut.cz

1. **Web app using Streamlit** (Week 18 May - 22 May)

    - Source codes: [streamlit folder:](courses/E375004/streamlit)
    - responsible person: michal.kuchar@fs.cvut.cz
