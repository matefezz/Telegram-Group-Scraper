from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import pandas as pd
import configparser

# قراءة بيانات API من ملف config
config = configparser.ConfigParser()
config.read("telethon.config")

api_id = config["telethon_credentials"]["api_id"]
api_hash = config["telethon_credentials"]["api_hash"]

# قراءة أسماء الجروبات من ملف groups.txt
with open("groups.txt", "r", encoding="utf-8") as f:
    target_groups = [line.strip() for line in f if line.strip()]

# تسجيل الدخول باستخدام الجلسة
with TelegramClient('test', int(api_id), api_hash) as client:
    client.start()  # هيطلب رقم الموبايل والكود أول مرة

    df = pd.DataFrame()

    for group in target_groups:
        try:
            print(f"🔄 Joining group: {group}")
            client(JoinChannelRequest(group))

            print("📥 Fetching participants...")
            all_participants = client.get_participants(group, aggressive=True)

            for user in all_participants:
                data = {
                    "user_id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone": user.phone,
                    "bot": user.bot,
                    "verified": user.verified,
                    "mutual_contact": user.mutual_contact,
                    "access_hash": user.access_hash,
                    "group": group
                }
                temp_df = pd.DataFrame([data])
                df = pd.concat([df, temp_df], ignore_index=True)

        except Exception as e:
            print(f"❌ Error in group {group}: {e}")
    # the path of the saved file in your pc
    df.to_excel(r"c:\Telegram\scrap-users-group.xlsx", index=False)
    print("✅ Data saved to Excel.")
