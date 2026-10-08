# Dashboard executivo, bancos publicos e cooperativismo financeiro

Data de corte: 2026-10-08

## Escopo desta versao

Radar publico refeito em portugues, concentrado em **Banco do Brasil, CAIXA, BRB, Sicoob e Banco Central**.

O recorte prioriza sinais de TI, conectividade, IA, pagamentos, seguranca, privacidade, governanca, compras publicas, regulacao, fornecedores estrategicos e continuidade operacional. A rodada usa fontes publicas verificaveis, misturando fontes oficiais, regulador, controle externo, midia setorial e ecossistema de parceiros.

## Leitura executiva

### Principais mudancas do dia

1. **Sicoob trouxe o sinal incremental mais forte**: publicacao de 03/10 informa nova versao do SuperApp para 8 milhoes de cooperados, 85% das transacoes pelo app, mais de sete milhoes de acessos diarios, cashback, agendamento de boletos e camadas adicionais de seguranca.
2. **Banco do Brasil segue com a esteira de TI mais quente**: continuam ativas as janelas publicas de DDI/DNS/DHCP/IPAM ate 09/10, IA juridica multimodal ate 12/10, GRC/reportes SaaS ate 13/10 e UEM/AEM/DEX Linux ate 16/10.
3. **Banco Central manteve outubro como mes operacional do Pix**: seguem no radar o bloqueio de chaves Pix marcadas por fraude desde 04/10, a norma prometida do Pix Parcelado e os impactos de Pix por aproximacao sem teto fixo desde 01/10.
4. **CAIXA continua com risco de escala em canais de massa**: o novo piso do Bolsa Familia de R$ 691 vale para a folha de outubro, com calendario de 19/10 a 30/10 e uso intensivo de Caixa Tem, agencias, lotericas e correspondentes.
5. **BRB permanece como maior foco de governanca e controle**: TCDF, STF, Banco Central e FGC seguem no centro do caso Master, enquanto app, Pix, limites e fabrica de software mantem a criticidade digital.

### Ranking estrategico de oportunidade

- **Prioridade maxima:** Banco do Brasil, Banco Central, Sicoob, CAIXA e BRB
- **Bancos mais quentes hoje:** **Sicoob, Banco do Brasil e Banco Central**
- **Maior risco institucional e de controles:** **BRB**
- **Maior risco operacional de canais de massa:** **CAIXA**
- **Maior densidade regulatoria em pagamentos e APIs:** **Banco Central**
- **Melhor sinal de IA aplicada:** **Banco do Brasil e Sicoob**
- **Melhor sinal de infraestrutura, rede e datacenter:** **Banco do Brasil**

## Sintese da rodada

A base estruturada desta edicao esta no CSV `reports/dashboard-bancos-publicos-e-cooperativos-2026-10-08.csv`, com **44 registros publicos verificaveis**.

Em relacao a **2026-10-07**, a rodada de 08/10 fez quatro ajustes principais:
- adicionou o reforco publico do **Sicoob SuperApp** de 03/10, com escala de cooperados, peso transacional do app, acessos diarios e seguranca;
- manteve como ativos os prazos de RFP do **Banco do Brasil** para DDI, IA juridica, GRC/reportes e endpoint Linux, porque ainda ha janelas publicas relevantes nesta semana;
- preservou o ciclo de **Banco Central/Pix** com Forum Pix, bloqueio de chaves marcadas por fraude, Pix por aproximacao sem teto fixo e Manual de Fluxos v2.2;
- reforcou a leitura de **CAIXA** e **BRB** como riscos operacionais/institucionais com fontes governamentais, regulador, controle externo e paginas oficiais.

## Radar por banco

