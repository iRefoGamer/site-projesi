from flask import Flask, render_template_string, abort

app = Flask(__name__)

scientists = [
    {
        "name": "Stephen Hawking",
        "years": "1942 - 2018",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Stephen_Hawking.StarChild.jpg",
        "info": "Kara delikler ve kozmoloji üzerine yaptığı çalışmalarla tanınan Stephen Hawking, modern fiziğin en önemli teorik fizikçilerinden biridir."
    },
    {
        "name": "Niels Bohr",
        "years": "1885 - 1962",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Niels_Bohr.jpg",
        "info": "Atom modeli ve kuantum teorisine yaptığı katkılar sayesinde modern atom fiziğinin gelişmesine öncülük etmiştir."
    },
    {
        "name": "Max Planck",
        "years": "1858 - 1947",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Max_Planck_1933.jpg",
        "info": "Kuantum teorisinin kurucusu olarak kabul edilen Max Planck, enerji kuantası kavramını geliştirmiştir."
    },
    {
        "name": "Richard Feynman",
        "years": "1918 - 1988",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/42/Richard_Feynman_Nobel.jpg",
        "info": "Kuantum elektrodinamiği alanındaki çalışmalarıyla Nobel Ödülü kazanan Richard Feynman, bilim anlatımıyla da ünlüdür."
    },
    {
        "name": "Werner Heisenberg",
        "years": "1901 - 1976",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Bundesarchiv_Bild183-R57262%2C_Werner_Heisenberg.jpg",
        "info": "Belirsizlik İlkesi ile tanınan Heisenberg, kuantum mekaniğinin gelişiminde büyük rol oynamıştır."
    },
    {
        "name": "Albert Einstein",
        "years": "1879 - 1955",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
        "info": "Görelilik teorisi ile modern fiziğin temelini değiştiren Albert Einstein, Nobel Fizik Ödülü kazanmıştır. E=mc² formülü ile enerji ve madde arasındaki ilişkiyi açıklamıştır."
    },
    {
        "name": "Isaac Newton",
        "years": "1643 - 1727",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Sir_Isaac_Newton_%281643-1727%29.jpg",
        "info": "Klasik fiziğin kurucularından biri olan Isaac Newton, hareket yasaları ve evrensel çekim kanunu ile bilim dünyasına büyük katkı sağlamıştır."
    },
    {
        "name": "Marie Curie",
        "years": "1867 - 1934",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/69/Marie_Curie_c1920.jpg",
        "info": "Radyoaktivite üzerine yaptığı çalışmalarla tanınan Marie Curie, iki farklı bilim dalında Nobel Ödülü kazanan ilk bilim insanıdır."
    },
    {
        "name": "Nikola Tesla",
        "years": "1856 - 1943",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/N.Tesla.JPG",
        "info": "Alternatif akım sistemleri üzerine yaptığı çalışmalar ile modern elektrik teknolojisinin gelişmesinde büyük rol oynamıştır."
    },
    {
        "name": "Feza Gürsey",
        "years": "1921 - 1992",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Feza_Gursey.jpg",
        "info": "Teorik fizik alanında dünya çapında tanınan Türk bilim insanı Feza Gürsey, parçacık fiziği ve matematiksel fizik üzerine önemli çalışmalar yapmıştır."
    },
    {
        "name": "Erdal İnönü",
        "years": "1926 - 2007",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/37/Erdal_Inonu.jpg",
        "info": "Türk fizikçi ve bilim insanı Erdal İnönü, grup teorisi ve teorik fizik alanında önemli katkılar sağlamıştır."
    },
    {
        "name": "Behram Kurşunoğlu",
        "years": "1922 - 2003",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Behram_Kursunoglu.jpg",
        "info": "Teorik fizik ve birleşik alan teorisi üzerine çalışan Türk bilim insanı Behram Kurşunoğlu, uluslararası bilim çevrelerinde tanınmıştır."
    },
    {
        "name": "Galileo Galilei",
        "years": "1564 - 1642",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/29/Galileo.arp.300pix.jpg",
        "info": "Modern gözlemsel astronominin öncüsü olan Galileo, teleskop gözlemleriyle bilim tarihine damga vurmuştur."
    }
]

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

        .card h2 {
            margin: 0;
            font-size: 28px;
        }

        .years {
            color: #cbd5e1;
            margin-bottom: 15px;
        }

        footer {
            text-align: center;
            padding: 20px;
            margin-top: 30px;
            border-top: 1px solid #475569;
            color: #cbd5e1;
        }
    </style>
</head>
<body>

<header>
    <h1>Fizik Bilim İnsanları</h1>
    <p>Fizik tarihine yön veren bilim insanlarını keşfet.</p>
</header>

<div class="container">
    {% for scientist in scientists %}
    <a href="/scientist/{{ scientist.name.replace(' ', '-').lower() }}" style="text-decoration:none; color:white;">
    <div class="card">
        <img src="{{ scientist.image }}" alt="{{ scientist.name }}">
        <div class="card-content">
            <h2>{{ scientist.name }}</h2>
            <p class="years">{{ scientist.years }}</p>
            <p>{{ scientist.info }}</p>
        </div>
    </div>
    </a>
    {% endfor %}
</div>

<footer>
    © 2026 Fizik Bilim İnsanları Sitesi
</footer>

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
            box-shadow: 0 5px 15px rgba(0,0,0,0.4);
        }

        img {
            width: 100%;
            height: 500px;
            object-fit: cover;
        }

        .content {
            padding: 30px;
        }

        h1 {
            font-size: 42px;
            margin-bottom: 10px;
        }

        .years {
            color: #cbd5e1;
            margin-bottom: 20px;
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
    <img src="{{ scientist.image }}" alt="{{ scientist.name }}">

    <div class="content">
        <h1>{{ scientist.name }}</h1>
        <p class="years">{{ scientist.years }}</p>
        <p>{{ scientist.info }}</p>

        <a href="/">← Ana Sayfaya Dön</a>
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_template, scientists=scientists)

@app.route('/scientist/<name>')
def scientist_detail(name):
    scientist = next((s for s in scientists if s['name'].replace(' ', '-').lower() == name.lower()), None)

    if not scientist:
        abort(404)

    return render_template_string(detail_template, scientist=scientist)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


