import click
import kofnet
import tabulate


@click.command()
@click.option(
    "-i", "--input", type=click.File(), help="Path to html contents to read from."
)
def country(input: click.File):
    """Get List of countries and their corresponding codes"""
    run = kofnet.Manipulator(input.read() if input else None)
    click.secho(
        tabulate.tabulate(
            [
                [str(count), code_country[0], code_country[1]]
                for count, code_country, in enumerate(
                    run.get_countries_code_map().items(), start=1
                )
            ],
            headers=["No.", "Code", "Country"],
            tablefmt="fancy_grid",
        ),
        color="cyan",
    )


@click.command()
@click.option(
    "-i", "--input", type=click.File(), help="Path to html contents to read from."
)
@click.argument("key", required=True)
def sni(input: click.File, key: str):
    """Get SNI bug host for a particular country|code"""
    run = kofnet.Manipulator(input.read() if input else None)
    try:
        if len(key) == 2:
            click.secho(run.get_sni(key))
        else:
            code_country = run.get_countries_code_map()
            country_code = dict(
                zip(tuple(code_country.values()), tuple(code_country.keys()))
            )
            click.secho(run.get_sni(country_code[key]))
    except KeyError:
        click.secho(f"Key '{key} didn't match any country/code", fg="yellow")


@click.command()
@click.argument("output", type=click.Path(dir_okay=False, resolve_path=True))
def cache(output):
    """Download and save the html contents"""
    run = kofnet.Hunter()
    run.update_contents()
    click.secho(f"Saving contents to '{output}'")
    with open(output, "w") as fh:
        fh.write(run.html_content)


def main():
    @click.group()
    @click.version_option(kofnet.__version__, package_name="kofnet")
    def run():
        """Extract SNI bug host for different ISPs based on country"""
        pass

    run.add_command(country)
    run.add_command(sni)
    run.add_command(cache)
    try:
        run()
    except Exception as e:
        click.secho(
            f"Quitting due to {e.args[1] if e.args and len(e.args)>1 else e}", fg="red"
        )


if __name__ == "__main__":
    main()
