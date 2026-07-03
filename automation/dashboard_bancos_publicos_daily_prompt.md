Atualize o radar estratégico de bancos públicos, regionais e cooperativismo financeiro do workspace.

Objetivo:
- Refazer a coleta pública em português com foco apenas em Banco do Brasil, CAIXA, BRB, Sicoob e Banco Central.
- Priorizar sinais ligados a TI, conectividade, IA, Cisco, Huawei, H3C, Fortinet, HP, Aruba, IBM, Check Point, Palo Alto, Arista, Juniper, Compwire, Zoom, NTT, Logicalis, Teltec, Teletex, modernização digital, pagamentos, segurança, privacidade, governança, licitações, contratos e TCU.
- Incluir empresas citadas pelos bancos e empresas que citam esses bancos.
- Trazer cobertura diária mais rica de notícias e fatos públicos relevantes para cada banco, sem depender só de uma ou duas fontes recorrentes.

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
- Pesquise de forma ativa em várias fontes por banco, não apenas nas páginas institucionais mais óbvias.
- Trate diversidade de fontes como requisito operacional, não como sugestão.
- Para cada banco, cubra no mínimo 3 fatos ou bullets relevantes por dia, desde que existam sinais públicos verificáveis; se houver mais, inclua mais.
- Não repita mecanicamente o mesmo fato antigo como se fosse novidade do dia. Se um item for reaproveitado por falta de novidade melhor, deixe isso claro como contexto sustentado, não como manchete nova.
- Aplique uma hierarquia de frescor antes de escolher os bullets:
  - prioridade 1: fatos novos do dia ou dos últimos 7 dias
  - prioridade 2: fatos recentes da rodada ou dos últimos 30 dias
  - prioridade 3: contexto sustentado dos últimos 90 dias, explicitamente marcado como contexto sustentado
- Evite montar o radar de um banco só com notícias do próprio banco. Sempre que houver material público disponível, inclua pelo menos 1 bullet vindo de fonte não pertencente ao próprio banco, como regulador, fornecedor, mídia setorial, órgão de controle ou parceiro tecnológico.
- Antes de concluir que um banco teve "pouca novidade", faça busca adicional em pelo menos estas frentes quando aplicável:
  - newsroom / imprensa oficial do banco
  - RI / fatos relevantes / apresentações institucionais
  - portal de compras, editais, licitações, contratos ou consultas públicas
  - páginas de desenvolvedores, APIs, open finance, segurança ou tecnologia
  - Banco Central / TCU / CVM / órgãos de controle quando houver conexão com o caso
  - mídia setorial confiável e parceiros tecnológicos citando o banco
- Sempre que possível, combine fontes de pelo menos 2 classes diferentes para cada banco na rodada, por exemplo: institucional + mídia setorial, institucional + regulatório, institucional + fornecedor, ou regulatório + fornecedor.
- Sempre que possível, combine também pelo menos 2 domínios distintos por banco na rodada. Se 3 bullets de um banco vierem do mesmo domínio, trate isso como falha de cobertura e pesquise de novo antes de concluir.
- Se depois da busca ampliada ainda não houver 3 fatos realmente defensáveis para um banco naquele dia, entregue os 3 bullets mesmo assim usando esta hierarquia:
  - primeiro fatos novos do dia ou da rodada
  - depois desdobramentos recentes ainda relevantes
  - por fim contexto estrutural ainda importante, marcado explicitamente como contexto sustentado
- Nessa situação de fallback, no máximo 1 dos 3 bullets pode ser puro contexto sustentado, salvo bloqueio externo real e explicado.
- Nunca inclua conteúdo alheio ao radar, como roteiros devocionais, textos litúrgicos, lembretes pessoais ou qualquer bloco que não trate diretamente do monitoramento bancário.
- Para o Banco Central, aceite como material válido notícias, consultas públicas, atas, agendas de inovação, regulação, supervisão, Pix, Drex, cibersegurança, open finance, infraestrutura financeira e manifestações que afetem diretamente o ecossistema bancário.
- Faça buscas direcionadas por banco com combinações de tema e ecossistema. Exemplos válidos:
  - nome do banco + IA / cibersegurança / conectividade / nuvem / open finance / Pix / licitação / edital / contrato / fornecedor / parceiro
  - nome do banco + Cisco / Huawei / Fortinet / IBM / Logicalis / Tecban / Visa / Microsoft / Oracle / Deloitte / Capgemini, quando houver aderência pública
  - nome do banco + TCU / Banco Central / CVM / CNJ / PGFN / Febraban / API / developer / portal do fornecedor
