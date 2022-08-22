from flask import Flask, render_template

data = [{"id":1,"body":"Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify.","title":"The Life of Cactus","subtitle":"Who knew that cacti lived such interesting lives."},{"id":2,"body":"Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today.","title":"Top 15 Things to do When You are Bored","subtitle":"Are you bored? Don't know what to do? Try these top 15 activities."},{"id":3,"body":"Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake.","title":"Introduction to Intermittent Fasting","subtitle":"Learn about the newest health craze."}]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs= data)

@app.route('/myAbout')
def get_about():
    return render_template("about.html")

@app.route('/myContact')
def get_contact():
    return render_template("contact.html")

@app.route('/myPost/<int:id>')
def get_post(id):
    the_blog = None
    for blog in data:
        if blog['id'] == id:
            the_blog = blog

    return render_template("post.html", blog= the_blog)


if __name__ == '__main__':
    app.run(debug= True)

