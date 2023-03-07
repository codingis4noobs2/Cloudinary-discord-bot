# message intent should be on for the bot, https://discord.com/developers/applications

import discord
from discord.ext import commands
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import random
import string

r_id = []

# discord token
token = "your_discord_token"

# cloudinary configs
cloudinary.config(
	cloud_name = "your_cloud_name",
	api_key = "your_api_key",
	api_secret = "your_api_secret",
	secure = True
)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

# functions
def is_verified(user, guild):
    role_name = "User"
    member = discord.utils.get(guild.members, id=user.id)
    role = discord.utils.get(guild.roles, name=role_name)
    if role in user.roles:
        return True
    else:
        return False

def line():
    print("__----------------------------------__\n")

def coms():
    message = ""
    message += "**`!help`**\n"
    message += "**`!usage`**\n"
    message += "**`!resize_fill`**\n"
    message += "**`!resize_scale`**\n"
    message += "**`!limit`**\n"
    message += "**`!crop`**\n"
    message += "**`!blur_face`**\n"
    message += "**`!pixelate_portion`**\n"
    message += "**`!to_grayscale`**\n"
    message += "**`!add_text`**\n"
    return message


def help(opreation):
    if opreation == "help":
        msg = "You serious? :joy:"
        return msg

    if opreation == "resize_fill":
        msg = "Resizes your images to fill specified dimensions by setting the width and height. This will resize and crop the image so an image with the exact specified dimensions is generated.\n"
        return msg
    
    if opreation == "resize_scale":
        msg = "Resizes your images to scale specified dimensions by setting the width and height. Cloudinary will automatically apply the scale crop mode.\n"
        return msg
    
    if opreation == "limit":
        msg = "Keep the original image aspect ratio and all its parts visible, and just limit it's size by specify the width and height. This will create an image that does not exceed the given width and height.\n"
        return msg
    
    if opreation == "crop":
        msg = "Crops your image based on custom/fixed coordinates. Use this method when you know beforehand what the correct absolute cropping coordinates are. This is very useful when your users manually select the region to crop out of the original image.\n"
        return msg
    
    if opreation == "blur_face":
        msg = "Hide faces in your images by using Cloudinary APIs to either blur or automatically pixelate the detected faces..\n"
        return msg
    
    if opreation == "pixelate_portion":
        msg = "Applies a pixelization effect to your image in given co-ordinates.\n"
        return msg
    
    if opreation == "to_grayscale":
        msg = "Converts your images to grayscale.\n"
        return msg
    
    if opreation == "add_text":
        msg = "Customize text overlay's position by setting the gravity and the optional offset of the x and y. While the default text positioning ('gravity') is center, you can place your text in any other area of the image (even outside the image's boundaries!).\n"
        return msg

def resize(img, width, height):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, width=width, height=height, crop="fill")
    return url

def resize_scale(img, width, height):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, width=width, height=height, crop="scale")
    return url

def limit(img, width, height):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, width=width, height=height, crop="limit")
    return url

def crop(img, x, y, width, height):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, width=width, height=height, x=x, y=y, crop="crop")
    return url

def blur_face(img):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, effect="blur_faces:2000")
    return url

def pixelate_portion(img, x, y, width, height):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, width=width, height=height, x=x, y=y, crop="fill", effect="pixelate_region")
    return url

def to_grayscale(img):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, effect="grayscale")
    return url

def add_text(img, color_code, font_family, font_size, position, text):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    while random_string in r_id:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    r_id.append(random_string)
    upload(img, public_id=random_string)
    url, options = cloudinary_url(random_string, overlay={"font_family":font_family, "font_size":font_size, "text":text, "color":color_code},  gravity=position)
    return url


# discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "hey" in message.content.lower():
        await message.add_reaction("👋")
    
    if "!verify" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            await message.reply("You are already verified!")
        else:
            await message.add_reaction("✔️")
            role = discord.utils.get(guild.roles, name="User")
            await user.add_roles(role)
            await message.reply("You have been assigned **User** role!")
    
    if "!commands" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            await message.reply(coms())
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!help" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                opreation = message.content.split(" ")[1]
                await message.reply(help(opreation))
            except:
                await message.reply("Please provide a valid command name!!!, for e.g. !help limit")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!resize_fill" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                width = int(lst[1])
                height = int(lst[2])
                url = resize(img, width, height)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!resize_scale" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                width = int(lst[1])
                height = int(lst[2])
                url = resize_scale(img, width, height)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!limit" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                width = int(lst[1])
                height = int(lst[2])
                url = limit(img, width, height)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!crop" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                x = int(lst[1])
                y = int(lst[2])
                width = int(lst[3])
                height = int(lst[4])
                url = crop(img, x, y, width, height)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!blur_face" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                img = message.attachments[0].url
                url = blur_face(img)
                await message.reply(url)
            except:
                await message.reply("Some problem with Image occurred, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!pixelate_portion" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                x = int(lst[1])
                y = int(lst[2])
                width = int(lst[3])
                height = int(lst[4])
                url = pixelate_portion(img, x, y, width, height)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!to_grayscale" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                url = to_grayscale(img)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    if "!add_text" in message.content:
        user = message.author
        guild = message.guild
        if is_verified(user, guild):
            try:
                lst = message.content.split(" ")
                img = message.attachments[0].url
                color_code = lst[1]
                font_family = lst[2]
                font_size = int(lst[3])
                position = lst[4]
                text = lst[5]
                url = add_text(img, color_code, font_family, font_size, position, text)
                await message.reply(url)
            except:
                await message.reply("Image not provided or Invalid dimensions, Please Try Again!!!")
        else:
            await message.reply("You are not verified yet, please verify yourself by typing !verify")

    

client.run(token)
