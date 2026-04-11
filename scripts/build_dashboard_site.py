#!/usr/bin/env python3
import csv
import html
import json
import re
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / 'reports'
OUT_DIR = ROOT / 'site' / 'dashboard-bancos-publicos'
OUT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATTERN = 'dashboard-bancos-publicos-e-cooperativos-*.csv'
DATE_RE = re.compile(r'dashboard-bancos-publicos-e-cooperativos-(\d{4}-\d{2}-\d{2})\.csv$')

WATCHLIST = [
    {'label': 'Cisco', 'aliases': ['cisco']},
    {'label': 'Huawei', 'aliases': ['huawei']},
    {'label': 'H3C', 'aliases': ['h3c']},
    {'label': 'Fortinet', 'aliases': ['fortinet']},
    {'label': 'HP', 'aliases': ['hp', 'hpe', 'hewlett packard enterprise']},
    {'label': 'Aruba', 'aliases': ['aruba', 'aruba networks', 'hpe aruba']},
    {'label': 'IBM', 'aliases': ['ibm']},
    {'label': 'Check Point', 'aliases': ['check point', 'checkpoint']},
    {'label': 'Palo Alto', 'aliases': ['palo alto', 'palo alto networks']},
    {'label': 'Arista', 'aliases': ['arista', 'arista networks']},
    {'label': 'Juniper', 'aliases': ['juniper', 'juniper networks']},
    {'label': 'Compwire', 'aliases': ['compwire', 'comp wire']},
    {'label': 'Zoom', 'aliases': ['zoom', 'zoom video communications']},
    {'label': 'NTT', 'aliases': ['ntt', 'ntt data']},
    {'label': 'Logicalis', 'aliases': ['logicalis']},
    {'label': 'Teltec', 'aliases': ['teltec']},
    {'label': 'Teletex', 'aliases': ['teletex']},
]


def normalize_text(value: str) -> str:
    value = unicodedata.normalize('NFKD', value or '')
    value = ''.join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower()
    value = re.sub(r'[^a-z0-9]+', ' ', value)
    return re.sub(r'\s+', ' ', value).strip()


VENDOR_MATCHERS = []
for item in WATCHLIST:
    aliases = [item['label'], *item.get('aliases', [])]
    normalized_aliases = sorted({normalize_text(alias) for alias in aliases if normalize_text(alias)}, key=len, reverse=True)
    patterns = [re.compile(rf'(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])') for alias in normalized_aliases]
    VENDOR_MATCHERS.append({'label': item['label'], 'patterns': patterns})


csv_candidates = sorted(REPORTS_DIR.glob(REPORT_PATTERN))
if not csv_candidates:
    raise SystemExit('Nenhum CSV de dashboard encontrado em reports/.')

latest_csv = csv_candidates[-1]
match = DATE_RE.search(latest_csv.name)
report_date = match.group(1) if match else latest_csv.stem.rsplit('-', 1)[-1]
latest_md = REPORTS_DIR / f'dashboard-bancos-publicos-e-cooperativos-{report_date}.md'
if not latest_md.exists():
    raise SystemExit(f'Markdown correspondente não encontrado: {latest_md.name}')

build_timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

rows = []
with latest_csv.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        companies = [part.strip() for part in row['Empresas_citadas'].split(';') if part.strip()]
        normalized_text = normalize_text(' '.join(str(value) for value in row.values()))
        matched_vendors = [
            matcher['label']
            for matcher in VENDOR_MATCHERS
            if any(pattern.search(normalized_text) for pattern in matcher['patterns'])
        ]
        row['__companies'] = companies
        row['__vendors'] = matched_vendors
        rows.append(row)

priority_counts = Counter(row['Prioridade'] for row in rows)
banks = sorted({row['Banco'] for row in rows})
bank_counts = Counter(row['Banco'] for row in rows)
watchlist_counts = Counter(vendor for row in rows for vendor in row['__vendors'])
company_counts = Counter(company for row in rows for company in row['__companies'])
detected_watchlist = [vendor for vendor in WATCHLIST if watchlist_counts[vendor['label']] > 0]

