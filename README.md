# dev repo for https://karlredman.github.io github pages

## TODO:
* create sitemap

## Notes:
* Static files for github are stored in `docs/`
* Use the build directory to populate the github repo for the site
* The project is split into to parts:
    * production: karlredman.github.io
    * development: karlredman.github.io-devel

## howto generate the static site from the flask application:
1. cd to `flask_site/`
2. switch to python 3 (if needed)
    ```
    pyenv local 3.6.5
    ```
3. setup virtual environment for development and testing
    ```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.py
    ```
4. build the site
    ```
    # Note: this will delete the contents of app/build
    python ./application.py build
    ```
5. files will be in `docs/`

6. test host the site
```
twistd -n web --port tcp:5000 --path .
```

## run the development site:

```
python application.py
```

## upload active to github karlredman.github.io

1. copy static output to the site clone
2. git commit and push
