CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL UNIQUE,
    country_language TEXT NOT NULL,
    country_capital TEXT NOT NULL
);

INSERT INTO countries (country_name, country_language, country_capital) VALUES
('Switzerland', 'German', 'Bern'),
('Sweden', 'Swedish', 'Stockholm'),
('Ukraine', 'Ukrainian', 'Kyiv'),
('Italy', 'Italian', 'Rome'),
('Netherlands', 'Dutch', 'Amsterdam'),
('Israel', 'Hebrew', 'Jerusalem'),
('Portugal', 'Portuguese', 'Lisbon'),
('Austria', 'German', 'Vienna'),
('Denmark', 'Danish', 'Copenhagen'),
('United Kingdom', 'English', 'London'),
('Azerbaijan', 'Azerbaijani', 'Baku');


CREATE TABLE competitions (
    competition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competition_year INTEGER NOT NULL UNIQUE,
    hosting_country_id INTEGER NOT NULL,
    FOREIGN KEY (hosting_country_id) REFERENCES countries (country_id)
);

INSERT INTO competitions (competition_year, hosting_country_id) VALUES
(2024, 2),
(2023, 10),
(2022, 4),
(2021, 5),
(2019, 6),
(2018, 7),
(2017, 3),
(2016, 2),
(2015, 8),
(2014, 9),
(2013, 2),
(2012, 11);

CREATE TABLE songs (
    song_id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name TEXT NOT NULL,
    song_language TEXT NOT NULL,
    singer TEXT NOT NULL
);

INSERT INTO songs (song_name, song_language, singer) VALUES
('The Code', 'English', 'Nemo'),
('Tattoo', 'English', 'Loreen'),
('Stefania', 'Ukrainian', 'Kalush Orchestra'),
('Zitti e buoni', 'Italian', 'Måneskin'),
('Arcade', 'English', 'Duncan Laurence'),
('Toy', 'English', 'Netta'),
('Amar pelos dois', 'Portuguese', 'Salvador Sobral'),
('1944', 'English/Ukrainian', 'Jamala'),
('Heroes', 'English', 'Måns Zelmerlöw'),
('Rise Like a Phoenix', 'English', 'Conchita Wurst'),
('Only Teardrops', 'English', 'Emmelie de Forest'),
('Euphoria', 'English', 'Loreen');

CREATE TABLE results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competition_id INTEGER NOT NULL,
    winning_country_id INTEGER NOT NULL,
    song_id INTEGER NOT NULL,
    FOREIGN KEY (competition_id) REFERENCES competitions (competition_id),
    FOREIGN KEY (winning_country_id) REFERENCES countries (country_id),
    FOREIGN KEY (song_id) REFERENCES songs (song_id)
);

INSERT INTO results (competition_id, winning_country_id, song_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 3, 8),
(9, 2, 9),
(10, 8, 10),
(11, 9, 11),
(12, 2, 12);


SELECT
    c.competition_year AS "Competition Year",
    hc.country_name AS "Hosting Country",
    wc.country_name AS "Winning Country",
    wc.country_language AS "Country Language",
    s.song_name AS "Song Name",
    s.song_language AS "Song Language",
    wc.country_capital AS "Country Capital",
    s.singer AS "Singer"
FROM
    results AS r
JOIN
    competitions AS c ON r.competition_id = c.competition_id
JOIN
    countries AS hc ON c.hosting_country_id = hc.country_id
JOIN
    countries AS wc ON r.winning_country_id = wc.country_id
JOIN
    songs AS s ON r.song_id = s.song_id

