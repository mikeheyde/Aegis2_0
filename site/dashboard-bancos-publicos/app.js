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
