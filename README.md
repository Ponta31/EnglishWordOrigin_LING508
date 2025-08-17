# Word Origin API

(This app is initially built for LING508 in the University of Arizona HLT program.)

## What is this?
This is a Flask-based API where you can enter an English word and retrieve: 
- Origin (etymology)
- Lemma form (dictionary form)
- Part of Speech
- Pronunciation (IPA)
- Definition
- Morphemes
- Example sentence


For more details about endpoints and expected input/output, see [documentation.md](https://github.com/Ponta31/EnglishWordOrigin_LING508/blob/main/documents/documentation.md)



### **How to use**
Please note, in order to use this, you will need to take the following steps.

1. Clone the git repository:
`git clone https://github.com/Ponta31/EnglishWordOrigin_LING508.git`
`cd EnglishWordOrigin_LING508`
1. Start MySQL and the app: `docker-compose up`
1. Run Flask: `python routes.py`
2. go to http://localhost:5000
1. Follow the directions there.
1. Send a get request, and you may now see the word info.

