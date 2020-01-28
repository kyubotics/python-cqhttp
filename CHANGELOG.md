# 更新日志

## v1.3.1

- 修复 1.3.0 中 `on_*` 装饰器的严重 bug

## v1.3.0

- `CQHttp` 类新增 `logger` 属性，可获取 Flask app 的 logger
- `on_*` 装饰器支持不加括号使用
- 不再支持 CQHTTP v3 和 v4.0~4.7，请升级到 v4.8 或更新版本
- 优化部分代码

## v1.2.3

- 支持插件 v4.5.0 的 `meta_event` 上报
- `CQHttp` 类新增 `server_app` 属性，以明确获得内部的 `Flask` 对象，和原来的 `wsgi` 属性等价
