from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from src.analysis.vulnerability import score_neighborhoods, scores_to_dataframe
from src.utils.city_registry import list_cities, load_city, get_city_meta

app = typer.Typer(help="HeatWatch - Urban heat island analysis for climate adaptation")
console = Console()

VERSION = "0.1.0"


@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(False, "--version", "-v", help="Show version and exit"),
    ctx: typer.Context = typer.Argument(None),
) -> None:
    if version:
        console.print(f"heatwatch {VERSION}")
        raise typer.Exit()


@app.command()
def analyze(
    city: str = typer.Option("detroit", "--city", "-c", help="City ID to analyze (see: heatwatch cities)"),
    output: Path = typer.Option(None, "--output", "-o", help="Export results to CSV file"),
) -> None:
    """Run heat vulnerability analysis for a city."""
    city = city.lower().strip()

    try:
        neighborhoods = load_city(city)
        meta = get_city_meta(city)
    except KeyError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(code=1)

    display_name = f"{meta['name']}, {meta['country']}" if meta['country'] else meta['name']
    console.print(f"[bold]Analyzing heat vulnerability for:[/bold] {display_name}")

    scores = score_neighborhoods(neighborhoods)

    table = Table(title=f"Heat Vulnerability Scores - {display_name}")
    table.add_column("Neighborhood")
    table.add_column("Risk Tier")
    table.add_column("Composite Score")
    table.add_column("LST Mean (C)")
    table.add_column("Tree Cover %")

    for s in scores:
        table.add_row(
            s.neighborhood,
            s.risk_tier,
            str(round(s.composite_score, 1)),
            str(round(s.lst_mean, 1)),
            str(round(s.tree_cover_pct, 1)),
        )

    console.print(table)

    if output:
        df = scores_to_dataframe(scores)
        df.to_csv(output, index=False)
        console.print(f"Results exported to [bold]{output}[/bold]")


@app.command()
def cities() -> None:
    """List all cities available in the registry."""
    city_ids = list_cities()
    table = Table(title="Available Cities")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Country")
    table.add_column("Region")
    table.add_column("Coordinates")

    for city_id in city_ids:
        meta = get_city_meta(city_id)
        table.add_row(
            city_id,
            meta["name"],
            meta["country"],
            meta["region"],
            meta["coordinate_system"],
        )

    console.print(table)


if __name__ == "__main__":
    app()
