################
#
# Scraping
# Profile
# Pics 
# from Telegram
# Groups.
#
################
# PYTHON 3.6.9
# Telethon Version v1.16.4 at repo https://github.com/LonamiWebs/Telethon
############################################################################
import os
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

############################################################################
#
# obtain keys from my.telegram.org
#
api_id = ''          # from my.telegram.org , go to API Tools
api_hash = ''        # same as above
phone = '+123456789' # the phone number you registered at my.telegram.org
#
#
#############################################################################
#
#initialize a client
# Remember to use different nick for different numbers , here it is 'friend'

client = TelegramClient('friend', api_id, api_hash)

##############################
#
# main function entry point
#
##############################

async def main():
    
    # displaying all the chats you are in
    
    async for dialog in client.iter_dialogs():
        print(dialog.name, ":", dialog.id)
    
    # dialog.id is groupID under your study
    # keep this field empty for the first time, note the ID from first run.
    chat = -1111111111111111
    
    # get all the lists of the usernames in the group
    async for user in client.iter_participants(chat):
        print(user.id, user.username)

    # Display the list of Administrators in the group
    from telethon.tl.types import ChannelParticipantsAdmins
    async for user in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        print(user.id,user.first_name)

    #########################################################################################
    # 
    # Download all the profile photos of all users
    # Output image format is userID_username_typeofMedia_date_imagenumber_fileextension
    #
    #########################################################################################

    print("Download profile pictures of all the users in the group.. \n")
    from telethon.tl.types import ChannelParticipantsAdmins
    async for user in client.iter_participants(chat, filter=""):
        print(user.id,user.first_name)
        counter = 0 
        async for photo in client.iter_profile_photos(user.id):
            x = await client.download_media(photo)
            filename,file_extension = os.path.splitext(x)
            counter += 1 
            final_filename = str(user.id)+"_ID_"+ str(user.username)+"_UNAME_"+str(filename) + "_counter_" + str(counter)+file_extension
            print(final_filename)
            os.system("mv "+x+" "+final_filename)
        
##############################################################################################

with client:
    client.loop.run_until_complete(main())
