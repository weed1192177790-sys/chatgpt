# ChatGPT Work Skills

这是为日常采购、工程、文件处理和研究工作维护的 Skill 仓库。

## 使用原则
- `SKILLS_INDEX.md` 是总路由：先判断任务类型，再读取对应 Skill。
- Skill 描述“怎么做事”，不是只针对某个产品。
- 多个 Skill 可以串联，例如：Excel 分类 → 厂家搜索 → 厂家筛选 → 询价表。
- 对外部事实、厂家、价格、法规等信息，优先检索最新公开来源并核验。
- 对 Excel / Word / PDF / PPT 等文件，优先保持原有结构、格式和数据完整性。

## 目录
- `skills/procurement/` 采购与供应商
- `skills/contract/` 合同
- `skills/engineering/` 工程与材料
- `skills/cambodia/` 柬埔寨合规
- `skills/spreadsheet/` Excel / 表格
- `skills/documents/` Word / PDF
- `skills/presentation/` PPT
- `skills/research/` 网页研究
- `skills/data/` 数据分析
- `skills/design/` 图片与设计
- `skills/github/` GitHub 工作流
- `skills/language/` 翻译与双语
- `rules/` 长期工作规则
- `templates/` 常用模板

## 维护
当出现新的高频任务时，优先新增或扩展 Skill，而不是把流程散落在聊天里。

## 检索入口与验证
通用“搜索、查资料、联网检索”和显式“anysearch”统一进入
`skills/research/web-research/SKILL.md`；AnySearch 的 CLI 调用、安装检查和回退策略见该文件。
本仓库是 Skill 指令集合，不是自动安装器。仅将仓库连接到 GitHub 不会让所有会话自动加载这些指令；
宿主需要先读取 `SKILLS_INDEX.md`，或调用下面的离线辅助入口并加载返回的 Skill。

```bash
python3 scripts/route_research.py "帮我联网检索调酒台厂家"
python3 -m unittest discover -s tests -v
```

路由器从索引读取别名，输出 JSON 的 skill 路径或 null，不调用网络。
测试验证常见表述、禁止联网、本地检索、索引路径和 Skill 调用说明；
复杂否定、引述、词义解释和跨域编排需代理按索引语义规则处理。
在线验证需在实际宿主确认已安装 AnySearch、运行时、网络权限和匿名额度/密钥，
再执行无敏感信息的查询；离线测试通过不等于在线服务或自动 Skill 加载已通过。
