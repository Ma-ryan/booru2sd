# booru2sd
Danbooru to SD tag format coverter.

This is a simple script to quickly convert tags copied from Danbooru into something readily usable by most Stable Diffusion models trained on Danbooru images (e.g. Illustrious, PonyV6, etc).

### Requirements:
Python 3.

### Usage:
1. Create a `.txt` file in the same directory as `booru2sd.py` (default is `tags.txt`).
2. Paste and save your tags into your `.txt` file.
3. Run `python booru2sd.py` in your terminal of choice.

Tip: You can change the default filename and path of your `.txt` file by modifying line 44 in `booru2sd.py`.

### Example:

Input:<br/>
![Model](example/input.jpg)
<br/>Art by [Komota](https://danbooru.donmai.us/posts/5312769?q=komota_%28kanyou_shoujo%29).<br/>
`komota_(kanyou_shoujo) 1girl black_dress black_ribbon child closed_mouth dress flower grey_eyes grey_hair head_wreath long_hair long_sleeves looking_at_viewer neck_ribbon pink_flower ribbon smile solo upper_body`

Output:<br/>
![Model](example/output.png)<br/>
Generated using [NoobaiCyberFix v3](https://civitai.com/models/913998/noobaicyberfix) (NoobAI Epsilon 1.1 derivative)<br/>
`komota \(kanyou shoujo\), 1girl, black dress, black ribbon, child, closed mouth, dress, flower, grey eyes, grey hair, head wreath, long hair, long sleeves, looking at viewer, neck ribbon, pink flower, ribbon, smile, solo, upper body`
