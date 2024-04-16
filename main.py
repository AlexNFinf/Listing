import discord
import requests
from discord.ext import commands

def get_input(prompt):
    return input(prompt + ": ")

def format_TBMK(number):
    if -999999999 <= number < -1000000:
        return f"{number / 1000000:.2f}M"
    elif -999999 <= number < -1000:
        return f"{number / 1000:.2f}K"
    elif -1000 <= number < 1000:  # Adjusted condition for values between -999 and 999
        return f"{number:.0f}"
    elif 1000 <= number < 1000000:
        return f"{number / 1000:.2f}K"
    elif 1000000 <= number < 1000000000:
        return f"{number / 1000000:.2f}M"
    elif 1000000000 <= number <= 999999999999:
        return f"{number / 1000000000:.2f}B"
    else:
        return str(number)

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
@client.event
async def on_ready():
    await client.tree.sync()
    print("Online")

@client.hybrid_command()

async def list(ctx: commands.Context, ign: str, price: int, payment_methods: str):
    with requests.get("https://api.mojang.com/users/profiles/minecraft/" +
                      ign) as mojangApiResponse:
        if mojangApiResponse.status_code == 200:
            ign = mojangApiResponse.json()["id"]
        else:
            pass
    with requests.get(f"http://api2.lenny.ie/v1/profiles/{ign}?key=INSERT_KEY_HERE") as skyHelperResponse:
        rank = skyHelperResponse.json()['data'][0]['rank']
        skyblock_level = skyHelperResponse.json()['data'][0]['sblevel']
        farming_level = skyHelperResponse.json()['data'][0]['skills']['farming']['level']
        mining_level = skyHelperResponse.json()['data'][0]['skills']['mining']['level']
        foraging_level = skyHelperResponse.json()['data'][0]['skills']['foraging']['level']
        fishing_level = skyHelperResponse.json()['data'][0]['skills']['fishing']['level']
        enchanting_level = skyHelperResponse.json()['data'][0]['skills']['enchanting']['level']
        alchemy_level = skyHelperResponse.json()['data'][0]['skills']['alchemy']['level']
        carpentry_level = skyHelperResponse.json()['data'][0]['skills']['carpentry']['level']
        taming_level = skyHelperResponse.json()['data'][0]['skills']['taming']['level']
        skill_average = (farming_level + mining_level + foraging_level + fishing_level + enchanting_level + alchemy_level + carpentry_level + taming_level) / 8
        zombie_slayer = str(skyHelperResponse.json()['data'][0]['slayer']['zombie']['level'])
        spider_slayer = str(skyHelperResponse.json()['data'][0]['slayer']['spider']['level'])
        wolf_slayer = str(skyHelperResponse.json()['data'][0]['slayer']['wolf']['level'])
        enderman_slayer = str(skyHelperResponse.json()['data'][0]['slayer']['enderman']['level'])
        blaze_slayer = str(skyHelperResponse.json()['data'][0]['slayer']['blaze']['level'])
        slayers = zombie_slayer + "/" + spider_slayer + "/" + wolf_slayer + "/" + enderman_slayer + "/" + blaze_slayer
        weight_senither = int(skyHelperResponse.json()['data'][0]['weight']['senither']['total'])
        weight_lily = int(skyHelperResponse.json()['data'][0]['weight']['lily']['total'])
        healer_class_lvl = skyHelperResponse.json()['data'][0]['dungeons']['classes']['healer']['level']
        mage_class_lvl = skyHelperResponse.json()['data'][0]['dungeons']['classes']['mage']['level']
        berserk_class_lvl = skyHelperResponse.json()['data'][0]['dungeons']['classes']['berserk']['level']
        archer_class_lvl = skyHelperResponse.json()['data'][0]['dungeons']['classes']['archer']['level']
        tank_class_lvl = skyHelperResponse.json()['data'][0]['dungeons']['classes']['tank']['level']
        catacombs_avg_class_lvl = (healer_class_lvl + mage_class_lvl + berserk_class_lvl + archer_class_lvl + tank_class_lvl) / 5
        catacombs_level = skyHelperResponse.json()['data'][0]['dungeons']['catacombs']['skill']['level']
        total_slots = skyHelperResponse.json()['data'][0]['minions']['minionSlots']
        bonus_slots = skyHelperResponse.json()['data'][0]['minions']['bonusSlots']
        mining_hotm_level = skyHelperResponse.json()['data'][0]['mining']['hotM_tree']['level']
        mithril_powder = int(skyHelperResponse.json()['data'][0]['mining']['mithril_powder']['total'])
        gemstone_powder = int(skyHelperResponse.json()['data'][0]['mining']['gemstone_powder']['total'])
        networth_total = int(skyHelperResponse.json()['data'][0]['networth']['networth'])
        networth_unsoulbound = int(skyHelperResponse.json()['data'][0]['networth']['unsoulboundNetworth'])
        purse = int(skyHelperResponse.json()['data'][0]['networth']['purse'])
        bank = int(skyHelperResponse.json()['data'][0]['networth']['bank'])
        networth_coins = bank + purse

        if rank == "§a[VIP§6+§a]":
            rank = "[VIP+]"
        elif rank == "§c[§fYOUTUBE§c]":
            rank = "[YOUTUBE]"
        elif rank == "§b[MVP§6+§b]":
            rank = "[MVP+]"
        elif rank == "§a[VIP]":
            rank = "[VIP]"
        elif rank == "§7":
            rank = "NON"
        elif rank == "§6[MVP§8++§6]":
            rank = "[MVP++]"
        elif rank == "§b[MVP]":
            rank = "[MVP]"
        else:
            rank = "New Rank??"

        mithril_powder = round(mithril_powder / 1000, 1)
        gemstone_powder = round(gemstone_powder / 1000,1)
        networth_total = round(networth_total / 1000000,1)
        networth_coins = round(networth_coins / 1000000,1)
        networth_unsoulbound = round(networth_unsoulbound / 1000000,1)


        # Format emoji names
        rank_emoji = ":{}:".format(rank.lower())
        mining_emoji = ":{}:".format("mining")
        networth_emoji = ":{}:".format("networth")
        catacombs_emoji = ":{}:".format("catacombs")

    #Create the embed
    embed = discord.Embed(title="Account Information", color=0x00ff00)
    embed.add_field(name="Rank", value=f"**Rank**\n{rank}", inline=True)
    embed.add_field(name="<:levels:1211132187747811369>", value=f"**Skyblock Level**\n{skyblock_level}", inline=True)
    embed.add_field(name="<:skills:1211150427408830534>", value=f"**Skill Average**\n{skill_average}", inline=True)
    embed.add_field(name="<:slayer:1178284858632589312>", value=f"**Slayers**\n{slayers}", inline=True)
    embed.add_field(name="<:weight:1211131905848778883>",
                    value=f"**Weight**\nSenither: {weight_senither}\nLily: {weight_lily}", inline=True)
    embed.add_field(name="<:catacombs:1211133460001984672>",
                    value=f"**Catacombs**\nDungeons: Avg Class Lvl: {catacombs_avg_class_lvl}\nCatacombs: {catacombs_level}",
                    inline=True)
    embed.add_field(name="<:minions:1211131855370326016>",
                    value=f"**Minions**\nTotal Slots: {total_slots}\nBonus Slots: {bonus_slots}", inline=True)
    if mithril_powder >= 100 or gemstone_powder >= 100:
        mithril_powder = round(mithril_powder / 1000,2)
        gemstone_powder = round(gemstone_powder / 1000,2)
        embed.add_field(name="<:mining:1211131788777496656>",
                value=f"**Mining**\nHOTM Level: {mining_hotm_level}\nMithril Powder: {mithril_powder}m\nGemstone Powder: {gemstone_powder}m ",
                        inline=True)
    else:
        embed.add_field(name="<:mining:1211131788777496656>",
                    value=f"**Mining**\nHOTM Level: {mining_hotm_level}\nMithril Powder: {mithril_powder}k\nGemstone Powder: {gemstone_powder}k ",
                    inline=True)
    if networth_total >= 100:
        networth_total = round(networth_total / 1000,2)
        networth_unsoulbound = round(networth_unsoulbound / 1000,2)
        networth_coins = round(networth_coins / 1000,2)
        embed.add_field(name="<:networth:1211131741948088360>",
                            value=f"**Networth**\nTotal: {networth_total}b\nUnsoulbound: {networth_unsoulbound}b\nCoins: {networth_coins}b",)
    else:
        embed.add_field(name="<:networth:1211131741948088360>",
                    value=f"**Networth**\nTotal: {networth_total}m\nUnsoulbound: {networth_unsoulbound}m\nCoins: {networth_coins}m",
                    inline=True)
    embed.add_field(name=":moneybag:", value=f"**Price & Details**\nPrice: {price}\nPayment Methods: {payment_methods}",
                    inline=True)
    embed.set_footer(text="Made By phantom_v5")

    # Send the embed to the webhook
    webhook_url = input("Enter your Discord webhook URL: ")
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "embeds": [embed.to_dict()],
        "username": "NAME_OF_EMBED",
        "avatar_url": "AVATAR_PICTURE"
    }
    requests.post(webhook_url, json=payload, headers=headers)


if __name__ == "__main__":
    client.run("ENTER_BOT_TOKEN")
