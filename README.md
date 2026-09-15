# tryPreCommitPackage
Trying out the Python pre-commit package. Seeing how it works with the uv package manager.

Note that the ruff checks are only done if python files are updated in the commit.

Note also that there is a hidden file, .pre-commit-config.yaml, that controls
the setup of the pre-commit hook (see the end of setup_uv.sh).

It assumes that ```uv``` is installed.

To use it :

* Run setup_uv.sh which is the rough equivalent of pip install, and sets up precommit (uv is *fast*)
* Optionally, run start_server.sh and look at the (minimal, hard coded) JSON it serves out in a browser
  at [http://localhost:8004/static-dict](http://localhost:8004/static-dict) or the documentation
  at [http://localhost:8004/docs](http://localhost:8004/docs)
* Edit the_fast_api.py and change the line ```"firstName": "Niles",``` to ```"firstName": "Miles",```
* With this error introduced, try to commit the change with
  ```git commit -a -m "This will not work"```
  That commit will fail due to the introduced error which is detected in the tests in ```test_suite.py```


