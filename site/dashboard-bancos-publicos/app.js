const rows = Array.from(document.querySelectorAll('tbody tr'));
const filterButtons = Array.from(document.querySelectorAll('[data-filter-kind]'));
const countBadges = Array.from(document.querySelectorAll('[data-count-kind]'));
const resultsCount = document.querySelector('[data-results-count]');
const activeBankLabel = document.querySelector('[data-active-bank-label]');
const activeVendorLabel = document.querySelector('[data-active-vendor-label]');
const activeWindowLabel = document.querySelector('[data-active-window-label]');
const emptyState = document.querySelector('[data-empty-state]');
const clearButtons = Array.from(document.querySelectorAll('[data-clear-filter]'));
const cards = {
  banks: document.querySelector('[data-card="Bancos monitorados"] .card-value'),
  rows: document.querySelector('[data-card="Matérias catalogadas"] .card-value'),
  vendors: document.querySelector('[data-card="Vendors com sinal"] .card-value'),
  veryHigh: document.querySelector('[data-card="Prioridade muito alta"] .card-value'),
  high: document.querySelector('[data-card="Prioridade alta"] .card-value'),
};
const DEFAULT_WINDOW = '30';
const WINDOW_LABELS = {
  '30': 'Últimos 30 dias',
  '90': 'Últimos 90 dias',
  '180': 'Últimos 180 dias',
  '365': 'Todos (1 ano)',
};
const referenceDate = parseIsoDate(document.documentElement.dataset.latestReportDate);

function parseIsoDate(value) {
  if (!value) return null;
  const parsed = new Date(`${value}T00:00:00Z`);
  return Number.isNaN(parsed.getTime()) ? null : parsed;
}

function normalizeWindow(value) {
  return WINDOW_LABELS[value] ? value : DEFAULT_WINDOW;
}

function getCurrentFilters() {
  const params = new URLSearchParams(window.location.search);
  return {
    bank: params.get('bank') || '__all__',
    vendor: params.get('vendor') || '__all__',
    window: normalizeWindow(params.get('window') || DEFAULT_WINDOW),
  };
}

function setCurrentFilters(bank, vendor, windowValue) {
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
  if (!windowValue || normalizeWindow(windowValue) === DEFAULT_WINDOW) {
    params.delete('window');
  } else {
    params.set('window', normalizeWindow(windowValue));
  }
  const query = params.toString();
  const nextUrl = `${window.location.pathname}${query ? `?${query}` : ''}`;
  window.history.replaceState({}, '', nextUrl);
}

function splitVendors(row) {
  return (row.dataset.vendors || '').split('|').filter(Boolean);
}

function matchesWindow(row, windowValue) {
  if (!referenceDate) return true;
  const rowDate = parseIsoDate(row.dataset.firstSeen);
  if (!rowDate) return true;
  const days = Number(normalizeWindow(windowValue));
  if (!Number.isFinite(days)) return true;
  const delta = Math.floor((referenceDate.getTime() - rowDate.getTime()) / 86400000);
  return delta >= 0 && delta < days;
}

function rowMatches(row, filters) {
  const targetBank = filters.bank || '__all__';
  const targetVendor = filters.vendor || '__all__';
  const rowVendors = splitVendors(row);
  const matchesBank = targetBank === '__all__' || row.dataset.bank === targetBank;
  const matchesVendor = targetVendor === '__all__' || rowVendors.includes(targetVendor);
  return matchesBank && matchesVendor && matchesWindow(row, filters.window);
}

function setButtonStates(current) {
  filterButtons.forEach((button) => {
    const kind = button.dataset.filterKind;
    const value = button.dataset.filterValue;
    const isActive = (kind === 'bank' && value === current.bank)
      || (kind === 'vendor' && value === current.vendor)
      || (kind === 'window' && value === current.window);
    button.classList.toggle('active', isActive);
  });
}

function countRowsFor(kind, value, current) {
  const filters = {
    bank: kind === 'bank' ? value : current.bank,
    vendor: kind === 'vendor' ? value : current.vendor,
    window: kind === 'window' ? value : current.window,
  };
  return rows.filter((row) => rowMatches(row, filters)).length;
}

function updateBadges(current) {
  countBadges.forEach((badge) => {
    const kind = badge.dataset.countKind;
    const value = badge.dataset.countValue || '__all__';
    const count = countRowsFor(kind, value, current);
    badge.textContent = String(count);

    if (kind === 'window' || value === '__all__') return;
    const filterChip = badge.closest('.filter-chip');
    if (filterChip) filterChip.classList.toggle('muted-zero', count === 0);
    const listRow = badge.closest('li');
    if (listRow) listRow.classList.toggle('muted-zero', count === 0);
  });
}

function applyFilters(bank, vendor, windowValue) {
  const targetBank = bank || '__all__';
  const targetVendor = vendor || '__all__';
  const targetWindow = normalizeWindow(windowValue || DEFAULT_WINDOW);
  const visibleRows = [];

  rows.forEach((row) => {
    const matches = rowMatches(row, {
      bank: targetBank,
      vendor: targetVendor,
      window: targetWindow,
    });
    row.classList.toggle('hidden-row', !matches);
    if (matches) visibleRows.push(row);
  });

  const current = {
    bank: targetBank,
    vendor: targetVendor,
    window: targetWindow,
  };

  setButtonStates(current);
  updateBadges(current);

  const visibleBanks = new Set(visibleRows.map((row) => row.dataset.bank));
  const visibleVendors = new Set(visibleRows.flatMap((row) => splitVendors(row)));
  const visibleVeryHigh = visibleRows.filter((row) => row.dataset.priority === 'Muito alta').length;
  const visibleHigh = visibleRows.filter((row) => row.dataset.priority === 'Alta').length;

  resultsCount.textContent = `${visibleRows.length} matéria(s) visível(is)`;
  activeBankLabel.textContent = targetBank === '__all__' ? 'Todos os bancos' : targetBank;
  activeVendorLabel.textContent = targetVendor === '__all__' ? 'Todos os vendors' : targetVendor;
  activeWindowLabel.textContent = WINDOW_LABELS[targetWindow] || WINDOW_LABELS[DEFAULT_WINDOW];
  cards.banks.textContent = String(visibleBanks.size || 0);
  cards.rows.textContent = String(visibleRows.length);
  cards.vendors.textContent = String(visibleVendors.size || 0);
  cards.veryHigh.textContent = String(visibleVeryHigh);
  cards.high.textContent = String(visibleHigh);
  emptyState.classList.toggle('visible', visibleRows.length === 0);
  setCurrentFilters(targetBank, targetVendor, targetWindow);
}

filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const current = getCurrentFilters();
    if (button.dataset.filterKind === 'bank') {
      applyFilters(button.dataset.filterValue, current.vendor, current.window);
    } else if (button.dataset.filterKind === 'vendor') {
      applyFilters(current.bank, button.dataset.filterValue, current.window);
    } else {
      applyFilters(current.bank, current.vendor, button.dataset.filterValue);
    }
  });
});

clearButtons.forEach((button) => {
  button.addEventListener('click', () => applyFilters('__all__', '__all__', DEFAULT_WINDOW));
});

const initial = getCurrentFilters();
applyFilters(initial.bank, initial.vendor, initial.window);
