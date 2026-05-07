from flask import Flask, render_template_string, abort
import os

app = Flask(__name__)

scientists = [
    {
        "name": "Stephen Hawking",
        "slug": "stephen-hawking",
        "years": "1942 - 2018",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Stephen_Hawking.StarChild.jpg",
        "info": "Kara delikler ve kozmoloji üzerine yaptığı çalışmalarla tanınan Stephen Hawking, modern fiziğin en önemli teorik fizikçilerinden biridir."
    },
    {
        "name": "Niels Bohr",
        "slug": "niels-bohr",
        "years": "1885 - 1962",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Niels_Bohr.jpg",
        "info": "Atom modeli ve kuantum teorisine yaptığı katkılar sayesinde modern atom fiziğinin gelişmesine öncülük etmiştir."
    },
    {
        "name": "Max Planck",
        "slug": "max-planck",
        "years": "1858 - 1947",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Max_Planck_1933.jpg",
        "info": "Kuantum teorisinin kurucusu olarak kabul edilen Max Planck, enerji kuantası kavramını geliştirmiştir."
    },
    {
        "name": "Richard Feynman",
        "slug": "richard-feynman",
        "years": "1918 - 1988",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/42/Richard_Feynman_Nobel.jpg",
        "info": "Kuantum elektrodinamiği alanındaki çalışmalarıyla Nobel Ödülü kazanan Richard Feynman, bilim anlatımıyla da ünlüdür."
    },
    {
        "name": "Werner Heisenberg",
        "slug": "werner-heisenberg",
        "years": "1901 - 1976",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Bundesarchiv_Bild183-R57262%2C_Werner_Heisenberg.jpg",
        "info": "Belirsizlik İlkesi ile tanınan Heisenberg, kuantum mekaniğinin gelişiminde büyük rol oynamıştır."
    },
    {
        "name": "Albert Einstein",
        "slug": "albert-einstein",
        "years": "1879 - 1955",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg",
        "info": "Görelilik teorisi ile modern fiziğin temelini değiştiren Albert Einstein, E=mc² formülü ile ünlüdür."
    },
    {
        "name": "Isaac Newton",
        "slug": "isaac-newton",
        "years": "1643 - 1727",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Sir_Isaac_Newton_%281643-1727%29.jpg",
        "info": "Klasik fiziğin kurucularından biri olan Isaac Newton, hareket yasaları ve yerçekimi ile bilinir."
    },
    {
        "name": "Marie Curie",
        "slug": "marie-curie",
        "years": "1867 - 1934",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/69/Marie_Curie_c1920.jpg",
        "info": "Radyoaktivite üzerine yaptığı çalışmalarla iki Nobel kazanan ilk bilim insanıdır."
    },
    {
        "name": "Nikola Tesla",
        "slug": "nikola-tesla",
        "years": "1856 - 1943",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d4/N.Tesla.JPG",
        "info": "Alternatif akım sistemlerinin geliştirilmesinde büyük rol oynamıştır."
    },
    {
        "name": "Feza Gürsey",
        "slug": "feza-gursey",
        "years": "1921 - 1992",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Feza_Gursey.jpg",
        "info": "Parçacık fiziği ve matematiksel fizik alanında önemli çalışmalar yapmıştır."
    },
    {
        "name": "Erdal İnönü",
        "slug": "erdal-inonu",
        "years": "1926 - 2007",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/37/Erdal_Inonu.jpg",
        "info": "Grup teorisi ve teorik fizik alanında katkılar sağlamıştır."
    },
    {
        "name": "Behram Kurşunoğlu",
        "slug": "behram-kursunoglu",
        "years": "1922 - 2003",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Behram_Kursunoglu.jpg",
        "info": "Birleşik alan teorisi üzerine çalışmıştır."
    },
    {
        "name": "Galileo Galilei",
        "slug": "galileo-galilei",
        "years": "1564 - 1642",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/29/Galileo.arp.300pix.jpg",
        "info": "Modern astronominin kurucusu sayılır."
    }
]

scientist_map = {s["slug"]: s for s in scientists}


home_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Fizik Bilim İnsanları</title>
<style>
body { margin:0; font-family:Arial; background:#0f172a; color:white; }
header { text-align:center; padding:40px; }
.container {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:20px;
    padding:20px;
}
.card {
    background:#334155;
    border-radius:15px;
    overflow:hidden;
    transition:0.3s;
}
.card:hover { transform:scale(1.03); }
.card img { width:100%; height:300px; object-fit:cover; }
.card-content { padding:15px; }
a { text-decoration:none; color:white; }
</style>
</head>
<body>

<header>
<h1>Fizik Bilim İnsanları</h1>
<p>Bilim tarihine yön verenler</p>
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
<title>{{ scientist.name }}</title>
<style>
body { margin:0; font-family:Arial; background:#0f172a; color:white; padding:40px; }
.container { max-width:900px; margin:auto; background:#334155; border-radius:20px; overflow:hidden; }
img { width:100%; height:500px; object-fit:cover; }
.content { padding:20px; }
a { color:white; display:inline-block; margin-top:20px; text-decoration:none; }
</style>
</head>
<body>

<div class="container">
<img src="{{ scientist.image }}">
<div class="content">
<h1>{{ scientist.name }}</h1>
<p>{{ scientist.years }}</p>
<p>{{ scientist.info }}</p>
<a href="/">← Geri</a>
</div>
</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(home_template, scientists=scientists)


@app.route("/scientist/<slug>")
def detail(slug):
    scientist = scientist_map.get(slug)
    if not scientist:
        abort(404)
    return render_template_string(detail_template, scientist=scientist)


# 🔥 RENDER FIX
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
