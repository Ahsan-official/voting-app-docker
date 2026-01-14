from flask import Flask

app = Flask(__name__)
votes = {"A": 0, "B": 0}

@app.route("/")
def home():
    return f"""
    <h1>Voting App</h1>
    <a href='/vote/A'>Vote A</a><br><br>
    <a href='/vote/B'>Vote B</a><br><br>
    Votes: {votes}
    """

@app.route("/vote/<option>")
def vote(option):
    votes[option] += 1
    return "Thanks for voting! <a href='/'>Go Back</a>"

app.run(host="0.0.0.0", port=5000)
