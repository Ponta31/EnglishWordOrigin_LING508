# Word Origin API

This API allows you to retrieve information about English words, including their lemma form, meaning (in Japanese), pronunciation (IPA), etymology (in Japanese), morphemes, and example sentences.  

---

## Lookup a Word 

You can look up an English word info using the "Lookup a word" interface. Enter an English word such as `revoked` in the box and click "Submit". The page will display the info for that word as a JSON string, for example

```json
{
  "origin": "revokeの語源は、ラテン語の「revocare」に由来しています。この言葉は、「re-」（再、逆）と「vocare」（呼ぶ、呼び戻す）という二つの部分から成り立っています。「re-」は「戻す」という意味を持ち、「vocare」は「呼ぶ」という意味を持つため、合成すると「呼び戻す」や「再び呼ぶ」という意味になります。英語においては、revokeは、一度与えられた権利や許可を取り消すこと、または無効にすることを示しています。この概念は元々の語源に通じており、何かを再び呼び戻すというニュアンスが反映されています。したがって、法的な文脈や契約の取り消しに関してよく使われる言葉となっています。",
  "lemma_form": "revoke",
  "definition": "正式に取り消す",
  "example_sentence": "The government decided to revoke the license.",
  "pos": "verb",
  "morphemes": [
    {"form": "re", "gloss": "again", "id": 3},
    {"form": "voc", "gloss": "call", "id": 4}
  ],
  "pronunciation": {"ipa": "rɪˈvoʊk"}
}
```

The API can be called directly without the UI, using a GET request. The endpoint is http://localhost:5000/entries/<surface_form>, where <surface_form> can be any English word that you want to lookup, for example revoked, play, or abruptly.

### Example request

**httpie**  
```http GET http://localhost:5000/entries/revoked```  
```http GET http://localhost:5000/entries/play```  
```http GET http://localhost:5000/entries/abruptly```

