from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from src.analysis.vulnerability import NeighborhoodData, score_neighborhoods, scores_to_dataframe

app = typer.Typer(help="HeatWatch - Urban heat island analysis for climate adaptation")
console = Console()

VERSION = "0.1.0"

SAMPLE_DATA: dict[str, list[NeighborhoodData]] = {
    "detroit": [
        NeighborhoodData(name="West Pullman",  lst_mean=42.1, lst_p90=46.0, tree_cover_pct=4.0,  pct_elderly=18.0, pct_no_ac=22.0, geometry_id="west_pullman"),
        NeighborhoodData(name="Englewood",     lst_mean=40.5, lst_p90=44.2, tree_cover_pct=6.0,  pct_elderly=21.0, pct_no_ac=28.0, geometry_id="englewood"),
        NeighborhoodData(name="Midtown",       lst_mean=36.0, lst_p90=39.5, tree_cover_pct=22.0, pct_elderly=12.0, pct_no_ac=10.0, geometry_id="midtown"),
        NeighborhoodData(name="Lincoln Park",  lst_mean=31.8, lst_p90=34.0, tree_cover_pct=58.0, pct_elderly=9.0,  pct_no_ac=5.0,  geometry_id="lincoln_park"),
    ],
    "phoenix": [
        NeighborhoodData(name="Downtown Phoenix", lst_mean=48.2, lst_p90=52.1, tree_cover_pct=3.0,  pct_elderly=11.0, pct_no_ac=8.0,  geometry_id="downtown_phoenix"),
        NeighborhoodData(name="South Mountain",   lst_mean=46.5, lst_p90=50.3, tree_cover_pct=5.0,  pct_elderly=16.0, pct_no_ac=12.0, geometry_id="south_mountain"),
        NeighborhoodData(name="Camelback East",   lst_mean=43.0, lst_p90=47.0, tree_cover_pct=14.0, pct_elderly=13.0, pct_no_ac=6.0,  geometry_id="camelback_east"),
        NeighborhoodData(name="Ahwatukee",        lst_mean=39.5, lst_p90=43.0, tree_cover_pct=28.0, pct_elderly=18.0, pct_no_ac=4.0,  geometry_id="ahwatukee"),
    ],
}

SUPPORTED_CITIES = sorted(SAMPLE_DATA.keys())


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
    city: str = typer.Option("detroit", "--city", "-c", help=f"City to analyze. Supported: {', '.join(SUPPORTED_CITIES)}"),
    output: Path = typer.Option(None, "--output", "-o", help="Export results to CSV file"),
) -> None:
    """Run heat vulnerability analysis for a city."""
    city = city.lower().strip()

    if city not in SAMPLE_DATA:
        console.print(f"[red]Unknown city:[/red] {city}")
        console.print(f"Supported cities: {', '.join(SUPPORTED_CITIES)}")
        raise typer.Exit(code=1)

    console.print(f"[bold]Analyzing heat vulnerability for:[/bold] {city.title()}")

    scores = score_neighborhoods(SAMPLE_DATA[city])

    table = Table(title=f"Heat Vulnerability Scores - {city.title()}")
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
    """List all supported sample cities."""
    console.print("[bold]Supported cities:[/bold]")
    for c in SUPPORTED_CITIES:
        console.print(f"  {c}")


if __name__ == "__main__":
    app()
