# Dashboard executivo, bancos publicos e cooperativismo financeiro

Data de corte: 2026-10-01

## Escopo desta versao

Radar publico refeito em portugues, concentrado em **Banco do Brasil, CAIXA, BRB, Sicoob e Banco Central**.

O recorte prioriza sinais de TI, conectividade, IA, pagamentos, seguranca, privacidade, governanca, compras publicas, regulacao, fornecedores estrategicos e continuidade operacional. A rodada usa fontes publicas verificaveis, misturando fontes oficiais, regulador, controle externo, midia setorial e ecossistema de parceiros.

## Leitura executiva

### Principais mudancas do dia

1. **Banco Central virou o gatilho mais quente de 01/10**: entram em vigor as mudancas de Pix por aproximacao/JSR e as regras de ativos virtuais/PLDFT, afetando limites, Open Finance, antifraude e monitoramento.
2. **CAIXA ganhou pressao regulatoria imediata em Pix**: a pagina operacional da CAIXA ja explicita Pix por aproximacao, MED e contestacao por app, enquanto a regra do BC exige gestao de limites sem teto fixo.
3. **BRB segue no maior risco institucional da rodada**: TCDF, STF, Banco Central e FGC mantem pressao sobre governanca, capital, transparencia e controles, mas o PE 055/2026 mostra agenda digital ainda ativa.
4. **Sicoob continua o melhor sinal de IA aplicada e Open Finance cooperativo**, com Sisbr IA, RAG, modelos open source em nuvem controlada pelo CCS, SuperApp e governanca cooperativa do ecossistema.
5. **Banco do Brasil permanece quente em infraestrutura e IA**, puxado por DDI/DNS/DHCP/IPAM, MySQL e AutoML H2O, alem de seguranca de canal com Origem Verificada e rollout do novo app.

### Ranking estrategico de oportunidade

- **Prioridade maxima:** Banco Central, CAIXA, Sicoob, Banco do Brasil e BRB
- **Bancos mais quentes hoje:** **Banco Central, CAIXA e Sicoob**
- **Maior risco institucional e de controles:** **BRB**
- **Maior risco operacional de canais de massa:** **CAIXA**
- **Maior densidade regulatoria em pagamentos e APIs:** **Banco Central**
- **Melhor sinal de IA aplicada:** **Sicoob e Banco do Brasil**
- **Melhor sinal de infraestrutura, rede e datacenter:** **Banco do Brasil**

## Sintese da rodada

A base estruturada desta edicao esta no CSV `reports/dashboard-bancos-publicos-e-cooperativos-2026-10-01.csv`, com **32 registros publicos verificaveis**.

Em relacao a **2026-09-30**, a rodada de hoje fez cinco ajustes principais:
- reposicionou **Banco Central** no topo por eventos com vigencia em 01/10: Pix por aproximacao/JSR sem teto fixo e novas regras de ativos virtuais/PLDFT;
- atualizou **CAIXA** com leitura direta do impacto regulatorio de Pix nos canais App CAIXA/CAIXA Tem, somando isso ao Novo App CAIXA beta, seguranca mobile e calendario de outubro do Bolsa Familia;
- manteve **BRB** como maior alerta de governanca, adicionando o vetor STF/BC/FGC ao bloqueio do TCDF e conectando Pix/limites aos canais digitais do banco;
- preservou **Sicoob** como frente mais forte de IA aplicada e Open Finance, com combinacao de fonte institucional, midia setorial e governanca cooperativa;
- manteve **Banco do Brasil** com oportunidade de infraestrutura e dados por RFPs abertas ate 05/10 e 06/10, alem de contexto recente de IA e seguranca antifraude.

## Radar por banco

### Banco do Brasil
- **DDI segue como oportunidade ativa de infraestrutura**: a RFP 2026/004629 fica publica ate 06/10/2026 para DNS, DHCP e IPAM, com migracao, integracao, transferencia de conhecimento e suporte oficial.
- **Banco de dados continua quente**: a RFP 2026/004636 cobre MySQL com cessao de direito de uso/subscricao e suporte dedicado, aberta ate 05/10/2026.
- **IA tem compra publica especifica**: a RFP 2026/004394 de AutoML H2O Driverless IA encerrou em 28/09/2026 e segue como sinal recente de modelagem, suporte e consultoria.
- **Seguranca de atendimento segue relevante**: Origem Verificada da Anatel protege chamadas do BB pelo numero 4003-3001 contra falsa central e spoofing.
- **App BB fechou a janela prometida de rollout**: a previsao de 100% dos clientes ate o fim de setembro torna estabilidade, assistente conversacional, IA e personalizacao temas de acompanhamento imediato.
- **Contexto sustentado de IA agentica**: o caso de cambio com Microsoft Foundry segue relevante por reduzir o tempo medio de operacao e manter validacao humana especializada.