### Banco do Brasil
- **DDI segue em janela ativa ate 09/10**: a RFP 2026/004629 pede subscricao para DNS, DHCP e IPAM, incluindo instalacao, configuracao, integracao, migracao, implantacao, documentacao, transferencia de conhecimento e suporte oficial do fabricante por 36 meses, prorrogavel ate 60 meses.
- **IA juridica e sinal quente da semana**: a RFP 2026/004652 fica aberta ate 12/10/2026 para IA aplicada a evidencias, manifestacoes processuais e documentos em texto, imagem, audio e video, com fraude documental, litigancia abusiva e validacao por advogado.
- **GRC/reportes tem prazo ativo ate 13/10**: a RFP 2026/004634 busca plataforma corporativa SaaS para reportes corporativos, financeiros, regulatorios e de sustentabilidade, alem de governanca, riscos, controles internos, RI, indices, ratings e rankings.
- **Endpoint Linux continua em janela viva ate 16/10**: a RFP 2026/004317 cobre SaaS de Unified Endpoint Management, Autonomous Endpoint Management e Digital Employee Experience para ate 53.700 endpoints Linux.
- **Contexto recente de IA corporativa**: diretrizes de IA generativa e agentica, Genera BB e AcademIA BB 2026 indicam plataforma interna, guardrails e capacitacao em escala.

### CAIXA
- **Bolsa Familia de outubro ganhou pressao adicional**: o MDS informou valor minimo de R$ 691 e beneficio medio estimado de R$ 777 para a folha de outubro, com valores disponiveis a partir de 19/10.
- **Calendario de outubro segue como janela de carga**: pagamentos de 19/10 a 30/10 sustentam pico esperado em Caixa Tem, terminais, lotericas e correspondentes Caixa Aqui.
- **Pix por aproximacao entrou no primeiro ciclo pos-vigencia**: a regra do BC de 01/10 retirou teto fixo de R$ 500 e exige gestao de limites nos canais das instituicoes, inclusive apps bancarios.
- **Pagina Pix da CAIXA confirma aderencia operacional**: App CAIXA e CAIXA Tem aparecem como canais de Pix, contestacao por fraude/MED e Pix por aproximacao via NFC/Carteira Google.
- **Seguranca mobile ganhou peso**: a pagina de seguranca orienta desativar VPN/localizacao alterada e informa que apps como CAIXA Tem podem exigir localizacao para Pix.
- **Novo App CAIXA segue como contexto recente**: beta usa biometria facial, liveness, criptografia, analise comportamental, antifraude, Pix, Open Finance e integracao do CAIXA Tem.

### BRB
- **TCDF manteve o caso Master no topo do risco**: decisao de 24/09/2026 bloqueou ate R$ 2,7 bilhoes de ex-dirigentes e pediu dados de auditoria independente em 24 horas.
- **STF/BC/FGC ampliam o risco prudencial**: decisao de 11/09 deu 15 dias para explicar entraves de emprestimo de R$ 6,6 bilhoes ao BRB, com risco de liquidacao pelo BC citado publicamente.
- **Agenda digital continua apesar da crise**: PE 055/2026 cobre fabrica de software para apps nativos/hibridos/PWA em smartphones, tablets, smartwatches, smartTVs, desktops e IoT.
- **Pix depende diretamente do App Banco BRB**: pagina oficial informa consulta e atualizacao de limites no app, com ajustes possiveis por determinacao do banco ou nova norma do BC.
- **Canal Pix reforca centralidade do app**: pagina publica informa acesso a conta exclusivamente via App Banco BRB em fluxo Pix, elevando criticidade de disponibilidade e autenticacao.
- **Seguranca digital tem trilha publica**: dicas oficiais orientam app apenas em lojas oficiais, limites diarios, atualizacoes de seguranca e cautela contra phishing/contatos suspeitos.
- **Contexto sustentado de ciberseguranca**: politica de privacidade lista WAF, IPS/IDS, SIEM, VPN, NAC, endpoint protection, criptografia e analise de dispositivo.

