#!/usr/bin/env python3
import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'reports' / 'dashboard-bancos-publicos-e-cooperativos-2026-04-11.csv'
OUT_DIR = ROOT / 'site' / 'dashboard-bancos-publicos'
OUT_DIR.mkdir(parents=True, exist_ok=True)

rows = []
with CSV_PATH.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

priority_order = ['Muito alta', 'Alta', 'Média', 'Baixa']
priority_counts = {p: 0 for p in priority_order}
for row in rows:
    if row['Prioridade'] in priority_counts:
        priority_counts[row['Prioridade']] += 1

banks = sorted({row['Banco'] for row in rows})

cards = [
    ('Bancos mapeados', str(len(banks))),
    ('Sinais catalogados', str(len(rows))),
    ('Prioridade muito alta', str(priority_counts['Muito alta'])),
    ('Prioridade alta', str(priority_counts['Alta'])),
]

def chip_class(value: str) -> str:
    value = value.lower()
    if 'muito alta' in value:
        return 'very-high'
    if 'alta' in value:
        return 'high'
    if 'média' in value or 'medio' in value:
        return 'medium'
    return 'low'

rows_html = []
for row in rows:
    rows_html.append(
        '<tr>'
        f'<td>{html.escape(row["Banco"])}</td>'
        f'<td>{html.escape(row["Tema"]).replace("_", " ")}</td>'
        f'<td>{html.escape(row["Fato_relevante"])}</td>'
        f'<td>{html.escape(row["Empresas_citadas"]).replace(";", ", ")}</td>'
        f'<td>{html.escape(row["Tipo_de_vinculo"]).replace("_", " ")}</td>'
        f'<td>{html.escape(row["Impacto_estrategico"])}</td>'
        f'<td>{html.escape(row["Risco_regulatorio_controle"])}</td>'
        f'<td><span class="chip {chip_class(row["Prioridade"])}">{html.escape(row["Prioridade"])}</span></td>'
        f'<td><a href="{html.escape(row["Fonte"])}" target="_blank" rel="noopener noreferrer">fonte</a></td>'
        '</tr>'
    )

bank_list = ''.join(f'<li>{html.escape(bank)}</li>' for bank in banks)
card_html = ''.join(
    f'<div class="card"><div class="card-label">{html.escape(label)}</div><div class="card-value">{html.escape(value)}</div></div>'
    for label, value in cards
)

