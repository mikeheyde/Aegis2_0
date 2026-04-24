Atualize o radar estratégico de bancos públicos, regionais e cooperativismo financeiro do workspace.

Objetivo:
- Refazer a coleta pública em português com foco em Banco do Brasil, CAIXA, BRB, BASA, BNB, Banestes, Banrisul, Banpará e Sicoob.
- Priorizar sinais ligados a TI, conectividade, IA, Cisco, Huawei, H3C, Fortinet, HP, Aruba, IBM, Check Point, Palo Alto, Arista, Juniper, Compwire, Zoom, NTT, Logicalis, Teltec, Teletex, modernização digital, pagamentos, segurança, privacidade, governança, licitações, contratos e TCU.
- Incluir empresas citadas pelos bancos e empresas que citam esses bancos.

Entregáveis obrigatórios:
1. Gerar um novo Markdown em `reports/dashboard-bancos-publicos-e-cooperativos-YYYY-MM-DD.md`
2. Gerar um novo CSV em `reports/dashboard-bancos-publicos-e-cooperativos-YYYY-MM-DD.csv`
3. Rodar `python3 scripts/build_dashboard_site.py`
4. Validar localmente que `site/dashboard-bancos-publicos/index.html` foi atualizado e que os artefatos de segurança do site estático (`_headers` e `.htaccess`) foram gerados
5. Fazer commit git com uma mensagem clara, apenas se houver mudança real
6. Se o remote GitHub `Aegis2_0` estiver configurado e autenticado, fazer push

Regras de execução:
- Trabalhe em português.
- Use fontes públicas verificáveis e prefira fontes oficiais, institucionais e mídia setorial confiável.
- Não apague relatórios antigos.
- Preserve o formato estruturado do CSV para manter o site funcional.
- Se não encontrar novidades relevantes para algum banco ou fornecedor, mantenha a cobertura honesta, sem inventar sinal.
- Ao final, entregue um resumo executivo curto com:
  - principais mudanças do dia
  - bancos com sinal mais quente
  - links de publicação do site e do CSV/Markdown mais recentes
  - um bloco curto chamado `Aprendizados do XING LING`, resumindo o que o xing-ling aprendeu de novo no estudo mais recente, com foco prático para Huawei data center e pré-vendas, se houver aprendizado novo registrado
- Para montar `Aprendizados do XING LING`, consulte o workspace `/home/ubuntu/.openclaw/workspace-xing-ling`, priorizando o arquivo diário mais recente em `study/`.
- Se houver bloqueio externo, explique objetivamente o que faltou.
