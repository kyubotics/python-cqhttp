from cqhttp import CQHttp, Error

bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='123',
             secret='abc')


@bot.on_message()
def handle_msg(event):
    try:
        # 下面这句等价于 bot.send_private_msg(user_id=event['user_id'],
        #                                  message='你好呀，下面一条是你刚刚发的：')
        bot.send(event, '你好呀，下面一条是你刚刚发的：')
    except Error as e:
        print('发送失败，错误码：{}'.format(e.retcode))

    # 返回 dict 给 CQHTTP 插件，走快速回复途径
    return {'reply': event['message'], 'at_sender': False}


@bot.on_notice('group_increase')
def handle_group_increase(event):
    info = bot.get_group_member_info(group_id=event.group_id,
                                     user_id=event.user_id)
    nickname = info['nickname']
    name = nickname if nickname else '新人'
    bot.send(event, message='欢迎{}～'.format(name))


@bot.on_request('group')
def handle_group_request(event):
    if event['comment'] != 'some-secret':
        # 如果插件版本是 3.x，这里需要使用 event.message
        # 验证信息不符，拒绝
        return {'approve': False, 'reason': '你填写的验证信息有误'}
    return {'approve': True}


bot.run(host='127.0.0.1', port=8080)