### CAIXA
- **Pix por aproximacao entrou em vigencia regulatoria hoje**: a regra do BC de 01/10 retira teto fixo de R$ 500 e exige gestao de limites nos canais das instituicoes.
- **Pagina Pix da CAIXA confirma aderencia operacional**: App CAIXA e CAIXA Tem aparecem como canais de Pix, contestacao por fraude/MED e Pix por aproximacao via NFC/Carteira Google.
- **Novo App CAIXA segue como eixo de seguranca**: beta usa biometria facial, liveness, criptografia, analise comportamental, antifraude, Pix, Open Finance e integracao do CAIXA Tem.
- **CAIXA Tem reforca controles de dispositivo**: pagina publica orienta bloqueios por modo desenvolvedor/debug, deteccao de risco, localizacao para Pix e apps oficiais.
- **Bolsa Familia de outubro ja tem calendario publico**: pagamentos de 19/10 a 30/10 antecipam nova janela de carga em Caixa Tem, terminais, lotericas e correspondentes.
- **Fila virtual em nuvem permanece sinal objetivo**: CECOT 249/2026 mira SaaS de fila e sala de espera para CAIXA Tem, FGTS, Loterias, sites e sistemas.

### BRB
- **TCDF manteve o caso Master no topo do risco**: decisao de 24/09/2026 bloqueou ate R$ 2,7 bilhoes de ex-dirigentes e pediu dados de auditoria independente em 24 horas.
- **STF/BC/FGC ampliam o risco prudencial**: decisao de 11/09 deu 15 dias para explicar entraves de emprestimo de R$ 6,6 bilhoes ao BRB, com risco de liquidacao pelo BC citado publicamente.
- **Agenda digital continua apesar da crise**: PE 055/2026 cobre fabrica de software para apps nativos/hibridos/PWA em smartphones, tablets, smartwatches, smartTVs, desktops e IoT.
- **Pix depende diretamente do App Banco BRB**: pagina oficial informa consulta e atualizacao de limites no app, com ajustes possiveis por determinacao do banco ou nova norma do BC.
- **Seguranca digital tem trilha publica**: Banknet/App usam criptografia, teclado virtual, token SMS/e-mail, BRB Code e ferramenta de protecao de canais.
- **Contexto sustentado de ciberseguranca**: politica de privacidade lista WAF, IPS/IDS, SIEM, VPN, NAC, endpoint protection, criptografia e analise de dispositivo.

### Sicoob
- **Sicoob segue como melhor sinal de IA aplicada**: Sisbr IA e Pesquisa Inteligente de Normativos foram anunciados em 23/09/2026 para mais de 62 mil colaboradores.
- **Governanca de IA ficou concreta**: a instituicao informa RAG, modelos open source, ambiente seguro/controlado, nuvem sob gestao exclusiva do CCS, LGPD, moderacao e logs restritos.
- **Modo Guardiao ganhou peso comercial**: a camada do SuperApp limita transacoes fora de redes confiaveis e reforca autenticacao para valores mais altos.
- **SuperApp continua vetor central**: nova geracao iniciada em 01/09/2026 combina Open Finance, IA generativa, personalizacao e assistente conversacional para texto, audio e imagem.
- **LetsMoney validou fora da fonte propria**: a cobertura setorial destacou contas de outras instituicoes na tela inicial e Pix a partir de contas externas mediante autorizacao.
- **Governanca Open Finance tem fonte cooperativa**: Sicoob atua via OCB no Conselho Deliberativo e em grupos de trabalho, o que reforca API, consentimento e interoperabilidade.
- **Convergencia Digital reforca complexidade cooperativa**: o sinal externo ajuda a posicionar API gateway, observabilidade, suporte multicooperativa e governanca federativa.

### Banco Central
- **Pix por aproximacao tem vigencia hoje**: a IN BCB 746 remove o teto fixo de R$ 500 para Pix por aproximacao e Jornada Sem Redirecionamento a partir de 01/10/2026.
- **Ativos virtuais/PLDFT tambem entram em prazo critico**: regras de PSAVs e comunicacao ao Coaf para carteiras autocustodiadas a partir de US$ 10 mil passam a vigorar em 01/10/2026.
- **Pix/TIPS segue como fato mais estrategico da semana**: BCB e BCE iniciaram avaliacao em 24/09 para conectar Pix ao sistema europeu TIPS, com analise tecnica, operacional, juridica e de negocio.
- **Fonte internacional confirma a dimensao global**: o BCE citou liquidacao em moeda de banco central e cerca de 250 milhoes de pagamentos instantaneos diarios no Pix.
- **Reuters/UOL valida fora das fontes oficiais**: cobertura de 24/09/2026 reforcou a avaliacao Pix-TIPS como agenda transfronteirica.
- **Resolucao BCB 587 mexe no Pix**: Pix Automatico em conta-salario, cobranca hibrida, participacao no arranjo, suspeita de fraude e recursos contra decisoes do BC afetam participantes.
- **IN 777 puxa backlog tecnico**: Manual de Fluxos do Processo de Efetivacao do Pix versao 2.2 exige planejamento de release, integracao e testes ate 2027.

## Observacao de frescor

