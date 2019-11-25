import discord, pytz
from discord.ext import commands
from datetime import datetime, date

tz = pytz.timezone('Asia/Tokyo')

bot_name = "Homework Bot"
default_value = "564835628542675265615265728356728"
owner_id = "402344993391640578"

client = commands.Bot(command_prefix=".")

weekdays_short = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
weekdays_long = ("monday", "tuesday", "wednesday", "thursday", "friday")

subject_list = (
            ("individuals & societies", "individuals and societies", "i&s", "ins"),
            ("english", "eng", "lal", "l&l", "language and literature", "language & literature", "ela", "eal"),
            ("math", "maths", "mathematics", "mth"),
            ("science", "sci"),
            ("jpn", "jap", "japanese", "japan"),
            ("mus", "music"),
            ("des", "design"),
            ("lib", "library"),
            ("pe", "phy", "physical education", "phys ed"),
            ("hea", "health"),
            ("hmrm", "homeroom", "hr")
        )

channel_ids_dict = {648498068949434378: "9", 648498140315385886: "8", 648498182577324042: "7"}


def DetermineValidity(subject, date_input, channel_id):
    if channel_id in channel_ids_dict:
        channel_grade = channel_ids_dict[channel_id]
        if subject in subject_list:
            if date_input in (weekdays_short or weekdays_long):
                day_to_index = {
                    "mon": 0,
                    "monday": 0,
                    "tue": 1,
                    "tuesday": 1,
                    "wed": 2,
                    "wednesday": 2,
                    "thu": 3,
                    "thursday": 3,
                    "fri": 4,
                    "friday": 4,
                    "sat": 5,
                    "saturday": 5,
                    "sun": 6,
                    "sunday": 6
                }
                date = day_to_index[date_input]
            else:
                try:
                    int(date_input[0] + date_input[1] + date_input[3] + date_input[4])
                except ValueError:
                    date = ""
                else:
                    date = int(date_input[0] + date_input[1] + date_input[3] + date_input[4])
            return date
        else:
            return ""
    else:
        return ""



@client.event
async def on_ready():
    print(bot_name + " is now running")
    await client.change_presence(activity=discord.Game("Use '.hw ?' for info"))


@client.command(pass_context=True)
async def hw(ctx, date_input, subject, *, task=default_value):
    date_input = str.lower(date_input)
    task = str.lower(task)
    subject = str.lower(subject)

    validity = DetermineValidity(subject, date_input, task)
    print(type(ctx.channel.id))
    if validity == "":
        await ctx.send(ctx.message.author.mention + "  |  That is not the correct use of this command\n Use **.hw ?** for information about how to use commands")
    elif task == default_value:
        await ctx.send(ctx.message.author.mention + "  |  Please specify the task, like this: **.hw *subject day task***\nFor more information, use **.tt ?**")
    elif validity.__len__() == 1:
        channel = channel_ids_dict[ctx.channel.id]
        count = 0
        for sub in subject_list:
            if subject in sub:
                subject = count
            count += 1
        with open("data/" + channel + ".txt", "r") as file:
            temp = eval(file.readline())[subject]
            temp.append((str(validity), task))
        with open("data/" + channel + ".txt", "w") as file:
            file.write(temp)
    else:
        print("")














print(str(datetime.now(tz).hour + datetime.now(tz).minute / 60))

client.run("NjQ4NDkzMzE0NzA1NzE5Mjk2.XdvCpA.t45jtxe8q1w9WbV_4rdCkiRF2Cs")