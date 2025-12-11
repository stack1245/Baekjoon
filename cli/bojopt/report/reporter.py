from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


class Reporter:
    def __init__(self):
        self.console = Console()
    
    def print_header(self, filepath, language):
        header_text = Text()
        header_text.append("BOJ 코드 최적화 분석 결과\n", style="bold cyan")
        header_text.append(f"파일: {filepath}\n", style="white")
        header_text.append(f"언어: {language.upper()}", style="yellow")
        
        panel = Panel(header_text, border_style="cyan")
        self.console.print(panel)
        self.console.print()
    
    def print_complexity(self, complexity):
        complexity_text = Text()
        complexity_text.append("예상 시간 복잡도: ", style="bold white")
        
        if "n^3" in complexity or "n^4" in complexity:
            complexity_text.append(complexity, style="bold red")
        elif "n^2" in complexity:
            complexity_text.append(complexity, style="bold yellow")
        else:
            complexity_text.append(complexity, style="bold green")
        
        self.console.print(Panel(complexity_text, border_style="blue"))
        self.console.print()
    
    def print_issues(self, issues):
        if not issues:
            self.console.print("[bold green]✓ 발견된 최적화 이슈가 없습니다![/bold green]")
            return
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("심각도", style="dim", width=12)
        table.add_column("라인", justify="right", width=8)
        table.add_column("메시지", width=60)
        
        severity_styles = {
            'warning': '[bold red]⚠ WARNING[/bold red]',
            'suggestion': '[bold yellow]💡 SUGGESTION[/bold yellow]',
            'info': '[bold blue]ℹ INFO[/bold blue]'
        }
        
        sorted_issues = sorted(issues, key=lambda x: (
            {'warning': 0, 'suggestion': 1, 'info': 2}.get(x['severity'], 3),
            x['line']
        ))
        
        for issue in sorted_issues:
            severity_text = severity_styles.get(issue['severity'], '[white]UNKNOWN[/white]')
            line_text = str(issue['line']) if issue['line'] > 0 else '-'
            
            table.add_row(
                severity_text,
                line_text,
                issue['message']
            )
        
        self.console.print(table)
        self.console.print()
    
    def print_summary(self, issues):
        warnings = sum(1 for i in issues if i['severity'] == 'warning')
        suggestions = sum(1 for i in issues if i['severity'] == 'suggestion')
        infos = sum(1 for i in issues if i['severity'] == 'info')
        
        summary_text = Text()
        summary_text.append("분석 요약: ", style="bold white")
        
        if warnings > 0:
            summary_text.append(f"{warnings} 경고", style="bold red")
        if suggestions > 0:
            if warnings > 0:
                summary_text.append(" | ", style="white")
            summary_text.append(f"{suggestions} 제안", style="bold yellow")
        if infos > 0:
            if warnings > 0 or suggestions > 0:
                summary_text.append(" | ", style="white")
            summary_text.append(f"{infos} 정보", style="bold blue")
        
        if warnings == 0 and suggestions == 0 and infos == 0:
            summary_text.append("이슈 없음", style="bold green")
        
        self.console.print(Panel(summary_text, border_style="white"))
    
    def print_error(self, message):
        self.console.print(f"[bold red]오류: {message}[/bold red]")
