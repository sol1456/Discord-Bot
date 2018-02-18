# coding: utf-8
import discord

client = discord.Client()


@client.event
async def on_ready():
     print(f'Login <{client.user.name}>')


@client.event
async def on_message(msg):


	def message_content(msg_content):
		if msg.content == msg_content:
			if client.user != msg.author:
				return True


	if message_content('test'):
		await client.send_message(msg.channel, 'test')

	if message_content('emoji'):
		await client.send_message(msg.channel, ':innocent:')


	if message_content('image'):
		await client.send_file(msg.channel, './test.png')

	if message_content('file'):
		await client.send_file(msg.channel, './test.text')

	if message_content('mention'):
		await client.send_message(msg.channel, '<@391405352840593411>')


	if message_content('server -name'):
		await client.send_message(msg.channel, msg.channel.server)

	if message_content('server -owner'):
		await client.send_message(msg.channel, msg.channel.server.owner)



client.run('bot token')