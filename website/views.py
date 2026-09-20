from flask import Blueprint, render_template, redirect, url_for, request;
from . import blockChain

views = Blueprint("views", __name__);

@views.route("/")
def index():
  # redirect to /home instead of /
  return redirect(url_for("views.home"))

@views.route("/home")
def home():
  return render_template("home.html", BlockChain=blockChain)

@views.route("/chain")
def chain():
  return render_template("see-chain.html", BlockChain=blockChain)

@views.route("/is-chain-valid")
def valid():
  return render_template("valid.html", BlockChain=blockChain)

@views.route("/add-block", methods=["GET","POST"])
def add_block():
  if request.method == "POST":
    if request.form['data'] == "":
      pass #flash an error message
    else:
      blockChain.add_block(request.form['data'])
      return redirect(url_for("views.home"));

  return render_template("add_block.html", BlockChain = blockChain)

@views.route("/mine-block")
def mine():
  return render_template("mine_block.html")

@views.route(f"/chain/block-<position>")
def block(position):
  if int(position) > len(blockChain.chain):
    return

  block = blockChain.chain[int(position)-1]
  return render_template("block.html", index=block.index, timestamp=block.timestamp, previous_hash=block.previous_hash, data=block.data, nonce=block.nonce, hash=block.hash)