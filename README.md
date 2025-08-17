# Word Origin API

(This app is initially built for LING508 in the University of Arizona HLT program.)

You can enter an English word and retrieve the information, not only the origin, but also dictionary form of the word, Part of Speech, Pronunciation(IPA), definition, morphemes, and an example sentence. 


For an English word "revoked", you will get:

```
"origin": "revokeの語源は、ラテン語の「revocare」に由来しています。この言葉は、「re-」（再、逆）と「vocare」（呼ぶ、呼び戻す）という二つの部分から成り立っています。「re-」は「戻す」という意味を持ち、「vocare」は「呼ぶ」という意味を持つため、合成すると「呼び戻す」や「再び呼ぶ」という意味になります。英語においては、revokeは、一度与えられた権利や許可を取り消すこと、または無効にすることを示しています。この概念は元々の語源に通じており、何かを再び呼び戻すというニュアンスが反映されています。したがって、法的な文脈や契約の取り消しに関してよく使われる言葉となっています。"
"lemma_form": "revoke",
"definition": "正式に取り消す"
"example_sentence": "The government decided to revoke the license."
"pos": "verb"
"morphemes": [{"form": "re", "gloss": "again", "id": 3 },
              {"form": "voc", "gloss": "call", "id": 4 }]
"pronunciation": {"ipa": "rɪˈvoʊk"}
```

For more details about the functionality of the Flask API, including endpoints and expected input/output, see [documentation.md]()


Please note, in order to use this you will need to take the following steps.

Clone the git repository.
run a local server python -m http.server
docker-compose up
go to http://localhost:5000
Follow the directions there, or reference the hyperlinked http://localhost:5000
Send a post request via the generate a database section.
You may now search the senses of a given word.

