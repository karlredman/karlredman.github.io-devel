# dev repo for https://karlredman.github.io github pages

## Notes:
* Static files for github are stored in `docs/`
* Use the build directory to populate the github repo for the site
* The project is split into to parts:
    * production: karlredman.github.io
    * development: karlredman.github.io-devel

## Run the Development environment

1. cd to `<project root>/`
2. switch to python 3 (if needed)
    ```
    pyenv local <version>
    ```
3. setup virtual environment for development and testing
    ```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.py
    ```
4. Prepare the site
  * setup localized package

  ```
  pip install -e .
  ```

5. run the site 1 of 2 ways
    * via flask
      * set environment for flask runtime

      ```
      export FLASK_APP=appx
      export FLASK_ENV=developmentx
      ```

      * run flask
      ```
      flask run
      ```

    * run the included script
    ```
    ./app.py
    ```

## Building the static site

* building
```
# files will be in `docs/`
./app.py build
```

* review the static site
```
pip install twisted
twistd -n web --port tcp:5000 --path docs/
```
