CREATE DATABASE en_jp;
ALTER DATABASE en_jp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE en_jp;


SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;
SET character_set_client = utf8mb4;
SET character_set_connection = utf8mb4;
SET collation_connection = utf8mb4_unicode_ci;


CREATE TABLE lexical_entry (
    id INT NOT NULL AUTO_INCREMENT,
    lemma_form VARCHAR(30),
    PRIMARY KEY (id)
);


CREATE TABLE meanings (
    id INT AUTO_INCREMENT,
    lexical_entry_id INT NOT NULL,
    pos ENUM('verb', 'noun', 'adjective'),
    definition NVARCHAR(150),
    example_sentence VARCHAR(150),
    PRIMARY KEY (id),
    FOREIGN KEY (lexical_entry_id) REFERENCES lexical_entry(id)
);

CREATE TABLE pronunciation (
    lexical_entry_id INT,
    ipa NVARCHAR(30),
    PRIMARY KEY (lexical_entry_id),
    FOREIGN KEY (lexical_entry_id) REFERENCES lexical_entry(id)
);

CREATE TABLE etymology (
    id INT AUTO_INCREMENT,
    lexical_entry_id INT,
    origin TEXT CHARACTER SET utf8mb4, #I modified here
    PRIMARY KEY (id),
    FOREIGN KEY (lexical_entry_id) REFERENCES lexical_entry(id)
);

CREATE TABLE morpheme (
    id INT AUTO_INCREMENT,
    form VARCHAR(30),
    gloss VARCHAR(30),
    PRIMARY KEY (id)
);

CREATE TABLE etymology_morpheme (
    etymology_id INT,
    morpheme_id INT,
    PRIMARY KEY (etymology_id, morpheme_id),  /*These two id can keep uniqueness*/
    FOREIGN KEY (etymology_id) REFERENCES etymology(id),
    FOREIGN KEY (morpheme_id) REFERENCES morpheme(id)
);

/*
CREATE TABLE mnemonic (
    id INT AUTO_INCREMENT,
    meaning_id INT,
    ja_sentence TEXT,
    sentence_vector VECTOR,
    similarity_to_lemma FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY (meaning_id) REFERENCES meanings(id)

);
*/

INSERT INTO lexical_entry
    (lemma_form)
VALUES
    ('abrupt'),
    ('revoke'),
    ('play')
;


INSERT INTO pronunciation
    (lexical_entry_id, ipa)
VALUES
    (1, N'əˈbrʌpt'),
    (2, N'rɪˈvoʊk'),
    (3, N'pleɪ')
;


INSERT INTO meanings
    (lexical_entry_id, pos, definition, example_sentence)
VALUES
    (1, 'adjective', N'突然の', 'The car came to an abrupt stop.'),
    (2, 'verb', N'正式に取り消す', 'The government decided to revoke the license.'),
    (3, 'verb', N'遊ぶ、演奏する', 'The children play in the park.'),
    (3, 'noun', N'演劇、遊び', 'They watched a play at the theater.');
;


INSERT INTO etymology
    (lexical_entry_id, origin)
VALUES
    (1,N'abruptの語源は、ラテン語の「abruptus」から来ています。この言葉は「ab-」という接頭辞と「rumpere」という動詞に由来します。「ab-」は「離れて」や「反対に」という意味を持ち、「rumpere」は「破る」や「壊す」という意味を表します。したがって、元々「abruptus」は「壊れることから離れる」、すなわち「突然の」「途切れた」というニュアンスを持つ言葉でした。中世ラテン語を経て、英語に取り入れられた際には、意味がより具体的に「急に」「無骨に」といった形で使われるようになりました。特に、物事の進行が突然止まる様子や、道が急に変わる状況を示す言葉として定着しています。現在では、会話や文章において、人々や出来事が予告なしに変化する様子を表現するのに使われます。'),
    (2,N'revokeの語源は、ラテン語の「revocare」に由来しています。この言葉は、「re-」（再、逆）と「vocare」（呼ぶ、呼び戻す）という二つの部分から成り立っています。「re-」は「戻す」という意味を持ち、「vocare」は「呼ぶ」という意味を持つため、合成すると「呼び戻す」や「再び呼ぶ」という意味になります。英語においては、revokeは、一度与えられた権利や許可を取り消すこと、または無効にすることを示しています。この概念は元々の語源に通じており、何かを再び呼び戻すというニュアンスが反映されています。したがって、法的な文脈や契約の取り消しに関してよく使われる言葉となっています。'),
    (3,N'playの語源は、古英語の「plegian」に由来しています。この言葉は「遊ぶ」「楽しむ」といった意味を持っており、さらにその起源はゲルマン語派の言葉にさかのぼります。たとえば、古ノルド語の「plegja」やオランダ語の「plegen」が同じルーツを持ちます。これらの言葉は、もともと「遊び」や「戯れ」といった行為を指していました。また、「play」は古代から、人々が楽しみながら行うさまざまな活動や娯楽を表すために使われてきました。例えば、スポーツや演劇、音楽など、多くの文化において「play」は重要な要素でした。そのため、言葉としての「play」は、人間の文化や生活の中で非常に重要な役割を果たしてきたと言えます。今日でも「play」は遊びや創造的な活動を示す言葉として広く使われています。')
;


INSERT INTO morpheme
    (form, meaning)
VALUES
    ('ab', 'off, away'),
    ('rupt', 'break'),
    ('re', 'again'),
    ('voc', 'call')
;


INSERT INTO etymology_morpheme
    (etymology_id, morpheme_id)
VALUES
    (1,1),
    (1,2),
    (2,3),
    (2,4)
;