- Para navegação e automação web, prefira `agent-browser` por padrão quando precisar abrir páginas, clicar, renderizar conteúdo dinâmico ou extrair texto diretamente do navegador.
- Se qualquer tentativa com `firecrawl` falhar por crédito, autenticação, timeout, erro do provedor ou indisponibilidade externa, trate isso como gatilho automático para fallback e continue a coleta com `agent-browser`, sem encerrar a rodada por causa do Firecrawl.
- Neste host, use a rotina estável de fallback do `agent-browser`: `./scripts/agent_browser_fallback.sh <subcomando...>`. Ela sobe um Chromium dedicado com CDP fixo, conecta a sessão e só então executa o comando pedido.
- Se precisar rodar manualmente sem o wrapper, siga esta ordem: `./scripts/agent_browser_cdp.sh 9333` → `agent-browser --session fallback connect 9333` → `agent-browser --session fallback open <url>` → demais comandos como `snapshot -i --json`, `get title --json`, `get text ...`.
- Se mesmo o `agent-browser` falhar em uma página específica, tente uma alternativa pública equivalente da mesma instituição antes de marcar bloqueio externo.
- Não apague relatórios antigos.
- Preserve o formato estruturado do CSV para manter o site funcional.
- Se não encontrar novidades relevantes para algum banco ou fornecedor, mantenha a cobertura honesta, sem inventar sinal.
- Para git, trate o repositório como possivelmente sujo por mudanças não relacionadas. Nunca dependa de worktree limpo para concluir a rodada.
- Nunca use `git add -A`, `git add .` ou stage amplo no repositório inteiro para este job.
- Para stage da rodada, use explicitamente `./scripts/stage_dashboard_update.sh YYYY-MM-DD`.
- Para decidir se houve mudança real, use o resultado do script acima e/ou `git diff --cached --quiet -- <paths do radar>`, nunca `git status` global como gate de sucesso.
- Para commit seguro num worktree sujo, prefira `./scripts/commit_dashboard_update.sh YYYY-MM-DD "mensagem clara"` em vez de compor lógica própria com `git status`.
- Se houver mudanças staged só nos artefatos do radar, faça commit apenas delas, mesmo que existam outros arquivos modificados no worktree.
- Se não houver diff staged nos artefatos do radar, não faça commit e siga com a entrega informando que não houve mudança real.
- Faça a validação final de modo objetivo e simples. Não tente "listar arquivos dentro" de arquivos como `index.html` e não dependa de inspeções em `.github/workflows` para concluir a rodada.
- Para validar o site estático, prefira `./scripts/validate_dashboard_artifacts.sh YYYY-MM-DD` e aceite a validação como concluída se ele retornar `OK`.
- Se precisar validar manualmente, confirme apenas estes pontos:
  - existem `site/dashboard-bancos-publicos/index.html`, `site/dashboard-bancos-publicos/_headers`, `site/dashboard-bancos-publicos/.htaccess`
  - existem `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.md` e `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.csv`
  - o arquivo `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.md` referencia a data da rodada atual `YYYY-MM-DD`
- Antes de concluir a rodada, prefira `./scripts/validate_dashboard_report_content.sh YYYY-MM-DD` para a checagem textual do markdown final e aceite a checagem como concluída se ele retornar `OK`.
- Se precisar validar manualmente, confirme que o markdown final não contém marcadores proibidos nem blocos estranhos ao radar.
- Se esses arquivos existirem e a data da rodada atual estiver no `dashboard-bancos-publicos-latest.md`, trate a validação como concluída.
- Ao final, entregue um resumo executivo curto com:
  - principais mudanças do dia
  - bancos com sinal mais quente
  - uma seção `Radar por banco` com no mínimo 3 bullets por banco para Banco do Brasil, CAIXA, BRB, Sicoob e Banco Central
  - links de publicação do site e do CSV/Markdown mais recentes
  - um bloco curto chamado `Aprendizados do XING LING`, resumindo o que o xing-ling aprendeu de novo no estudo mais recente, com foco prático para Huawei data center e pré-vendas, se houver aprendizado novo registrado
- Para montar `Aprendizados do XING LING`, consulte o workspace `/home/ubuntu/.openclaw/workspace-xing-ling`, priorizando o arquivo diário mais recente em `study/`.
- Se houver bloqueio externo, explique objetivamente o que faltou.

Checklist mínimo de qualidade antes de encerrar a rodada:
- Cada um dos 5 bancos aparece no resumo final.
- Cada banco tem pelo menos 3 bullets defensáveis no bloco `Radar por banco`.
- O conjunto da rodada não depende majoritariamente de uma única URL repetida por banco.
- Há mistura razoável entre fontes oficiais, regulatórias, setoriais e/ou de parceiros tecnológicos, quando disponível.
- Cada banco deve fechar a rodada com pelo menos 2 classes de fonte e, quando houver material público suficiente, pelo menos 2 domínios distintos.
- Se um banco terminar com maioria de bullets vindos do mesmo domínio próprio, faça mais uma rodada de busca antes de encerrar.
- Se um bullet usar material com mais de 30 dias, deixe isso claro no texto; se passar de 90 dias, marque como contexto sustentado.
