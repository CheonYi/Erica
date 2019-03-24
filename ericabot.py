import discord



from discord.ext import commands



import asyncio





import os





client = discord.Client()



bot = commands.Bot(command_prefix='T')







@bot.event



async def on_ready():



    print("로그인")



    print(bot.user.name)



    print(bot.user.id)



    print("------------------")



    await bot.change_presence(game=discord.Game(name="서버주소: EricaS.kr", type=1))



async def on_message(message):



    if message.content.startswith("/상담"):



        id = message.author.id



        server = message.server



        name = message.author.name



        name2 = name.lower()



        everyone = discord.PermissionOverwrite(read_messages=False, send_messages=False, create_instant_invite=False,



                                                           manage_channel=False, manage_permissions=False, manage_webhooks=False,



                                                           send_TTS_messages=False, manage_messages=False, embed_links=False,



                                                           attach_files=False, read_message_history=False, mention_everyone=False,



                                                           use_external_emojis=False, add_reactions=False)



        Member = discord.PermissionOverwrite(read_messages=True, send_messages=True, create_instant_invite=False,read_message_history=True,



                                                         manage_channel=False, manage_permissions=False, manage_webhooks=False)



        member_perms = [(mentioned, Member) for mentioned in message.mentions]



        await bot.create_channel(server, name2, (discord.utils.get(message.server.roles, name="@everyone"), everyone),



                                                (discord.utils.get(message.server.members, name=name), Member),



                                             *member_perms, type=discord.ChannelType.text)



        



        



        await bot.send_message(discord.utils.get(message.server.channels, name=name2), "@everyone\n"+ "<@"+id+">님의 상담을 시작합니다.\n상담 내용은 본인, 관리진만 확인 할 수 있습니다.\n상담이 끝나면 채널이 삭제 될 수도 있습니다.")



        



        



    if message.content.startswith("공지띄우기1"):



        await bot.delete_message(message)



        embed = discord.Embed(title="에리카 관리자",



                              description="",



                              color=0x00ff00)



        await bot.send_message(message.channel, embed=embed)



    if message.content.startswith("/서버정보"):



        embed = discord.Embed(color=0x00ff00)



        embed.add_field(name="서버 이름", value="EricaServer", inline=True)



        embed.add_field(name="서버 관리자", value="천이", inline=True)



        embed.add_field(name="서버 주소", value="RPSV.kr", inline=True)



        embed.add_field(name="오픈일", value="미정", inline=True)



        embed.add_field(name="카페 주소", value="https://cafe.naver.com/ericas", inline=True)



        embed.set_thumbnail(url=message.author.avatar_url)



        await bot.send_message(message.channel, embed=embed)



        



access_token = os.environ["BOT_TOKEN"]



bot.run(access_token)
