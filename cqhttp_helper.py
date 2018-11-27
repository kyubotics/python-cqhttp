import cqhttp as _cqhttp

# working as a replacement.
Error = _cqhttp.Error


class CQHttp(_cqhttp.CQHttp):
    """
    **CoolQ HTTP API Python SDK封装类**

    :作者: SuperMarioSF
    :参考: HTTP API v3.4
    :版本: v1.0

    本类封装了CoolQ HTTP API的Python SDK中对应HTTP API的所有API。
    封装时参考并引用了HTTP API所提供的文档。


    感谢 **richardchien** 为我们提供了如此简便酷Q应用开发方式。

    本文件使用 WTFPL 2.0 许可证发布。

    ------------

    本文件适用于JetBrains PyCharm开发环境。
    你可以在PyCharm中在任何使用到本类的封装方法的位置按下 **Ctrl+Q** 来快速查看文档的内容。

    本页帮助文档也会下方会介绍原Python SDK中已有的功能的用法。

    要查看HTTP API的完整在线文档，请访问：

    | https://richardchien.github.io/coolq-http-api/
    | http://richardchien.gitee.io/coolq-http-api/docs/

    ------------

    **使用本文件**

    你可以将本文件作为导入 cqhttp 包的替代来使用。
    但需要注意，本文件需要你的 Python 环境中能够导入原 cqhttp 包，因为本文件只是对原 cqhttp 包的封装。
    在用本文件在PyCharm IDE开发完毕之后，你可以直接把对本文件的引用恢复为对原 cqhttp 包的引用。

    将原先导入 cqhttp 包的写法:

    >>> from cqhttp import CQHttp, Error

    更换成:

    >>> from cqhttp_helper import CQHttp, Error

    即可完成对本文件的所有内容的引用，享受自动补全和即时文档吧！

    在本帮助页面中，`bot` 指的是已初始化的 CQHttp 对象。

    ------------

    **对象列表**

    | cqhttp_helper.CQHttp(api_root=None, access_token=None, secret=None): CQHttp 封装类，继承原 cqhttp 的 CQHttp 类，提供封装的方法列表和实时帮助信息。
    | cqhttp_helper.Error(status_code, retcode=None): CQHttp 异常类。直接引用 cqhttp 的 Error 类，用于兼容目的。

    ------------

    **cqhttp_helper.CQHttp 中封装的方法列表**

    | send_private_msg(self, *, user_id, message, auto_escape=False): 发送私聊消息
    | send_private_msg_async(self, *, user_id, message, auto_escape=False): 发送私聊消息 (异步版本)
    | send_group_msg(self, *, group_id, message, auto_escape=False): 发送群消息
    | send_group_msg_async(self, *, group_id, message, auto_escape=False): 发送群消息 (异步版本)
    | send_discuss_msg(self, *, discuss_id, message, auto_escape=False): 发送讨论组消息
    | send_discuss_msg_async(self, *, discuss_id, message, auto_escape=False): 发送讨论组消息 (异步版本)
    | send_msg(self, *, message_type, user_id=None, group_id=None, discuss_id=None, message, auto_escape=False): 发送消息
    | send_msg_async(self, *, message_type, user_id=None, group_id=None, discuss_id=None, message, auto_escape=False): 发送消息 (异步版本)
    | delete_msg(self, *, message_id): 撤回消息
    | send_like(self, *, user_id, times=1): 发送好友赞
    | set_group_kick(self, *, group_id, user_id, reject_add_request=False): 群组踢人
    | set_group_ban(self, *, group_id, user_id, duration=30 * 60): 群组单人禁言
    | set_group_anonymous_ban(self, *, group_id, flag, duration=30 * 60): 群组匿名用户禁言
    | set_group_whole_ban(self, *, group_id, enable=True): 群组全员禁言
    | set_group_admin(self, *, group_id, user_id, enable=True): 群组设置管理员
    | set_group_anonymous(self, *, group_id, enable=True): 群组匿名
    | set_group_card(self, *, group_id, user_id, card=None): 设置群名片（群备注）
    | set_group_leave(self, *, group_id, is_dismiss=False): 退出群组
    | set_group_special_title(self, *, group_id, user_id, special_title, duration=-1): 设置群组专属头衔
    | set_discuss_leave(self, *, discuss_id): 退出讨论组
    | set_friend_add_request(self, *, flag, approve=True, remark=None): 处理加好友请求
    | set_group_add_request(self, *, flag, type, approve=True, reason=None): 处理加群请求、群组成员邀请
    | get_login_info(self): 获取登录号信息
    | get_stranger_info(self, *, user_id, no_cache=False): 获取陌生人信息
    | get_group_list(self): 获取群列表
    | get_group_member_info(self, *, group_id, user_id, no_cache=False): 获取群成员信息
    | get_group_member_list(self, *, group_id): 获取群成员列表
    | get_cookies(self): 获取 Cookies
    | get_csrf_token(self): 获取 CSRF Token
    | get_record(self, *, file, out_format): 获取语音
    | get_status(self): 获取插件运行状态
    | get_version_info(self): 获取酷 Q 及 HTTP API 插件的版本信息
    | set_restart(self): 重启酷 Q，并以当前登录号自动登录（需勾选快速登录）
    | set_restart_plugin(self): 重启 HTTP API 插件
    | clean_data_dir(self, *, data_dir): 清理数据目录
    | clean_data_dir_async(self, *, data_dir): 清理数据目录 (异步版本)
    | _get_friend_list(self): 获取好友列表 (实验性功能)

    ------------

    **创建实例**

    首先创建 CQHttp 类的实例，传入 api_root，即为酷 Q HTTP API 插件的监听地址，如果你不需要调用 API，也可以不传入。Access token 和签名密钥也在这里传入，如果没有配置 access_token 或 secret 项，则不传。

    ------------

    **异常处理**

    每个 API 调用最后都会由 `requests` 库来发出请求，如果网络无法连接，它可能会抛出 `ConnectionError` 等异常，见 requests错误与异常_ 。而一旦请求成功，本 SDK 会判断 HTTP 响应状态码，只有当状态码为 200，且 status 字段为 ok 或 async 时，会返回 data 字段的内容，否则抛出 cqhttp.Error 异常，在这个异常中你可以通过 status_code 和 retcode 属性来获取 HTTP 状态码和插件的 retcode（如果状态码不为 200，则 retcode 为 None），具体响应状态码和 retcode 的含义，见 响应说明_ 。

    .. _requests错误与异常: http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#id11
    .. _响应说明: https://richardchien.github.io/coolq-http-api/#/API?id=%E5%93%8D%E5%BA%94%E8%AF%B4%E6%98%8E

    ------------

    **消息发送**

    为了简化发送消息的操作，Python SDK 提供了 send(context, message) 函数，这里的第一个参数 context 也就是上报数据，传入之后函数会自己判断当前需要发送到哪里（哪个好友，或哪个群），无需手动再指定，其它参数仍然可以从 keyword argument 指定，例如 auto_escape=True。

    以 `send_` 开头（也就是消息发送相关）的接口都会包含一个 `message` 的参数。此参数接受普通的字符串(str)，也接受一个特定格式的列表(list)。列表格式在原HTTP API文档中是表示为 `array` ，称为 JSON数组类型。在Python中，表示为一个列表(list)中包括的数个字典(dict)。

    以下是调用范例:

    .. code-block:: python

        # 以字符串形式发送的普通消息。
        bot.send_private_message(user_id=1234567,
                    message="这是一条普通消息。\\n可以用这种方式换行。"

        # 以列表(list)形式发送的多段消息组合。
        bot.send_private_message(user_id=1234567,
                message=[
                                {
                                    "type": "text",
                                    "data": {"text": "这是第一段"}
                                },
                                {
                                    "type": "face",
                                    "data": {"id": "111"}
                                },
                                {
                                    "type": "text",
                                    "data": {"text": "这是表情之后的一段。"}
                                }
                        ])

    关于多段消息的每个单段的具体格式，请参见 HTTP API 文档中的 **消息格式** 的 **消息段（广义 CQ 码）** 一节。

    ------------

    **事件处理**

    `on_message`、`on_event`、`on_request` 三个装饰器分别对应三个上报类型（`post_type`），括号中指出要处理的消息类型（`message_type`）、事件名（`event`）、请求类型（`request_type`），一次可指定多个，如果留空，则会处理所有这个上报类型的上报。

    以下为范例:

    .. code-block:: python

        # 监听消息输入
        @bot.on_message()
        def handle_msg(context):
          bot.send(context, '你好呀，下面一条是你刚刚发的：')
          return {'reply': context['message'], 'at_sender': False}

        # 监听群组成员增加事件
        @bot.on_event('group_increase')
        def handle_group_increase(context):
           bot.send(context, message='欢迎新人～', is_raw=True)  # 发送欢迎新人

        # 监听加群和加好友请求
        @bot.on_request('group', 'friend')
        def handle_request(context):
           return {'approve': True}  # 同意所有加群、加好友请求


        bot.run(host='127.0.0.1', port=8080)

    上面三个装饰器装饰的函数，统一接受一个参数，即为上报的数据，具体数据内容见  事件上报_ ；返回值可以是一个字典，会被自动作为 JSON 响应返回给 HTTP API 插件，具体见 上报请求的响应数据格式_ 。


    .. _事件上报: https://richardchien.github.io/coolq-http-api/#/Post
    .. _上报请求的响应数据格式: https://richardchien.github.io/coolq-http-api/#/Post?id=%E4%B8%8A%E6%8A%A5%E8%AF%B7%E6%B1%82%E7%9A%84%E5%93%8D%E5%BA%94%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F

    ------------

    **运行实例**

    使用装饰器定义好处理函数之后，调用 `bot.run()` 即可运行。你需要传入 `host` 和 `port` 参数，来指定服务端需要运行在哪个地址，**然后在 HTTP API 插件的配置文件中，在 `post_url` 项中配置此地址（http://host:port/）**。

    **务必注意:** 如果不在插件配置文件中指定 `post_url` 为运行实例时指定的地址，Python SDK 将无法收到任何消息和事件。



    """
    def __init__(self, api_root=None, access_token=None, secret=None):
        """
        创建 CoolQ HTTP API 对象

        ------------

        :param str | None api_root: 酷 Q HTTP API 插件的监听地址的 URL ，与 HTTP API 的配置文件设定和实际使用环境相关。如果你不需要调用 API，也可以不传入。
        :param str | None access_token: 插件配置文件中所指定的 `access_token` 。如果未设定可不传此参数。
        :param str | None secret: 插件配置文件中所指定的 `secret` 。如果未设定可不传此参数。
        """
        super().__init__(api_root=api_root, access_token=access_token, secret=secret)

    def send_private_msg(self, *, user_id, message, auto_escape=False):
        '''
        发送私聊消息

        ------------

        :param int user_id: 对方 QQ 号
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: {"message_id": int 消息ID}
        :rtype: dict[string, int]
        '''
        return super().__getattr__('send_private_msg') \
            (user_id=user_id, message=message, auto_escape=auto_escape)

    def send_private_msg_async(self, *, user_id, message, auto_escape=False):
        """
        发送私聊消息 (异步版本)

        ------------

        :param int user_id: 对方 QQ 号
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: None
        :rtype: None
        """
        return super().__getattr__('send_private_msg_async') \
            (user_id=user_id, message=message, auto_escape=auto_escape)

    def send_group_msg(self, *, group_id, message, auto_escape=False):
        """
        发送群消息

        ------------

        :param int group_id: 群号
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: {"message_id": int 消息ID}
        :rtype: dict[string, int]
        """
        return super().__getattr__('send_group_msg') \
            (group_id=group_id, message=message, auto_escape=auto_escape)

    def send_group_msg_async(self, *, group_id, message, auto_escape=False):
        """
        发送群消息 (异步版本)

        ------------

        :param int group_id: 群号
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: None
        :rtype: None
        """
        return super().__getattr__('send_group_msg_async') \
            (group_id=group_id, message=message, auto_escape=auto_escape)

    def send_discuss_msg(self, *, discuss_id, message, auto_escape=False):
        """
        发送讨论组消息

        ------------

        :param int discuss_id: 讨论组 ID（正常情况下看不到，需要从讨论组消息上报的数据中获得）
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: {"message_id": int 消息ID}
        :rtype: dict[string, int]
        """
        return super().__getattr__('send_discuss_msg') \
            (discuss_id=discuss_id, message=message, auto_escape=auto_escape)

    def send_discuss_msg_async(self, *, discuss_id, message, auto_escape=False):
        """
        发送讨论组消息 (异步版本)

        ------------

        :param int discuss_id: 讨论组 ID（正常情况下看不到，需要从讨论组消息上报的数据中获得）
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: None
        :rtype: None
        """
        return super().__getattr__('send_discuss_msg_async') \
            (discuss_id=discuss_id, message=message, auto_escape=auto_escape)

    def send_msg(self, *, message_type, user_id=None, group_id=None, discuss_id=None, message, auto_escape=False):
        """
        发送消息

        ------------

        :param str message_type: 消息类型，支持 `private`、`group`、`discuss`，分别对应私聊、群组、讨论组
        :param int user_id: 对方 QQ 号（消息类型为 `private` 时需要）
        :param int group_id: 群号（消息类型为 `group` 时需要）
        :param int discuss_id: 讨论组 ID（需要从上报消息中获取，消息类型为 `discuss` 时需要）
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: {"message_id": int 消息ID}
        :rtype: dict[string, int]
        """
        return super().__getattr__('send_msg') \
            (message_type=message_type, user_id=user_id, group_id=group_id,
             discuss_id=discuss_id, message=message, auto_escape=auto_escape)

    def send_msg_async(self, *, message_type, user_id=None, group_id=None, discuss_id=None, message, auto_escape=False):
        """
        发送消息 (异步版本)

        ------------

        :param str message_type: 消息类型，支持 `private`、`group`、`discuss`，分别对应私聊、群组、讨论组
        :param int user_id: 对方 QQ 号（消息类型为 `private` 时需要）
        :param int group_id: 群号（消息类型为 `group` 时需要）
        :param int discuss_id: 讨论组 ID（需要从上报消息中获取，消息类型为 `discuss` 时需要）
        :param str | list[ dict[ str, unknown ] ] message: 要发送的内容
        :param bool auto_escape: 消息内容是否作为纯文本发送（即不解析 CQ 码），`message` 数据类型为 `list` 时无效
        :return: None
        :rtype: None
        """
        return super().__getattr__('send_msg_async') \
            (message_type=message_type, user_id=user_id, group_id=group_id,
             discuss_id=discuss_id, message=message, auto_escape=auto_escape)

    def delete_msg(self, *, message_id):
        """
        撤回消息

        ------------

        :param int message_id: 消息 ID
        :return: None
        :rtype: None
        """
        return super().__getattr__('delete_msg') \
            (message_id=message_id)

    def send_like(self, *, user_id, times=1):
        """
        发送好友赞

        ------------

        :param int user_id: 对方 QQ 号
        :param int times: 赞的次数，每个好友每天最多 10 次
        :return: None
        :rtype: None
        """
        return super().__getattr__('send_like') \
            (user_id=user_id, times=times)

    def set_group_kick(self, *, group_id, user_id, reject_add_request=False):
        """
        群组踢人

        ------------

        :param int group_id: 群号
        :param int user_id: 要踢的 QQ 号
        :param bool reject_add_request: 拒绝此人的加群请求
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_kick') \
            (group_id=group_id, user_id=user_id, reject_add_request=reject_add_request)

    def set_group_ban(self, *, group_id, user_id, duration=30 * 60):
        """
        群组单人禁言

        ------------

        :param int group_id: 群号
        :param int user_id: 要禁言的 QQ 号
        :param int duration: 禁言时长，单位秒，0 表示取消禁言
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_ban') \
            (group_id=group_id, user_id=user_id, duration=duration)

    def set_group_anonymous_ban(self, *, group_id, flag, duration=30 * 60):
        """
        群组匿名用户禁言

        ------------

        :param int group_id: 群号
        :param str flag: 要禁言的匿名用户的 flag（需从群消息上报的数据中获得）
        :param int duration: 禁言时长，单位秒，**无法取消匿名用户禁言**
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_anonymous_ban') \
            (group_id=group_id, flag=flag, duration=duration)

    def set_group_whole_ban(self, *, group_id, enable=True):
        """
        群组全员禁言

        ------------

        :param int group_id: 群号
        :param bool enable: 是否禁言
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_whole_ban') \
            (group_id=group_id, enable=enable)

    def set_group_admin(self, *, group_id, user_id, enable=True):
        """
        群组设置管理员

        ------------

        :param int group_id: 群号
        :param user_id: 要设置管理员的 QQ 号
        :param enable: True 为设置，False 为取消
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_admin') \
            (group_id=group_id, user_id=user_id, enable=enable)

    def set_group_anonymous(self, *, group_id, enable=True):
        """
        群组匿名

        ------------

        :param int group_id: 群号
        :param bool enable: 是否允许匿名聊天
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_anonymous') \
            (group_id=group_id, enable=enable)

    def set_group_card(self, *, group_id, user_id, card=None):
        """
        设置群名片（群备注）

        ------------

        :param int group_id: 群号
        :param int user_id: 要设置的 QQ 号
        :param str | None card: 群名片内容，不填或空字符串表示删除群名片
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_card') \
            (group_id=group_id, user_id=user_id, card=card)

    def set_group_leave(self, *, group_id, is_dismiss=False):
        """
        退出群组

        ------------

        :param int group_id: 群号
        :param bool is_dismiss: 是否解散，如果登录号是群主，则仅在此项为 true 时能够解散
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_leave') \
            (group_id=group_id, is_dismiss=is_dismiss)

    def set_group_special_title(self, *, group_id, user_id, special_title, duration=-1):
        """
        设置群组专属头衔

        ------------

        :param int group_id: 群号
        :param int user_id: 要设置的 QQ 号
        :param str special_title: 专属头衔，不填或空字符串表示删除专属头衔，只能保留前6个英文与汉字，Emoji 根据字符实际字符长度占用只能放最多3个甚至更少，超出长度部分会被截断
        :param int duration: 专属头衔有效期，单位秒，-1 表示永久，不过此项似乎没有效果，可能是只有某些特殊的时间长度有效，有待测试
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_special_title') \
            (group_id=group_id, user_id=user_id, special_title=special_title, duration=duration)

    def set_discuss_leave(self, *, discuss_id):
        """
        退出讨论组

        ------------

        :param int discuss_id: 讨论组 ID（正常情况下看不到，需要从讨论组消息上报的数据中获得）
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_discuss_leave') \
            (discuss_id=discuss_id)

    def set_friend_add_request(self, *, flag, approve=True, remark=None):
        """
        处理加好友请求

        ------------

        :param str flag: 加好友请求的 flag（需从上报的数据中获得）
        :param bool approve: 是否同意请求
        :param str remark: 添加后的好友备注（仅在同意时有效）
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_friend_add_request') \
            (flag=flag, approve=approve, remark=remark)

    def set_group_add_request(self, *, flag, type, approve=True, reason=None):
        """
        处理加群请求、群组成员邀请

        ------------

        :param str flag: 加群请求的 flag（需从上报的数据中获得）
        :param str type: `add` 或 `invite`，请求类型（需要和上报消息中的 `sub_type` 字段相符）
        :param bool approve: 是否同意请求/邀请
        :param str reason: 拒绝理由（仅在拒绝时有效）
        :return: None
        :rtype: None
        """
        return super().__getattr__('set_group_add_request') \
            (flag=flag, type=type, approve=approve, reason=reason)

    def get_login_info(self):
        """
        获取登录号信息

        ------------

        :return: { "user_id": (QQ 号: int), "nickname": (QQ 昵称: str) }
        :rtype: dict[ str, int | str ]

        ------------

        =========  =========  =========
        响应数据
        -------------------------------
        数据类型   字段名      说明
        =========  =========  =========
        int        user_id    QQ 号
        str        nickname   QQ 昵称
        =========  =========  =========
        """
        return super().__getattr__('get_login_info') \
            ()

    def get_stranger_info(self, *, user_id, no_cache=False):
        """
        获取陌生人信息

        ------------

        :param int user_id: QQ 号（不可以是登录号）
        :param bool no_cache: 是否不使用缓存（使用缓存可能更新不及时，但响应更快）
        :return: { "user_id": (QQ 号: int), "nickname": (昵称: str), "sex": (性别: str in ['male', 'female', 'unknown']), "age": (年龄: int) }
        :rtype: dict[ str, int | str ]

        ------------

        ========  =========  ======================================
        响应数据
        -----------------------------------------------------------
        数据类型  字段名     说明
        ========  =========  ======================================
        int       user_id    QQ 号
        str       nickname   昵称
        str       sex        性别，`male` 或 `female` 或 `unknown`
        int       age        年龄
        ========  =========  ======================================

        """
        return super().__getattr__('get_stranger_info') \
            (user_id=user_id, no_cache=no_cache)

    def get_group_list(self):
        """
        获取群列表

        ------------

        :return: [{ "group_id": (群号: int), "group_name": (群名称: str) }, ...]
        :rtype: list[ dict[ str, int | str ] ]

        ------------

        ========  ===========  =========
        响应数据
        --------------------------------
        数据类型  字段名       说明
        ========  ===========  =========
        int       group_id     群号
        str       group_name   群名称
        ========  ===========  =========

        """
        return super().__getattr__('get_group_list') \
            ()

    def get_group_member_info(self, *, group_id, user_id, no_cache=False):
        """
        获取群成员信息

        ------------

        :param int group_id: 群号
        :param int user_id: QQ 号（不可以是登录号）
        :param bool no_cache: 是否不使用缓存（使用缓存可能更新不及时，但响应更快）
        :return: { "group_id": (群号: int), "user_id": (QQ 号: int), "nickname": (昵称: str), "card": (群名片/备注: str), "sex": (性别: str in ['male', 'female', 'unknown']), "age": (年龄: int), "area": (地区: str), "join_time": (加群时间戳: int), "last_sent_time": (最后发言时间戳: int), "level": (成员等级: str), "role": (角色: str in ['owner', 'admin', 'member']), "unfriendly": (是否不良记录成员: bool), "title": (专属头衔: str), "title_expire_time": (专属头衔过期时间戳: int), "card_changeable": (是否允许修改群名片: bool) }
        :rtype: dict[ str, int | str | bool ]

        ------------

        ========  ===================  ======================================
            响应数据
        ---------------------------------------------------------------------
        数据类型  字段名               说明
        ========  ===================  ======================================
        int       group_id             群号
        int       user_id              QQ 号
        str       nickname             昵称
        str       card                 群名片/备注
        str       sex                  性别，`male` 或 `female` 或 `unknown`
        int       age                  年龄
        str       area                 地区
        int       join_time            加群时间戳
        int       last_sent_time       最后发言时间戳
        str       level                成员等级
        str       role                 角色，`owner` 或 `admin` 或 `member`
        bool      unfriendly           是否不良记录成员
        str       title                专属头衔
        int       title_expire_time    专属头衔过期时间戳
        bool      card_changeable      是否允许修改群名片
        ========  ===================  ======================================
        """
        return super().__getattr__('get_group_member_info') \
            (group_id=group_id, user_id=user_id, no_cache=no_cache)

    def get_group_member_list(self, *, group_id):
        """
        获取群成员列表

        ------------

        :param int group_id: 群号
        :return: [{ "group_id": (群号: int), "user_id": (QQ 号: int), "nickname": (昵称: str), "card": (群名片/备注: str), "sex": (性别: str in ['male', 'female', 'unknown']), "age": (年龄: int), "area": (地区: str), "join_time": (加群时间戳: int), "last_sent_time": (最后发言时间戳: int), "level": (成员等级: str), "role": (角色: str in ['owner', 'admin', 'member']), "unfriendly": (是否不良记录成员: bool), "title": (专属头衔: str), "title_expire_time": (专属头衔过期时间戳: int), "card_changeable": (是否允许修改群名片: bool) }, ...]
        :rtype: list[ dict[ str, int | str | bool ] ]

        ------------

        响应数据以 **列表** 包装的字典的形式提供。`( List[ Dict[ ...] ] )`

        ========  ===================  ======================================
            响应数据
        ---------------------------------------------------------------------
        数据类型  字段名               说明
        ========  ===================  ======================================
        int       group_id             群号
        int       user_id              QQ 号
        str       nickname             昵称
        str       card                 群名片/备注
        str       sex                  性别，`male` 或 `female` 或 `unknown`
        int       age                  年龄
        str       area                 地区
        int       join_time            加群时间戳
        int       last_sent_time       最后发言时间戳
        str       level                成员等级
        str       role                 角色，`owner` 或 `admin` 或 `member`
        bool      unfriendly           是否不良记录成员
        str       title                专属头衔
        int       title_expire_time    专属头衔过期时间戳
        bool      card_changeable      是否允许修改群名片
        ========  ===================  ======================================

        **备注:** 响应内容为包含字典的列表 *( List[ Dict[] ] )* ，每个元素的内容和 `get_group_member_info` 接口相同，但对于同一个群组的同一个成员，获取列表时和获取单独的成员信息时，某些字段可能有所不同，例如 `area`、`title` 等字段在获取列表时无法获得，具体应以单独的成员信息为准。

        """
        return super().__getattr__('get_group_member_list') \
            (group_id=group_id)

    def get_cookies(self):
        """
        获取 Cookies

        ------------

        :return: { "cookies": (Cookies: str)}
        :rtype: dict[ str, str ]

        ------------

        ========  ===========  =========
        响应数据
        --------------------------------
        数据类型  字段名       说明
        ========  ===========  =========
        str       cookies      Cookies
        ========  ===========  =========

        """
        return super().__getattr__('get_cookies') \
            ()

    def get_csrf_token(self):
        """
        获取 CSRF Token

        ------------

        :return: { "token": (CSRF Token: int)}
        :rtype: dict[ str, int ]

        ------------

        ========  ===========  ==========
        响应数据
        ---------------------------------
        数据类型  字段名       说明
        ========  ===========  ==========
        int       token        CSRF Token
        ========  ===========  ==========

        """
        return super().__getattr__('get_csrf_token') \
            ()

    def get_record(self, *, file, out_format):
        """
        获取语音

        ------------

        :param str file: 收到的语音文件名，如 `0B38145AA44505000B38145AA4450500.silk`
        :param str out_format: 要转换到的格式，目前支持 `mp3`、`amr`、`wma`、`m4a`、`spx`、`ogg`、`wav`、`flac`
        :return: { "file": (转换后的语音文件名: str)}
        :rtype: dict[ str, str ]


        ------------

        其实并不是真的获取语音，而是转换语音到指定的格式，然后返回语音文件名（`data/record` 目录下）。

        ========  ===========  =============================================================
        响应数据
        ------------------------------------------------------------------------------------
        数据类型   字段名       说明
        ========  ===========  =============================================================
        str       file          转换后的语音文件名，如 `0B38145AA44505000B38145AA4450500.mp3`
        ========  ===========  =============================================================

        """
        return super().__getattr__('get_record') \
            (file=file, out_format=out_format)

    def get_status(self):
        """
        获取插件运行状态

        ------------

        :return: { "good": (正常运行: bool), "app_initialized": (插件已初始化: bool), "app_enabled": (插件已启用: bool), "online": (当前QQ在线: bool), "http_service_good": (HTTP服务正常运行: bool), "ws_service_good": (WebSocket服务正常运行: bool), "ws_reverse_service_good": (反向WebSocket服务正常运行: bool) }
        :rtype: dict[ str, bool ]

        ------------

        ========  ========================  ====================================
        响应数据
        ------------------------------------------------------------------------
        数据类型  字段名                    说明
        ========  ========================  ====================================
        bool      good                      插件状态符合预期，意味着插件已初始化，需要启动的服务都在正常运行，且 QQ 在线
        bool      app_initialized           插件已初始化
        bool      app_enabled               插件已启用
        bool      online                    当前 QQ 在线
        bool      http_service_good         `use_http` 配置项为 `yes` 时有此字段，表示 HTTP 服务正常运行
        bool      ws_service_good           `use_ws` 配置项为 `yes` 时有此字段，表示 WebSocket 服务正常运行
        bool      ws_reverse_service_good   `use_ws_reverse` 配置项为 `yes` 时有此字段，表示反向 WebSocket 服务正常运行
        ========  ========================  ====================================
        """
        return super().__getattr__('get_status') \
            ()

    def get_version_info(self):
        """
        获取酷 Q 及 HTTP API 插件的版本信息

        ------------

        :return: { "coolq_directory": (酷Q根目录路径: str), "coolq_edition": (酷Q版本: str in ['air', 'pro']), "plugin_version": (API插件版本: str), "plugin_build_number": (API插件build号: int), "plugin_build_configuration": (API插件编译配置: str in ['debug', 'release']) }
        :rtype: dict[ str, int | str ]


        ------------

        ========  ==========================  ===============================
        响应数据
        ---------------------------------------------------------------------
        数据类型  字段名                      说明
        ========  ==========================  ===============================
        str       coolq_directory             酷 Q 根目录路径
        str       coolq_edition               酷 Q 版本，`air` 或 `pro`
        str       plugin_version              HTTP API 插件版本，例如 2.1.3
        int       plugin_build_number         HTTP API 插件 build 号
        str       plugin_build_configuration  HTTP API 插件编译配置，`debug` 或 `release`
        ========  ==========================  ===============================
        """
        return super().__getattr__('get_version_info') \
            ()

    def set_restart(self):
        """
        重启酷 Q，并以当前登录号自动登录（需勾选快速登录）

        ------------

        :return: None
        :rtype: None
        """
        return super().__getattr__('set_restart') \
            ()

    def set_restart_plugin(self):
        """
        重启 HTTP API 插件

        ------------

        :return: None
        :rtype: None

        ------------

        由于重启插件同时需要重启 API 服务，这意味着当前的 API 请求会被中断，因此这个接口会延迟 2 秒重启插件，接口返回的 status 是 async。

        **在Python SDK中返回 None 。**
        """
        return super().__getattr__('set_restart_plugin') \
            ()

    def clean_data_dir(self, *, data_dir):
        """
        清理数据目录

        ------------

        :param str data_dir: 收到清理的目录名，支持 `image`、`record`、`show`、`bface`
        :return: None
        :rtype: None

        ------------

        用于清理积攒了太多旧文件的数据目录，如 `image`。

        HTTP API v3.3.4 新增
        """
        return super().__getattr__('clean_data_dir') \
            (data_dir=data_dir)

    def clean_data_dir_async(self, *, data_dir):
        """
        清理数据目录 (异步版本)

        ------------

        :param str data_dir: 收到清理的目录名，支持 `image`、`record`、`show`、`bface`
        :return: None
        :rtype: None

        ------------

        用于清理积攒了太多旧文件的数据目录，如 `image`。

        HTTP API v3.3.4 新增
        """
        return super().__getattr__('clean_data_dir_async') \
            (data_dir=data_dir)

    def _get_friend_list(self):
        """
        获取好友列表 (实验性功能)

        ------------

        :return: [{ "friend_group_id": (好友分组 ID: int), "friend_group_name": (好友分组名称: str), "friends": (分组中的好友: [{ "nickname": (好友昵称: str), "remark": (好友备注: str), "user_id": (好友 QQ 号: int) }, ...]) }, ...]
        :rtype: list[ dict[ str, int | str | list[ dict[ str, int | str ] ] ] ]

        ------------

        响应数据以 **列表** 包装的字典的形式提供。`( List[ Dict[ ...] ] )`

        ========  ==================  ===============================
        响应数据
        -------------------------------------------------------------
        数据类型  字段名                      说明
        ========  ==================  ===============================
        int       friend_group_id     好友分组 ID
        str       friend_group_name   好友分组名称
        list      friends             分组中的好友
        ========  ==================  ===============================

        其中，好友信息结构以 **字典** 的形式存储在响应数据中的分组中的好友 `friends` 的 **列表** 中。`( List[ Dict[ ...] ] )`

        ========  ==================  ===============================
        好友信息结构
        -------------------------------------------------------------
        数据类型  字段名                      说明
        ========  ==================  ===============================
        str       nickname            好友昵称
        str       remark              好友备注
        int       user_id             好友 QQ 号
        ========  ==================  ===============================

        """
        return super().__getattr__('_get_friend_list') \
            ()

    def send(self, context, message, **kwargs):
        """
        便捷回复。会根据传入的context自动判断回复对象
        ------------
        :param dict context: 事件收到的content
        :return: None
        :rtype: None
        ------------
        """
        context = context.copy()
        context['message'] = message
        context.update(kwargs)
        if 'message_type' not in context:
            if 'group_id' in context:
                context['message_type'] = 'group'
            elif 'discuss_id' in context:
                context['message_type'] = 'discuss'
            elif 'user_id' in context:
                context['message_type'] = 'private'
        return super().__getattr__('send_msg')(**context)

