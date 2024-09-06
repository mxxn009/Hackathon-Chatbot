# Hackathon-Chatbot

This is a Chatbot which we made for booking tickets, it can respond but currently it cannot store user information, feel free to contribute.

To use the chatbot:
Clone this repository and change directory to the cloned repository and then follow the steps mentioned below:
1. Make a virtual environment using the command
```
python3 -m venv venv
```

2. Activate the virtual environment using the command
```
 . venv/Scripts/activate.bat (for windows)
```

3. Install dependencies
   
```
(venv) pip install Flask torch torchvision nltk
```

5. Install nltk package

```
      (venv) python
      >>> import nltk
      >>> nltk.download('punkt')
```
6. Modify intents.json according to your requirement
7. Run
   
```
(venv) python train.py
```
9. This will create data.pth file, Run the following command to test it in your console

```
(venv) python chat.py
```
or directly run 
```
(venv) app.py
```
