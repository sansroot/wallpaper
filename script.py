import os

wallpaper_dir = "wallpaper"
output_file = "README.md"
repo_url = "https://raw.githubusercontent.com/sansroot/wallpapers/master"
columns = 4

files = sorted([
    f for f in os.listdir(wallpaper_dir)
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))
])

rows = ""
for i in range(0, len(files), columns):
    row = files[i:i + columns]
    while len(row) < columns:
        row.append("")
    row_md = " | ".join(
        f"![{name}]({repo_url}/{name})" if name else "" for name in row
    )
    rows += f"| {row_md} |\n"

with open(output_file, "w") as f:
    f.write(rows)