html_doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dashboard, Bancos Públicos e Cooperativismo Financeiro</title>
  <style>
    :root {{
      --bg: #0b1020;
      --panel: #121933;
      --panel-2: #192347;
      --text: #e8ecf8;
      --muted: #9aa6c7;
      --line: #2b3762;
      --accent: #67e8f9;
      --high: #f59e0b;
      --vhigh: #ef4444;
      --medium: #10b981;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif; background: linear-gradient(180deg, #0b1020, #10172f 30%, #0b1020); color: var(--text); }}
    .wrap {{ max-width: 1400px; margin: 0 auto; padding: 32px 20px 56px; }}
    .hero {{ display: grid; gap: 12px; margin-bottom: 24px; }}
    h1 {{ margin: 0; font-size: 34px; line-height: 1.1; }}
    .subtitle {{ color: var(--muted); font-size: 16px; max-width: 980px; }}
    .meta {{ color: var(--muted); font-size: 13px; }}
    .grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin: 24px 0; }}
    .card {{ background: rgba(18, 25, 51, 0.9); border: 1px solid var(--line); border-radius: 16px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.22); }}
    .card-label {{ color: var(--muted); font-size: 13px; margin-bottom: 8px; }}
    .card-value {{ font-size: 30px; font-weight: 700; }}
    .layout {{ display: grid; grid-template-columns: 320px 1fr; gap: 18px; align-items: start; }}
    .panel {{ background: rgba(18, 25, 51, 0.9); border: 1px solid var(--line); border-radius: 16px; padding: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.22); }}
    .panel h2 {{ margin: 0 0 14px; font-size: 18px; }}
    .panel h3 {{ margin: 18px 0 10px; font-size: 14px; color: var(--accent); text-transform: uppercase; letter-spacing: .04em; }}
    ul {{ margin: 10px 0 0 18px; padding: 0; }}
    li {{ margin: 8px 0; color: #d6def5; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{ padding: 12px 10px; border-bottom: 1px solid var(--line); vertical-align: top; text-align: left; }}
    th {{ position: sticky; top: 0; background: #101937; z-index: 2; font-size: 12px; letter-spacing: .02em; color: #b9c5e4; text-transform: uppercase; }}
    tr:hover td {{ background: rgba(103, 232, 249, 0.03); }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .chip {{ display: inline-block; padding: 6px 10px; border-radius: 999px; font-size: 12px; font-weight: 700; white-space: nowrap; }}
    .chip.very-high {{ background: rgba(239, 68, 68, 0.18); color: #fecaca; border: 1px solid rgba(239, 68, 68, 0.35); }}
    .chip.high {{ background: rgba(245, 158, 11, 0.18); color: #fde68a; border: 1px solid rgba(245, 158, 11, 0.35); }}
    .chip.medium {{ background: rgba(16, 185, 129, 0.18); color: #bbf7d0; border: 1px solid rgba(16, 185, 129, 0.35); }}
    .downloads {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }}
    .btn {{ display: inline-flex; align-items: center; gap: 8px; padding: 10px 14px; background: var(--panel-2); border: 1px solid var(--line); color: var(--text); border-radius: 12px; }}
    .btn:hover {{ background: #20305f; text-decoration: none; }}
    .table-wrap {{ max-height: 72vh; overflow: auto; border: 1px solid var(--line); border-radius: 14px; }}
    .small {{ color: var(--muted); font-size: 12px; }}
    @media (max-width: 1100px) {{
      .layout {{ grid-template-columns: 1fr; }}
      .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 720px) {{
      .grid {{ grid-template-columns: 1fr; }}
      h1 {{ font-size: 28px; }}
      .wrap {{ padding: 20px 14px 36px; }}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <div class="meta">Publicado em 2026-04-11 · versão web do radar estratégico</div>
      <h1>Dashboard, bancos públicos, regionais e cooperativismo financeiro</h1>
      <div class="subtitle">Radar executivo com foco em tecnologia, IA, conectividade, transformação digital, canais, pagamentos, privacidade, governança e compras de TI em bancos públicos, regionais e no Sicoob.</div>
      <div class="downloads">
        <a class="btn" href="dashboard-bancos-publicos-e-cooperativos-2026-04-11.csv" download>Baixar CSV</a>
        <a class="btn" href="dashboard-bancos-publicos-e-cooperativos-2026-04-11.md" download>Baixar Markdown</a>
      </div>
    </section>

    <section class="grid">{card_html}</section>

    <section class="layout">
      <aside class="panel">
        <h2>Leitura rápida</h2>
        <h3>Prioridade máxima</h3>
        <ul>
          <li>Banco do Brasil</li>
          <li>CAIXA</li>
          <li>BNB</li>
          <li>Sicoob</li>
        </ul>
        <h3>Prioridade alta</h3>
        <ul>
          <li>Banestes</li>
          <li>Banrisul</li>
          <li>BASA</li>
        </ul>
        <h3>Prioridade seletiva</h3>
        <ul>
          <li>BRB</li>
          <li>Banpará</li>
        </ul>
        <h3>Bancos no escopo</h3>
        <ul>{bank_list}</ul>
        <h3>Recorte por fornecedor</h3>
        <ul>
          <li><strong>Huawei:</strong> sinal direto e forte no Banco do Brasil.</li>
          <li><strong>Cisco:</strong> sinal relevante no Banco da Amazônia, especialmente em conectividade e data center.</li>
          <li><strong>H3C:</strong> sem evidência pública forte nesta rodada.</li>
        </ul>
        <div class="small">Observação: o radar privilegia sinais públicos verificáveis, não hipóteses comerciais sem fonte.</div>
      </aside>

      <main class="panel">
        <h2>Base estruturada</h2>
        <div class="small">Tabela com fatos relevantes, empresas citadas, impacto estratégico, risco regulatório/controle, prioridade e link de fonte.</div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Banco</th>
                <th>Tema</th>
                <th>Fato relevante</th>
                <th>Empresas citadas</th>
                <th>Tipo de vínculo</th>
                <th>Impacto</th>
                <th>Risco</th>
                <th>Prioridade</th>
                <th>Fonte</th>
              </tr>
            </thead>
            <tbody>
              {''.join(rows_html)}
            </tbody>
          </table>
        </div>
      </main>
    </section>
  </div>
</body>
</html>
'''

(OUT_DIR / 'index.html').write_text(html_doc, encoding='utf-8')
(OUT_DIR / 'dashboard-bancos-publicos-e-cooperativos-2026-04-11.csv').write_text(CSV_PATH.read_text(encoding='utf-8'), encoding='utf-8')
md_path = ROOT / 'reports' / 'dashboard-bancos-publicos-e-cooperativos-2026-04-11.md'
(OUT_DIR / 'dashboard-bancos-publicos-e-cooperativos-2026-04-11.md').write_text(md_path.read_text(encoding='utf-8'), encoding='utf-8')

print(json.dumps({
    'out_dir': str(OUT_DIR),
    'rows': len(rows),
    'banks': len(banks),
    'files': ['index.html', 'dashboard-bancos-publicos-e-cooperativos-2026-04-11.csv', 'dashboard-bancos-publicos-e-cooperativos-2026-04-11.md']
}, ensure_ascii=False))
