from cqhttp import CQHttp

bot = CQHttp(api_root='http://127.0.0.1:5700/')


@bot.on_message()
def handle_msg(context):
    # 下面这句等价于 bot.send_private_msg(user_id=context['user_id'], message='你好呀，下面一条是你刚刚发的：')
    bot.send(context, '你好呀，下面一条是你刚刚发的：')
    return {'reply': context['message'], 'at_sender': False}  # 返回给 HTTP API 插件，走快速回复途径


@bot.on_event('group_increase')
def handle_group_increase(context):
    nickname = bot.get_group_member_info(group_id=context['group_id'],
                                         user_id=context['user_id'])['nickname']
    name = nickname if nickname else '新人'
    bot.send(context, message='欢迎{}～'.format(name), is_raw=True)


@bot.on_request('group')
def handle_group_request(context):
    if context['message'] != 'some-secret':
        # 验证信息不符，拒绝
        return {'approve': False, 'reason': '你填写的验证信息有误'}
    return {'approve': True}


bot.run(host='127.0.0.1', port=8080)