A rodada de 01/10 encontrou dois fatos com vigencia no proprio dia no Banco Central e impactos diretos em CAIXA, BRB e demais participantes do Pix/Open Finance. Para Banco do Brasil, BRB e Sicoob, os sinais mais fortes continuam concentrados nos ultimos 7 a 30 dias; itens com mais de 90 dias foram marcados como contexto sustentado.

## Fontes principais
- https://www.bb.com.br/site/compras-contratacao-e-venda-de-imoveis/compras-e-contratacoes/avisos-e-editais/
- https://imprensa.bb.com.br/bb-amplia-seguranca-nas-ligacoes-com-origem-verificada/
- https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/banco-do-brasil-lanca-novo-aplicativo-com-foco-em-ia-e-personalizacao
- https://imprensa.bb.com.br/banco-do-brasil-reduz-em-90-o-tempo-de-operacoes-de-cambio-com-agente-autonomo-de-ia/
- https://www.bcb.gov.br/detalhenoticia/21169/noticia
- https://www.caixa.gov.br/pix/Paginas/default.aspx
- https://caixanoticias.caixa.gov.br/Paginas/Not%C3%ADcias/2026/08-AGOSTO/CAIXA-inicia-fase-Beta-do-novo-aplicativo-do-banco.aspx
- https://www.caixa.gov.br/caixatem/Paginas/default.aspx?lang=pt
- https://www.gov.br/mds/pt-br/noticias-e-conteudos/desenvolvimento-social/noticias-desenvolvimento-social/confira-o-calendario-de-pagamentos-do-bolsa-familia-de-2026
- https://guialicite.com.br/oportunidades/00360305000104-1-000691/2026
- https://agenciabrasil.ebc.com.br/justica/noticia/2026-09/caso-master-tcdf-bloqueia-ate-r-27-bi-de-ex-dirigentes-do-brb
- https://agenciabrasil.ebc.com.br/justica/noticia/2026-09/fux-da-15-dias-para-uniao-e-bc-responderem-sobre-emprestimo-ao-brb
- https://www.portaldecompraspublicas.com.br/processos/DF/BRB-BANCO-DE-BRASILIA-SA-3635/PE-055-2026-2026-499166
- https://novo.brb.com.br/pix/
- https://novo.brb.com.br/para-voce/seguranca/como-o-brb-protege-voce/
- https://novo.brb.com.br/politica-de-privacidade/
- https://www.sicoob.com.br/web/sicoob/noticias/-/asset_publisher/xAioIawpOI5S/content/id/275173922
- https://www.sicoob.com.br/web/sicoob/noticias/-/asset_publisher/xAioIawpOI5S/content/id/267075551
- https://www.sicoob.com.br/web/sicoobcentralscrs/noticias/-/asset_publisher/xAioIawpOI5S/content/id/326354161
- https://www.letsmoney.com.br/noticias/sicoob-superapp-open-finance-ia-generativa/
- https://www.sicoob.com.br/web/sicoob4474/noticias/-/asset_publisher/xAioIawpOI5S/content/id/71072642
- https://convergenciadigital.com.br/mercado/sicoob-cooperativas-enfrentam-a-complexidade-do-open-finance/
- https://www.bcb.gov.br/detalhenoticia/21267/nota
- https://www.bcb.gov.br/detalhenoticia/21271/nota
- https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews260924.it.html
- https://economia.uol.com.br/noticias/reuters/2026/09/24/bc-e-bce-iniciam-fase-de-avaliacao-para-interligacao-entre-pix-e-tips.htm
- https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=587&tipo=Resolu%C3%A7%C3%A3o+BCB
- https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=777&tipo=Instru%C3%A7%C3%A3o+Normativa+BCB

## Publicacao
- Site estatico: `site/dashboard-bancos-publicos/index.html`
- Markdown local da rodada: `reports/dashboard-bancos-publicos-e-cooperativos-2026-10-01.md`
- CSV local da rodada: `reports/dashboard-bancos-publicos-e-cooperativos-2026-10-01.csv`
- Markdown publicado no site: `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.md`
- CSV publicado no site: `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.csv`

## Aprendizados do XING LING
- O estudo mais recente disponivel em `workspace-xing-ling/study/2026-07-29.md` segue focado em **CloudCampus Huawei**, **management VLAN auto-negotiation**, **Option 43** e **VRRP** no onboarding de **Fit APs**.
- Para pre-vendas Huawei, o principal aprendizado pratico e tratar **management VLAN auto-negotiation** como parte do desenho de gestao e continuidade operacional, nao como detalhe de implantacao.
- O limiar de **500 APs** continua util como gatilho de arquitetura: abaixo disso, a recomendacao documentada favorece um dominio de gerenciamento; a partir disso, a Huawei recomenda multiplos dominios por predio, area ou quantidade de APs.
- Em bancos, a ponte com data center/campus e antecipar discovery sobre dominios de gestao, caminho AP-WAC L2/L3, DHCP, Option 43, VRRP e separacao entre gestao wired/wireless antes de fechar BoM e escopo de servicos.
