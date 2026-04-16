from tabulate import tabulate


def render_table(rows: list[dict]) -> str:
    return tabulate(rows, headers="keys", tablefmt="github")
