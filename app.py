from flask import Flask, render_template_string, abort
import os

app = Flask(__name__)

scientists = [
    {
        "name": "Stephen Hawking",
        "slug": "stephen-hawking",
        "years": "1942 - 2018",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Stephen_Hawking.StarChild.jpg",
        "info": "Kara delikler ve kozmoloji üzerine yaptığı çalışmalarla tanınır."
    },
    {
        "name": "Albert Einstein",
        "slug": "albert-einstein",
        "years": "1879 - 1955",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
        "info": "Görelilik teorisi ile modern fiziğin temelini değiştirmiştir."
    },
    {
        "name": "Isaac Newton",
        "slug": "isaac-newton",
        "years": "1643 - 1727",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Sir_Isaac_Newton_%281643-1727%29.jpg",
        "info": "Klasik mekaniğin kurucusudur."
    }
]

scientist_map = {s["slug"]: s for s in scientists}

home_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fizik Bilim İnsanları</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #0f172a, #1e293b);
            color: white;
        }

        header {
            text-align: center;
            padding: 50px 20px;
        }

        h1 {
            font-size: 48px;
        }

        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }

        .card {
            background-color: #334155;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.4);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: scale(1.03);
        }

        .card img {
            width: 100%;
            height: 300px;
            object-fit: cover;
        }

        .card-content {
            padding: 20px;
        }

        a {
            text-decoration: none;
            color: white;
        }
    </style>
</head>
<body>

<header>
    <h1>Fizik Bilim İnsanları</h1>
    <p>Fizik tarihine yön veren bilim insanlarını keşfet.</p>
</header>

<div class="container">
    {% for s in scientists %}
    <a href="/scientist/{{ s.slug }}">
        <div class="card">
            <img src="{{ s.image }}">
            <div class="card-content">
                <h2>{{ s.name }}</h2>
                <p>{{ s.years }}</p>
                <p>{{ s.info }}</p>
            </div>
        </div>
    </a>
    {% endfor %}
</div>

</body>
</html>
"""

detail_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ scientist.name }}</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #0f172a, #1e293b);
            color: white;
            padding: 40px;
        }

        .container {
            max-width: 900px;
            margin: auto;
            background-color: #334155;
            border-radius: 20px;
            overflow: hidden;
        }

        img {
            width: 100%;
            height: 500px;
            object-fit: cover;
        }

        .content {
            padding: 30px;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            color: white;
            text-decoration: none;
            background-color: #0f172a;
            padding: 12px 20px;
            border-radius: 10px;
        }
    </style>
</head>
<body>

<div class="container">
    <img src="{{ scientist.image }}">

    <div class="content">
        <h1>{{ scientist.name }}</h1>
        <p>{{ scientist.years }}</p>
        <p>{{ scientist.info }}</p>

        <a href="/">← Ana Sayfa</a>
    </div>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(home_template, scientists=scientists)

@app.route("/scientist/<slug>")
def scientist_detail(slug):
    scientist = scientist_map.get(slug)
    if not scientist:
        abort(404)
    return render_template_string(detail_template, scientist=scientist)


# 🔥 RENDER FIX
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
