from flask import Flask, render_template
import json

app = Flask(__name__)


# import json

@app.route("/")
def homepage():
    json_ld = {
        "@context": "http://schema.org",
        "@type": "Person",
        "name": "Chuah Seong Han",
        "jobTitle": "MUSA BOSS",
        "affiliation": "MOnash Uni",
        "additionalName": "Boss",
        "url": "http://www.seonghan.com",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "1234 Peach Drive",
            "addressLocality": "Wonderland",
            "addressRegion": "Georgia"
        }
    }
    output = """
	<!DOCTYPE html>
		<html>
			<head>
				<meta charset="UTF-8">
				<title>Website Title</title>
			</head>
			<script type="application/ld+json">"""
    output += json.dumps(json_ld, indent=4)
    output += """
			</script>
			<body>
				<h1>Hello Seong Han</h1>
			</body>
		</html>
	"""
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run()
