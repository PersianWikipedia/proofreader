This repository hosts the code for the backend API of the proofreader Gadget used on Persian Wikipedia (also known as اشتباه‌یاب). You can read more about the gadget on [وپ:اشتباه‌یاب on Persian Wikipedia](https://fa.wikipedia.org/wiki/ویکی‌پدیا:اشتباه‌یاب)

## Develop

For local development and testing, create a python virtual envinroment and install the required packages. If you use the name `venv` for the virtual environment directory, it will be ignored by git.

```
python -m venv venv
. ./venv/bin/activate
pip install -r Requirements.txt
```

One of the packages is `hunspell` and on most machines, installing it requires installing an upstream package. For Linux machines, the requirement is called `libhunspell` and can be installed by running a command like `sudo apt install libhunspell-dev`

## Deploy

Only those with Maintainer access to the associated Toolforge tool can deploy or update this tool. The list of Maintainers is accessible at https://toolsadmin.wikimedia.org/tools/id/persian-typos

### Initial Setup

The code must be deployed as a webservice on the [Toolforge k8s cluster](https://wikitech.wikimedia.org/wiki/Help:Toolforge/Kubernetes). The Python source code (i.e. this repo) must be placed in `~/www/python/src` and the Python virtual environment must be created in `~/www/python/venv` for the code to run successfully as a webservice.

To simplify the process, a read-only clone of this repository can be found in `~/git/proofreader`. In the `~/git/proofreader` subdirectory, run `git pull` to pull the latest version of the code.

Copy the latest code from `~/git/proofreader` into the deployment directory `~/www/python/src`

Start the webservice using `toolforge webservice python3.11 start`

As new versions of Python are enabled on Toolforge, you may wish to `stop` the webservice and `start` it again using the newer versions of Python.

### Deploying Updates

On toolforge, become the tool account: `become persian-typos zsh`

In the `~/git/proofreader` subdirectory, run `git pull` to pull the latest version of the code.

Copy the latest code from `~/git/proofreader` into the deployment directory `~/www/python/src`

Restart the webservice by running `toolforge webservice restart`

Check to make sure the deployed code is working, e.g. by accessing [وپ:اشتباه‌یاب/تست on Persian Wikipedia](https://persian-typos.toolforge.org/check/وپ:اشتباه‌یاب/تست)

Note that webservice errors are logged in `~/uwsgi.log`