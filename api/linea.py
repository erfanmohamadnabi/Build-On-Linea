
#! Get Token Balances

# import requests

# address = "0x029f781A6218d49B547ac058D0b045a07905e089"

# url = f"https://api.dune.com/api/beta/balance/{address}"

# headers = {"X-Dune-Api-Key": "Rp7JUdyywkX6WDIzeDUSF0LHoV3ZvOYj"}

# response = requests.request("GET", url, headers=headers)

# data = response.json()['balances']

# for x in data:
#     if x:
#         print(x)

from dune_client.client import DuneClient

custom = "t0S9A3xCz0kIHVZqgIjAiUclkAuQUDtW"
NFT_API_KEY = 'zeWCimbw8U2VHwu66g7dRMnBGcQyeNJB'

dune = DuneClient(NFT_API_KEY)
response = dune.get_custom_endpoint_result(
    "test123222",
    "nft",
    limit=80000,
    filters = "address = '0x029f781A6218d49B547ac058D0b045a07905e089'"

)

# دسترسی به ردیف‌ها
rows = response.result.rows


print(rows)

# # به عنوان مثال: فیلتر کردن صفات خاص
# filtered_results = [
#     row for row in rows 
#     if row['wallet'] == '0x867e29c16a1b921676c0c201e1dce6626609cbf6'
# ]

# # چاپ نتایج فیلتر شده
# for result in filtered_results:
#     print(result)