cards = [
    ('Bancos monitorados', str(len(banks))),
    ('Matérias catalogadas', str(len(rows))),
    ('Vendors com sinal', str(sum(1 for vendor in WATCHLIST if watchlist_counts[vendor['label']] > 0))),
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



def source_label(url: str) -> str:
    parsed = urlparse(url)
    host = (parsed.netloc or url).lower().replace('www.', '')
    if parsed.path.lower().endswith('.pdf'):
        return f'{host} (PDF)'
    return host



def compact_url(url: str) -> str:
    parsed = urlparse(url)
    host = (parsed.netloc or url).replace('www.', '')
    path = parsed.path.strip('/')
    if not path:
        return host
    short_path = '/'.join(path.split('/')[:2])
    compact = f'{host}/{short_path}'
    return compact[:72] + '…' if len(compact) > 72 else compact


bank_filter_buttons = [
    '<button class="filter-chip active" type="button" data-filter-kind="bank" data-filter-value="__all__">Todos</button>'
]
for bank in banks:
    bank_filter_buttons.append(
        f'<button class="filter-chip" type="button" data-filter-kind="bank" data-filter-value="{html.escape(bank)}">{html.escape(bank)} <span>{bank_counts[bank]}</span></button>'
    )

vendor_filter_buttons = [
    '<button class="filter-chip active" type="button" data-filter-kind="vendor" data-filter-value="__all__">Todos</button>'
]
for item in WATCHLIST:
    label = item['label']
    extra_class = ' muted-zero' if watchlist_counts[label] == 0 else ''
    vendor_filter_buttons.append(
        f'<button class="filter-chip{extra_class}" type="button" data-filter-kind="vendor" data-filter-value="{html.escape(label)}">{html.escape(label)} <span>{watchlist_counts[label]}</span></button>'
    )

bank_list = ''.join(
    f'<li><button type="button" class="bank-link" data-filter-kind="bank" data-filter-value="{html.escape(bank)}">{html.escape(bank)}</button><span class="bank-count">{bank_counts[bank]}</span></li>'
    for bank in banks
)

vendor_watchlist_items = []
for item in WATCHLIST:
    label = item['label']
    vendor_watchlist_items.append(
        f'<li><button type="button" class="vendor-link" data-filter-kind="vendor" data-filter-value="{html.escape(label)}">{html.escape(label)}</button><span class="bank-count">{watchlist_counts[label]}</span></li>'
    )
vendor_watchlist_list = ''.join(vendor_watchlist_items)

observed_company_list = ''.join(
    f'<li><span class="vendor-label">{html.escape(company)}</span><span class="bank-count">{count}</span></li>'
    for company, count in company_counts.most_common(12)
)

if detected_watchlist:
    vendor_summary_parts = []
    for item in sorted(detected_watchlist, key=lambda item: (-watchlist_counts[item['label']], item['label']))[:6]:
        label = item['label']
        vendor_summary_parts.append(
            f'<li><strong>{html.escape(label)}</strong> aparece em {watchlist_counts[label]} matéria(s) desta base pública.</li>'
        )
    vendor_summary_items = ''.join(vendor_summary_parts)
else:
    vendor_summary_items = '<li>Nenhum vendor da watchlist apareceu explicitamente nesta rodada. A cobertura segue armada para captar o sinal nas próximas atualizações.</li>'

rows_html = []
for row in rows:
    bank = row['Banco']
    priority = row['Prioridade']
    source = row['Fonte']
    row_vendors = row['__vendors']
    row_vendors_attr = html.escape('|'.join(row_vendors))
    vendor_cell = ''.join(
        f'<button type="button" class="vendor-pill" data-filter-kind="vendor" data-filter-value="{html.escape(vendor)}">{html.escape(vendor)}</button>'
        for vendor in row_vendors
    ) or '<span class="small">Sem vendor da watchlist nesta matéria</span>'
    rows_html.append(
        '<tr '
        f'data-bank="{html.escape(bank)}" '
        f'data-priority="{html.escape(priority)}" '
        f'data-vendors="{row_vendors_attr}">'
        f'<td><button type="button" class="table-bank" data-filter-kind="bank" data-filter-value="{html.escape(bank)}">{html.escape(bank)}</button></td>'
        f'<td>{html.escape(row["Tema"]).replace("_", " ")}</td>'
        f'<td>{html.escape(row["Fato_relevante"])}</td>'
        f'<td>{html.escape(row["Empresas_citadas"]).replace(";", ", ")}</td>'
        f'<td><div class="vendor-cell">{vendor_cell}</div></td>'
        f'<td>{html.escape(row["Tipo_de_vinculo"]).replace("_", " ")}</td>'
        f'<td>{html.escape(row["Impacto_estrategico"])}</td>'
        f'<td>{html.escape(row["Risco_regulatorio_controle"])}</td>'
        f'<td><span class="chip {chip_class(priority)}">{html.escape(priority)}</span></td>'
        f'<td><a class="source-link" href="{html.escape(source)}" target="_blank" rel="noopener noreferrer external">'
        f'<span class="source-name">{html.escape(source_label(source))}</span>'
        f'<span class="source-url">{html.escape(compact_url(source))}</span>'
        '</a></td>'
        '</tr>'
    )

card_html = ''.join(
    f'<div class="card" data-card="{html.escape(label)}"><div class="card-label">{html.escape(label)}</div><div class="card-value">{html.escape(value)}</div></div>'
    for label, value in cards
)

style_css = '''
:root {
  --bg: #0b1020;
  --panel: rgba(18, 25, 51, 0.92);
  --panel-2: #192347;
  --text: #e8ecf8;
  --muted: #9aa6c7;
  --line: #2b3762;
  --accent: #67e8f9;
  --accent-2: #38bdf8;
  --high: #f59e0b;
  --vhigh: #ef4444;
  --medium: #10b981;
  --shadow: 0 12px 34px rgba(0,0,0,.24);
}
* { box-sizing: border-box; }
html { color-scheme: dark; }
body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  background: linear-gradient(180deg, #0b1020, #10172f 30%, #0b1020);
  color: var(--text);
}
button, input, select { font: inherit; }
button { cursor: pointer; }
button:focus-visible, a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.wrap { max-width: 1540px; margin: 0 auto; padding: 32px 20px 56px; }
.hero { display: grid; gap: 12px; margin-bottom: 24px; }
h1 { margin: 0; font-size: 34px; line-height: 1.1; }
.subtitle { color: var(--muted); font-size: 16px; max-width: 1040px; }
.meta, .small { color: var(--muted); font-size: 13px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px; margin: 24px 0; }
.card, .panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: var(--shadow);
}
.card { padding: 18px; }
.card-label { color: var(--muted); font-size: 13px; margin-bottom: 8px; }
.card-value { font-size: 30px; font-weight: 700; }
.layout { display: grid; grid-template-columns: 360px 1fr; gap: 18px; align-items: start; }
.panel { padding: 18px; }
.panel h2 { margin: 0 0 14px; font-size: 18px; }
.panel h3 { margin: 18px 0 10px; font-size: 13px; color: var(--accent); text-transform: uppercase; letter-spacing: .06em; }
ul { margin: 0; padding: 0; list-style: none; }
li { color: #d6def5; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.downloads, .filters { display: flex; flex-wrap: wrap; gap: 10px; }
.btn, .filter-chip, .table-bank, .bank-link, .vendor-link, .clear-btn, .vendor-pill {
  border-radius: 12px;
  border: 1px solid var(--line);
}
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: var(--panel-2);
  color: var(--text);
}
.btn:hover { background: #20305f; text-decoration: none; }
.filters { margin: 14px 0 8px; }
.filter-chip {
  background: rgba(25, 35, 71, 0.95);
  color: var(--text);
  padding: 10px 14px;
}
.filter-chip span {
  color: var(--muted);
  font-size: 12px;
  margin-left: 6px;
}
.filter-chip.active, .table-bank:hover, .bank-link:hover, .vendor-link:hover, .clear-btn:hover, .vendor-pill:hover {
  background: rgba(56, 189, 248, 0.16);
  border-color: rgba(103, 232, 249, 0.5);
}
.filter-chip.active { color: #dffaff; }
.muted-zero { opacity: 0.72; }
.bank-list { display: grid; gap: 8px; }
.bank-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.bank-link, .table-bank, .vendor-link {
  background: transparent;
  color: var(--text);
  padding: 8px 10px;
  text-align: left;
}
.bank-link, .vendor-link { width: 100%; }
.table-bank { padding: 6px 10px; }
.bank-count {
  min-width: 24px;
  text-align: center;
  color: var(--muted);
  font-size: 12px;
}
.vendor-label {
  display: inline-flex;
  align-items: center;
  color: var(--text);
}
.controls {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}
.active-filter {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.active-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(56, 189, 248, 0.16);
  border: 1px solid rgba(103, 232, 249, 0.35);
}
.clear-btn {
  padding: 8px 12px;
  background: transparent;
  color: var(--text);
}
.table-wrap {
  max-height: 72vh;
  overflow: auto;
  border: 1px solid var(--line);
  border-radius: 14px;
}
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td {
  padding: 12px 10px;
  border-bottom: 1px solid var(--line);
  vertical-align: top;
  text-align: left;
}
th {
  position: sticky;
  top: 0;
  background: #101937;
  z-index: 2;
  font-size: 12px;
  letter-spacing: .02em;
  color: #b9c5e4;
  text-transform: uppercase;
}
tr:hover td { background: rgba(103, 232, 249, 0.03); }
tr.hidden-row { display: none; }
.source-link {
  display: inline-flex;
  flex-direction: column;
  gap: 4px;
}
.source-name { font-weight: 700; }
.source-url {
  color: var(--muted);
  font-size: 12px;
  word-break: break-all;
}
.vendor-cell {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.vendor-pill {
  padding: 6px 10px;
  background: rgba(25, 35, 71, 0.95);
  color: var(--text);
}
.chip {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
}
.chip.very-high { background: rgba(239, 68, 68, 0.18); color: #fecaca; border: 1px solid rgba(239, 68, 68, 0.35); }
.chip.high { background: rgba(245, 158, 11, 0.18); color: #fde68a; border: 1px solid rgba(245, 158, 11, 0.35); }
.chip.medium { background: rgba(16, 185, 129, 0.18); color: #bbf7d0; border: 1px solid rgba(16, 185, 129, 0.35); }
.chip.low { background: rgba(148, 163, 184, 0.18); color: #dbeafe; border: 1px solid rgba(148, 163, 184, 0.35); }
.summary-list { display: grid; gap: 10px; }
.summary-list li {
  border-left: 3px solid rgba(103, 232, 249, 0.35);
  padding-left: 10px;
}
.empty-state {
  display: none;
  padding: 18px;
  border: 1px dashed var(--line);
  border-radius: 14px;
  color: var(--muted);
  margin-top: 14px;
}
.empty-state.visible { display: block; }
.security-note {
  border-left: 3px solid rgba(16, 185, 129, 0.45);
  padding-left: 10px;
}
@media (max-width: 1200px) {
  .layout { grid-template-columns: 1fr; }
}
@media (max-width: 720px) {
  .grid { grid-template-columns: 1fr; }
  h1 { font-size: 28px; }
  .wrap { padding: 20px 14px 36px; }
  .controls { align-items: flex-start; }
}
'''

app_js = '''
const rows = Array.from(document.querySelectorAll('tbody tr'));
const filterButtons = Array.from(document.querySelectorAll('[data-filter-kind]'));
const resultsCount = document.querySelector('[data-results-count]');
const activeBankLabel = document.querySelector('[data-active-bank-label]');
const activeVendorLabel = document.querySelector('[data-active-vendor-label]');
const emptyState = document.querySelector('[data-empty-state]');
const clearButtons = Array.from(document.querySelectorAll('[data-clear-filter]'));
const cards = {
  banks: document.querySelector('[data-card="Bancos monitorados"] .card-value'),
  rows: document.querySelector('[data-card="Matérias catalogadas"] .card-value'),
  vendors: document.querySelector('[data-card="Vendors com sinal"] .card-value'),
  veryHigh: document.querySelector('[data-card="Prioridade muito alta"] .card-value'),
  high: document.querySelector('[data-card="Prioridade alta"] .card-value'),
};

function getCurrentFilters() {
  const params = new URLSearchParams(window.location.search);
  return {
    bank: params.get('bank') || '__all__',
    vendor: params.get('vendor') || '__all__',
  };
}

function setCurrentFilters(bank, vendor) {
  const params = new URLSearchParams(window.location.search);
  if (!bank || bank === '__all__') {
    params.delete('bank');
  } else {
    params.set('bank', bank);
  }
  if (!vendor || vendor === '__all__') {
    params.delete('vendor');
  } else {
    params.set('vendor', vendor);
  }
  const query = params.toString();
  const nextUrl = `${window.location.pathname}${query ? `?${query}` : ''}`;
  window.history.replaceState({}, '', nextUrl);
}

function splitVendors(row) {
  return (row.dataset.vendors || '').split('|').filter(Boolean);
}

function applyFilters(bank, vendor) {
  const targetBank = bank || '__all__';
  const targetVendor = vendor || '__all__';
  const visibleRows = [];

  rows.forEach((row) => {
    const matchesBank = targetBank === '__all__' || row.dataset.bank === targetBank;
    const rowVendors = splitVendors(row);
    const matchesVendor = targetVendor === '__all__' || rowVendors.includes(targetVendor);
    const matches = matchesBank && matchesVendor;
    row.classList.toggle('hidden-row', !matches);
    if (matches) visibleRows.push(row);
  });

  filterButtons.forEach((button) => {
    const isActive = (button.dataset.filterKind === 'bank' && button.dataset.filterValue === targetBank)
      || (button.dataset.filterKind === 'vendor' && button.dataset.filterValue === targetVendor);
    button.classList.toggle('active', isActive);
  });

  const visibleBanks = new Set(visibleRows.map((row) => row.dataset.bank));
  const visibleVendors = new Set(visibleRows.flatMap((row) => splitVendors(row)));
  const visibleVeryHigh = visibleRows.filter((row) => row.dataset.priority === 'Muito alta').length;
  const visibleHigh = visibleRows.filter((row) => row.dataset.priority === 'Alta').length;

  resultsCount.textContent = `${visibleRows.length} matéria(s) visível(is)`;
  activeBankLabel.textContent = targetBank === '__all__' ? 'Todos os bancos' : targetBank;
  activeVendorLabel.textContent = targetVendor === '__all__' ? 'Todos os vendors' : targetVendor;
  cards.banks.textContent = String(visibleBanks.size || 0);
  cards.rows.textContent = String(visibleRows.length);
  cards.vendors.textContent = String(visibleVendors.size || 0);
  cards.veryHigh.textContent = String(visibleVeryHigh);
  cards.high.textContent = String(visibleHigh);
  emptyState.classList.toggle('visible', visibleRows.length === 0);
  setCurrentFilters(targetBank, targetVendor);
}

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const current = getCurrentFilters();
    if (button.dataset.filterKind === 'bank') {
      applyFilters(button.dataset.filterValue, current.vendor);
    } else {
      applyFilters(current.bank, button.dataset.filterValue);
    }
  });
});

clearButtons.forEach((button) => {
  button.addEventListener('click', () => applyFilters('__all__', '__all__'));
});

const initial = getCurrentFilters();
applyFilters(initial.bank, initial.vendor);
'''

html_doc = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Radar estratégico, bancos públicos e cooperativismo financeiro</title>
  <meta name="description" content="Radar executivo com foco em tecnologia, IA, conectividade, transformação digital, canais, pagamentos, privacidade, governança e compras de TI em bancos públicos e cooperativas financeiras.">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; base-uri 'self'; form-action 'none'; frame-ancestors 'none'; object-src 'none'; img-src 'self' data:; script-src 'self'; style-src 'self'; connect-src 'self'; font-src 'self' data:; manifest-src 'self'; upgrade-insecure-requests">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <div class="meta">Atualizado em {html.escape(build_timestamp)} · base publicada em {html.escape(report_date)} · atualização diária programada</div>
      <h1>Radar estratégico, bancos públicos, regionais e cooperativismo financeiro</h1>
      <div class="subtitle">Painel executivo com foco em tecnologia, IA, conectividade, transformação digital, canais, pagamentos, privacidade, governança, compras de TI e vendors críticos para bancos públicos, regionais e cooperativas financeiras.</div>
      <div class="downloads">
        <a class="btn" href="dashboard-bancos-publicos-latest.csv" download>Baixar CSV mais recente</a>
        <a class="btn" href="dashboard-bancos-publicos-latest.md" download>Baixar Markdown mais recente</a>
      </div>
    </section>

    <section class="grid">{card_html}</section>

    <section class="layout">
      <aside class="panel">
        <h2>Filtros e leitura rápida</h2>
        <h3>Filtrar por banco</h3>
        <div class="filters">{''.join(bank_filter_buttons)}</div>
        <h3>Filtrar por vendor</h3>
        <div class="filters">{''.join(vendor_filter_buttons)}</div>
        <h3>Bancos monitorados</h3>
        <ul class="bank-list">{bank_list}</ul>
        <h3>Watchlist de vendors</h3>
        <ul class="bank-list">{vendor_watchlist_list}</ul>
        <h3>Vendors citados na base</h3>
        <ul class="bank-list">{observed_company_list}</ul>
        <h3>Resumo executivo</h3>
        <ul class="summary-list">
          <li><strong>Banco do Brasil</strong> segue quente em conectividade e IA aplicada a pagamentos.</li>
          <li><strong>CAIXA</strong> concentra sinal forte em inclusão, pagamentos offline e contratação de IA jurídica.</li>
          <li><strong>BNB</strong> aparece bem em modernização de canais, Open Finance e agenda de privacidade.</li>
          <li><strong>Sicoob</strong> mostra maturidade superior em IA generativa integrada ao core bancário.</li>
        </ul>
        <h3>Recorte por fornecedor</h3>
        <ul class="summary-list">{vendor_summary_items}</ul>
        <div class="small security-note">Site endurecido para publicação estática com CSP, políticas de navegação restritivas, links externos com isolamento e cabeçalhos de segurança gerados junto do build.</div>
      </aside>

      <main class="panel">
        <h2>Base estruturada</h2>
        <div class="controls">
          <div class="active-filter">
            <div class="active-pill">Banco: <strong data-active-bank-label>Todos os bancos</strong></div>
            <div class="active-pill">Vendor: <strong data-active-vendor-label>Todos os vendors</strong></div>
            <div class="small" data-results-count>{len(rows)} matéria(s) visível(is)</div>
          </div>
          <button type="button" class="clear-btn" data-clear-filter>Limpar filtros</button>
        </div>
        <div class="small">Clique no banco para isolar a instituição, clique no vendor para cruzar fabricante e use a fonte para abrir a publicação original.</div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Banco</th>
                <th>Tema</th>
                <th>Fato relevante</th>
                <th>Empresas citadas</th>
                <th>Vendors radar</th>
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
        <div class="empty-state" data-empty-state>Nenhuma matéria encontrada para esse recorte. Limpe os filtros para voltar ao panorama completo.</div>
      </main>
    </section>
  </div>
  <script src="app.js"></script>
</body>
</html>
'''

headers_content = '''/*
  Content-Security-Policy: default-src 'self'; base-uri 'self'; form-action 'none'; frame-ancestors 'none'; object-src 'none'; img-src 'self' data:; script-src 'self'; style-src 'self'; connect-src 'self'; font-src 'self' data:; manifest-src 'self'; upgrade-insecure-requests
  Cross-Origin-Opener-Policy: same-origin
  Cross-Origin-Resource-Policy: same-origin
  Permissions-Policy: accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()
  Referrer-Policy: strict-origin-when-cross-origin
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
'''

htaccess_content = '''<IfModule mod_headers.c>
  Header always set Content-Security-Policy "default-src 'self'; base-uri 'self'; form-action 'none'; frame-ancestors 'none'; object-src 'none'; img-src 'self' data:; script-src 'self'; style-src 'self'; connect-src 'self'; font-src 'self' data:; manifest-src 'self'; upgrade-insecure-requests"
  Header always set Cross-Origin-Opener-Policy "same-origin"
  Header always set Cross-Origin-Resource-Policy "same-origin"
  Header always set Permissions-Policy "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "DENY"
</IfModule>
'''

(OUT_DIR / 'index.html').write_text(html_doc, encoding='utf-8')
(OUT_DIR / 'style.css').write_text(style_css.strip() + '\n', encoding='utf-8')
(OUT_DIR / 'app.js').write_text(app_js.strip() + '\n', encoding='utf-8')
(OUT_DIR / '_headers').write_text(headers_content, encoding='utf-8')
(OUT_DIR / '.htaccess').write_text(htaccess_content, encoding='utf-8')
(OUT_DIR / latest_csv.name).write_text(latest_csv.read_text(encoding='utf-8'), encoding='utf-8')
(OUT_DIR / latest_md.name).write_text(latest_md.read_text(encoding='utf-8'), encoding='utf-8')
(OUT_DIR / 'dashboard-bancos-publicos-latest.csv').write_text(latest_csv.read_text(encoding='utf-8'), encoding='utf-8')
(OUT_DIR / 'dashboard-bancos-publicos-latest.md').write_text(latest_md.read_text(encoding='utf-8'), encoding='utf-8')

print(json.dumps({
    'out_dir': str(OUT_DIR),
    'rows': len(rows),
    'banks': len(banks),
    'vendors_with_signal': sum(1 for vendor in WATCHLIST if watchlist_counts[vendor['label']] > 0),
    'report_date': report_date,
    'build_timestamp': build_timestamp,
    'files': [
        'index.html',
        'style.css',
        'app.js',
        '_headers',
        '.htaccess',
        latest_csv.name,
        latest_md.name,
        'dashboard-bancos-publicos-latest.csv',
        'dashboard-bancos-publicos-latest.md',
    ]
}, ensure_ascii=False))
