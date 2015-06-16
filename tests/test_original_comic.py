from xkcd_types import TypesREPL

xkcd_tests = [
    ('2+"2"', '"4"'),
    ('"2"+[]', '"[2]"'),
    ('(2/0)', 'NaN'),
    ('(2/0)+2', 'NaP'),
    ('"" + ""', '\'"+"\''),
    ('[1,2,3]+2', 'FALSE'),
    ('[1,2,3]+4', 'TRUE'),
    ('2/(2-(3/2+1/2))', 'NaN.000000000000013'),
    ('RANGE(" ")', '''('"', "!", " ", "!", '"')'''),
    ('+ 2', '12'),
    ('2+2', 'DONE'),
    ('RANGE(1,5)', '(1, 4, 3, 4, 5)'),
    ('FLOOR(10.5)', '''|
|
|
|_ _ _10.5_ _ _ '''),
]


def test_original_comic():
    repl = TypesREPL()
    for case, expected in xkcd_tests:
        assert repl.enter_command(case) == expected
