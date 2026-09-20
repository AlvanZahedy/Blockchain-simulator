from flask import Flask;
from block_chain import BlockChain;

blockChain = BlockChain();

print(blockChain.is_chain_valid())

def create_app():
  app = Flask(__name__);
  app.config["SECRET_KEY"] = "Secret Key";

  from .views import views as view_routes;
  from .auth import auth as auth_routes;
  
  app.register_blueprint(view_routes, url_prefix="/");
  app.register_blueprint(auth_routes, url_prefix="/");

  return app;
