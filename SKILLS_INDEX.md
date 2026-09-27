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
- 网页检索、资料调研、核验来源 → `skills/research/web-research/SKILL.md`
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
