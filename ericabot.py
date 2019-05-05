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
@bot.event
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
        embed.add_field(name="서버 주소", value="EricaS.kr", inline=True)
        embed.add_field(name="오픈일", value="2019-05-05", inline=True)
        embed.add_field(name="카페 주소", value="https://cafe.naver.com/ericas", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("봇 "):
        YES = "네,"
        YES2 = "너"
        YES3 = "<@"
        YES4 = ">님이\""
        YES5 = "\"라고 말하였습니다."
        if message.content[-1] == "?":
            if message.content[2] == "나":
                embed = discord.Embed(title="Erica:", description= YES + YES2+message.content[3:-1], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="Erica:", description= YES + message.content[2:-1], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
        else:
            if message.content[2]== "나":
                embed = discord.Embed(title="Erica:", description= YES + YES2+message.content[3:-1], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="Erica:", description= YES+message.content[2:], color=0x383b38)
                await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("tr "):
         embed = discord.Embed(title="Erica:", description=YES3 + id + YES4 + message.content[3:] + YES5, color=0x383b38)
         await bot.send_message(message.channel, embed=embed)
    if "검색" == message.content.split(" ")[0]:
        group = message.content.split(" ")[1]
        search = requests.get("https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        bp = bs(search.text, "html.parser")
        img = bp.find_all('img')
        img2=img[2]
        img_src=img2.get('src')
        embed = discord.Embed(title="Erica:", description= "https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group, color=0x383b38)
        embed.set_footer(icon_url="https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        embed.set_image(url=img_src)
        await bot.send_message(message.channel, embed=embed)
        del group, search, bp, img, embed
    if message.content.startswith("비밀"):
        await bot.delete_message(message)
        embed = discord.Embed(title="비밀 메시지 입니다.", description=message.content[2:], color=0x383b38)
        await bot.send_message(message.channel, embed=embed)
        # await bot.send_message(message.channel, "https://www.google.com/search?q=")
    if message.content.startswith("T표현 "):
        AA = message.content[4:]
        AA2 = AA.upper()
        A = AA2.replace('A', ":regional_indicator_a:")
        B = A.replace('B', ":regional_indicator_b:")
        CC = B.replace('C', ":regional_indicator_c:")
        DD = CC.replace('D', ":regional_indicator_d:")
        EE = DD.replace('E', ":regional_indicator_e:")
        FF = EE.replace('F', ":regional_indicator_f:")
        GG = FF.replace('G', ":regional_indicator_g:")
        HH = GG.replace('H', ":regional_indicator_h:")
        II = HH.replace('I', ":regional_indicator_i:")
        JJ = II.replace('J', ":regional_indicator_j:")
        KK = JJ.replace('K', ":regional_indicator_k:")
        LL = KK.replace('L', ":regional_indicator_l:")
        MM = LL.replace('M', ":regional_indicator_m:")
        NN = MM.replace('N', ":regional_indicator_n:")
        OO = NN.replace('O', ":regional_indicator_o:")
        PP = OO.replace('P', ":regional_indicator_p:")
        QQ = PP.replace('Q', ":regional_indicator_q:")
        RR = QQ.replace('R', ":regional_indicator_r:")
        SSS = RR.replace('S', ":regional_indicator_s:")
        TT = SSS.replace('T', ":regional_indicator_t:")
        UU = TT.replace('U', ":regional_indicator_u:")
        VV = UU.replace('V', ":regional_indicator_v:")
        WW = VV.replace('W', ":regional_indicator_w:")
        XX = WW.replace('X', ":regional_indicator_x:")
        YY = XX.replace('Y', ":regional_indicator_y:")
        ZZ = YY.replace('Z', ":regional_indicator_z:")
        Z0 = ZZ.replace('0', ":zero:")
        Z1 = Z0.replace('1', ':one:')
        Z2 = Z1.replace('2', ':two:')
        Z3 = Z2.replace('3', ':three:')
        Z4 = Z3.replace('4', ':four:')
        Z5 = Z4.replace('5', ':five:')
        Z6 = Z5.replace('6', ':six:')
        Z7 = Z6.replace('7', ':seven:')
        Z8 = Z7.replace('8', ':eight:')
        Z9 = Z8.replace('9', ':nine:')
        embed = discord.Embed(description=Z9, color=0x383b38)
        await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("T명령어"):
        embed = discord.Embed(description= "봇 <내용> (대화 기능)\ntr <내용> (내용 강조)\n검색 <내용> (이미지 검색)\n비밀 <내용> (비밀 메시지)\nT표현 <내용> (이모티콘으로 영어,숫자표시)\nT투표 <(내용)/투표)> (투표)\nT랜덤 <1번/2번/3번/4번...> (랜덤 추첨)", color=0x383b38)
        await bot.send_message(message.channel, embed=embed)
    if message.content.startswith("T투표"):
        vote = message.content[4:].split("/")
        await bot.send_message(message.channel, vote[0])
        for TTT in range(1, len(vote)):
            choose = await bot.send_message(message.channel, "*"+vote[TTT]+"*")
            await bot.add_reaction(choose, '✅')
            await bot.add_reaction(choose, '❌')
    if message.content.startswith("T랜덤"):
        select = message.content[4:].split("/")
        select2 = random.choice(select)
        embed = discord.Embed(description="선정:"+select2, color=0x383b38)
        await bot.send_message(message.channel, embed=embed)
access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
