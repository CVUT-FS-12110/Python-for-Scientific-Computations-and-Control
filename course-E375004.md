# Python for Scientific Computations and Control 
## Codenames: E375004, 2375004

## [Classification](courses/classification.md)

## Note

In case of getting error while accessing jupyter notebooks from our repository, use https://nbviewer.org and provide the link to the notebook you need to open. This is unfortunately not an error on our side and we cannot do anything about that.

## Sylabus

1. **Python Basics 1** - installation, IDEs, data types, for, while, if, functions (Week 26 February - 1 March)

   - Notebook a) [intro](courses/intro.md)
   - Notebook b) [Program flow](courses/E375004/python_basics_1/basics_01.ipynb)
   - task: [Caesar cipher encryption](https://github.com/CVUT-FS-12110/Python-for-Scientific-Computations-and-Control/blob/master/tasks/EN_Caesar_cipher_encryption.ipynb)
   - responsible person: martin.vitousek@fs.cvut.cz
   
2. **Python Basics 2** - functions, classes, files and venv (Week 4 March - 8 March)

   - study any introduction to Python classes, for example: [W3Schools](https://www.w3schools.com/python/python_classes.asp) (easy to understand) or [Python docs](https://docs.python.org/3/tutorial/classes.html) (more detailed)
   - Notebook a) [Advanced functions](courses/E375004/python_basics_2/basics_02a_functions_adv.ipynb)
   - Notebook b) [Classes and objects](courses/E375004/python_basics_2/basics_02b_oop.ipynb)
   - Notebook c) [File manipulation](courses/E375004/python_basics_2/basics_02c_files.ipynb)
   - Notebook d) [Virtual environment](courses/E375004/python_basics_2/basics_02d_venv.ipynb)
   - task: [Rock, paper, scissors](https://github.com/CVUT-FS-12110/Python-for-Scientific-Computations-and-Control/tree/master/tasks/rock_paper_scissors)
   - responsible person: martin.vitousek@fs.cvut.cz

3. **Math and visualization** - work with packages: numpy, scipy, matplotlib - linear algebra, calculus, graphs (Week 11 March - 15 March)

   - Notebook: [numpy, scipy, matplotlib](courses/E375004/numpy_matplotlib/numpy_matplotlib.ipynb)
   - task: [image convolution](tasks/convolution/EN_numpy_convolution_filter.ipynb)
   - responsible person: michal.kuchar@fs.cvut.cz

4. **Sympy - Equations of Motion** (Week 18 March - 22 March)

   - [Introduction](courses/E375004/sympy/introduction.md)
   - task: Derive an equation / set of equations that require derivatives to be taken
   - responsible person: juraj.lieskovsky@fs.cvut.cz

5. **Convex optimization** (Week 25 March - 29 March)

   - [Introduction](courses/E375004/optimization/introduction.md)
   - task: Solve an optimization problem of your chooosing
   - responsible person: juraj.lieskovsky@fs.cvut.cz

6. **Model Predictive Control** (Weeks 25 March - 12 April)

   - [Introduction](courses/E375004/model_predictive_control/introduction.md)
   - task: None
   - responsible person: juraj.lieskovsky@fs.cvut.cz

7. **Simulation of mechanical systems using Mujoco** (Week 8 April - 12 April)

   - Controlled Cart-Pole
      - [LQR](courses/E375004/mujoco/cartpole_control_LQR.ipynb)
      - [MPC](courses/E375004/mujoco/cartpole_control_MPC.ipynb)
   - task: None
   - responsible person: juraj.lieskovsky@fs.cvut.cz

8. **Data processing and visualization using pandas** (Week 15 April - 19 April)

   - Notebook a) [tabular data, pandas](courses/E375004/data_pandas/basics_01.ipynb)
   - Notebook b) [COVID data example](courses/E375004/data_pandas/basics_02.ipynb)
   - Interactive graphs using plotly: [plotly_example](courses/E375004/data_pandas/visualization.ipynb)
   - task: [covid data](tasks/EN_pandas_covid_2.ipynb)
   - responsible person: michal.kuchar@fs.cvut.cz


9. **Asyncio** (Week 22 April - 26 April)

   - Notebook: [asyncio](courses/E375004/asyncio/asyncio.ipynb)
   - task: [CTUSS Commander](tasks/ctuss_commander/README.md)
   - responsible person: martin.vitousek@fs.cvut.cz


10. **Artificial Intelligence I.** (Week 29 April - 3 May)

    - Source codes: [start-here](courses/E375004/ai_chapter1/ai_chapter1.md)
    - responsible person: adam.peichl@fs.cvut.cz


11. **Artificial Intelligence II.** (Week 6 May - 10 May)

    - Source codes: [start-here](courses/E375004/ai_chapter2/ai_chapter2.md)
    - responsible person: michal.kuchar@fs.cvut.cz
    - task: [Activation Functions](tasks/EN_Activation_Functions.ipynb)


12. **Web app using Streamlit** (Week 13 May - 17 May)

    - Source codes: [streamlit folder:](courses/E375004/streamlit)
    - responsible person: michal.kuchar@fs.cvut.cz

13. **Requests, database, API** (Week 20 May - 24 May)

    - Using HTTP protocol: [Requests](courses/E375004/requests_api_db/requests.ipynb)
    - Building own API: [FastAPI](courses/E375004/requests_api_db/fastapi.ipynb)
    - Exploring database: [sqlite](courses/E375004/requests_api_db/sqlite_db.ipynb)
    - Example application: [user_register](courses/E375004/requests_api_db/user_register.ipynb)
    - Complete lecture code in one file: [main.py](courses/E375004/requests_api_db/main.py)
        - run with `fastapi dev main.py`
    - responsible person: martin.vitousek@fs.cvut.cz
