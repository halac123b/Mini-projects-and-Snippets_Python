from mle.function import *
import mle.function.data
import textwrap

def process_report(requirement: str, suggestions: dict):
    return textwrap.dedent(f"""
        {requirement}

        [green]Dataset Summary:[/green] {suggestions.get('data_summary')}

        [green]Suggestion Summary:[/green] {suggestions.get('suggestion')}

        [green]Task:[/green] {suggestions.get('task')}
        [green]Model:[/green] {suggestions.get('model_or_algorithm')}
        [green]Training Strategy:[/green] {suggestions.get('training_method')}
        [green]Evaluation Metric:[/green] {suggestions.get('evaluation_metric')}
        [green]Training Device:[/green] {suggestions.get('device')}

        [green]Serving Strategy:[/green] {suggestions.get('serving_method')}

        [green]Reference:[/green] {suggestions.get('reference')}
        [green]Dependency:[/green] {suggestions.get('frameworks')}
    """).strip()

class AdviseAgent:
    def __init__(self, model, console=None, mode='normal'):
        pass