Scripts are compatible with python version 3.x and the packages listed in the file *requirements.txt*.

To install all required packages in a virtual environment, run the following in terminal from the *exploratory_notebook/* level:

```
$ python3 -m pyenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

To start the notebook server, add the line

```
$ jupyter notebook
```
