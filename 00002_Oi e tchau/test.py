class Test(unittest.TestCase):
  
  def test_obs_foi_removida(self):
     self.assertFalse("obs" in cinemas, "coluna obs deveria ter sido removida")
  
  def test_category_foi_removida(self):
     self.assertFalse("category" in cinemas, "a coluna de categoria deveria ter sido removida")
    
  def test_update_year_foi_removida(self):
     self.assertFalse("update_year" in cinemas, "a coluna update_year deveria ter sido removida")