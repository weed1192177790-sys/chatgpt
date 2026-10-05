# Skill Router

根据用户任务自动选择一个或多个 Skill。若任务跨域，可按顺序串联多个 Skill。

## 采购 / 供应商
- 找厂家、推荐厂家、谁能做、定制厂家 → `skills/procurement/supplier-search/SKILL.md`
- 筛厂家、排除贸易商、判断是否靠谱 → `skills/procurement/supplier-screening/SKILL.md`
- 生成询价内容、询价单、RFQ → `skills/procurement/rfq/SKILL.md`
- 比价、报价对比、性价比分析 → `skills/procurement/quotation-comparison/SKILL.md`

## Excel / 表格
- Excel、表格整理、清洗、公式、合并拆分 → `skills/spreadsheet/excel-general/SKILL.md`
- 漏项、材料分类、采购分类 → `skills/spreadsheet/classify-items/SKILL.md`
- 按厂家/品类拆成多份询价表 → `skills/spreadsheet/split-by-supplier/SKILL.md`
- 用户要求样式不动、格式保持 → `skills/spreadsheet/preserve-format/SKILL.md`

## 合同 / 文档
- 看合同风险、审合同 → `skills/contract/contract-review/SKILL.md`
- 改合同、规范条款 → `skills/contract/contract-rewrite/SKILL.md`
- Word 编辑、排版、生成文档 → `skills/documents/word-general/SKILL.md`
- PDF 提取、整理、生成 → `skills/documents/pdf-general/SKILL.md`

## 工程 / 材料
- 选材料、设备选型、参数建议 → `skills/engineering/material-selection/SKILL.md`
- 算量、体积、面积、数量 → `skills/engineering/quantity-calculation/SKILL.md`
- 施工方案、装卸、现场处理 → `skills/engineering/construction-solution/SKILL.md`

## 柬埔寨
- 进口合规、是否能进口、监管 → `skills/cambodia/import-compliance/SKILL.md`

## 通用高频
- PPT/演示文稿 → `skills/presentation/ppt-general/SKILL.md`
- anysearch、any search、搜索、搜一下、查资料、联网检索、联网搜索、上网查、网上查、网页检索、资料调研、核验来源 → `skills/research/web-research/SKILL.md`
- 数据分析、统计、图表 → `skills/data/data-analysis/SKILL.md`
- 图片修改、效果图、设计指令 → `skills/design/image-editing/SKILL.md`
- GitHub 仓库、代码、issue、PR → `skills/github/github-general/SKILL.md`
- 翻译、中英柬双语 → `skills/language/translation/SKILL.md`

## 默认组合示例
- “这个表格有漏项，按厂家分包并推荐厂家”
  1. classify-items
  2. supplier-search
  3. supplier-screening
  4. split-by-supplier
  5. preserve-format

- “帮我改合同付款方式并规范一下”
  1. contract-review
  2. contract-rewrite
  3. word-general

## 检索路由优先级
- 先判断用户意图：明确“不要联网 / 不用联网 / 不联网 / 不要搜索 / 不用搜索 / 禁止联网 / 仅本地 / 只搜索本地 / 只查本地”，或搜索本地文件、仓库代码、聊天记录、表格内内容时，不触发公网检索。
- anysearch 是 web-research 的工具入口别名；只读取一个检索 Skill，不新增重复调研流程。
- 采购、法规等跨域请求保留领域 Skill，并在需要公开事实时串联 web-research；例如“联网搜索调酒台厂家” → supplier-search → web-research → supplier-screening。
- “搜索是什么”等词义解释、引述搜索指令、否定与肯定混合、局部联网等复杂句由代理按上下文判断；不要只依赖关键词。
- 离线辅助调用：`python3 scripts/route_research.py "帮我查资料"`。输出检索 Skill 路径或 null；该脚本只处理通用检索入口，不替代其他领域路由，也不会发起网络请求。
