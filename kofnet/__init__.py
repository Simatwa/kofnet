import re
import requests

from importlib import metadata

try:
    __version__ = metadata.version("kofnet")
except metadata.PackageNotFoundError:
    __version__ = "1.0.0"

__repo__ = "https://github.com/Simatwa/kofnet"

__info__ = "Extract SNI bug host for different ISPs based on country"

__author__ = "Smartwa"

__all__ = ["Hunter", "Manipulator"]


class Hunter:
    """Hunt SNI bugs for different countries"""

    url = "https://kofnet.co.za/sni-bug-host-generator/"

    def __init__(self, contents: str = None, url: str = ""):
        """Constructor

        Args:
            contents (str, optional): Html Contents. Defaults to None.
            url (str, optional): url to replace the generator link at the extracted SNIs. Defaults to "".
        """
        self.html_content = contents
        self.url = url
        self.update_contents()

    def update_contents(self, ignore_check: bool = False) -> str:
        """Fetch new html contents

        Args:
            ignore_check (bool, optional): Ignore cache check instead fetch new content. Defaults to False.

        Returns:
            str: html contents
        """
        if not ignore_check and self.html_content is not None:
            return self.html_content
        else:
            resp = requests.get(self.url, timeout=20)
            resp.raise_for_status()
            self.html_content = resp.text
            return resp.text

    def get_countries_code_map(self) -> dict[str, str]:
        """Extract codes and their corresponding countries.

        Returns:
            dict[str, str]: code : country
        """
        code_countries: str = re.findall(
            r"var\sisoCountries=(\{[^{}]*\})", self.html_content
        )[0]
        code_countries_2: list[tuple[str, str]] = re.findall(
            r'([A-Z]{2}):"(\w*|[\w\s]*)"',
            code_countries,
        )
        cache = {}
        for code, country in code_countries_2:
            cache[code] = country

        return cache

    def get_code_sni_map(self) -> dict[str, str]:
        """Extract sni bug host mapped with their country codes.

        Returns:
            dict[str, str]: {code : sni}
        """
        code_sni_map = r"data\s*=\s*\{[^{}]*\}"
        hunt = re.findall(code_sni_map, self.html_content)
        target: str = hunt[0]

        results = re.findall(r"\W*([A-Z]{2}):\W*`([\w\W][^`]*)\W*", target)

        cache = {}
        for code, sni in results:
            sanitized_sni = re.sub(r"</?a[^>]*>", self.url, sni)
            cache[code] = sanitized_sni

        return cache


class Manipulator(Hunter):
    """Manipulate country, code and sni of `Hunter` class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cached = {
            "country_code": self.get_countries_code_map(),
            "code_sni": self.get_code_sni_map(),
        }

    def update_cache(self):
        """Fetch new html contents and update cache"""
        self.update_contents(ignore_check=True)
        self.cached["country_code"] = self.get_countries_code_map()
        self.cached["code_sni"] = self.get_code_sni_map()

    def get_country(self, code: str, default: str = None) -> str | None:
        """Convert country code to country name

        Args:
            code (str): Country abbreviation.
            default (str): Default counrry name to be returned. Default to None

        Returns:
            str|None: Country name.
        """
        return self.cached["country_code"].get(code, default)

    def get_sni(self, code: str) -> str:
        """Get SNI for a particular  country by code

        Args:
            code (str): Country code

        Returns:
            str|None: SNI bug
        """
        return self.cached["code_sni"][code]


if __name__ == "__main__":
    run = Manipulator(open("assets/kofnet-cache1.html", "r").read())
    a = run.get_code_sni_map()
    while True:
        try:
            print(run.get_sni(input(">>")))
        except KeyError:
            print("No Match!")
