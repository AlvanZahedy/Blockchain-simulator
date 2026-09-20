from hashlib import sha256
import datetime

class Block:
  def __init__(self, data, index=0, previous_hash = None):
    self.index = index;
    self.timestamp = str(datetime.datetime.now());
    self.previous_hash = previous_hash;
    self.data = data
    self.nonce = 0

  def __str__(self):
    return f"<index: {self.index} timestamp: {self.timestamp} previous_hash: {self.previous_hash} data: {self.data} nonce: {self.nonce} hash: {self.hash}>"
  
  @property
  def hash(self):
    return sha256(f"{self.data}{self.index}{self.timestamp}{self.previous_hash}{self.nonce}".encode()).hexdigest()
    
  def mine(self, difficulty):
    while self.hash[:difficulty] != "".join(["0"] * difficulty):
      self.nonce += 1;

    print(f"Block mined! Found hash: {self.hash}")

class BlockChain:
  def __init__(self, miningDifficulty=4, miningReward=100):
    """Initializing a new Block Chain with the Genesis block."""
    self.miningDifficulty = miningDifficulty
    genesis_block = Block("Genesis Block")
    genesis_block.mine(self.miningDifficulty)
    self.chain = [genesis_block];
    self.mining_reward = miningReward;

  """Setting a property to get the latest block."""
  @property
  def latest_block(self):
    return self.chain[-1];

  def add_block(self, data):
    new_block = Block(data)
    new_block.previous_hash = self.latest_block.hash;
    new_block.index = len(self.chain)
    new_block.mine(difficulty = self.miningDifficulty)
    self.chain.append(new_block);
    return new_block;

  def is_chain_valid(self):
    for i in range(1, len(self.chain)):
      current_block = self.chain[i];
      previous_block = self.chain[i - 1];

      if not current_block.hash.startswith("".join(["0"] * self.miningDifficulty)):
        return False;

      if current_block.previous_hash != previous_block.hash:
        return False;

    return True;