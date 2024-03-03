# firebase_tutorial

A firebase tutorial project that allows accessing the functions described in the getting started document of Firebase here: https://firebase.google.com/docs/functions/get-started?gen=2nd#python

# How to run?

Follow the steps in the getting started document.

Here is a summary of steps to take (commands to be executed from the terminal locally):

* Install Firebase and make sure that locally it runs well e.g., via `firebase --version`;
* Configure a Firebase project in the web interface;
* Create a Python version 3.11 `venv` environment in the directory where the `main.py` source file is (note: issues came up when trying to run Firebase locally with Python 3.10);

For example, using `fish` shell, this could look like:

```fish
python3.11 -m venv venv
source venv/bin/activate.fish
```

* Install the required Python dependencies:
```fish
pip install -r requirements.txt
```
* Start up the Firebase emulator via `firebase emulators:start --debug`;

The output of this command should output the URLs where each of the services are running locally.

* Update the `send_request.py` Python script with the URL of where `addmessage`
  Firebase function is accepting requests and update the request parameter with
  the text that you would like to be sent to the locally running Firebase function;
* Send the HTTP request by exectuing the Python script: `python send_request.py`;
* Check what the Firestore service URL was when the emulator startup command
  was executed, visit in the web browser and check if the message was received
  and turned into upper case letters too.
