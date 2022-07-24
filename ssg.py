import typer

from ssg.site import Site
import ssg.parsers

def main(source="content", dest="dist", parsers=[ssg.parsers.ResourceParse()]):
    config = {"source": source, "dest": dest}

    Site(**config).build()

typer.run(main)