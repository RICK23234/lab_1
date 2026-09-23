from toolkit.__main__ import main


def test_cli_calc_success(capsys):
    assert main(["calc", "3+6-8"]) == 0
    assert capsys.readouterr().out.strip() == "1"


def test__cli_calc_unsuccess(capsys):
    assert main(["calc", "2+a"]) == 2
    assert capsys.readouterr().err != ""


def test_cli_convert_success(capsys):
    assert main(["convert", "2000", "--from", "g", "--to", "kg"]) == 0
    assert capsys.readouterr().out.strip() == "2.0"


def test_cli_convert_unsuccess(capsys):
    assert main(["convert", "2000", "--from", "g", "--to", "m"]) == 2
    assert capsys.readouterr().err != ""


def tets_cli_help(capsys):
    assert main(["--help"]).value.code == 0
