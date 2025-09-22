
url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Bold.woff") format("woff");
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff/FiraCode-Regular.woff") format("woff");
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Bold.woff2") format("woff2"),
                url("https://cdnjs.cloudflare.com/ajax/libs/firacode/6.2.0/woff2/FiraCode-Regular.woff2") format("woff2"),
        font-family: "Fira Code";
        font-family: arial;
        font-family: Fira Code, monospace;
        font-size: {char_height}px;
        font-size: 18px;
        font-style: bold;
        font-style: normal;
        font-variant-east-asian: full-width;
        font-weight: 400;
        font-weight: 700;
        font-weight: bold;
        line-height: {line_height}px;
        src: local("FiraCode-Bold"),
        src: local("FiraCode-Regular"),
      <rect x="0" y="0" width="{terminal_width}" height="{terminal_height}" />
    .{unique_id}-matrix {{
    .{unique_id}-title {{
    @font-face {{
    {backgrounds}
    {chrome}
    {lines}
    {matrix}
    {styles}
    }}
    <!-- Generated with Rich https://www.textualize.io -->
    </clipPath>
    </defs>
    </g>
    </style>
    <clipPath id="{unique_id}-clip-terminal">
    <defs>
    <g class="{unique_id}-matrix">
    <g transform="translate({terminal_x}, {terminal_y})" clip-path="url(#{unique_id}-clip-terminal)">
    <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><code>{code}</code></pre>
    <style>
    background-color: {background};
    color: {foreground};
"""
_SVG_CLASSES_PREFIX = "rich-svg"
_SVG_FONT_FAMILY = "Rich Fira Code"
{stylesheet}
}}
<!DOCTYPE html>
</body>
</head>
</html>
</style>
</svg>
<body>
<head>
<html>
<meta charset="UTF-8">
<style>
<svg class="rich-terminal" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
body {{
CONSOLE_HTML_FORMAT = """\
CONSOLE_SVG_FORMAT = """\

pass