### Sicoob
- **SuperApp ganhou novo reforco publico em 03/10**: publicacao regional informa nova versao para 8 milhoes de cooperados, 85% das transacoes pelo app e mais de sete milhoes de acessos diarios.
- **O app adicionou jornadas e seguranca**: a mesma fonte cita agendamento automatico de boletos, cashback, lojas parceiras, pontos Coopera, reformulacao de jornadas de Pix/deposito/pagamentos e ampliacao das camadas de seguranca.
- **Escala Pix segue como sinal relevante**: publicacao recente informa mais de 1 bilhao de transacoes Pix processadas, 46% acima do ano anterior, alem de dialogo com Banco Central, Open Finance e Drex.
- **DeepSeek-R1 segue como sinal quente de IA cooperativa**: publicacao de 30/09/2026 informa uso do modelo na Interacao com Documentos do Sisbr 3.0, com arquitetura customizada e confidencial.
- **Sisbr IA e RAG seguem quentes**: publicacao recente descreve chat conversacional integrado ao core bancario e Pesquisa Inteligente de Normativos para mais de 62 mil colaboradores.
- **Fontes setoriais validam fora da fonte propria**: LetsMoney, TI Inside e Convergencia Digital reforcam app como agregador multibanco, Pix por contas externas, IA generativa e complexidade cooperativa do Open Finance.

### Banco Central
- **Pix Parcelado segue como gatilho central de outubro**: o BC informou no Forum Pix que a regulacao sera publicada em outubro, com definicao padronizada do produto e detalhamento operacional previsto para dezembro.
- **Bloqueio de chaves Pix associadas a fraude entrou no radar operacional**: sistemas do BC passam a bloquear chaves marcadas pelas instituicoes participantes como usadas em golpes e fraudes a partir de 04/10.
- **Pix por aproximacao esta no ciclo pos-vigencia**: a IN BCB 746 removeu o teto fixo de R$ 500 para Pix por aproximacao e Jornada Sem Redirecionamento a partir de 01/10/2026.
- **Manual de Fluxos do Pix v2.2 puxa backlog tecnico**: a IN BCB 777 divulga a versao 2.2 do Manual de Fluxos do Processo de Efetivacao do Pix.
- **Ciberseguranca e nuvem seguem como pauta transversal**: novas exigencias incluem certificados digitais, integracao segura, inteligencia cibernetica, rastreabilidade, pentest anual, controles de acesso e protecao de rede.
- **Pix/TIPS segue como fato estrategico recente**: BCB e BCE iniciaram avaliacao em 24/09 para conectar Pix ao sistema europeu TIPS, com analise tecnica, operacional, juridica e de negocio.
- **Ativos virtuais/PLDFT estao em prazo critico**: regras de PSAVs e comunicacao ao Coaf para carteiras autocustodiadas a partir de US$ 10 mil passaram a vigorar em 01/10/2026.

## Observacao de frescor

A rodada de 08/10 encontrou novo reforco publico para Sicoob e manteve sinais ativos de BB e Banco Central na janela de sete dias. Para CAIXA e BRB, os fatos mais fortes seguem concentrados em setembro/outubro, com suporte de fontes governamentais, regulador, controle externo, midia publica e paginas oficiais. Itens com mais de 90 dias foram marcados como contexto sustentado.

