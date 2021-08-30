import datetime
import sys
import unicodedata
import os
from pytz import country_timezones, timezone


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


try:
    name = sys.argv[1]
except:
    name = "Varšava"
key_name = remove_accents(name).lower().replace(' ', '_')
today = datetime.datetime.now(timezone("Europe/Helsinki"))
filename = f"{datetime.date.today()}-{key_name.replace('_', '-')}"
post_nr = len(os.listdir("_posts"))
content = f"""---
layout: post
title: {name}
date: {datetime.date.today()} {today.strftime('%H:%M:%S')} {today.strftime('%z')}
img_folder: {post_nr:02d}-{key_name}
description: 
img: cover.jpg # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: []
---
"""

with open(f"_posts/{filename}.markdown", "x", encoding="utf-8") as f:
    f.write(content)
img_dir=f"assets/img/{post_nr:02d}-{key_name}"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)