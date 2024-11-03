<h1 align="center">
<a href="https://kofnet.co.za/sni-bug-host-generator/">Kofnet</a>

</h1>

> Extract SNI bug host for different ISPs based on country.

The bug hosts are extracted from https://kofnet.co.za/sni-bug-host-generator/

---

## Installation

   ```sh
   git clone https://github.com/Simatwa/kofnet.git
   cd kofnet
   pip install -r requirements.txt
   pip install .
   ```

---

## Usage

```python
from kofnet import Hunter
# Extract codes and their corresponding countries.
hunter = Hunter()

hunter.get_countries_code_map()

# Extract sni bug host mapped with their country codes.
hunter.get_code_sni_map()
```

---

The package also features out of the box CLI:

<details>

<summary>

`$ kofnet --help`

</summary>

```
Usage: kofnet [OPTIONS] COMMAND [ARGS]...

  Extract SNI bug host for different ISPs based on country

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  cache    Download and save the html contents
  country  Get List of a country and their corresponding codes
  sni      Get SNI bug host for a particular country|code

```

</details>

---

<h2 align="center">Disclaimer</h2>

This software is designed to extract information regarding potential Server Name Indication (SNI) bugs from the website kofnet.co.za. It is intended for use by security researchers, IT professionals, and individuals interested in improving web security.

### Limitations and Assumptions

- The accuracy of the extracted data depends on the current state and configuration of the target website. Changes to the website may affect the results.
- This tool assumes that the user has legal permission to perform scans or tests on the target website. Unauthorized scanning or testing activities may violate local laws and regulations.
- The tool does not guarantee the discovery of all possible vulnerabilities related to SNI bugs. Its effectiveness is subject to the specific characteristics of the target website.

### Usage Restrictions

- Users must comply with all applicable laws and regulations when using this tool, including but not limited to privacy laws, data protection laws, and cybersecurity laws.
- The tool should only be used for legitimate purposes such as security research, penetration testing, or authorized vulnerability assessments.
- Misuse of this tool, including but not limited to unauthorized scanning, spamming, or attempting to exploit discovered vulnerabilities without proper authorization, is strictly prohibited.

### Liability

- The authors and maintainers of this software disclaim any liability for damages resulting directly or indirectly from the use of this tool.
- Users acknowledge that they use this tool at their own risk and agree to hold harmless the authors and maintainers of this software against any claims or damages arising from its use.

> [!WARNING]
> This tool is intentionally **NOT** published on pypi and **NO** one should.