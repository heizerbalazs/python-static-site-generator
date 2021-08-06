import typer
import ssg.parsers
from ssg.site import Site


def main(source: str = 'content', dest: str = 'dist') -> None:
    config = {
        'source': source,
        'dest': dest,
        'parsers': [ssg.parsers.ResourceParser()]
    }

    Site(**config).build()


typer.run(main)