## Fontes principais
- https://www.bb.com.br/site/compras-contratacao-e-venda-de-imoveis/compras-e-contratacoes/avisos-e-editais/
- https://imprensa.bb.com.br/bb-e-pioneiro-global-em-diretrizes-para-ia-generativa-e-agentica/
- https://imprensa.bb.com.br/bb-amplia-seguranca-nas-ligacoes-com-origem-verificada/
- https://www.bb.com.br/site/developers/
- https://www.bcb.gov.br/detalhenoticia/20872/nota
- https://www.bcb.gov.br/detalhenoticia/21169/noticia
- https://www.bcb.gov.br/detalhenoticia/20979/nota
- https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=777&tipo=Instru%C3%A7%C3%A3o+Normativa+BCB
- https://www.caixa.gov.br/pix/Paginas/default.aspx
- https://www.caixa.gov.br/seguranca/paginas/default.aspx
- https://www.caixa.gov.br/caixatem/Paginas/default.aspx?lang=pt
- https://www.gov.br/mds/pt-br/noticias/bolsa-familia-tera-valor-minimo-de-r-691-a-partir-de-outubro
- https://www.gov.br/mds/pt-br/acoes-e-programas/bolsa-familia/conheca-as-regras/Conheca-as-Regras
- https://caixanoticias.caixa.gov.br/Paginas/Not%C3%ADcias/2026/08-AGOSTO/CAIXA-inicia-fase-Beta-do-novo-aplicativo-do-banco.aspx
- https://agenciabrasil.ebc.com.br/justica/noticia/2026-09/caso-master-tcdf-bloqueia-ate-r-27-bi-de-ex-dirigentes-do-brb
- https://agenciabrasil.ebc.com.br/justica/noticia/2026-09/fux-da-15-dias-para-uniao-e-bc-responderem-sobre-emprestimo-ao-brb
- https://buscarlicitacao.com.br/licitacao/df/brasilia/00000208000100-1-000008/2026/pregao-eletronico-edital-no-0552026
- https://novo.brb.com.br/pix/
- https://novo.brb.com.br/pix-2-2/
- https://novo.brb.com.br/dicas-de-seguranca/
- https://novo.brb.com.br/politica-de-privacidade/
- https://www.sicoob.com.br/web/sicoobfronteiras/noticias/-/asset_publisher/xAioIawpOI5S/content/id/199170100
- https://www.sicoob.com.br/web/sicoobourocredi/noticias/-/asset_publisher/xAioIawpOI5S/content/id/175914342
- https://www.sicoob.com.br/web/sicoobcentralunicoob/noticias/-/asset_publisher/xAioIawpOI5S/content/id/247097736
- https://www.sicoob.com.br/web/sicoob/noticias/-/asset_publisher/xAioIawpOI5S/content/id/275173922
- https://www.sicoob.com.br/web/sicoobcentralscrs/noticias/-/asset_publisher/xAioIawpOI5S/content/id/326354161
- https://www.letsmoney.com.br/noticias/sicoob-superapp-open-finance-ia-generativa/
- https://tiinside.com.br/01/09/2026/nova-versao-do-app-sicoob-incorpora-ia-e-open-finance/
- https://convergenciadigital.com.br/mercado/sicoob-cooperativas-enfrentam-a-complexidade-do-open-finance/
- https://www.bcb.gov.br/detalhenoticia/21267/nota
- https://www.bcb.gov.br/detalhenoticia/21271/nota
- https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews260924.it.html

## Publicacao
- Site estatico: `site/dashboard-bancos-publicos/index.html`
- Markdown local da rodada: `reports/dashboard-bancos-publicos-e-cooperativos-2026-10-08.md`
- CSV local da rodada: `reports/dashboard-bancos-publicos-e-cooperativos-2026-10-08.csv`
- Markdown publicado no site: `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.md`
- CSV publicado no site: `site/dashboard-bancos-publicos/dashboard-bancos-publicos-latest.csv`

## Aprendizados do XING LING
- O estudo mais recente disponivel em `workspace-xing-ling/study/2026-07-29.md` segue focado em **CloudCampus Huawei**, **management VLAN auto-negotiation**, **Option 43** e **VRRP** no onboarding de **Fit APs**.
- Para pre-vendas Huawei, o principal aprendizado pratico e tratar **management VLAN auto-negotiation** como parte do desenho de gestao e continuidade operacional, nao como detalhe de implantacao.
- O limiar de **500 APs** continua util como gatilho de arquitetura: abaixo disso, a recomendacao documentada favorece um dominio de gerenciamento; a partir disso, a Huawei recomenda multiplos dominios por predio, area ou quantidade de APs.
- Em bancos, a ponte com data center/campus e antecipar discovery sobre dominios de gestao, caminho AP-WAC L2/L3, DHCP, Option 43, VRRP e separacao entre gestao wired/wireless antes de fechar BoM e escopo de servicos.
