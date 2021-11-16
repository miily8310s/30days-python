class Animal:
  noise = 'Rrrr'
  color='Red'
  def make_noise(self):
    print(f'{self.noise}')
  def set_noise(self, new_noise: str):
    self.noise = new_noise
    return new_noise
  def get_noise(self):
    return self.noise
  def set_color(self, new_color: str):
    self.color = new_color
    return self.color
  def get_color(self):
    return self.color

class Wolf(Animal):
  noise = "grrrr"

class BabyWolf(Wolf):
  color = "yellow"