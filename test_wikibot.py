from mylib.bot import scrape
from wikibot import cli
from click.testing import CliRunner


def test_bot():
    name = ("facebook",)
    result = scrape(name)
    assert result is not None, f"The scrape function returned none for '{name}'"
    assert (
        "facebook" in result
    ), f"The name '{name} is not found:; in the scraped result"


def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(cli, ["--topic", "facebook"])
    assert result.exit_code == 0
    assert "facebook" in result.output
