# holiday-cn

[![Build Status](https://github.com/NateScarlet/holiday-cn/workflows/CI/badge.svg)](https://github.com/NateScarlet/holiday-cn/actions)
[![Release](https://img.shields.io/github/release/NateScarlet/holiday-cn.svg)](https://github.com/NateScarlet/holiday-cn/releases/latest)
[![CalVer](https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg)](http://calver.org)
[![Maintainability](https://api.codeclimate.com/v1/badges/c8e9d9c51bd2d858c577/maintainability)](https://codeclimate.com/github/NateScarlet/holiday-cn/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c8e9d9c51bd2d858c577/test_coverage)](https://codeclimate.com/github/NateScarlet/holiday-cn/test_coverage)
![Maintenance](https://img.shields.io/maintenance/yes/2021.svg)

中国法定节假日数据 自动每日抓取国务院公告23

- [x] 提供 JSON 格式节假日数据
- [x] CI 自动更新
- [x] 数据变化时自动发布新版本 ( `Watch` - `Release only` 以获取邮件提醒! )
- [x] [发布页面]提供 JSON 打包下载

数据格式:

[JSON Schema](./schema.json)

```TypeScript
interface Holidays {
  /** 完整年份, 整数。*/
  year: number;
  /** 所用国务院文件网址列表 */
  papers: string[];
  days: {
    /** 节日名称 */
    name: string;
    /** 日期, ISO 8601 格式 */
    date: string;
    /** 是否为休息日 */
    isOffDay: boolean;
  }[]
}
```

## 注意事项

- 年份是按照国务院文件标题年份而不是日期年份，12 月份的日期可能会被下一年的文件影响，因此应检查两个文件。

## 通过互联网使用

数据地址格式:

    https://raw.githubusercontent.com/liurenjie520/holiday-cn/master/{年份}.json
    https://raw.githubusercontent.com/liurenjie520/holiday-cn/master/{年份}节假日.ics

