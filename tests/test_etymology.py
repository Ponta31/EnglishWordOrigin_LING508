from model.etymology import *

def test_etymology():
    root1 = Root(morpheme='re', meaning='again')
    root2 = Root(morpheme='voke', meaning='to call')

    etym = Etymology(
        origin_and_history="revokeの語源は、ラテン語の「revocare」に由来しています。この言葉は、「re-」（再、逆）と「vocare」（呼ぶ、呼び戻す）という二つの部分から成り立っています。「re-」は「戻す」という意味を持ち、「vocare」は「呼ぶ」という意味を持つため、合成すると「呼び戻す」や「再び呼ぶ」という意味になります。英語においては、revokeは、一度与えられた権利や許可を取り消すこと、または無効にすることを示しています。この概念は元々の語源に通じており、何かを再び呼び戻すというニュアンスが反映されています。したがって、法的な文脈や契約の取り消しに関してよく使われる言葉となっています。",
        roots=[root1, root2]
    )

    assert etym.origin_and_history.startswith("revokeの語源は")
    assert etym.roots[0].morpheme == 're'
    assert etym.len(etym.roots) == 2




